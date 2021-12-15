from licpy.lic import runlic
from licpy.plot import grey_save, grey_show
import numpy as np
import matplotlib.pyplot as plt


# import sympy as sy
# from sympy import cos, sin, pi, S  
# ## the S is sympify, i.e., S(1)/2 means the rational number 1/2, not a float 0.5
# from sympy.matrices import Matrix

# vortex_spacing = S(7) / 8

# a = Matrix([1, 0]) * vortex_spacing
# b = Matrix([cos(pi / 3), sin(pi / 3)]) * vortex_spacing

# def V(x, y):
#     sigma = - S(1) / 6
#     vx, vy = 0, 0
#     for (n, m, s) in [
#         (0, 0, 1),
#         (1, 0, sigma),
#         (0, 1, sigma),
#         (-1, 0, sigma),
#         (0, -1, sigma),
#         (-1, 1, sigma),
#         (1, -1, sigma),
#     ]:
#         xv, yv = n * a + m * b
#         rr = (x - xv) ** 2 + (y - yv) ** 2
#         vx += -s * (y - yv) / rr
#         vy += +s * (x - xv) / rr

#     return vx, vy

# x, y = sy.symbols('x, y')
# v = sy.lambdify((x, y), V(x, y), 'numpy')

# N = 250
# x = np.linspace(-1, 1, N)
# y = np.linspace(-1, 1, N)
# x, y = np.meshgrid(x, y)
# vx, vy = v(x, y)

import h5py
from matplotlib import cm
def show_c(tex, colorData):
    plt.figure()
    tex = tex.T
    colorData = colorData.T
    lim = (0.2,0.8)
    alpha = 1
    lic_data_rgba = cm.ScalarMappable(norm=None,cmap='jet').to_rgba(colorData)
    lic_data_clip_rescale = (tex - lim[0]) / (lim[1] - lim[0])
    lic_data_rgba[...,3] = lic_data_clip_rescale * alpha

    plt.imshow(lic_data_rgba, origin='lower',cmap='jet',alpha=alpha)
    # plt.show()

def show(tex):
    plt.figure()
    tex = tex.T
    plt.imshow(tex, origin = 'lower', cmap='jet')
    # plt.show()

def show_grey(tex):
    plt.figure()
    tex = tex.T
    plt.imshow(tex, origin = 'lower', cmap='Greys')

with h5py.File("D:\CUHK\Data_from_zcao\struct01\struct01_snap52.h5", 'r') as f:
    B_x = f['i_mag_field'][80:120,50:90,50]
    B_y = f['j_mag_field'][80:120,50:90,50]
    rho = f['gas_density'][80:120,50:90,50]
    rho = np.log2(rho)


L = 10
tex = runlic(B_x, B_y, L)
# dir = r'D:\CUHK\SbCodes\licpy\LIC_Sbsource\running_test\test.png'
show(rho)
show_grey(tex)
show_c(tex, rho)
plt.figure()
plt.quiver(B_x.T, B_y.T)
plt.show()


