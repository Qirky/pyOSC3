import sys

if sys.version_info[0] > 2:

    from .OSC3 import *

else:

    from OSC2 import *
