import numpy as np
from mayavi import mlab
from plyfile import PlyData

iterable = (x * x for x in range(5))
print(np.fromiter(iterable, float))

ply = PlyData.read("./tet.ply")
print(ply['vertex']['x'])
print(ply['face'])
print(ply['face']['vertex_indices'])
print(ply['face'].count)


def test_triangular_mesh():
    """An example of a cone, ie a non-regular mesh defined by its
        triangles.
    """
    n = 8
    t = np.linspace(-np.pi, np.pi, n)
    z = np.exp(1j * t)
    x = z.real.copy()
    y = z.imag.copy()
    z = np.zeros_like(x)

    triangles = [(0, i, i + 1) for i in range(1, n)]
    px = np.r_[0, x]
    py = np.r_[0, y]
    pz = np.r_[1, z]
    pt = np.r_[0, t]

    return mlab.triangular_mesh(px, py, pz, triangles, scalars=pt)


test_triangular_mesh()
mlab.show()
