"""
常用函数
"""
"""
查找
get(key, default=None)
返回指定键的值，如果值不在字典中返回default值
setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
popitem()
随机返回并删除字典中的一对键和值(一般删除末尾对)。
items()
以列表返回可遍历的(键, 值) 元组数组
keys()
返回一个迭代器，可以使用 list() 来转换为列表
values()
返回一个迭代器，可以使用 list() 来转换为列表

修改
update(dict2)
字典记录累加
clear()
删除字典内所有元素
"""

"""
查找
L.index(v [, begin[, end]]) | 返回对应元素的索引下标, begin为开始索引，end为结束索引,当 value 不存在时触发ValueError错误 
L.count(x) | 用于统计某个元素在列表中出现的次数 
L.pop([index]) | 删除索引对应的元素，如果不加索引，默认删除最后元素，同时返回删除元素的引用关系
修改
L.insert(index, obj) | 将某个元素插放到列表中指定的位置 
L.extend(lst) | 向列表追加另一个列表
L.remove(x) | 从列表中删除第一次出现在列表中的值 
L.clear() | 清空列表,等同于 L[:] = [] 
L.sort(reverse=False) | 将列表中的元素进行排序，默认顺序按值的小到大的顺序排列 
L.reverse() | 列表的反转，用来改变原列表的先后顺序 
拷贝
L.copy() | 复制此列表（只复制一层，不会复制深层对象) """

"""
常用方法
update() 给集合添加元素
clear() 移除集合中的所有元素
copy() 拷贝一个集合
pop() 随机移除元素
"""

"""
判断
isspace()
如果字符串中只包含空白，则返回 True，否则返回 False.
startswith(substr, beg=0,end=len(string))
检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
endswith(suffix, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
查找
find(str, beg=0 end=len(string))
检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
rfind(str, beg=0,end=len(string))
类似于 find()函数，不过是从右边开始查找.
count(str, beg= 0,end=len(string))
返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
修改
replace(old, new [, max])
把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
lstrip()
截掉字符串左边的空格或指定字符。
rstrip()
删除字符串字符串末尾的空格.
strip([chars])
在字符串上执行 lstrip()和 rstrip()
lower()
转换字符串中所有大写字符为小写.
upper()
转换字符串中的小写字母为大写
swapcase()
将字符串中大写转换为小写，小写转换为大写
对齐
center(width, fillchar)
返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
zfill (width)
返回长度为 width 的字符串，原字符串右对齐，前面填充0
ljust(width[, fillchar])
返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。"""