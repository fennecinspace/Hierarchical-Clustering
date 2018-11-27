function i = calc_qua(l)
    for i = 1 : size(l,1)
        qua = sum(l(1:i)) / sum(l,1);
        if qua >= 0.80
            break
        end
    end
end