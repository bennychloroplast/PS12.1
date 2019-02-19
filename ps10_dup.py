
from math import sin, cos, radians, degrees

def rotate_n_degrees(vector_init , theta):
    X = [[ cos( radians(theta) ) , -sin( radians(theta) ) ] , [ sin( radians(theta) ) , cos( radians(theta) ) ]]
    vector_result = []
    vector_result.append(X[0][0]*vector_init[0] + X[0][1]*vector_init[1])
    vector_result.append(X[1][0]*vector_init[0] + X[1][1]*vector_init[1])
    return vector_result
