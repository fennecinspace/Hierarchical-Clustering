clear all
clc

T = [
    {'oui'}, {'oui'};
    {'oui'}, {'non'};
    {'non'}, {'oui'};
    {'non'}, {'non'};
    {'oui'}, {'oui'};
    {'oui'}, {'non'};
    {'non'}, {'oui'};
];

% number of indiviuals
N = size(T, 1);
N

% % CODED MATRIX (enteries is 1 / variables is 2)
C = encode_i(T);
C

% % BURT MATRIX
B = calc_burt(C);
B

% % % CONTENGENCE MATRIX (lines are C1 unique, columns are C2 unique)
% % c1 and c2 are indexes of the 2 columns representing the variables
C1 = 1;
C2 = 2;
Con = calc_contengence(T, C1, C2);
Con


% % % FREQUENCY MATRIX
[F, Fi, Fj, Fij] = calc_frequency(Con);
Fij
