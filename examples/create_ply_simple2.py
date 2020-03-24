import numpy as np
from plyfile import PlyData
from plyfile import PlyElement, PlyListProperty

plydata = PlyData.read('tet.ply')

# with open('tet.ply', 'rb') as f:
#    plydata = PlyData.read(f)

plydata.elements[0].name
plydata.elements[0].data[0]
plydata.elements[0].data[0]

vertex = np.array([(0, 0, 0),
                   (0, 1, 1),
                   (1, 0, 1),
                   (1, 1, 0),
                   (1, 2, 0)],
                  dtype=[('x', 'f4'), ('y', 'f4'),
                         ('z', 'f4')])
face = np.array([([0, 1, 2], 0.0),
                 ([0, 1, 3], 2.0),
                 ([0, 2, 3], 1.0),
                 ([1, 2, 3], 3.0),
                 ([1, 2, 4], 4.0)],
                dtype=[('vertex_indices', 'i4', (3,)), ('color4', 'f4')])

elv = PlyElement.describe(vertex, "vertex")
elf = PlyElement.describe(face, "face")

PlyData([elv, elf], text=True).write('./create_ply_simple2.ply')
