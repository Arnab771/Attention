from split_stat import split_stat
from normal_stat import normal_stat
import sys

arg = sys.argv
help = """
    **HELP**

    python main.py [file]                                  for simple graph(taking messages from both participants in chat together).\n
    python main.py [file] --split [Person1] [Person2]      Takes messages from participants seperately and plots them together. "Person1" and "Person2" should also be the name used in the given file.\n
    """

if "--split" in arg and len(arg) == 5:
    try:
        split_stat(arg[1], arg[3], arg[4])
    except Exception:
        print(help)
elif "--split" not in arg and "--help" not in arg and len(arg) == 2:
    try:
        normal_stat(arg[1])
    except Exception:
        print(help)
elif "--help" in arg and len(arg) == 2:
    print(help)
else:
    print(help)
