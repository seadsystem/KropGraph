import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.path import Path

from backend_kivyagg import FigureCanvasKivyAgg


def draw_battery(box, power_level):
    fig = plt.figure(2)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()

    left, width = .258, (.00485 * power_level)
    bottom, height = .345, .31
    right = left + width
    top = bottom + height
    power = patches.Rectangle(
        (left, bottom), width, height,
        fill=True, transform=ax.transAxes, facecolor='#54d326', clip_on=False, zorder=10
    )
    ax.add_patch(power)
    ######################################
    verts = [
        (.25, .335),  # left, bottom
        (.25, .46),
        (.23, .46),
        (.23, .54),
        (.25, .54),
        (.25, .665),  # left, top
        (.75, .665),  # right, top
        (.75, .54),
        (.77, .54),
        (.77, .46),
        (.75, .46),
        (.75, .335),  # right, bottom
        (0., 0.),  # ignored
    ]

    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO,
             Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
             Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
             Path.CLOSEPOLY,
             ]

    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='black', lw=7, zorder=5)
    ax.add_patch(patch)
    ###########################################################
    verts2 = [(.51, .6), (.40, .47), (.491, .47), (.48, .38), (.59, .53), (.50, .53), (0., 0.)]
    codes2 = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO,
              Path.LINETO, Path.LINETO, Path.CLOSEPOLY, ]
    path2 = Path(verts2, codes2)
    patch2 = patch2 = patches.PathPatch(path2, facecolor='yellow', lw=2, zorder=20)
    ax.add_patch(patch2)

    box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
