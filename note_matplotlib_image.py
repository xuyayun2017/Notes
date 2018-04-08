# coding=utf-8
'''
   image 图片显示
'''
import matplotlib.pyplot as plt
import numpy as np

# image data
if __name__ == '__main__':
 a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)

"""
for the value of "interpolation", check this:
http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
for the value of "origin"= ['upper', 'lower'], check this:
http://matplotlib.org/examples/pylab_examples/image_origin.html
"""

# 这是颜色的标注
# 主要使用imshow来显示图片，这里暂时不适用图片来显示，采用色块的方式演示。
plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
plt.colorbar(shrink=.90)  # 这是颜色深度的标注，shrink表示压缩比例

plt.xticks(())
plt.yticks(())
plt.show()