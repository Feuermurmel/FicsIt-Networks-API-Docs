from __future__ import annotations

import dataclasses
import json
import os
import re
import shutil
from collections.abc import Callable
from collections.abc import Collection
from collections.abc import Iterable
from collections.abc import Iterator
from dataclasses import dataclass
from functools import partial
from pathlib import Path

from fin_api_docs.api import API
from fin_api_docs.api import ArrayType
from fin_api_docs.api import Class
from fin_api_docs.api import Field
from fin_api_docs.api import FutureType
from fin_api_docs.api import Member
from fin_api_docs.api import MemberID
from fin_api_docs.api import Method
from fin_api_docs.api import Parameter
from fin_api_docs.api import PrimitiveType
from fin_api_docs.api import Signal
from fin_api_docs.api import Struct
from fin_api_docs.api import StructuredType
from fin_api_docs.api import StructuredTypeID
from fin_api_docs.api import TypeRef
from fin_api_docs.util import UserError


def get_relative_path(path: Path, relative_to: Path) -> str:
    parts_from = list(relative_to.parts[:-1])
    parts_to = list(path.parts)

    while parts_from and parts_to and parts_from[0] == parts_to[0]:
        parts_from.pop(0)
        parts_to.pop(0)

    return "/".join([".." for _ in parts_from] + parts_to)


@dataclass
class Link:
    relative_to: Page
    page: Page
    fragment: str | None = None

    def render(self, link_text: str) -> str:
        url = get_relative_path(self.page.path, self.relative_to.path)

        if self.fragment is not None:
            url = f"{url}#{self.fragment}"

        return f'<a href="{url}">{link_text}</a>'

    def with_fragment(self, fragment: str) -> Link:
        return dataclasses.replace(self, fragment=fragment)


@dataclass
class Page:
    path: Path
    get_content: Callable[[PageContext], str]


@dataclass
class APIDocs:
    api: API
    structured_type_pages: dict[StructuredTypeID, Page]

    def write_pages(self, output_path: Path) -> None:
        for i in self.structured_type_pages.values():
            content = i.get_content(PageContext(i, self))
            path = output_path / i.path

            if not path.parent.exists():
                path.parent.mkdir(parents=True)

            path.write_text(content)


@dataclass
class PageContext:
    page: Page
    api_docs: APIDocs

    def type_ref(self, ref: TypeRef) -> str:
        if isinstance(ref, PrimitiveType):
            return ref.value
        elif isinstance(ref, ArrayType):
            return f"list of {self.type_ref(ref.elementType)}"
        elif isinstance(ref, FutureType):
            return f"future of {self.type_ref(ref.resultType)}"
        else:
            return self.page_link_target(ref).render(
                self.api_docs.api.structured_types[ref].name
            )

    def page_link_target(self, id: StructuredTypeID) -> Link:
        return Link(self.page, self.api_docs.structured_type_pages[id])

    def member_anchor(self, id: MemberID) -> str:
        anchor = re.sub("(?=[A-Z]+)", "-", id.member).lower()

        if id.static:
            anchor = "s-" + anchor

        return anchor

    def member_link_target(self, id: MemberID) -> Link:
        return self.page_link_target(id.type).with_fragment(
            f"user-content-{self.member_anchor(id)}"
        )


def member_sort_key(member: Member) -> tuple[int, str]:
    if isinstance(member, Field):
        category_rank = 0
    elif isinstance(member, Method):
        category_rank = 1
    else:
        category_rank = 2

    return category_rank, member.name


