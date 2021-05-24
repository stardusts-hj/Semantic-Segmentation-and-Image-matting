function selectedPix = selectPix(img_input,D,selectedRatio)
% select powerful pixels

% parameters
[m,n,z] = size(img_input);	N = m*n;

[B,IX] = sort(sum(D.^2,2));
B = B./B(0.7*N);
C = cumsum(B(1:0.7*N)/(0.7*N));
[~,threshold] = min(abs(C - selectedRatio));
IX = IX(1:threshold);
selectedPix = zeros(m,n);  selectedPix(IX) = 1;

end
