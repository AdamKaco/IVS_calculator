###############################
# Project: IVS_Calculator
# Authors: xkacoa00, xbaris01, xkosin09
###############################
XLOG=xkosin09_xbaris01_xkacoa00

ROOT_DIR=$(shell cd)\..
ZIP_DIR=$(ROOT_DIR)\..\..\$(XLOG)
DEL_FILE="$(ROOT_DIR)\delete.txt" "nmb_1000*.txt" "debug.py" "$(ZIP_DIR).zip" 
DEL_DIR="$(ROOT_DIR)\src\__pycache__" 

all:
	@make run --no-print-directory

pack:
	@make clean --no-print-directory
	@cd .. & cd .. & zip -r $(ZIP_DIR).zip .  
clean:
	@for %%f in ($(DEL_FILE)) do ( if exist %%f del %%f )
	@for %%d in ($(DEL_DIR)) do ( if exist %%d del %%d /q & rmdir %%d /q)
run:
	 @py calc_logic.py
profile:
	 py profiling.py <nmb_100.txt
help:
	@type help.txt
use:
	@echo all - runs calc, default (make without arguments) 
	@echo pack - make clean and zip main directory
	@echo clean - delete unnecessary files
	@echo run - same as all
	@echo profile - runs profiler with 100 input numbers
	@echo help - prints what to do before first time running programm