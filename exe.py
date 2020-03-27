import os


from pmod import benv               # 'benv' is not a standard pmod module and must be added
from pmod import ioparse as iop
from pmod import cmdline as cml 

skval, eos = True, True

cmv = cml.path_parse('linux')
success, pwd = cmv.cmd('pwd')


benv_instance = benv.benv()
benvals = benv.benv_skval_loop(benv_instance)

outlines = []
for i in xrange(len(benvals)):
    if(i > 0):
        outlines.append(str(benvals[i][0][0])+str(benvals[i][0][1])+'  '+str(benvals[i][1][0])+str(benvals[i][1][1]))
    else:
        outlines.append(benvals[i][0]+' '+benvals[i][1])

iop.flat_file_write(cmv.pw_join(pwd,"results.srt"), outlines)
cmv.cmd('mv results.srt benv_data')
