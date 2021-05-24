function demo()


%% 1 my picture and trimap
fn_im='.\data\my_in\input.png';
fn_mask = '.\data\my_tri\trimap.png';

%% 2
fn_im='.\data\my_in\lamp.png';
fn_mask = '.\data\my_tri\lamp_tri.png';

%% parameters to change according to your requests
fn_im='.\data\input_lowres\doll.png';
fn_mask='.\data\trimap_lowres\Trimap1\doll.png';

%% configuration
addpath(genpath('.\code'));

%% read image and mask
imdata=imread(fn_im);
mask=getMask_onlineEvaluation(fn_mask);

%% compute alpha matte
[alpha]=learningBasedMatting(imdata,mask);

%% show and save results
figure,subplot(2,1,1); imshow(imdata);
imwrite(uint8(alpha*255),"fg.png")
subplot(2,1,2),imshow(uint8(alpha*255));

% imwrite(uint8(alpha*255),fn_save);