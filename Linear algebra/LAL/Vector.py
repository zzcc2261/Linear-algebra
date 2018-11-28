from ._global import EPSILON
import math

class Vector:

    def __init__(self, lst):
        """ 初始化一个向量的维度（所含变量） """
        self._values = lst
    
    def __repr__(self):
        """ 机器返回 """
        return "Vector({})".format(self._values)
    
    def __str__(self):
        """ 用户返回 """
        return "Vector:\n({})".format(" ".join(str(e) for e in self._values))
    
    def underlying_list(self):
        """ 返回向量的的底层列表 """
        return self._values[:]

    # 向量的定义
    def __getitem__(self, index):
        """ 取出向量的第n个元素 """
        return self._values[index]

    def __len__(self):
        """ 返回向量长度（有多少元素） """
        return len(self._values)
    
    def __iter__(self):
        """ 返回向量的迭代器 """
        return self._values.__iter__()
    
    # 向量的基本运算
    def __add__(self, another):
        """ 向量的加法， 返回结果 """
        assert len(self) == len(another), \
            "Error in adding. Length of venctor must be same !!!"
        return Vector([a + b for a, b in zip(self, another)])
        ## zip(self._values, another._values)
        # 返回一个新的向量类 而并非去修改本身！！！

    def __sub__(self, another):
        """ 向量的减法， 返回结果 """
        assert len(self) ==  len(another), \
            "Error in subing. Length of venctor must be same !!!"
        return Vector([a - b for a, b in zip(self, another)])

    def __mul__(self, k):
        """ 向量的数乘， 返回结果 """
        return Vector([k*e for e in self])

    def __rmul__(self, k):
        """ 向量的数乘，返回结果 """
        return Vector([e*k for e in self])

    def __truediv__(self, k):
        """ 向量的数除， 返回结果 """
        return Vector(1/k * self)

    def __pos__(self):
        """ 向量取正 """
        return 1 * self
    
    def __neg__(self):
        """ 向量取负 """
        return -1 * self

    def dot(self, another):
        """ 向量的点乘，返回结果 """
        assert len(self) == len(another), \
            "Error in dot product. Length of venctor must be same !!!"
        return sum(a*b for a, b in zip(self, another))

    # 向量的基本性质
    @classmethod
    def zero(cls, dim):
        """ 返回一个dim维的零向量 """
        return  cls([0] * dim)

    def norm(self):
        """ 返回向量的模 """
        return math.sqrt(sum(e**2 for e in self))
    
    def normalize(self):
        """ 返回向量的单位向量 """
        if self.norm() < EPSILON: # 判断近似度
            raise ZeroDivisionError("Normalize error !!! norm is zero.")
        return  Vector(self / self.norm())