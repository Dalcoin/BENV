import os

from pmod import benv               # 'benv' is not a standard pmod module and must be added
from pmod import ioparse as iop
from pmod import cmdline as cml 
from pmod import mathops as mops

cmv = cml.path_parse('linux')

benv_inst = benv.benv()
groups = benv_inst.benv_eos_loop()

outlines = []
outlines.append('\n')
for i,j in groups:
    outlines.append(j+"\n")
    for k in i:
        outlines.append('  '+k)
    outlines.append('\n')

success = benv_inst.move_results_to_data_folder()
