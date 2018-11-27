function X = calc_center(M)
    X = [];

    for i = 1 : size(M, 2)
       g = sum(M(:,i)) / size(M, 1);
       X = [X, M(:, i) - g];

    end
end