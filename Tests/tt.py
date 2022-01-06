import sys
from os.path import dirname, abspath

from Tools.scripts.ndiff import fail

sys.path.append(dirname(dirname(abspath(__file__))))
print("++++++++++: "+ dirname(dirname(abspath(__file__))))
fail(1)