from LAL.Matrix import Matrix


if __name__=="__main__":

    A = Matrix([[1,-1,-1,-1],[-1,1,-1,-1],[-1,-1,1,-1],[-1,-1,-1,1]])
    # B = Matrix([[3,4,5],[1,2,3]])
    B = Matrix([[1,-1,-1,-1],[-1,1,-1,-1],[-1,-1,1,-1],[-1,-1,-1,1]])
    C = Matrix([[1,2,3],[4,5,6]])
    I3 = Matrix.unityMatrix(3)
    Z3 = Matrix.zero(3,3)

    # print('m1:{} + m2:{} = {}'.format(A, B, A+B))
    
    
    