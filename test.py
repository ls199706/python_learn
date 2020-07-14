import pandas as pd
import numpy as np
a = pd.DataFrame(np.arange(10).reshape(2, 5))    # ndarray创建
# print(a)
dt = {'one': pd.Series([1, 2, 3], ['a', 'b', 'c']),
      'two': pd.Series([4, 5, 6, 7], ['e', 'f', 'g', 'h'])}
d = pd.DataFrame(dt)                              # 键对应列索引，与原始列表索引组合，不存在的元素系统自动添加NAN
dl = {'one': [1, 2, 3, 4], 'two': [5, 6, 7, 8]}
e = pd.DataFrame(dl, index=['a', 'b', 'c', 'd'])                                # 列表生成
dl = {'城市': ['北京', '上海', '上海', '广州', '深圳'],
      '环比': ['101.5', '101.2', '101.3', '102.0', '100.1'],
      '同比': ['120.7', '127.3', '119.4', '140.9', '101.4'],
      '定基': ['121.4', '127.8', '120.0', '145.5', '101.6']}
g = pd.DataFrame(dl, ['c1', 'c2', 'c3', 'c4', 'c5'])
# print(g)
# print(g['同比'])            # 横向取一行
# print(g.loc['c1'])          # 纵向取一列
# print(g['城市']['c2'])       # 取特点的一个数据
g = g.reindex(index=['c5', 'c4', 'c3', 'c2', 'c1'])     # 改变排序
# print(g)

g = g.reindex(columns=['定基', '同比', '环比', '城市'])
# print(g)

newc = g.columns.insert(4, '新增')              # 标签取出作为一个对象，新增一个“新增”
newd = g.reindex(columns=newc, fill_value=200)
print(newd)
print(newc)