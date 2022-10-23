# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/5/29 6:50
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

unicode_t = type('')
bytes_t = type(b'')

if sys.version_info.major < 3:
    num_t = (int, long, float)
else:
    num_t = (int, float)


def set_or_connect(in_value, out_attr):
    if isinstance(in_value, (unicode_t, bytes_t, cc.Attr)):
        in_attr = cc.new_object(in_value)
        in_attr >> out_attr
        return
    out_attr.set_value(in_value)


def set_or_connect_3d(in_value, out_attr):
    if isinstance(in_value, (unicode_t, bytes_t, cc.Attr)):
        in_attr = cc.new_object(in_value)
        in_attr >> out_attr
        return
    out_attr.set_value((in_value[0], in_value[1], in_value[2]))


def set_or_connect_matrix(in_value, out_attr):
    if isinstance(in_value, (unicode_t, bytes_t, cc.Attr)):
        in_attr = cc.new_object(in_value)
        in_attr >> out_attr
        return
    out_attr.set_value(in_value)


__all__ = ['set_or_connect', 'set_or_connect_3d', 'set_or_connect_matrix']
