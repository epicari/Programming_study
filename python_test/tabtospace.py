#tab to 4Xspace

import sys

src = sys.argv[1] #python tabtospace.py src dst
dst = sys.argv[2]

f = open(src)
old_f = f.read()
f.close()

new_f = old_f.replace("\t", " "*4)

f = open(dst, 'w')
f.write(new_f)
f.close()
