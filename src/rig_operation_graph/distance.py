# -*-coding:utf-8 -*-
"""
:创建时间: 2022/8/4 22:45
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:Github: https://github.com/cpcgskill
:QQ: 2921251087
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
:爱发电: https://afdian.net/@Phantom_of_the_Cang

"""
from __future__ import unicode_literals, print_function, division
from rig_operation_graph._utils import *

__all__ = ['distance']


def distance(ctx, a, b):
    node = ctx.create_node('distanceBetween')
    node.rename('distance')
    set_or_connect_3d(a, node.point1)
    set_or_connect_3d(b, node.point2)
    return node.distance


if __name__ == '__main__':
    from rig_core.ctx import Ctx

    c = Ctx()
    out_attr = distance(c, (-1, -1, -1), (1, 1, 1))
    print(out_attr, out_attr.get_value())
