%% path_define  
pic_path = 'E:\MSRA\code\data\people\';
tri_path = 'E:\MSRA\code\data\people_trimap\';
out_path = 'E:\MSRA\code\data\matting\';
name = ["man1", "man2", "man3", "man4", "man5", "man6", "woman1", "woman2"];
str0 = ".png";
pic= strcat(pic_path, name(1), str0);

for i = 1:length(name)
    fn_im=strcat(pic_path, name(i), str0);
    fn_mask=strcat(tri_path, name(i), str0);
    save_path = strcat(out_path, name(i), str0);
    addpath(genpath('.\code'));
    imdata=imread(fn_im);
    mask=getMask_onlineEvaluation(fn_mask);
    [alpha]=learningBasedMatting(imdata,mask);
    imwrite(uint8(alpha*255),save_path);
end


