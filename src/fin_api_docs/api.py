from __future__ import annotations

import dataclasses
from dataclasses import dataclass
from enum import Enum
from typing import Optional, NewType

from fin_api_docs.reflection_json import FileJSON, TypeRefJSON, PropertyJSON, FunctionJSON, SignalJSON


class PrimitiveType(Enum):
    nil = 'nil'
    boolean = 'boolean'
    integer = 'integer'
    float = 'float'
    string = 'string'
    unknown = 'unknown'


@dataclass
class ArrayType:
    elementType: TypeRef


@dataclass
class FutureType:
    resultType: TypeRef


StructuredTypeID = NewType('StructuredTypeID', str)

TypeRef = PrimitiveType | ArrayType | FutureType | StructuredTypeID


@dataclass
class _Item:
    name: str
    description: str


@dataclass(frozen=True)
class MemberID:
    type: StructuredTypeID
    member: str
    static: bool


@dataclass
class _Member(_Item):
    id: MemberID


@dataclass
class Field(_Member):
    type: TypeRef
    read_only: bool


@dataclass
class Parameter(_Item):
    type: TypeRef
    is_var_arg: bool


@dataclass
class Method(_Member):
    parameters: list[Parameter]
    return_values: list[Parameter]


@dataclass
class Signal(_Member):
    parameters: list[Parameter]


Member = Field | Method | Signal


@dataclass
class _StructuredType(_Item):
    id: StructuredTypeID
    instance_members: dict[MemberID, Member]
    static_members: dict[MemberID, Member]


@dataclass
class Struct(_StructuredType):
    pass


@dataclass
class Class(_StructuredType):
    parent_class: Optional[StructuredTypeID]


StructuredType = Struct | Class


def _type_ref_from_json(data: TypeRefJSON) -> TypeRef:
    if data['type'] == 'Int':
        return PrimitiveType.integer
    elif data['type'] == 'Float':
        return PrimitiveType.float
    elif data['type'] == 'String':
        return PrimitiveType.string
    elif data['type'] == 'Bool':
        return PrimitiveType.boolean
    elif data['type'] == 'Array':
        return ArrayType(_type_ref_from_json(data['inner']))
    elif data['type'] == 'Struct':
        return StructuredTypeID(data['inner'])
    else:
        subclass = data.get('subclass')

        if subclass is None:
            return PrimitiveType.unknown
        else:
            return StructuredTypeID(subclass)


class _MembersBuilder:
    def __init__(self, type_id: StructuredTypeID):
        self.type_id = type_id
        self.instance_members = list[Member]()
        self.static_members = list[Member]()

    def add_field(self, data: PropertyJSON):
        member_name = data['internalName']
        static = data['Flag_ClassProp']

        field = Field(
            name=member_name,
            description=data['description'],
            type=_type_ref_from_json(data['type']),
            id=MemberID(self.type_id, member_name, static),
            read_only=data['Flag_ReadOnly'])

        if static:
            self.static_members.append(field)
        else:
            self.instance_members.append(field)

    def add_method(self, data: FunctionJSON):
        member_name = data['internalName']
        parameters = list[Parameter]()
        return_values = list[Parameter]()
        static = data['Flag_ClassFunc']

        for pa in data['parameters']:
            parameter = Parameter(
                name=pa['internalName'],
                description=pa['description'],
                type=_type_ref_from_json(pa['type']),
                is_var_arg=False)

            if pa['Flag_OutParam']:
                return_values.append(parameter)
            else:
                parameters.append(parameter)

        if data['Flag_VarArgs']:
            parameters.append(
                Parameter(
                    name='args',
                    description='',
                    type=PrimitiveType.unknown,
                    is_var_arg=True))

        if data['Flag_VarRets']:
            return_values.append(
                Parameter(
                    name='results',
                    description='',
                    type=PrimitiveType.unknown,
                    is_var_arg=True))

        if data['Flag_RT_Async']:
            if return_values:
                return_values = [
                    dataclasses.replace(i, type=FutureType(i.type))
                    for i in return_values]
            else:
                return_values = [
                    Parameter('result', '', FutureType(PrimitiveType.nil), False)]

        method = Method(
            name=member_name,
            description=data['description'],
            id=MemberID(self.type_id, member_name, static),
            parameters=parameters,
            return_values=return_values)

        if static:
            self.static_members.append(method)
        else:
            self.instance_members.append(method)

    def add_signal(self, data: SignalJSON):
        member_name = data['internalName']
        parameters = list[Parameter]()

        for pa in data['parameters']:
            parameters.append(
                Parameter(
                    name=pa['internalName'],
                    description=pa['description'],
                    type=_type_ref_from_json(pa['type']),
                    is_var_arg=False))

        if data['isVarArgs']:
            parameters.append(
                Parameter(
                    name='values',
                    description='',
                    type=PrimitiveType.unknown,
                    is_var_arg=True))

        self.instance_members.append(
            Signal(
                name=member_name,
                description=data['description'],
                id=MemberID(self.type_id, member_name, False),
                parameters=parameters))


@dataclass
class API:
    structured_types: dict[StructuredTypeID, StructuredType]

    def get_parent_chain(self, id: StructuredTypeID) -> list[StructuredTypeID]:
        res = list[StructuredTypeID]()
        current_ref: StructuredTypeID | None = id

        while current_ref is not None:
            res.append(current_ref)
            type = self.structured_types[current_ref]

            if isinstance(type, Class):
                current_ref = type.parent_class
            else:
                current_ref = None

        return res

    def get_direct_subclasses(
            self, id: StructuredTypeID) \
            -> list[StructuredTypeID]:
        res = list[StructuredTypeID]()

        for i in self.structured_types.values():
            if isinstance(i, Class) and i.parent_class == id:
                res.append(i.id)

        return res

    @classmethod
    def from_json(cls, data: FileJSON):
        structured_types = list[StructuredType]()

        for c in data['structs']:
            type_id = StructuredTypeID(c['internalName'])
            members_builder = _MembersBuilder(type_id)

            for p in c['properties']:
                members_builder.add_field(p)

            for f in c['functions']:
                members_builder.add_method(f)

            structured_types.append(
                Struct(
                    name=c['internalName'],
                    description=c['description'],
                    id=type_id,
                    instance_members={i.id: i for i in members_builder.instance_members},
                    static_members={i.id: i for i in members_builder.static_members}))

        for c in data['classes']:
            type_id = StructuredTypeID(c['internalName'])
            members_builder = _MembersBuilder(type_id)

            for p in c['properties']:
                members_builder.add_field(p)

            for f in c['functions']:
                members_builder.add_method(f)

            for s in c['signals']:
                members_builder.add_signal(s)

            parent_class_name = c.get('parent')

            if parent_class_name is None:
                parent_class = None
            else:
                parent_class = StructuredTypeID(parent_class_name)

            structured_types.append(
                Class(
                    name=c['internalName'],
                    description=c['description'],
                    id=type_id,
                    instance_members={i.id: i for i in members_builder.instance_members},
                    static_members={i.id: i for i in members_builder.static_members},
                    parent_class=parent_class))

        return API(
            structured_types={i.id: i for i in structured_types})
