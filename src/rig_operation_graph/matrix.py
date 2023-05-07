# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/4/1 20:03
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

矩阵模块
"""
from __future__ import unicode_literals, print_function, division
import cpmel.cmds as cc
from rig_operation_graph._utils import *

is_load, _, _ = cc.pluginInfo('matrixNodes', q=True, set=True)
if not is_load:
    print("loading matrixNodes.mll")
    cc.loadPlugin('matrixNodes', qt=True)

__all__ = [
    'new_matrix_from_transform',
    'new_matrix_from_transform_attr',
    'matrix_from_transform',
    'new_matrix_from_transform_value',
    'matrix_from_transform_using_quaternion',
    'copy_matrix',
    'add_matrix', 'mult_matrix',
    'inverse_matrix', 'pass_matrix',
    'matrix_to_transform_attr', 'to_transform_attr',
]


def new_matrix_from_transform(ctx, t=None, r=None, s=None, sh=None):
    n = ctx.create_node('composeMatrix')
    n.rename('matrix_from_transform')
    if t is not None:
        set_or_connect_3d(t, n.attr('inputTranslate'))
    if r is not None:
        set_or_connect_3d(r, n.attr('inputRotate'))
    if s is not None:
        set_or_connect_3d(s, n.attr('inputScale'))
    if sh is not None:
        set_or_connect_3d(sh, n.attr('inputShear'))
    return n.attr('outputMatrix')


new_matrix_from_transform_attr = new_matrix_from_transform

matrix_from_transform = new_matrix_from_transform


def matrix_from_transform_using_quaternion(ctx, t=None, q=None, s=None, sh=None):
    n = ctx.create_node('composeMatrix')
    n.rename('matrix_from_transform_using_quaternion')
    if t is not None:
        set_or_connect_3d(t, n.attr('inputTranslate'))
    if q is not None:
        n['useEulerRotation'] = False
        set_or_connect_quaternion(q, n.attr('inputQuat'))
    if s is not None:
        set_or_connect_3d(s, n.attr('inputScale'))
    if sh is not None:
        set_or_connect_3d(sh, n.attr('inputShear'))
    return n.attr('outputMatrix')


def new_matrix_from_transform_value(ctx, t, r, s, sh=(0.0, 0.0, 0.0)):
    n = ctx.create_node('composeMatrix')
    n.rename('new_matrix_from_transform')
    n['inputTranslate'] = t
    n['inputRotate'] = r
    n['inputScale'] = s
    n['inputShear'] = sh
    # n['inputRotateOrder'] = ro
    return n.attr('outputMatrix')


def copy_matrix(ctx, m):
    n = ctx.create_node('decomposeMatrix')
    n.rename('copy_matrix')
    n['inputMatrix'] = m.get_value()
    t, r, s, sh = (
        n.attr('outputTranslate').get_value(),
        n.attr('outputRotate').get_value(),
        n.attr('outputScale').get_value(),
        n.attr('outputShear').get_value()
    )
    cc.delete(n)
    return new_matrix_from_transform_value(ctx, t, r, s, sh)


def add_matrix(ctx, *m_list):
    n = ctx.create_node('addMatrix')
    n.rename('add_matrix')
    for i, a in enumerate(m_list):
        set_or_connect_matrix(ctx, a, n.attr('matrixIn[{}]'.format(i)))
    return n.attr('matrixSum')


def mult_matrix(ctx, *m_list):
    n = ctx.create_node('multMatrix')
    n.rename('mult_matrix')
    for i, a in enumerate(m_list):
        set_or_connect_matrix(ctx, a, n.attr('matrixIn[{}]'.format(i)))
    return n.attr('matrixSum')


def inverse_matrix(ctx, m):
    n = ctx.create_node('inverseMatrix')
    n.rename('inverse_matrix')
    set_or_connect_matrix(ctx, m, n.attr('inputMatrix'))
    return n.attr('outputMatrix')


def pass_matrix(ctx, m, s):
    n = ctx.create_node('passMatrix')
    n.rename('pass_matrix')
    set_or_connect_matrix(ctx, m, n.inMatrix)
    set_or_connect(s, n.inScale)
    return n.outMatrix


def matrix_to_transform_attr(ctx, a):
    n = ctx.create_node('decomposeMatrix')
    n.rename('matrix_to_transform')
    set_or_connect_matrix(ctx, a, n.attr('inputMatrix'))
    return n.attr('outputTranslate'), n.attr('outputRotate'), n.attr('outputScale'), n.attr('outputShear')


to_transform_attr = matrix_to_transform_attr

if __name__ == "__main__":
    from rig_core.ctx import Ctx

    cc.eval("""
file -f -new;
""")
    ctx = Ctx()
    a = new_matrix_from_transform_value(ctx, (1, 5, 6), (360, 0, 0), (1, 1, 1), (0, 0, 0))
    # 俩个b切换之后下方的计算结果应该一致
    # b = new_matrix_from_transform_value(ctx, (1, 5, 6), (360, 0, 0), (1, 1, 1), (0, 0, 0))
    b = [[1.0, 0.0, 0.0, 0.0],
         [0.0, 1.0, -2.4492935982947064e-16, 0.0],
         [0.0, 2.4492935982947064e-16, 1.0, 0.0],
         [1.0, 5.0, 6.0, 1.0], ]
    out_attr = add_matrix(ctx, a, b)
    print("add_matrix", out_attr, 'value == ', out_attr.get_value())

    out_attr = mult_matrix(ctx, a, b)
    print("mult_matrix", out_attr, 'value == ', out_attr.get_value())

    out_attr = inverse_matrix(ctx, a)
    print("inverse_matrix", out_attr, 'value == ', out_attr.get_value())

    out_attr = pass_matrix(ctx, a, 2)
    print("pass_matrix", out_attr, 'value == ', out_attr.get_value())

    out_attr = copy_matrix(ctx, a)
    print("copy_matrix", out_attr, 'value == ', out_attr.get_value())
    print('check org matrix == new matrix', a.get_value() == out_attr.get_value())

    out_attr = matrix_to_transform_attr(ctx, a)
    print("matrix_to_transform_attr", out_attr)
