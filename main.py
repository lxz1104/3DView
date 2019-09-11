import numpy as np
# GPU加速绘制
import mayavi.mlab

"""
三维点云可视化
"""


def viz_mayavi(points, vals="distance"):
    x = points[:, 0]  # x 坐标
    y = points[:, 1]  # y 坐标
    z = points[:, 2]  # z 坐标
    # r = lidar[:, 3]  # 置信值
    d = np.sqrt(x ** 2 + y ** 2)  # 图像到触感器的距离

    if vals == "height":
        col = z
    else:
        col = d

    fig = mayavi.mlab.figure(bgcolor=(0, 0, 0), size=(640, 360))
    mayavi.mlab.points3d(x, y, z,
                         col,  # 色彩值
                         mode="point",
                         colormap='spectral',  # 'bone', 'copper', 'gnuplot'
                         # color=(0, 1, 0),   # 使用固定的颜色
                         figure=fig,
                         )
    mayavi.mlab.show()


points = np.loadtxt('data/6.xyz')
viz_mayavi(points)
