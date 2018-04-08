# coding=utf-8
'''
   easy to define structure 分格显示
'''
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
# sharex表示共享X轴，sharey表示共享y轴
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
# 显示点（1, 2）, （1, 2）
ax11.scatter([1, 2], [1, 2])

ax11.set_title('11')
ax12.set_title('11')
ax21.set_title('21')
ax22.set_title('22')

plt.tight_layout()
if __name__ == '__main__':
  plt.show()