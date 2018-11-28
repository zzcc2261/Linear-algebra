import re
from .Vector import Vector

class Matrix:

    # 基本矩阵初始化返回
    def __init__(self, lit2d):
        """ 初始化构造函数 """
        self._values = [row[:] for row in lit2d] 

    def __repr__(self):
        """ 机器返回 """
        return "Matrix:({})".format(self._values)
    
    def __str__(self):
        """ 用户返回 """
        #TMD实现这个正则一句话正不简单FUCK
        return re.sub(r',',' ',('Matrix:\n['+' \n '.join(str(e)  for e in self._values)+']'))


    # 矩阵的定义属性返回
    def shape(self):
        """ 返回矩阵的形状（行、列） """
        return len(self._values), len(self._values[0])
    
    def row_num(self):
        """ 返回矩阵的行数 """
        return self.shape()[0]

    def col_num(self):
        """ 返回矩阵的列数 """
        return self.shape()[1]
    
    def size(self):
        """ 返回该矩阵元素个数 """
        r, c = self.shape()
        return r*c 

    def __getitem__(self,pos):
        """ 返回该矩阵的‘pos’处的元素 """
        r ,c = pos
        return self._values[r][c]
    
    def row_vector(self, index):
        """ 返回该矩阵的第‘index’个行向量 """
        return Vector(self._values[index])
    
    def col_vector(self, index):
        """ 返回该矩阵的第‘index’个列向量 """
        return Vector([row[index] for row in self._values])


    # 矩阵的基本运算
    def __add__(self, another):
        """ 返回两矩阵相加的的结果 """
        assert self.shape() == another.shape(), \
            "Error in adding. Shape of Maritx must be same !!!"
        return Matrix([[a+b for a, b in zip(self.row_vector(i), another.row_vector(i))]
                    for i in range(self.row_num())]) #此处语法特高阶 半懂！！！！！ 列表表达式？？？
    
    def __sub__(self, another):
        """ 返回两矩阵相减的的结果 """
        assert self.shape() == another.shape(), \
            "Error in adding. Shape of Maritx must be same !!!"
        return Matrix([[a-b for a, b in zip(self.row_vector(i), another.row_vector(i))]
                    for i in range(self.row_num())]) #此处语法特高阶 半懂！！！！！ 列表表达式？？？

    def __mul__(self, k):
        """ 返回矩阵数量乘法的结果 """
        return Matrix([[e*k for e in self.row_vector(i)]
                    for i in range(self.row_num())])

    def __rmul__(self, k):
        """ 返回矩阵数量乘法的结果 """
        return Matrix([[k*e for e in self.row_vector(i)]
                    for i in range(self.row_num())])

    def __truediv__(self, k):
        """ 返回矩阵数量除法的结果 """
        return (1/k) * self

    def __pos__(self):
        """ 返回矩阵取正的结果 """
        return 1 * self

    def __neg__(self):
        """ 返回矩阵取反的结果 """
        return -1 * self
    
    #高级矩阵运算
    def dot(self, another):
        """ 返回矩阵乘法的结果 """
        if isinstance(another, Vector):
            # 矩阵和向量的乘法
            assert self.col_num() == len(another), \
                "Error in Matrix-Vector Multiplication !!!"
            return Vector([self.row_vector(i).dot(another) for i in range(self.row_num())])

        if isinstance(another, Matrix):
            #矩阵和矩阵的乘法
            assert self.col_num() == another.row_num(), \
                "Error in Matrix-Matrix Multiplication !!!"
            return Matrix([[self.row_vector(i).dot(another.col_vector(j)) for j in range(another.col_num())]
                        for i in range(self.row_num())])

    def T(self):
        """ 矩阵的转置 """
        return Matrix([[row[col] for row in self._values] for col in range(self.col_num())]) # ---每个行向量的元素去遍历
        # return Matrix([[e for e in self.col_vector(i) ] for i in len(self.col_num())]) ---直接列向量的元素组成行


    #矩阵的基本性质
    @classmethod
    def zero(cls,r,c):
        """ 返回一个r行c列的零矩阵 """
        return cls([[0]*c for _ in range(r)])
    
    @classmethod
    def unityMatrix(cls,n):
        """ 返回一个n行n列的单位矩阵 """
        m = [[0]*n for _ in range(n)]
        for i in range(n):
            m[i][i] = 1
        return cls(m)
        