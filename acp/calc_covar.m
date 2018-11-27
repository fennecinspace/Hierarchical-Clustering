function V  = cal_covar(X)
    N = size(X,1);

    V = (X' * X) / N;
end