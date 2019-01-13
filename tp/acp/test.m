clear all
clc

M = [
    8, 1, 0;
    4, 6, 5;
    6, 8, 7;
    10, 4, 7;
    8, 2, 5;
    0, 3, 6;
]



X = calc_center(M)

V = calc_covar(X)

[u,l] = eig(V)

l= diag(l)

[l, index] = sort(l,'descend')

u = u(:,index)


i = calc_qua(l)

l=l(1:i)

u = u(:,1:i)

C = X * u

plot(C(:,1), C(:,2), 'r*')
grid on
