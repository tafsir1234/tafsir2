import os
import sys

downloads = os.path.join(os.path.expanduser("~"), "Downloads")

if sys.platform.startswith("win"):
    os.startfile(downloads)
elif sys.platform == "darwin":
    os.system(f'open "{downloads}"')
else:
    os.system(f'xdg-open "{downloads}"')
