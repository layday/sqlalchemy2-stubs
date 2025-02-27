from typing import Any
from typing import Optional

from . import roles as roles
from .base import Executable as Executable
from .base import SchemaVisitor as SchemaVisitor
from .elements import ClauseElement as ClauseElement
from .. import exc as exc
from .. import util as util
from ..util import topological as topological

class _DDLCompiles(ClauseElement): ...

class DDLElement(roles.DDLRole, Executable, _DDLCompiles):
    target: Any = ...
    on: Any = ...
    dialect: Any = ...
    callable_: Any = ...
    def execute(
        self, bind: Optional[Any] = ..., target: Optional[Any] = ...
    ): ...
    def against(self, target: Any) -> None: ...
    state: Any = ...
    def execute_if(
        self,
        dialect: Optional[Any] = ...,
        callable_: Optional[Any] = ...,
        state: Optional[Any] = ...,
    ) -> None: ...
    def __call__(self, target: Any, bind: Any, **kw: Any): ...
    def bind(self): ...
    bind: Any = ...

class DDL(DDLElement):
    __visit_name__: str = ...
    statement: Any = ...
    context: Any = ...
    def __init__(
        self,
        statement: Any,
        context: Optional[Any] = ...,
        bind: Optional[Any] = ...,
    ) -> None: ...

class _CreateDropBase(DDLElement):
    element: Any = ...
    bind: Any = ...
    if_exists: Any = ...
    if_not_exists: Any = ...
    def __init__(
        self,
        element: Any,
        bind: Optional[Any] = ...,
        if_exists: bool = ...,
        if_not_exists: bool = ...,
        _legacy_bind: Optional[Any] = ...,
    ) -> None: ...
    @property
    def stringify_dialect(self): ...

class CreateSchema(_CreateDropBase):
    __visit_name__: str = ...
    quote: Any = ...
    def __init__(
        self, name: Any, quote: Optional[Any] = ..., **kw: Any
    ) -> None: ...

class DropSchema(_CreateDropBase):
    __visit_name__: str = ...
    quote: Any = ...
    cascade: Any = ...
    def __init__(
        self,
        name: Any,
        quote: Optional[Any] = ...,
        cascade: bool = ...,
        **kw: Any,
    ) -> None: ...

class CreateTable(_CreateDropBase):
    __visit_name__: str = ...
    columns: Any = ...
    include_foreign_key_constraints: Any = ...
    def __init__(
        self,
        element: Any,
        bind: Optional[Any] = ...,
        include_foreign_key_constraints: Optional[Any] = ...,
        if_not_exists: bool = ...,
    ) -> None: ...

class _DropView(_CreateDropBase):
    __visit_name__: str = ...

class CreateColumn(_DDLCompiles):
    __visit_name__: str = ...
    element: Any = ...
    def __init__(self, element: Any) -> None: ...

class DropTable(_CreateDropBase):
    __visit_name__: str = ...
    def __init__(
        self, element: Any, bind: Optional[Any] = ..., if_exists: bool = ...
    ) -> None: ...

class CreateSequence(_CreateDropBase):
    __visit_name__: str = ...

class DropSequence(_CreateDropBase):
    __visit_name__: str = ...

class CreateIndex(_CreateDropBase):
    __visit_name__: str = ...
    def __init__(
        self,
        element: Any,
        bind: Optional[Any] = ...,
        if_not_exists: bool = ...,
    ) -> None: ...

class DropIndex(_CreateDropBase):
    __visit_name__: str = ...
    def __init__(
        self, element: Any, bind: Optional[Any] = ..., if_exists: bool = ...
    ) -> None: ...

class AddConstraint(_CreateDropBase):
    __visit_name__: str = ...
    def __init__(self, element: Any, *args: Any, **kw: Any) -> None: ...

class DropConstraint(_CreateDropBase):
    __visit_name__: str = ...
    cascade: Any = ...
    def __init__(
        self, element: Any, cascade: bool = ..., **kw: Any
    ) -> None: ...

class SetTableComment(_CreateDropBase):
    __visit_name__: str = ...

class DropTableComment(_CreateDropBase):
    __visit_name__: str = ...

class SetColumnComment(_CreateDropBase):
    __visit_name__: str = ...

class DropColumnComment(_CreateDropBase):
    __visit_name__: str = ...

class DDLBase(SchemaVisitor):
    connection: Any = ...
    def __init__(self, connection: Any) -> None: ...

class SchemaGenerator(DDLBase):
    checkfirst: Any = ...
    tables: Any = ...
    preparer: Any = ...
    dialect: Any = ...
    memo: Any = ...
    def __init__(
        self,
        dialect: Any,
        connection: Any,
        checkfirst: bool = ...,
        tables: Optional[Any] = ...,
        **kwargs: Any,
    ) -> None: ...
    def visit_metadata(self, metadata: Any) -> None: ...
    def visit_table(
        self,
        table: Any,
        create_ok: bool = ...,
        include_foreign_key_constraints: Optional[Any] = ...,
        _is_metadata_operation: bool = ...,
    ) -> None: ...
    def visit_foreign_key_constraint(self, constraint: Any) -> None: ...
    def visit_sequence(self, sequence: Any, create_ok: bool = ...) -> None: ...
    def visit_index(self, index: Any, create_ok: bool = ...) -> None: ...

class SchemaDropper(DDLBase):
    checkfirst: Any = ...
    tables: Any = ...
    preparer: Any = ...
    dialect: Any = ...
    memo: Any = ...
    def __init__(
        self,
        dialect: Any,
        connection: Any,
        checkfirst: bool = ...,
        tables: Optional[Any] = ...,
        **kwargs: Any,
    ) -> None: ...
    def visit_metadata(self, metadata: Any): ...
    def visit_index(self, index: Any, drop_ok: bool = ...) -> None: ...
    def visit_table(
        self,
        table: Any,
        drop_ok: bool = ...,
        _is_metadata_operation: bool = ...,
    ) -> None: ...
    def visit_foreign_key_constraint(self, constraint: Any) -> None: ...
    def visit_sequence(self, sequence: Any, drop_ok: bool = ...) -> None: ...

def sort_tables(
    tables: Any,
    skip_fn: Optional[Any] = ...,
    extra_dependencies: Optional[Any] = ...,
): ...
def sort_tables_and_constraints(
    tables: Any,
    filter_fn: Optional[Any] = ...,
    extra_dependencies: Optional[Any] = ...,
    _warn_for_cycles: bool = ...,
): ...
