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


def is_attr(attr):
    return isinstance(attr, (unicode_t, bytes_t, cc.Attr))


def set_or_connect(in_value, out_attr):
    if is_attr(in_value):
        in_attr = cc.new_object(in_value)
        in_attr >> out_attr
        return
    out_attr.set_value(in_value)


def set_or_connect_3d(in_attr, out_attr):
    attr_plug = out_attr.api1_m_plug()
    child_of_out_attr_list = [cc.new_object(attr_plug.child(i).name()) for i in range(attr_plug.numChildren())]

    if is_attr(in_attr):
        in_attr = cc.new_object(in_attr)
        if in_attr.type() not in {'float', 'double'}:
            in_attr >> out_attr
            return
        in_attr = [in_attr, in_attr, in_attr]
    elif isinstance(in_attr, (int, float)):
        in_attr = [in_attr, in_attr, in_attr]

    set_or_connect(in_attr[0], child_of_out_attr_list[0])
    set_or_connect(in_attr[1], child_of_out_attr_list[1])
    set_or_connect(in_attr[2], child_of_out_attr_list[2])


def set_or_connect_matrix(ctx, in_value, out_attr):
    if is_attr(in_value):
        in_attr = cc.new_object(in_value)
        in_attr >> out_attr
        return
    if isinstance(in_value, (list, tuple)):
        if (len(in_value) == 4 or len(in_value) == 16):
            opened_in_value = [t for i in in_value for t in (i if isinstance(i, (list, tuple)) else [i])]
            if len(opened_in_value) == 16:
                n = ctx.create_node('fourByFourMatrix')
                n.rename('convert_to_matrix')
                for o, i in zip(opened_in_value, ['in00', 'in01', 'in02', 'in03',
                                                  'in10', 'in11', 'in12', 'in13',
                                                  'in20', 'in21', 'in22', 'in23',
                                                  'in30', 'in31', 'in32', 'in33', ]):
                    set_or_connect(o, n.attr(i))
                in_attr = n.attr('output')
                in_attr >> out_attr
                return

    out_attr.set_value(in_value)


def set_or_connect_quaternion(in_value, out_attr):
    if is_attr(in_value):
        in_attr = cc.new_object(in_value)
        in_attr >> out_attr
        return
    attr_plug = out_attr.api1_m_plug()
    out_attr_list = [cc.new_object(attr_plug.child(i).name()) for i in range(attr_plug.numChildren())]

    set_or_connect(in_value[0], out_attr_list[0])
    set_or_connect(in_value[1], out_attr_list[1])
    set_or_connect(in_value[2], out_attr_list[2])
    set_or_connect(in_value[3], out_attr_list[3])


__all__ = ['is_attr', 'set_or_connect', 'set_or_connect_3d', 'set_or_connect_matrix', 'set_or_connect_quaternion']
