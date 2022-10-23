# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/5/12 21:47
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

混合计算模块
"""
from __future__ import unicode_literals, print_function, division

import sys

import cpmel.cmds as cc

from rig_operation_graph._utils import *

from rig_core.all import *

if False:
    from typing import AnyStr, Any, List, Tuple, Dict

__all__ = ['blend']


def blend(ctx, a, b, control):
    """
    混合两个属性

    :type ctx: Ctx
    :type a: cc.Attr or float
    :type b: cc.Attr or float
    :type control: cc.Attr or float
    :rtype: cc.Attr
    """
    node = cc.createNode('blendTwoAttr')
    set_or_connect(a, node.attr('input[0]'))
    set_or_connect(b, node.attr('input[1]'))
    set_or_connect(control, node.attributesBlender)
    return node.output


if __name__ == '__main__':
    def test():
        from maya_test_tools import open_file, question_open_maya_gui

        ctx = Ctx()

        print('blend', blend(ctx, 2, 1, 0.5).value)

        question_open_maya_gui()


    test()
