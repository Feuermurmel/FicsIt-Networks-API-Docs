from __future__ import annotations

import json
from pathlib import Path
from typing import Literal
from typing import TypedDict

from typing_extensions import NotRequired


class PrimitiveTypeRefJSON(TypedDict):
    type: Literal["Int", "Float", "String", "Bool"]


class ArrayTypeRefJSON(TypedDict):
    type: Literal["Array"]
    inner: TypeRefJSON


class StructRefJSON(TypedDict):
    type: Literal["Struct"]
    inner: str


class ClassRefJSON(TypedDict):
    type: Literal["Class", "Object", "Trace"]
    # Sometimes this key is missing...
    subclass: NotRequired[str]


TypeRefJSON = PrimitiveTypeRefJSON | ArrayTypeRefJSON | StructRefJSON | ClassRefJSON


class PropertyJSON(TypedDict):
    internalName: str
    displayName: str
    description: str
    type: TypeRefJSON
    Flag_Attrib: bool
    Flag_ReadOnly: bool
    Flag_Param: bool
    Flag_OutParam: bool
    Flag_RetVal: bool
    Flag_RT_Sync: bool
    Flag_RT_Parallel: bool
    Flag_RT_Async: bool
    Flag_ClassProp: bool


class FunctionJSON(TypedDict):
    internalName: str
    displayName: str
    description: str
    parameters: list[PropertyJSON]
    Flag_VarArgs: bool
    Flag_RT_Sync: bool
    Flag_RT_Parallel: bool
    Flag_RT_Async: bool
    Flag_MemberFunc: bool
    Flag_ClassFunc: bool
    Flag_StaticFunc: bool
    Flag_VarRets: bool


class SignalJSON(TypedDict):
    internalName: str
    displayName: str
    description: str
    parameters: list[PropertyJSON]
    isVarArgs: bool


class ClassJSON(TypedDict):
    internalName: str
    displayName: str
    description: str
    parent: NotRequired[str]
    properties: list[PropertyJSON]
    functions: list[FunctionJSON]
    signals: list[SignalJSON]


class StructJSON(TypedDict):
    internalName: str
    displayName: str
    description: str
    properties: list[PropertyJSON]
    functions: list[FunctionJSON]


class FileJSON(TypedDict):
    classes: list[ClassJSON]
    structs: list[StructJSON]


def load_reflection_data_from_file(path: Path) -> FileJSON:
    return json.loads(path.read_bytes())
