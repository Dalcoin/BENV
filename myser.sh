make
python nm_run.py
f90 $F90FLAGS -o run -s -w nskin_v3.f eb_v3.f $LINK_FNL
./run
