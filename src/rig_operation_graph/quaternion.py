# -*-coding:utf-8 -*-
"""
:创建时间: 2023/5/2 7:53
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:Github: https://github.com/cpcgskill
:QQ: 2921251087
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
:爱发电: https://afdian.net/@Phantom_of_the_Cang

"""
from __future__ import unicode_literals, print_function, division

if False:
    from typing import *

import cpmel.cmds as cc
from rig_core.ctx import Ctx
from rig_operation_graph._utils import *

is_load, _, _ = cc.pluginInfo('quatNodes', q=True, set=True)
if not is_load:
    print("loading quatNodes.mll")
    cc.loadPlugin('quatNodes', qt=True)


def quaternion_product(ctx, left, right):
    n = ctx.create_node('quatProd')
    set_or_connect_quaternion(left, n.attr('input1Quat'))
    set_or_connect_quaternion(right, n.attr('input2Quat'))
    return n.attr('outputQuat')


def quaternion_add(ctx, left, right):
    n = ctx.create_node('quatAdd')
    set_or_connect_quaternion(left, n.attr('input1Quat'))
    set_or_connect_quaternion(right, n.attr('input2Quat'))
    return n.attr('outputQuat')


def quaternion_sub(ctx, left, right):
    n = ctx.create_node('quatSub')
    set_or_connect_quaternion(left, n.attr('input1Quat'))
    set_or_connect_quaternion(right, n.attr('input2Quat'))
    return n.attr('outputQuat')


def quaternion_invert(ctx, value):
    n = ctx.create_node('quatInvert')
    set_or_connect_quaternion(value, n.attr('inputQuat'))
    return n.attr('outputQuat')


def quaternion_normalize(ctx, value):
    n = ctx.create_node('quatNormalize')
    set_or_connect_quaternion(value, n.attr('inputQuat'))
    return n.attr('outputQuat')


def quaternion_conjugate(ctx, value):
    n = ctx.create_node('quatConjugate')
    set_or_connect_quaternion(value, n.attr('inputQuat'))
    return n.attr('outputQuat')


def quaternion_to_euler(ctx, value):
    n = ctx.create_node('quatToEuler')
    set_or_connect_quaternion(value, n.attr('inputQuat'))
    return n.attr('outputRotate')


def quaternion_from_euler(ctx, value):
    n = ctx.create_node('eulerToQuat')
    set_or_connect_3d(value, n.attr('inputRotate'))
    return n.attr('outputQuat')


__all__ = [
    'quaternion_product',
    'quaternion_add',
    'quaternion_sub',
    'quaternion_invert',
    'quaternion_normalize',
    'quaternion_conjugate',
    'quaternion_to_euler',
    'quaternion_from_euler',
]

if __name__ == '__main__':
    from maya_test_tools import question_open_maya_gui

    ctx = Ctx()

    # Test quaternion_product
    out_attr = quaternion_product(ctx, (0, 0, 0, 1), (0, 0, 0, 1))
    print("quaternion_product:", out_attr.get_value())

    # Test quaternion_add
    out_attr = quaternion_add(ctx, (0, 0, 0, 1), (0, 0, 0, 1))
    print("quaternion_add:", out_attr.get_value())

    # Test quaternion_sub
    out_attr = quaternion_sub(ctx, (0, 0, 0, 1), (0, 0, 0, 1))
    print("quaternion_sub:", out_attr.get_value())

    # Test quaternion_invert
    out_attr = quaternion_invert(ctx, (0, 0, 0, 1))
    print("quaternion_invert:", out_attr.get_value())

    # Test quaternion_normalize
    out_attr = quaternion_normalize(ctx, (0, 0, 0, 1))
    print("quaternion_normalize:", out_attr.get_value())

    # Test quaternion_conjugate
    out_attr = quaternion_conjugate(ctx, (0, 0, 0, 1))
    print("quaternion_conjugate:", out_attr.get_value())

    # Test quaternion_to_euler
    out_attr = quaternion_to_euler(ctx, (0, 0, 0, 1))
    print("quaternion_to_euler:", out_attr.get_value())

    # Test quaternion_from_euler
    out_attr = quaternion_from_euler(ctx, (0, 0, 0))
    print("quaternion_from_euler:", out_attr.get_value())

    question_open_maya_gui()
