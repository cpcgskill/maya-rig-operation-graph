# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/5/29 5:30
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function, division
import cpmel.cmds as cc
from rig_operation_graph._utils import *

__all__ = ['float_add', 'float_sub', 'float_mul', 'float_div',
           'float_pow', 'float_mean', 'float_max', 'float_min', 'float_sum',
           'float_sin', 'float_cos', 'float_tan']


def float_add(ctx, a, b):
    n = ctx.create_node('plusMinusAverage')
    n.rename('float_add')
    n['operation'] = 1
    set_or_connect(a, n.input1D[0])
    set_or_connect(b, n.input1D[1])
    return n.output1D


def float_sub(ctx, a, b):
    n = ctx.create_node('plusMinusAverage')
    n.rename('float_sub')
    n['operation'] = 2
    set_or_connect(a, n.input1D[0])
    set_or_connect(b, n.input1D[1])
    return n.output1D


def float_mul(ctx, a, b):
    n = ctx.create_node('multiplyDivide')
    n.rename('float_mul')
    n['operation'] = 1
    set_or_connect(a, n.input1X)
    set_or_connect(b, n.input2X)
    return n.outputX


def float_div(ctx, a, b):
    n = ctx.create_node('multiplyDivide')
    n.rename('float_div')
    n['operation'] = 2
    set_or_connect(a, n.input1X)
    set_or_connect(b, n.input2X)
    return n.outputX


def float_pow(ctx, a, b):
    n = ctx.create_node('multiplyDivide')
    n.rename('float_pow')
    n['operation'] = 3
    set_or_connect(a, n.input1X)
    set_or_connect(b, n.input2X)
    return n.outputX


def float_mean(ctx, *values):
    n = ctx.create_node('plusMinusAverage')
    n.rename('float_mean')
    n['operation'] = 3
    for id_, v in enumerate(values):
        set_or_connect(v, n.input1D[id_])
    return n.output1D


def float_max(ctx, a, b):
    n = ctx.create_node('condition')
    n.rename('float_max')
    n['operation'] = 2
    set_or_connect(a, n.firstTerm)
    set_or_connect(b, n.secondTerm)
    set_or_connect(a, n.colorIfTrueR)
    set_or_connect(b, n.colorIfFalseR)

    return n.outColorR


def float_min(ctx, a, b):
    n = ctx.create_node('condition')
    n.rename('float_min')
    n['operation'] = 4
    set_or_connect(a, n.firstTerm)
    set_or_connect(b, n.secondTerm)
    set_or_connect(a, n.colorIfTrueR)
    set_or_connect(b, n.colorIfFalseR)

    return n.outColorR


def float_sum(ctx, *values):
    n = ctx.create_node('plusMinusAverage')
    n.rename('float_sum')
    n['operation'] = 1
    for id_, v in enumerate(values):
        set_or_connect(v, n.input1D[id_])
    return n.output1D


def float_sin(ctx, value):
    exp = cc.expression(s='', o='', ae=False, uc='all')
    ctx.add_nodes(exp)
    exp.rename('float_sin')
    input_attr = ctx.add_attribute(exp, 'input_value')
    output_attr = ctx.add_attribute(exp, 'output_value')
    cc.expression(
        exp,
        e=True,
        s="{} = sin({})".format(output_attr.name(), input_attr.name())
    )
    set_or_connect(value, input_attr)
    return output_attr


def float_cos(ctx, value):
    exp = cc.expression(s='', o='', ae=False, uc='all')
    ctx.add_nodes(exp)
    exp.rename('float_cos')
    input_attr = ctx.add_attribute(exp, 'input_value')
    output_attr = ctx.add_attribute(exp, 'output_value')
    cc.expression(
        exp,
        e=True,
        s="{} = cos({})".format(output_attr.name(), input_attr.name())
    )
    set_or_connect(value, input_attr)
    return output_attr


def float_tan(ctx, value):
    exp = cc.expression(s='', o='', ae=False, uc='all')
    ctx.add_nodes(exp)
    exp.rename('float_tan')
    input_attr = ctx.add_attribute(exp, 'input_value')
    output_attr = ctx.add_attribute(exp, 'output_value')
    cc.expression(
        exp,
        e=True,
        s="{} = tan({})".format(output_attr.name(), input_attr.name())
    )
    set_or_connect(value, input_attr)
    return output_attr


if __name__ == "__main__":
    from rig_core.ctx import Ctx
    from maya_test_tools import question_open_maya_gui

    c = Ctx()

    out_attr = float_min(c, 0, 1)
    print(out_attr, out_attr.get_value())

    out_attr = float_max(c, 0, 1)
    print(out_attr, out_attr.get_value())

    out_attr = float_mean(c, 0, 1)
    print(out_attr, out_attr.get_value())

    out_attr = float_pow(c, 10, 10)
    print(out_attr, out_attr.get_value())

    out_attr = float_sin(c, 0.5)
    print(out_attr, out_attr.get_value())
    out_attr = float_cos(c, 0.5)
    print(out_attr, out_attr.get_value())
    out_attr = float_tan(c, 0.5)
    print(out_attr, out_attr.get_value())

    question_open_maya_gui()
