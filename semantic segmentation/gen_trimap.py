"""
get alpha channel of a picture and generate the trimap
(trimap 是一个三值图，确定前景为255，确定背景为0，不确定的边缘为128)
"""
import numpy as np
from PIL import Image
from scipy import ndimage
# ndimage.morphology.distance_transform_edt()



def generate_trimap(alpha):
    fg = np.array(np.equal(alpha, 255).astype(np.float32))
    unknown = np.array(np.not_equal(alpha, 0).astype(np.float32))  # unknown = alpha > 0
    unknown = unknown - fg
    unknown = ndimage.morphology.distance_transform_edt(unknown == 0) <= np.random.randint(1, 13)
    trimap = fg * 255
    trimap[unknown] = 128
    return trimap.astype(np.uint8)

if __name__ == "__main__":
    im_path = 'E:/MSRA/code/semantic segmentation/seg_a.png'
    alpha = Image.open(im_path)
    alpha = alpha
    trimap = generate_trimap(alpha)
    trimap = Image.fromarray(trimap)
    trimap.save("trimap.png")
    trimap.show()

