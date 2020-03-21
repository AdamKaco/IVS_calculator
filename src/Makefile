XLOG=xkosin09_xbaris01_xkacoa00

ROOT_DIR=$(shell cd)\..
ZIP_DIR=$(ROOT_DIR)\..\$(XLOG)
DEL_FILE="$(ROOT_DIR)\delete.txt" "nmb_1000*.txt" "debug.py"  
DEL_DIR="$(ROOT_DIR)\src\__pycache__"

all:
	@make run --no-print-directory

pack:
	make clean
	cd .. & zip -r $(ZIP_DIR).zip .  
clean:
	for %%f in ($(DEL_FILE)) do ( if exist %%f del %%f )
	for %%d in ($(DEL_DIR)) do ( if exist %%d del %%d /q & rmdir %%d /q)
run:
	 py profiling.py <nmb_100.txt
profile:
	 py profiling.py <nmb_100.txt
help:
	@echo Program and bla bla bla