# -*-coding:utf-8 -*-
"""
:创建时间: 2022/8/23 8:54
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
from rig_operation_graph._utils import *

__all__ = ['float_gauss', 'float_noise', 'float_rand']


def float_gauss(ctx, value):
    exp = cc.expression(s='', o='', ae=True, uc='all')
    ctx.add_nodes(exp)
    exp.rename('float_gauss')
    input_attr = ctx.add_attribute(exp, 'input_value')
    output_attr = ctx.add_attribute(exp, 'output_value')
    cc.expression(
        exp,
        e=True,
        s="{} = gauss({})".format(output_attr.name(), input_attr.name())
    )
    set_or_connect(value, input_attr)
    return output_attr


def float_noise(ctx, value):
    exp = cc.expression(s='', o='', ae=True, uc='all')
    ctx.add_nodes(exp)
    exp.rename('float_noise')
    input_attr = ctx.add_attribute(exp, 'input_value')
    output_attr = ctx.add_attribute(exp, 'output_value')
    cc.expression(
        exp,
        e=True,
        s="{} = noise({})".format(output_attr.name(), input_attr.name())
    )
    set_or_connect(value, input_attr)
    return output_attr


def float_rand(ctx, min, max):
    exp = cc.expression(s='', o='', ae=True, uc='all')
    ctx.add_nodes(exp)
    exp.rename('float_rand')
    input_min_attr = ctx.add_attribute(exp, 'input_min_value')
    input_max_attr = ctx.add_attribute(exp, 'input_max_value')
    output_attr = ctx.add_attribute(exp, 'output_value')
    cc.expression(
        exp,
        e=True,
        s="{} = rand({}, {})".format(output_attr.name(), input_min_attr.name(), input_max_attr.name())
    )
    set_or_connect(min, input_min_attr)
    set_or_connect(max, input_max_attr)
    return output_attr
