# * PROJ
# * Author: Jonas S.
# * Date: 11/07/21
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
BSP = ".kreate" # BASE SOURCE PATH
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

def create_readme(project_name, path=f"{CWD_PATH}"):
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
	create_module_code(module_name, path="src")
	create_module_header(module_name)

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
	"1 - COMPLETE PROJECT                 \n"
	"2 - CODE + HEADER                    \n"
	"3 - CODE ONLY                        \n"
	"4 - HEADER ONLY                      \n"
	"5 - MAKEFILE ONLY                    \n"
	"\n"

	)

	# PROJECT
	if choice == '1': 
		print(f"{Fore.BLUE}FULL PROJECT IS BEING CREATED.")
		createCompleteProject()

	## CODE + HEADER
	#elif choice == '2':
	#	print(f"{Fore.BLUE}A CODE AND HEADER FILE ARE BEING CREATED.")
	#	createCodeHeader(input("WHAT FILE NAME DO YOU WANT : "))		
	
	## CODE 
	#elif choice == '3':
	#	print(f"{Fore.BLUE}A CODE FILE IS BEING CREATED.")
	#	createCodeFile(input("WHAT FILE NAME DO YOU WANT : "))
	#	print("+ CODE FILE CREATED")

	## HEADER
	#elif choice == '4':
	#	print(f"{Fore.BLUE}A HEADER FILE IS BEING CREATED.")
	#	createHeaderFile(input("WHAT FILE NAME DO YOU WANT : "))	
	#	print("+ CODE FILE CREATED")

	## MAKEFILE
	#elif choice == '5':
	#	print(f"{Fore.BLUE}A HEADER FILE IS BEING CREATED.")
	#	createMakefile()		
	#	print("+  MAKEFILE CREATED")

if __name__ == "__main__":

	#create_makefile()
	#create_dir_structure("TESTING")
	create_complete_project("proj")

	##menu()

	#colorama.init()

	#NAME = "Jonas S."
	#DATE = datetime.now().strftime('%d/%m/%Y')
	#PROJECT = input("Project name")

	#placeholders = {"DATE":f"{DATE}",
	#				"NAME":f"{NAME}",
	#				"FILENAME":"replaced3"}
	#test = replace_placeholders(test, placeholders)
	#print(test)