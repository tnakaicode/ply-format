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
                   (1, 1, 0)],
                  dtype=[('x', 'f4'), ('y', 'f4'),
                         ('z', 'f4')])
face = np.array([([0, 1, 2], 255, 255, 255),
                 ([0, 2, 3], 255, 0, 0),
                 ([0, 1, 3], 0, 255, 0),
                 ([1, 2, 3], 0, 0, 255)],
                dtype=[('vertex_indices', 'i4', (3,)),
                       ('red', 'u1'), ('green', 'u1'),
                       ('blue', 'u1')])

elv = PlyElement.describe(vertex, "vertex")
elf = PlyElement.describe(face, "face")

PlyData([elv, elf]).write('some_binary.ply')
PlyData([elv, elf], text=True).write('some_ascii.ply')

# Force the byte order of the output to big-endian, independently of
# the machine's native byte order
PlyData([elv, elf], byte_order='>').write('some_big_endian_binary.ply')

# Use a file object.  Binary mode is used here, which will cause
# Unix-style line endings to be written on all systems.
# with open('some_ascii.ply', mode='wb') as f:
#     PlyData([el], text=True).write(f)
