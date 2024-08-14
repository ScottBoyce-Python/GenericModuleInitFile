"""
Developed by Scott E. Boyce
Boyce@engineer.com

GenericModuleInitFile is a __init__.py that will auto-load all module folders
that the parent directory holds. It will automatically detect the names of
each valid module folder that it contains.

For example, assume that this file (__init__.py) is placed in the
lib_directory directory and the directory contains three modules
(module1, module2, and module3).

This would have the following structure:

lib_directory/
│
├── __init__.py       # This file
├── module1/
│   ├── __init__.py
│   ├── sub_module1.py
├── module2/
│   ├── __init__.py
│   ├── sub_module1.py
│   └── sub_module2.py
└── module3/
    ├── __init__.py
    ├── sub_module1.py

This file (lib_directory/__init__.py) would then load into memory
each of the three module folders. It is dynamic in that the module folders
can change their name and this file would not have to be changed.

That is you can do:

`import lib_directory`

and the following would be imported:

lib_directory.module1
lib_directory.module2
lib_directory.module3

or you can do

`from lib_directory import *`

and the following would be imported:

module1
module2
module3
"""

from pathlib import Path

import pkgutil
import importlib

# Metadata
__version__ = "0.1.0"

__author__ = "Scott E. Boyce"
__email__ = "boyce@engineer.com"
__license__ = "MIT"
__status__ = "Development"  # set to "Prototype", "Development", "Production"
__maintainer__ = "Scott E. Boyce"
__url__ = "https://github.com/ScottBoyce-Python/GenericModuleInitFile"
__description__ = "An __init__.py file that imports all submodules in the same directory."
__copyright__ = "Copyright (c) 2024 Scott E. Boyce"


# Path to the current directory containing this file
mod_dir = Path(__file__).resolve().parent

# mods = [path for path in mod_dir.iterdir() if path.is_dir() and not path.name.startswith("_")]
# -- Expanded code as what is done above ----------------
# mods = []
# for path in mod_dir.iterdir():
#     if path.is_dir() and "__" not in path.name:
#         mods.append(path)
# ------------------------------------------------------

# Dynamically import all submodules in each module directory
mods = [mod_name for _, mod_name, _ in pkgutil.iter_modules([mod_dir]) if mod_dir.joinpath(mod_name).is_dir()]

__all__ = []
for mod_name in mods:
    # Import the module dynamically
    module = importlib.import_module(f".{mod_name}", __package__)
    # Optionally, you could iterate deeper to import submodules of subdirectories
    globals()[mod_name] = module
    __all__.append(mod_name)
