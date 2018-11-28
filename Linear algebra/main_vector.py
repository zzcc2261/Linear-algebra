from LAL.Vector import Vector


if __name__=='__main__':
    vec1 = Vector([5,2])
    print(vec1)
    print("vec[0]={}, vec[1]={}".format(vec1[0], vec1[1]))

    vec2 = Vector([2,3])
    print('{} + {} = {}'.format(vec1, vec2, vec1+vec2))

    print('{} - {} = {}'.format(vec1, vec2, vec1-vec2))
    
    print('{} * {} = {}'.format(vec1, 5, vec1*5))
    print('{} * {} = {}'.format(5, vec2, 5*vec2))

    vec0 = Vector.zero(2)

    print('{}'.format(vec2.norm()))
    print('{}'.format(vec2.normalize().norm()))
    print(vec1.dot(vec2))