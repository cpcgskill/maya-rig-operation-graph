from cpmel.cmds import Attr
from rig_core.all import *
from rig_operation_graph._utils import *

from typing import Union

InValue = Union[float, int, Attr]
OutAttr = Attr

__all__ = ['float_add', 'float_sub', 'float_mul', 'float_div',
           'float_pow', 'float_mean', 'float_max', 'float_min', 'float_sum',
           'float_sin', 'float_cos', 'float_tan']


def float_add(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def float_sub(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def float_mul(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def float_div(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def float_pow(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def float_mean(ctx: Ctx, *values: InValue) -> OutAttr: pass


def float_max(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def float_min(ctx: Ctx, a: InValue, b: InValue) -> OutAttr: pass


def float_sum(ctx: Ctx, *values: InValue) -> OutAttr: pass


def float_sin(ctx: Ctx, value: InValue) -> OutAttr: pass


def float_cos(ctx: Ctx, value: InValue) -> OutAttr: pass


def float_tan(ctx: Ctx, value: InValue) -> OutAttr: pass
