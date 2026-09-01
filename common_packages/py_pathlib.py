from pathlib import Path
# This module offers classes representing filesystem paths with semantics appropriate
# for different operating systems

p = Path(".")
print([x for x in p.iterdir() if x.is_dir()])
