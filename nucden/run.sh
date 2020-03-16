f90 $F90FLAGS -o go -s -w dens.f eb_v3.f $LINK_FNL
./go
rm go
