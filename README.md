Project Name 
=================
IVS_calculator

Authors
=================
- Adam Kačo (xkacoa00)
- Peter Bariš (xbaris03)
- Simon Košina (xkosina01)

Describtion
=================
1) Basic calculator with these functions
   a) plus (+)
   b) minus (-)
   c) multiply (*)
   d) divide (/)
   e) power (^)
   f) root (√)
   g) combination number (C)
2) Profiling - it calculates standard deviation, we used it as profiling tool.

Instalation
=================
FIX ME

Usage
=================
You can run the following these ways
Calculator
-----------------
- Run directly calc_logic.py
- Run via Makefile using::
    make
or
    make run
Profiling
-----------------
- Run directly profiling.py "file" (in file are numbers with white spaces between them)
- Run via Makefile using (input file will be nmb_100.txt)::
    make profile
Makefile
-----------------
runs calc, default (make without arguments)::
    make all 
make clean and zip main directory::
    make pack
deletes unnecessary files::
    make clean
same as all::
    make run
runs profiler with 100 input numbers::
    make profile
prints what to do before first time running programm::
    make help

License
=================
GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007