# -*-coding:utf-8 -*-
"""
:创建时间: 2022/10/6 10:58
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
from rig_core.all import *

if False:
    from typing import AnyStr, Any, List, Tuple, Dict

__all__ = ['curve_length']


def curve_length(ctx, curve):
    """
    获得曲线长度

    :type ctx: Ctx
    :type curve: cc.Transform or cc.Curve
    :rtype: cc.Attr
    """
    curve_info = cc.arclen(curve, ch=True, n='curve_length')
    ctx.add_nodes(curve_info)
    return curve_info.attr('arcLength')


if __name__ == '__main__':
    def test():
        from maya_test_tools import open_file, question_open_maya_gui

        cc.eval(
            '''curve -d 3 -p -8.392285 0 -3.922698 -p -7.125865 0 -0.366994 -p -4.593023 0 6.744413 -p 6.853808 0 8.101182 -p -3.133833 0 -3.155691 -p 0.739452 0 -4.285575 -p 5.09475 0 -1.164347 -p 7.272399 0 0.396268 -k 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 5 -k 5 ;''')

        ctx = Ctx()

        print('curve_length', curve_length(ctx, cc.new_object('curve1')).value)

        question_open_maya_gui()


    test()
