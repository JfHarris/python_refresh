# modules code using my_module.py

# importing from a module
# from my_module import my_func

# my_func()

# package code using my_main_package and subpackage folders

# importing main package
from my_main_package import some_main_script

# importing subpackage
from my_main_package.subpackage import my_subscript

# calling from my_main_package
some_main_script.report_main()

# calling from sub_package
my_subscript.sub_report()

# then run this file in command line