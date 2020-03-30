import os


from pmod import benv               # 'benv' is not a standard pmod module and must be added
from pmod import ioparse as iop
from pmod import cmdline as cml 
from pmod import mathops as mops

skval, eos = True, True

cmv = cml.path_parse('linux')
success, pwd = cmv.cmd('pwd')


benv_instance = benv.benv()
benvals = benv.benv_skval_loop(benv_instance)
printlines = benv_instance.format_skval_benv_vals(benvals)

iop.flat_file_write(cmv.pw_join(pwd,"results.srt"), printlines)
cmv.cmd('mv results.srt data')
