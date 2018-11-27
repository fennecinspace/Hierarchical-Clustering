% returns "contengence" matrix
% input :
%   M is individuals / variables MATRIX
%   V1 is index of column representing 1st variable
%   V2 is index of column representing 2nd variable

function C = calc_contengence(M, V1, V2)
    % getting unique variables values
    U1 = unique (M(:, V1));
    U2 = unique (M(:, V2));

    % V1 is 1st dim (i) / V2 is 2nd dim (j)
    C = zeros( size(U1,1) , size(U2,1) );

    % going through individuals
    for i = 1: size ( M(:,1) )
        % getting location of V1 value in F (lines)
        l_i = strmatch(M(i, V1), U1);
        % getting location of V2 value in F (columns)
        c_i = strmatch(M(i, V2), U2);
        % incrementing contengence by 1 at the location
        C(l_i, c_i) =  C(l_i, c_i) + 1;
    end
end