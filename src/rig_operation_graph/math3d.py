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


def vector_dot_product(ctx, left, right):
    n = ctx.create_node('vectorProduct')
    n.rename('vector_dot_product')
    n['operation'] = 1
    n['normalizeOutput'] = False

    set_or_connect_3d(left, n.attr('input1'))
    set_or_connect_3d(right, n.attr('input2'))
    return n.attr('outputX')


def vector_cross_product(ctx, left, right):
    n = ctx.create_node('vectorProduct')
    n.rename('vector_cross_product')
    n['operation'] = 2
    n['normalizeOutput'] = False

    set_or_connect_3d(left, n.attr('input1'))
    set_or_connect_3d(right, n.attr('input2'))
    return n.attr('output')


def vector_normalization(ctx, in_attr):
    if is_attr(in_attr):
        in_attr = cc.new_object(in_attr)
        if in_attr.type() == 'float3':
            n = in_attr.node()
            if cc.objectType(n) == 'vectorProduct':
                n['normalizeOutput'] = True
                return in_attr
    n = ctx.create_node('vectorProduct')
    n.rename('vector_normalization')
    n['operation'] = 0
    n['normalizeOutput'] = True

    set_or_connect_3d(in_attr, n.attr('input1'))
    return n.attr('output')


__all__ = [
    'add3d', 'sub3d', 'mul3d', 'div3d', 'pow3d', 'mean3d', 'sum3d',
    'vector_add', 'vector_sub', 'vector_mul', 'vector_div', 'vector_pow', 'vector_mean', 'vector_sum',
    'vector_dot_product', 'vector_cross_product', 'vector_normalization',
]

if __name__ == "__main__":
    from rig_core.ctx import Ctx
    from maya_test_tools import question_open_maya_gui

    ctx = Ctx()

    out_attr = vector_add(ctx, (1, 1, 1), (-1, -1, -1))
    print(out_attr, out_attr.get_value())

    out_attr = vector_sub(ctx, out_attr, (-1, 1, -1))
    print(out_attr, out_attr.get_value())

    out_attr = vector_mul(ctx, out_attr, (1.5, 1.5, 1.5))
    print(out_attr, out_attr.get_value())

    out_attr = vector_div(ctx, out_attr, (3, 3, 3))
    print(out_attr, out_attr.get_value())

    out_attr = vector_pow(ctx, out_attr, (3, 3, 3))
    print(out_attr, out_attr.get_value())

    out_attr = vector_mean(ctx, out_attr, (0, 0, 0), (0, 0, 0), (0, 0, 0))
    print(out_attr, out_attr.get_value())

    out_attr = vector_sum(ctx, out_attr, out_attr, out_attr, out_attr)
    print(out_attr, out_attr.get_value())

    out_attr = vector_dot_product(ctx, (1, 0, 0), (1, 0, 0))
    print(out_attr, out_attr.get_value())
    assert 0.999 < out_attr.get_value() < 1.0001

    out_attr = vector_cross_product(ctx, (0, 0, 1), (1, 0, 0))
    print(out_attr, out_attr.get_value())
    assert -0.0001 < out_attr.get_value().x < 0.0001
    assert 0.999 < out_attr.get_value().y < 1.0001
    assert -0.0001 < out_attr.get_value().z < 0.0001

    out_attr = vector_normalization(ctx, (0, 0.5, 0))
    print(out_attr, out_attr.get_value())
    assert -0.0001 < out_attr.get_value().x < 0.0001
    assert 0.999 < out_attr.get_value().y < 1.0001
    assert -0.0001 < out_attr.get_value().z < 0.0001

    out_attr = vector_cross_product(ctx, (0, 0, 5), (5, 0, 0))
    print(out_attr, out_attr.get_value())
    new_out_attr = vector_normalization(ctx, out_attr)
    print(new_out_attr, new_out_attr.get_value())
    assert new_out_attr == out_attr

    question_open_maya_gui()
