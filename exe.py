import sys

from lib import benv
from lib.progLib.pmod import ioparse as iop


'''
This script is the main routine for the BENV program

Direction:

    programMode : If True, will run the BENV program in the shell
    benvMode :    If True, will run only the BENV Loop

'''

programMode = True
benvMode = False

benvInst = benv.benv()

if(programMode):
    benvInst.get_skval()
    benvInst.set_benv_menu()
    benvInst.program_loop(benvInst.benv_program_loop, program_name='BENV')
elif(benvMode):
    benvInst.get_skval()
    benvInst.benv_run(benvInst.skval)
    benvInst.exit_function()
else:
    benvInst.exit_function()