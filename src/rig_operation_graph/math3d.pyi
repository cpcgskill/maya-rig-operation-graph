from cpmel.cmds import Attr
from rig_core.all import *
from rig_operation_graph._utils import *

from typing import Tuple, Union, Any

Number = Union[float, int]
Vector3d = Tuple[Union[float, int], Union[float, int], Union[float, int]]
InValue = Union[Vector3d, Attr, Any]
OutAttr = Attr


def add3d(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def sub3d(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def mul3d(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def div3d(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def pow3d(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def mean3d(ctx: Ctx, *values: InValue) -> OutAttr: pass


def sum3d(ctx: Ctx, *values: InValue) -> OutAttr: pass


def vector_add(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def vector_sub(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def vector_mul(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def vector_div(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def vector_pow(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def vector_mean(ctx: Ctx, *values: InValue) -> OutAttr: pass


def vector_sum(ctx: Ctx, *values: InValue) -> OutAttr: pass


def vector_dot_product(ctx, left: InValue, right: InValue) -> OutAttr: pass


def vector_cross_product(ctx, left: InValue, right: InValue) -> OutAttr: pass


def vector_normalization(ctx, in_attr: InValue) -> OutAttr: pass


__all__ = [
    'add3d', 'sub3d', 'mul3d', 'div3d', 'pow3d', 'mean3d', 'sum3d',
    'vector_add', 'vector_sub', 'vector_mul', 'vector_div', 'vector_pow', 'vector_mean', 'vector_sum',
    'vector_dot_product', 'vector_cross_product', 'vector_normalization',
]
