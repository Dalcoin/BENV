# This code attempts to compile BENV binaries from their source code
# If Error: syntax error: unexpected end of file: in vim for this file ":set fileformat=unix"  

FILESERV=$PWD/xeb_server
FILEREF=$PWD/aux

COMPILE_XEB="f90 $F90FLAGS -o xeb_server -s -w eb_v3.f eb_server_v3.f $LINK_FNL"
COMPILE_AUX="f90 $F90FLAGS -o aux -s -w nskin_v3.f eb_v3.f $LINK_FNL"

if [ -f "$FILESERV" ]
then
    servexist=$true 
else
    servexist=$false
fi

if [ !$servexist ]; then 
    eval $COMPILE_XEB
fi 

if [ -f "$FILEREF" ]
then
    refexist=$true 
else
    refexist=$false
fi

if [ !$refexist ]; then 
    eval $COMPILE_AUX
fi 

    
