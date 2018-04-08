# coding=utf-8
'''
   gridspec
'''
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
# 首先，定义网格的布局为3行3列
gs = gridspec.GridSpec(3, 3)
# 这里表示从0行全部都是ax1的
ax1 = plt.subplot(gs[0, :])
ax1.set_title(r'$ax1\_title$')

# 这里表示第一行中0列和1列都是ax2的
ax2 = plt.subplot(gs[1, :2])
ax2.set_title(r'$ax2\_title$')

# 这里表示第一行中2列是ax3的
ax3 = plt.subplot(gs[1:, 2])
ax3.set_title(r'$ax3\_title$')

# 这里表示最后一行中0列是ax4的
ax4 = plt.subplot(gs[-1, 0])
ax4.set_title(r'$ax4\_title$')

# 这里表示最后一行中倒数第二列是ax5的
ax5 = plt.subplot(gs[-1, -2])
ax5.set_title(r'$ax5\_title$')

plt.tight_layout()
plt.show()