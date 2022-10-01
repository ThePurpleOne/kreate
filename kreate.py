#!/usr/bin/env python

# * PROJ
# * Author: Jonas S.
# * Date: 11/07/21

# ! LOT OF HARDCODED STUFF FOR PERSONNAL USE
# ! LOT OF USELESS REPETITIVE CODE
# ! OBJECTIVE
# ? CREATE A BASIC RUNNING PROJECT 
# ? CREATE SIMPLE C OR HEADER FILE WITH HEADERS
# ? CREATE MAKEFILE
# ! NEED COLORAMA AND OS

import colorama
import os
import re

from colorama import Fore, Back
from datetime import datetime
from shutil import copyfile

# GLOBAL
NAME = "Jonas S."
DATE = datetime.now().strftime('%d/%m/%Y')
BSP = f"{os.path.expanduser('~')}/.kreate" # BASE SOURCE PATH
CWD_PATH = os.path.abspath(".")
BASE_PLACEHOLDER = 	{"DATE":f"{DATE}",
					"NAME":f"{NAME}",}

def gprint(text):
	print(f"{Fore.GREEN}{text}{Fore.RESET}")

def read_file(filename):
	content = ""
	with open(filename, 'r') as f:
		content = f.read()
	return content

def create_file(fileName, content):
	with open(f"{fileName}", 'w', encoding = 'utf-8') as f:
		f.write(content)

def replace_placeholders(file_content, placeholders_dict):
	return re.sub(r"@@(\w+?)@@", lambda match: placeholders_dict[match.group(1)], file_content)

def create_dir_structure(project_name):
	from os import mkdir
	dirs = ["bin", "include", "src"]

	# BASE PROJECT DIRECTORY
	if not os.path.exists(f'{project_name}'):
		mkdir(f'{project_name}')

	# ACTUAL STRUCTURE OF PROJECT
	for d in dirs:
		if not os.path.exists(f'{project_name}/{d}'):
			mkdir(f'{project_name}/{d}')

def create_makefile(path=CWD_PATH):
	copyfile(f"{BSP}/BASE_MAKEFILE", f"{path}/Makefile")

def create_main(path=f"{CWD_PATH}/src"):
	content = read_file(f"{BSP}/BASE_MAIN.c")
	content = replace_placeholders(content, BASE_PLACEHOLDER)
	create_file(f"{path}/main.c", content)

def create_readme(project_name="PROJECT NAME", path=f"{CWD_PATH}"):
	content = read_file(f"{BSP}/BASE_README.md")
	pholder = BASE_PLACEHOLDER.copy()
	pholder["PROJECT"] = project_name
	content = replace_placeholders(content, pholder)
	create_file(f"{path}/readme.md", content)

def create_gitignore(path=f"{CWD_PATH}"):
	copyfile(f"{BSP}/BASE_GITIGNORE", f"{path}/.gitignore")

def create_clang(path=f"{CWD_PATH}"):
	copyfile(f"{BSP}/BASE_CLANG", f"{path}/.clang-format")

def create_module_code(module_name : str, path=f"{CWD_PATH}"):
	content = read_file(f"{BSP}/BASE_CODE.c")
	pholder = BASE_PLACEHOLDER.copy()
	pholder["MOD_NAME"] = module_name
	pholder["UPPER_MOD_NAME"] = module_name.upper()
	content = replace_placeholders(content, pholder)
	create_file(f"{path}/{module_name}.c", content)

def create_module_header(module_name : str, path=f"{CWD_PATH}"):
	content = read_file(f"{BSP}/BASE_HEADER.h")
	pholder = BASE_PLACEHOLDER.copy()
	pholder["MOD_NAME"] = module_name
	pholder["UPPER_MOD_NAME"] = module_name.upper()
	content = replace_placeholders(content, pholder)
	create_file(f"{path}/{module_name}.h", content)

def add_module(module_name):
	if os.path.exists(f'{CWD_PATH}/src'):
		create_module_code(module_name, path=f"{CWD_PATH}/src/.")
	else:
		print("Could not find src folder")

	if os.path.exists(f'{CWD_PATH}/include'):
		create_module_header(module_name, path=f"{CWD_PATH}/include/.")
	else:
		print("Could not find include folder")

def create_complete_project(project_name):
	create_dir_structure(project_name)
	gprint("+ Basic Structure added")
	
	create_makefile(f"{project_name}/.")
	gprint("+ Makefile added")
	
	create_main(f"{project_name}/src")
	gprint("+ main.c added")

	create_readme(f"{project_name}", f"{project_name}/.")
	gprint("+ readme.md added")

	create_gitignore(f"{project_name}/.")
	gprint("+ .gitignore added")

	create_clang( f"{project_name}/.")
	gprint("+ .clang-format added")


## ! MENU
def menu():
	choice = input(
	"1 - Complete project                 \n"
	"2 - Module (code + header)                    \n"
	"3 - Code only                        \n"
	"4 - Header only                      \n"
	"5 - Metafiles (Makefile, readme, clang, gitignore)                    \n"
	"6 - Makefile                    \n"
	"7 - clang                    \n"
	"8 - readme                    \n"
	"9 - gitignore                    \n"
	"\n"

	)

	# PROJECT
	if choice == '1': 
		project_name = input("Project name: ")
		print(f"{Fore.BLUE}Full project is being created.")
		create_complete_project(project_name)
		os.system(f'tree -a {project_name}/')

	# CODE + HEADER (module)
	elif choice == '2':
		add_module(input("Module name: "))
		gprint("+ Module created")
		os.system(f'tree -a')

	# CODE 
	elif choice == '3':
		if os.path.exists(f'{CWD_PATH}/src'):
			create_module_code(input("Code name: "), path=f"{CWD_PATH}/src/.")
		else:
			print("Could not find src folder")
		os.system(f'tree -a')

	# HEADER
	elif choice == '4':
		if os.path.exists(f'{CWD_PATH}/include'):
			create_module_code(input("Header name: "), path=f"{CWD_PATH}/include/.")
		else:
			print("Could not find include folder")
		gprint("+ Header created")
		os.system(f'tree -a')

	# META FILES
	elif choice == '5':
		create_makefile()		
		create_clang()		
		create_readme()		
		create_gitignore()
		gprint("+ Makefile")
		gprint("+ .clang-format")
		gprint("+ readme.md")
		gprint("+ .gitignore")
		os.system(f'tree -a')

	# MAKEFILE
	elif choice == '6':
		create_makefile()		
		gprint("+ Makefile")

	# CLANG
	elif choice == '7':
		create_clang()		
		gprint("+ .clang-format")
	
	# README
	elif choice == '8':
		create_readme()		
		gprint("+ readme.md")
	
	# GITIGNORE
	elif choice == '9':
		create_gitignore()		
		gprint("+ .gitignore")

if __name__ == "__main__":
	colorama.init()
	menu()