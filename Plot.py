# Script to create plots and sliders

import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.ticker as ticker
import matplotlib.colors as color


class Page_Slider(matplotlib.widgets.Slider):

    def __init__(self, ax, variable, label, var_init, val_fmt):
        self.variable = variable
        super(Page_Slider, self).__init__(ax, label, 1, variable, valinit=var_init, valfmt=val_fmt)


fig = plt.figure()
# information about the slider
ax1 = fig.add_subplot(111)
cut = 1
axcolor = 'lightgoldenrodyellow'
xaxis = axes([0.2, 0.02, 0.55, 0.02], facecolor=axcolor)
cut_slider = Page_Slider(xaxis, C_t.shape[0], 'x-Grid', cut, '%i')

ax1.plot(r, C_t[cut, :], 'g^')
ax1.set_xlabel(r'$r$', fontsize=18)
ax1.set_ylabel(r'$C$', fontsize=18)


def update_2by2(val):
    cut_val = int(cut_slider.val)
    ax1.clear()
    ax1.plot(r, C_t[cut_val, :], 'g^')

    ax1.set_xlabel(r'$r$', fontsize=18)
    ax1.set_ylabel(r'$C$', fontsize=18)


cut_slider.on_changed(update_2by2)

plt.show()
