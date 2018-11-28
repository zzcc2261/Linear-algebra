from LAL.Vector import Vector
from LAL.Matrix import Matrix
from LAL.LinearSystem import LinearSystem

if __name__ == '__main__':
    A7 = Matrix([[1,-1,2,0,3],
        [-1,1,0,2,-5],[1,-1,4,2,4],
        [-2,2,-5,-1,-3]])
    b7 = Vector([1,5,13,-1])
    ls7 = LinearSystem(A7,b7)
    print(ls7)
    ls7.gauss_jordan_elimination()
    print(ls7)