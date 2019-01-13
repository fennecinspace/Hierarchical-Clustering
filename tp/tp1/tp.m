
clear all

a = 2
b = 5

V = a + (b - a) * rand(6,1);

X = round(V)
W=find (X==3)
X(W,1)=100

[U, P] = unique(X)