import matplotlib.pyplot as plt
from LAL.Matrix import Matrix
from LAL.Vector import Vector

if __name__=='__main__':
    points = [[0,0],[0,5],[3,5],[3,4],[1,4],
                [1,3],[2,3],[2,2],[1,2],[1,0]]
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.figure(figsize=(5,5))
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.plot(x,y)
    plt.show()

    p = Matrix(points)
    
    T = Matrix([[2,0],[0,1.5]])

    p2 = T.dot(p.T())
    plt.plot([p2.col_vector])