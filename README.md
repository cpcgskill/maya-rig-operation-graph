# maya-rig-operation-graph

maya计算图的实现

## 目录

- [快速开始](#快速开始)
    * [安装](#安装)
    * [使用](#使用)
- [版权说明](#版权说明)

## 快速开始

### 安装

注意下方的python是你的Python, 正常情况下可以直接通过python调用, 而Maya的python一般是"C:\Program
Files\Autodesk\<Maya版本>\bin\mayapy.exe"

```commandline
python -m pip install maya-rig-operation-graph
```

在windows下maya的安装例子

注意:

1. 请将Maya路径替换为自己的。
2. 如果你需要安装到maya的python的site-packages下时, 请使用管理员身份运行安装命令. (
   在你没有安装到一个特定目录下时建议你这么干)

```commandline
"C:\Program Files\Autodesk\Maya2018\bin\mayapy.exe" -m pip install maya-rig-operation-graph
```

### 使用

#### 例子

```python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division
from rig_core.all import *
from rig_operation_graph.all import *

ctx = Ctx()

# 使用计算图进行数学运算

out_attr = float_min(ctx, 0, 1)
print(out_attr, out_attr.get_value())

out_attr = float_max(ctx, 0, 1)
print(out_attr, out_attr.get_value())

out_attr = float_mean(ctx, 0, 1)
print(out_attr, out_attr.get_value())

out_attr = float_pow(ctx, 10, 10)
print(out_attr, out_attr.get_value())

out_attr = float_sin(ctx, 0.5)
print(out_attr, out_attr.get_value())
out_attr = float_cos(ctx, 0.5)
print(out_attr, out_attr.get_value())
out_attr = float_tan(ctx, 0.5)
print(out_attr, out_attr.get_value())

# 使用计算图进行向量数学运算

out_attr = vector_add(ctx, (1, 1, 1), (-1, -1, -1))
print(out_attr, out_attr.get_value())

out_attr = vector_sub(ctx, out_attr, (-1, 1, -1))
print(out_attr, out_attr.get_value())

out_attr = vector_mul(ctx, out_attr, (1.5, 1.5, 1.5))
print(out_attr, out_attr.get_value())

out_attr = vector_div(ctx, out_attr, (3, 3, 3))
print(out_attr, out_attr.get_value())

out_attr = vector_pow(ctx, out_attr, (3, 3, 3))
print(out_attr, out_attr.get_value())

out_attr = vector_mean(ctx, out_attr, (0, 0, 0), (0, 0, 0), (0, 0, 0))
print(out_attr, out_attr.get_value())

out_attr = vector_sum(ctx, out_attr, out_attr, out_attr, out_attr)
print(out_attr, out_attr.get_value())
```

## 版权说明

该项目签署了Apache-2.0 授权许可，详情请参阅 LICENSE

