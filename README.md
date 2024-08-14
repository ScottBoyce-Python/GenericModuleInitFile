# GenericModuleInitFile

GenericModuleInitFile is a Python `__init__.py` file that will auto-load all module folders that the parent directory holds. It will automatically detect the names of each valid module folder that it contains. This is only done for the first level of modules and will not detect modules within modules.

For example, assume that this `__init__.py` is placed in the a directory called `lib_directory` directory, which contains three modules, `module1`, `module2`, and `module3` and has the following structure:  

```
lib_directory/
│
├── __init__.py    # <- GenericModuleInitFile
├── module1/
│  ├── __init__.py
│  ├── sub_module1.py
├── module2/
│  ├── __init__.py
│  ├── sub_module1.py
│  └── sub_module2.py
└── module3/
  ├── __init__.py
  ├── sub_module1.py
```

This file `lib_directory/__init__.py` would then load into memory each of the three module folders. It is dynamic in that the module folders can change their name and this file would not have to be changed. That is you can do:  
```
import lib_directory
```
and the following would be imported:  
`lib_directory.module1`  
`lib_directory.module2`  
`lib_directory.module3`

or you can do  
```
from lib_directory import *
```
and the following would be imported:  
`module1`  
`module2`  
`module3`  

This is not meant for use in a final production product. Instead it provides a convenient way to nest multiple modules in a single folder during development. This reduces the need to constantly update the  `__init__.py`  each time a module name is changed or code is restructured. After the final stable design is made, then the final  `__init__.py`  can be written.



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author
Scott E. Boyce
