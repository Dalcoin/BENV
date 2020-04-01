import os

from pmod import benv               # 'benv' is not a standard pmod module and must be added
from pmod import ioparse as iop
from pmod import cmdline as cml 
from pmod import mathops as mops

cmv = cml.path_parse('linux')
success, pwd = cmv.cmd('pwd')

success, value = cmv.cmd('cd data')
success, value = cmv.cmd('ls')
if('results.srt' in value):
    success, value = cmv.cmd('rm results.srt')    
success, value = cmv.cmd('cd ..')

benv_inst = benv.benv()
groups = benv_inst.benv_eos_loop()

outlines = []
outlines.append('\n')
for i,j in groups:
    outlines.append(j+"\n")
    for k in i:
        outlines.append('  '+k)
    outlines.append('\n')

iop.flat_file_write(cmv.pw_join(pwd,"results.srt"), outlines)
cmv.cmd('mv results.srt data')
