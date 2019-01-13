% returns the same matrix incoded 
% input :
%   M is individuals / variables MATRIX

function C = encode_i(M)
%     UC = [];
%     U = [];
    C = [];
    
    % going through variables
    for j = 1: size(M,2)
        
        % extracting variable column
        V = M(:,j);
        % getting unique variable values
        u = unique(V);
        % creating an identity matrix to code the unique variable values
        uc = eye(size(u,1), size(u,1));

        % code wille contain the coded variable values for each row
        code= [];
        
        % going through the rows 
        for i=1: size(V,1)
            % getting position of variable value in identity matrix
            p_i = strmatch(V(i,1), u);
            
            % getting code in identity matrix at the returned position
            % and using it to fill the new coded individuals/variables matrix
            code= [code; uc(p_i,:)];
        end

        C = [C, code];
%         UC = [UC, uc];
%         U = [U, u];
    end
end