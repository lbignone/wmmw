def scatter_circles(x, y, s, c='b', ax=None, vmin=None, vmax=None, **kwargs):
    """
    Make a scatter of circles plot of x vs y, where x and y are sequence
    like objects of the same lengths. The size of circles are in data scale.

    Parameters
    ----------
    x,y : scalar or array_like, shape (n, )
        Input data
    s : scalar or array_like, shape (n, )
        Radius of circle in data scale (ie. in data unit)
    c : color or sequence of color, optional, default : 'b'
        `c` can be a single color format string, or a sequence of color
        specifications of length `N`, or a sequence of `N` numbers to be
        mapped to colors using the `cmap` and `norm` specified via kwargs.
        Note that `c` should not be a single numeric RGB or
        RGBA sequence because that is indistinguishable from an array of
        values to be colormapped.  `c` can be a 2-D array in which the
        rows are RGB or RGBA, however.
    ax : Axes object, optional, default: None
        Parent axes of the plot. It uses gca() if not specified.
    vmin, vmax : scalar, optional, default: None
        `vmin` and `vmax` are used in conjunction with `norm` to normalize
        luminance data.  If either are `None`, the min and max of the
        color array is used.  (Note if you pass a `norm` instance, your
        settings for `vmin` and `vmax` will be ignored.)

    Returns
    -------
    paths : `~matplotlib.collections.PathCollection`

    Other parameters
    ----------------
    kwargs : `~matplotlib.collections.Collection` properties
        eg. alpha, edgecolors, facecolors, linewidths, linestyles, norm, cmap

    Examples
    --------
    a = np.arange(11)
    circles(a, a, a*0.2, c=a, alpha=0.5, edgecolor='none')

    License
    --------
    This code is under [The BSD 3-Clause License]
    (http://opensource.org/licenses/BSD-3-Clause)
    """
    from matplotlib.patches import Circle
    from matplotlib.collections import PatchCollection
    import pylab as plt
    import numpy as np
    # import matplotlib.colors as colors

    if ax is None:
        ax = plt.gca()

    if isinstance(c, str):
        color = c     # ie. use colors.colorConverter.to_rgba_array(c)
    else:
        color = None  # use cmap, norm after collection is created
    kwargs.update(color=color)

    if isinstance(x, (int, float)):
        patches = [Circle((x, y), s), ]
    elif isinstance(s, (int, float)):
        patches = [Circle((x, y), s) for x, y in zip(x, y)]
    else:
        patches = [Circle((x, y), s) for x, y, s in zip(x, y, s)]
    collection = PatchCollection(patches, **kwargs)

    if color is None:
        collection.set_array(np.asarray(c))
        if vmin is not None or vmax is not None:
            collection.set_clim(vmin, vmax)

    ax.add_collection(collection)
    return collection


def filter_by_region(df, xmin, xmax, ymin, ymax, zmin, zmax):
    out = df[(df.x > xmin) &
             (df.x < xmax) &
             (df.y > ymin) &
             (df.y < ymax) &
             (df.z > zmin) &
             (df.z < zmax)]
    return out


def compute_bounding_box(pos, box_lengh):

    x0 = pos.x[0]
    y0 = pos.y[0]
    z0 = pos.z[0]

    dx = pos.x - x0
    dy = pos.y - y0
    dz = pos.z - z0

    dx[dx > box_lengh/2.0] = -(dx[dx > box_lengh/2.0] - box_lengh/2.0)
    dy[dy > box_lengh/2.0] = -(dy[dy > box_lengh/2.0] - box_lengh/2.0)
    dz[dz > box_lengh/2.0] = -(dz[dz > box_lengh/2.0] - box_lengh/2.0)

    dx[dx < -box_lengh/2.0] = -(dx[dx < -1.0 * box_lengh/2.0] + box_lengh/2.0)
    dy[dy < -box_lengh/2.0] = -(dy[dy < -1.0 * box_lengh/2.0] + box_lengh/2.0)
    dz[dz < -box_lengh/2.0] = -(dz[dz < -1.0 * box_lengh/2.0] + box_lengh/2.0)

    x = dx + pos.x[0]
    y = dy + pos.y[0]
    z = dz + pos.z[0]

    extent = []
    center = []
    for k in [x, y, z]:
        kmin = k.min()
        kmax = k.max()
        extent.append(kmax - kmin)
        cent = (kmax + kmin)/2.0

        if cent < 0:
            cent += box_lengh
        elif cent > box_lengh:
            cent -= box_lengh

    return center, extent
