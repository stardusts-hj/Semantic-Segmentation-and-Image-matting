# import

from PIL import Image
import numpy as np

pic_name = ['man1', 'man2', 'man3', 'man4', 'man5', 'man6', 'woman1', 'woman2']
image_base = 'E:/MSRA/code/data/'
directory = ['people/', 'people_seg/', 'people_alpha/', 'people_trimap/', 'matting/', 'background/', 'new_image/']
bg = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# choose a piture

def image_matting(fg_path, bg_path, alpha_path, out_path):
    fg = Image.open(fg_path)
    bg = Image.open(bg_path)
    alpha = Image.open(alpha_path)
    fg_w, fg_h = fg.size
    bg_w, bg_h = bg.size
    # Image crop 函数 对背景图进行裁剪 (left, low, right, up)
    bg.show()

    mid_w = int(0.5*bg_w)
    mid_h = int(0.5*bg_h)
    left = mid_w - int(0.5 * fg_w)
    right = mid_w + int(0.5 * fg_w)
    up = mid_h + int(0.5 * fg_h)
    low = mid_h - int(0.5 * fg_h)
    crop_bg = bg.crop((left, low, right, up))
    crop_bg.show()
    resized_bg = crop_bg.resize((fg_w, fg_h))
    resized_bg.show()

    alpha = alpha

    np_alpha = np.array(alpha)/255
    np_fg = np.array(fg)
    np_bg = np.array(resized_bg)
    np_alpha = np.expand_dims(np_alpha, 2).repeat(3, axis=2)
    output = np.multiply(np_fg, np_alpha) + np.multiply(np_bg, (1-np_alpha))
    output_im = Image.fromarray(np.uint8(output)).convert('RGB')
    output_im.show()
    output_im.save(out_path)
    return output_im




if __name__ == "__main__":

    pic_num = 3
    bg_num = 7
    fg_path = image_base + directory[0] + pic_name[pic_num] + '.png'
    bg_path = image_base + directory[5] + bg[bg_num] + '.png'
    alpha_path = image_base + directory[4] + pic_name[pic_num] + '.png'
    out_path = image_base + directory[6] + pic_name[pic_num] + '_bg_' + bg[bg_num] + '.png'
    x = image_matting(fg_path, bg_path, alpha_path, out_path)
    x.show()