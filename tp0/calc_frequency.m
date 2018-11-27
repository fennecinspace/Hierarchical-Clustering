% returns frequency matrix
% input :
%   C is Contegence MATRIX

function [F, Fi, Fj, Fij] = calc_frequency(C)
    % number of individuals
    N = sum( sum( C ) );

    % main part of frequency matrix
    F = C ./ N;

    % Fi. column
    Fi = sum( C , 2 ) ./ N;

    % F.j column
    Fj = sum( C , 1 ) ./ N;

    % full frequency matrix
    Fij = [[F,Fi]; [Fj, 1] ];
end