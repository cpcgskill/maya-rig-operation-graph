# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/5/11 22:41
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

限制模块
"""
from __future__ import unicode_literals, print_function, division

import sys

import cpmel.cmds as cc

from rig_operation_graph._utils import *

from rig_core.all import *

if False:
    from typing import AnyStr, Any, List, Tuple, Dict

__all__ = ['clamp']


def clamp(ctx, input, min=0.0, max=1.0):
    """
    限制最大最小值

    :type ctx: Ctx
    :type input: cc.Attr or float
    :type min: cc.Attr or float
    :type max: cc.Attr or float
    :rtype: cc.Attr
    """
    node = cc.createNode('clamp')
    set_or_connect(min, node.minR)
    set_or_connect(max, node.maxR)
    set_or_connect(input, node.inputR)
    return node.outputR


if __name__ == '__main__':
    def test():
        from maya_test_tools import open_file, question_open_maya_gui

        ctx = Ctx()

        print('clamp', clamp(ctx, 1.5, 0, 0.8).value)

        question_open_maya_gui()


    test()
