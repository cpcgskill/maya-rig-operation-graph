# -*-coding:utf-8 -*-
"""
:创建时间: 2022/8/22 10:13
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:Github: https://github.com/cpcgskill
:QQ: 2921251087
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
:爱发电: https://afdian.net/@Phantom_of_the_Cang

"""
from __future__ import unicode_literals, print_function, division
import cpmel.cmds as cc

__all__ = ['current_frame']


def current_frame():
    """
    :rtype: cc.Attr
    """
    return cc.new_object('time1.outTime')
