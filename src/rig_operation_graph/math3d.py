# -*-coding:utf-8 -*-
"""
:创建时间: 2022/8/4 16:45
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:Github: https://github.com/cpcgskill
:QQ: 2921251087
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
:爱发电: https://afdian.net/@Phantom_of_the_Cang

3d向量计算图模块
"""
from __future__ import unicode_literals, print_function, division
import cpmel.cmds as cc
from rig_operation_graph._utils import *

__all__ = [
    'add3d', 'sub3d', 'mul3d', 'div3d', 'pow3d', 'mean3d', 'sum3d',
    'vector_add', 'vector_sub', 'vector_mul', 'vector_div', 'vector_pow', 'vector_mean', 'vector_sum'
]


def vector_add(ctx, a, b):
    n = ctx.create_node('plusMinusAverage')
    n.rename('vector_add')
    n['operation'] = 1
    set_or_connect_3d(a, n.input3D[0])
    set_or_connect_3d(b, n.input3D[1])
    return n.output3D


add3d = vector_add


def vector_sub(ctx, a, b):
    n = ctx.create_node('plusMinusAverage')
    n.rename('vector_sub')
    n['operation'] = 2
    set_or_connect_3d(a, n.input3D[0])
    set_or_connect_3d(b, n.input3D[1])
    return n.output3D


sub3d = vector_sub


def vector_mul(ctx, a, b):
    n = ctx.create_node('multiplyDivide')
    n.rename('vector_mul')
    n['operation'] = 1
    set_or_connect_3d(a, n.input1)
    set_or_connect_3d(b, n.input2)
    return n.output


mul3d = vector_mul


def vector_div(ctx, a, b):
    n = ctx.create_node('multiplyDivide')
    n.rename('vector_div')
    n['operation'] = 2
    set_or_connect_3d(a, n.input1)
    set_or_connect_3d(b, n.input2)
    return n.output


div3d = vector_div


def vector_pow(ctx, a, b):
    n = ctx.create_node('multiplyDivide')
    n.rename('vector_pow')
    n['operation'] = 3
    set_or_connect_3d(a, n.input1)
    set_or_connect_3d(b, n.input2)
    return n.output


pow3d = vector_pow


def vector_mean(ctx, *values):
    n = ctx.create_node('plusMinusAverage')
    n.rename('vector_mean')
    n['operation'] = 3
    for id_, v in enumerate(values):
        set_or_connect_3d(v, n.input3D[id_])
    return n.output3D


mean3d = vector_mean


def vector_sum(ctx, *values):
    n = ctx.create_node('plusMinusAverage')
    n.rename('vector_sum')
    n['operation'] = 1
    for id_, v in enumerate(values):
        set_or_connect_3d(v, n.input3D[id_])
    return n.output3D


sum3d = vector_sum

if __name__ == "__main__":
    from rig_core.ctx import Ctx
    from maya_test_tools import question_open_maya_gui

    c = Ctx()

    out_attr = vector_add(c, (1, 1, 1), (-1, -1, -1))
    print(out_attr, out_attr.get_value())

    out_attr = vector_sub(c, out_attr, (-1, 1, -1))
    print(out_attr, out_attr.get_value())

    out_attr = vector_mul(c, out_attr, (1.5, 1.5, 1.5))
    print(out_attr, out_attr.get_value())

    out_attr = vector_div(c, out_attr, (3, 3, 3))
    print(out_attr, out_attr.get_value())

    out_attr = vector_pow(c, out_attr, (3, 3, 3))
    print(out_attr, out_attr.get_value())

    out_attr = vector_mean(c, out_attr, (0, 0, 0), (0, 0, 0), (0, 0, 0))
    print(out_attr, out_attr.get_value())

    out_attr = vector_sum(c, out_attr, out_attr, out_attr, out_attr)
    print(out_attr, out_attr.get_value())

    # question_open_maya_gui()
