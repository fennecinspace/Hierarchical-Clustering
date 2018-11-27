function B = calc_burt(M)
    N = size(M, 1);
    B = M'* M ./ N; 
end