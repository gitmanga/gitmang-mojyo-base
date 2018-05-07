import os
from glob import glob

# for i, path in enumerate(glob('vol.1/*')):
#     new = (os.path.join(os.path.dirname(path), '%03d.png'%i))
#     os.rename(path, new)

for i, path in enumerate(glob('Vol.001/*')):
    print('- -', path.replace('\\', '/'))