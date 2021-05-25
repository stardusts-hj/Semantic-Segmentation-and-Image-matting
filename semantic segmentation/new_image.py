# import
from PIL import Image
import numpy as np

pic_name = ['man1', 'man2', 'man3', 'man4', 'man5', 'man6', 'woman1', 'woman2']
image_base = 'E:/MSRA/code/data/'
directory = ['people/', 'people_seg/', 'people_alpha/', 'people_trimap/', 'matting/', 'background/', 'new_image/']
bg = ['1', '2', '3', '4']

# choose a piture

def image_matting(fg_path, bg_path, alpha_path, out_path):
    fg = Image.open(fg_path)
    bg = Image.open(bg_path)
    alpha = Image.open(alpha_path)
    fg_w, fg_h = fg.size
    bg_w, bg_h = bg.size
    # Image crop 函数 对背景图进行裁剪 (left, up, right, low)
    mid_w = int(0.5*bg_w)
    mid_h = int(0.5*bg_h)
    left = mid_w - int(0.5 * fg_w)
    right = mid_w + int(0.5 * fg_w)
    up = mid_h + int(0.5 * fg_h)
    low = mid_h + int(0.5 * fg_h)
    resized_bg = bg.crop(left, up, right, low)
    resized_bg = resized_bg.resize((fg_w, fg_h))
    alpha = alpha/255
    

    output = fg * alpha + bg * (1-alpha)

    return




if __name__ == "__main__":
