from operator import truediv
from typing import Any
from typing import Optional

from .. import util as util

div = truediv

class Operators:
    def __and__(self, other: Any): ...
    def __or__(self, other: Any): ...
    def __invert__(self): ...
    def op(
        self,
        opstring: Any,
        precedence: int = ...,
        is_comparison: bool = ...,
        return_type: Optional[Any] = ...,
    ): ...
    def bool_op(self, opstring: Any, precedence: int = ...): ...
    def operate(self, op: Any, *other: Any, **kwargs: Any) -> None: ...
    def reverse_operate(self, op: Any, other: Any, **kwargs: Any) -> None: ...

class custom_op:
    __name__: str = ...
    opstring: Any = ...
    precedence: Any = ...
    is_comparison: Any = ...
    natural_self_precedent: Any = ...
    eager_grouping: Any = ...
    return_type: Any = ...
    def __init__(
        self,
        opstring: Any,
        precedence: int = ...,
        is_comparison: bool = ...,
        return_type: Optional[Any] = ...,
        natural_self_precedent: bool = ...,
        eager_grouping: bool = ...,
    ) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def __call__(self, left: Any, right: Any, **kw: Any): ...

class ColumnOperators(Operators):
    timetuple: Any = ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    __hash__: Any = ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def is_distinct_from(self, other: Any): ...
    def is_not_distinct_from(self, other: Any): ...
    isnot_distinct_from: Any = ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
    def __neg__(self): ...
    def __contains__(self, other: Any): ...
    def __getitem__(self, index: Any): ...
    def __lshift__(self, other: Any): ...
    def __rshift__(self, other: Any): ...
    def concat(self, other: Any): ...
    def like(self, other: Any, escape: Optional[Any] = ...): ...
    def ilike(self, other: Any, escape: Optional[Any] = ...): ...
    def in_(self, other: Any): ...
    def not_in(self, other: Any): ...
    notin_: Any = ...
    def not_like(self, other: Any, escape: Optional[Any] = ...): ...
    notlike: Any = ...
    def not_ilike(self, other: Any, escape: Optional[Any] = ...): ...
    notilike: Any = ...
    def is_(self, other: Any): ...
    def is_not(self, other: Any): ...
    isnot: Any = ...
    def startswith(self, other: Any, **kwargs: Any): ...
    def endswith(self, other: Any, **kwargs: Any): ...
    def contains(self, other: Any, **kwargs: Any): ...
    def match(self, other: Any, **kwargs: Any): ...
    def regexp_match(self, pattern: Any, flags: Optional[Any] = ...): ...
    def regexp_replace(
        self, pattern: Any, replacement: Any, flags: Optional[Any] = ...
    ): ...
    def desc(self): ...
    def asc(self): ...
    def nulls_first(self): ...
    nullsfirst: Any = ...
    def nulls_last(self): ...
    nullslast: Any = ...
    def collate(self, collation: Any): ...
    def __radd__(self, other: Any): ...
    def __rsub__(self, other: Any): ...
    def __rmul__(self, other: Any): ...
    def __rdiv__(self, other: Any): ...
    def __rmod__(self, other: Any): ...
    def between(self, cleft: Any, cright: Any, symmetric: bool = ...): ...
    def distinct(self): ...
    def any_(self): ...
    def all_(self): ...
    def __add__(self, other: Any): ...
    def __sub__(self, other: Any): ...
    def __mul__(self, other: Any): ...
    def __div__(self, other: Any): ...
    def __mod__(self, other: Any): ...
    def __truediv__(self, other: Any): ...
    def __rtruediv__(self, other: Any): ...

def commutative_op(fn: Any): ...
def comparison_op(fn: Any): ...
def from_() -> None: ...
def function_as_comparison_op() -> None: ...
def as_() -> None: ...
def exists() -> None: ...
def is_true(a: Any) -> None: ...

istrue = is_true

def is_false(a: Any) -> None: ...

isfalse = is_false

def is_distinct_from(a: Any, b: Any): ...
def is_not_distinct_from(a: Any, b: Any): ...

isnot_distinct_from = is_not_distinct_from

def is_(a: Any, b: Any): ...
def is_not(a: Any, b: Any): ...

isnot = is_not

def collate(a: Any, b: Any): ...
def op(a: Any, opstring: Any, b: Any): ...
def like_op(a: Any, b: Any, escape: Optional[Any] = ...): ...
def not_like_op(a: Any, b: Any, escape: Optional[Any] = ...): ...

notlike_op = not_like_op

def ilike_op(a: Any, b: Any, escape: Optional[Any] = ...): ...
def not_ilike_op(a: Any, b: Any, escape: Optional[Any] = ...): ...

notilike_op = not_ilike_op

def between_op(a: Any, b: Any, c: Any, symmetric: bool = ...): ...
def not_between_op(a: Any, b: Any, c: Any, symmetric: bool = ...): ...

notbetween_op = not_between_op

def in_op(a: Any, b: Any): ...
def not_in_op(a: Any, b: Any): ...

notin_op = not_in_op

def distinct_op(a: Any): ...
def any_op(a: Any): ...
def all_op(a: Any): ...
def startswith_op(
    a: Any, b: Any, escape: Optional[Any] = ..., autoescape: bool = ...
): ...
def not_startswith_op(
    a: Any, b: Any, escape: Optional[Any] = ..., autoescape: bool = ...
): ...

notstartswith_op = not_startswith_op

def endswith_op(
    a: Any, b: Any, escape: Optional[Any] = ..., autoescape: bool = ...
): ...
def not_endswith_op(
    a: Any, b: Any, escape: Optional[Any] = ..., autoescape: bool = ...
): ...

notendswith_op = not_endswith_op

def contains_op(
    a: Any, b: Any, escape: Optional[Any] = ..., autoescape: bool = ...
): ...
def not_contains_op(
    a: Any, b: Any, escape: Optional[Any] = ..., autoescape: bool = ...
): ...

notcontains_op = not_contains_op

def match_op(a: Any, b: Any, **kw: Any): ...
def regexp_match_op(a: Any, b: Any, flags: Optional[Any] = ...): ...
def not_regexp_match_op(a: Any, b: Any, flags: Optional[Any] = ...): ...
def regexp_replace_op(
    a: Any, b: Any, replacement: Any, flags: Optional[Any] = ...
): ...
def not_match_op(a: Any, b: Any, **kw: Any): ...

notmatch_op = not_match_op

def comma_op(a: Any, b: Any) -> None: ...
def filter_op(a: Any, b: Any) -> None: ...
def concat_op(a: Any, b: Any): ...
def desc_op(a: Any): ...
def asc_op(a: Any): ...
def nulls_first_op(a: Any): ...

nullsfirst_op = nulls_first_op

def nulls_last_op(a: Any): ...

nullslast_op = nulls_last_op

def json_getitem_op(a: Any, b: Any) -> None: ...
def json_path_getitem_op(a: Any, b: Any) -> None: ...
def is_comparison(op: Any): ...
def is_commutative(op: Any): ...
def is_ordering_modifier(op: Any): ...
def is_natural_self_precedent(op: Any): ...
def is_boolean(op: Any): ...
def mirror(op: Any): ...
def is_associative(op: Any): ...
def is_precedent(operator: Any, against: Any): ...
