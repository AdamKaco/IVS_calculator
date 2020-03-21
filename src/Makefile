XLOG=xkosin09_xbaris01_xkacoa00

ROOT_DIR=$(shell cd)\..
ZIP_DIR=$(ROOT_DIR)\..\$(XLOG)

all:
	py profiling.py <nmb_100.txt

pack:
	cd .. & zip -r $(ZIP_DIR).zip .  
