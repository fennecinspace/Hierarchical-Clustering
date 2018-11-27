T = [
  {"oui"}, {"oui"};
  {"oui"}, {"non"};
  {"non"}, {"oui"};
  {"non"}, {"non"};
  {"oui"}, {"oui"};
  {"oui"}, {"non"};
  {"non"}, {"oui"};
]

size(T)

V1 = T(:,1)

U = unique(V1)

cc = eye(size(U,1), size(U,1))

mat_code = []
for j = 1: size(T,2)
  code= [];
  V = T(:,j)
  for i=1: size(V,1)

    S = strmatch(V(i,1), U);
    code=[code;cc(S,:)];
  end
  code
  mat_code = [mat_code, code]
end