def structured_type_content(type: StructuredType, context: PageContext) -> str:
    def member_title(member: Member) -> str:
        return f'<code id="{context.member_anchor(member.id)}">{member.name}</code>'

    def iter_parameter_descriptions(
        heading: str, parameters: list[Parameter]
    ) -> Iterator[str]:
        if parameters:
            yield f"<b>{heading}:</b>"
            yield ""

            for p in parameters:
                yield f"- <code><b>{p.name}</b></code> {context.type_ref(p.type)}"
                yield f""
                yield f"  {p.description}"

    # TODO: Fix newlines in descriptions.
    # TODO: Also write "(no description)" when a description is missing.
    def iter_members(
        heading: str,
        type: StructuredType,
        get_members: Callable[[StructuredType], Collection[Member]],
    ) -> Iterator[str]:
        parents = context.api_docs.api.get_parent_chain(type.id)[1:]

        parent_members = list[tuple[StructuredTypeID, Iterable[Member]]]()

        for t in parents:
            members = get_members(context.api_docs.api.structured_types[t])

            if members:
                parent_members.append((t, members))

        members = get_members(type)

        if members or parent_members:
            yield f"## {heading}"

            if parent_members:
                yield f"<b>Inherited Members:</b>"

            for parent_id, pm in parent_members:
                parent = context.api_docs.api.structured_types[parent_id]

                def member_link_text(member: Member) -> str:
                    if isinstance(member, Method):
                        return f"{member.name}()"
                    else:
                        return member.name

                members_str = ", ".join(
                    f"{context.member_link_target(m.id).render(member_link_text(m))}"
                    for m in sorted(pm, key=lambda i: i.name)
                )

                yield f"- {parent.name}: {members_str}"

            fields = list[Field]()
            methods = list[Method]()
            signals = list[Signal]()

            for m in members:
                if isinstance(m, Field):
                    fields.append(m)
                elif isinstance(m, Method):
                    methods.append(m)
                else:
                    signals.append(m)

            if fields:
                yield "### Fields"

                for f in fields:
                    yield f"- {member_title(f)} {context.type_ref(f.type)}"
                    yield f""
                    yield f"  {f.description}"

            for mm in methods:
                params_str = ", ".join(i.name for i in mm.parameters)

                if mm.return_values:
                    return_part = " → " + ", ".join(i.name for i in mm.return_values)
                else:
                    return_part = ""

                yield f"### Method {member_title(mm)} ({params_str}){return_part}"
                yield f"{mm.description}"
                yield f""
                yield from iter_parameter_descriptions("Parameters", mm.parameters)
                yield f""
                yield from iter_parameter_descriptions(
                    "Return Values", mm.return_values
                )

            for s in signals:
                if s.parameters:
                    parameters_part = " → " + ", ".join(i.name for i in s.parameters)
                else:
                    parameters_part = ""

                yield f"### Signal {member_title(s)}{parameters_part}"
                yield f"{s.description}"
                yield f""
                yield from iter_parameter_descriptions("Parameters", s.parameters)

    def iter_parts() -> Iterator[str]:
        if isinstance(type, Struct):
            kind_str = "Struct"
        else:
            kind_str = "Class"

        yield f"# {kind_str} <code>{type.name}</code>"
        yield f""

        if isinstance(type, Class):
            parents = context.api_docs.api.get_parent_chain(type.id)[1:]
            children = context.api_docs.api.get_direct_subclasses(type.id)

            if parents:
                parents_str = " < ".join(context.type_ref(i) for i in parents)

                yield f"Superclasses: {parents_str}"
                yield ""

            if children:
                children_str = ", ".join(context.type_ref(i) for i in children)

                yield f"Direct subclasses: {children_str}"
                yield ""

        yield type.description

        yield from iter_members(
            "Instance Members", type, lambda x: x.instance_members.values()
        )
        yield from iter_members(
            "Static Members", type, lambda x: x.static_members.values()
        )

    return "\n".join(iter_parts())


def main(output_path: Path, clear: bool, input_json_path: Path | None) -> None:
    if input_json_path is None:
        local_app_data = os.environ.get("LOCALAPPDATA")

        if local_app_data is None:
            raise UserError(
                "LOCALAPPDATA environment variable is not set and "
                "input_json_path has not been given on the command line."
            )

        input_json_path = (
            Path(local_app_data) / "FactoryGame/Saved/FINReflectionDocumentation.json"
        )

    api = API.from_json(json.loads(input_json_path.read_bytes()))
    structured_type_pages = dict[StructuredTypeID, Page]()

    for type in api.structured_types.values():
        if isinstance(type, Struct):
            dir = Path("structs")
        else:
            dir = Path("classes")

        structured_type_pages[type.id] = Page(
            dir / f"{type.name}.md", partial(structured_type_content, type)
        )

    api_docs = APIDocs(api=api, structured_type_pages=structured_type_pages)

    if clear and output_path.exists():
        for i in output_path.iterdir():
            if i.is_dir():
                shutil.rmtree(i)
            else:
                i.unlink()

    api_docs.write_pages(output_path)
