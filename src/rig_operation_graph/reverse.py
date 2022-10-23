# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/5/11 23:07
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

反转模块
"""
from __future__ import unicode_literals, print_function, division

import sys

import cpmel.cmds as cc

from rig_operation_graph._utils import *


def reverse(ctx, val):
    node = cc.createNode('reverse')
    set_or_connect(val, node.inputX)
    return node.outputX
