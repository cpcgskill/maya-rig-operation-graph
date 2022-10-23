# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/5/29 7:15
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function, division

import sys

import cpmel.cmds as cc

from rig_operation_graph._utils import *

operation_map = {
    '==': 0,
    '!=': 1,
    '>': 2,
    '>=': 3,
    '<': 4,
    '<=': 5,
}


def float_logic(ctx, l_attr, r_attr, operation, true_attr, false_attr):
    node = cc.createNode('condition')
    set_or_connect(l_attr, node.firstTerm)
    set_or_connect(r_attr, node.secondTerm)

    node['operation'] = operation_map[operation]

    set_or_connect(true_attr, node.colorIfTrueR)
    set_or_connect(false_attr, node.colorIfFalseR)
    return node.outColorR


def float_equal(ctx, l_attr, r_attr, true_attr, false_attr):
    """等于"""
    return float_logic(ctx, l_attr, r_attr, '==', true_attr, false_attr)


def float_not_equal(ctx, l_attr, r_attr, true_attr, false_attr):
    """不等于"""
    return float_logic(ctx, l_attr, r_attr, '!=', true_attr, false_attr)


def float_greater(ctx, l_attr, r_attr, true_attr, false_attr):
    """大于"""
    return float_logic(ctx, l_attr, r_attr, '>', true_attr, false_attr)


def float_greater_or_equal(ctx, l_attr, r_attr, true_attr, false_attr):
    """大于等于"""
    return float_logic(ctx, l_attr, r_attr, '>=', true_attr, false_attr)


def float_less(ctx, l_attr, r_attr, true_attr, false_attr):
    """小于"""
    return float_logic(ctx, l_attr, r_attr, '<', true_attr, false_attr)


def float_less_or_equal(ctx, l_attr, r_attr, true_attr, false_attr):
    """小于等于"""
    return float_logic(ctx, l_attr, r_attr, '<=', true_attr, false_attr)


if __name__ == '__main__':
    from rig_core.ctx import Ctx
    from maya_test_tools import question_open_maya_gui

    c = Ctx()

    node = cc.createNode('transform')

    out_attr = float_equal(
        c,
        node.tx, 0,
        1, 0
    )
    print(out_attr, out_attr.get_value())

    question_open_maya_gui()
