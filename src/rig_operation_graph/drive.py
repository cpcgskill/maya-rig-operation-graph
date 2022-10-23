# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/5/11 21:38
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

驱动模块
"""
from __future__ import unicode_literals, print_function, division

import sys

import cpmel.cmds as cc

from rig_operation_graph._utils import *


def range(ctx, drive, old_min=0.0, old_max=1.0, new_min=0.0, new_max=1.0):
    node = cc.createNode('setRange')
    set_or_connect(old_min, node.oldMinX)
    set_or_connect(old_max, node.oldMaxX)
    set_or_connect(new_min, node.minX)
    set_or_connect(new_max, node.maxX)
    drive >> node.valueX
    return node.outValueX
