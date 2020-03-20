import os


from pmod import benv
from pmod import ioparse as iop
from pmod import cmdline as cml 

cmv = cml.path_parse('linux')
success, pwd = cmv.cmd('pwd')

benv_inst = benv.benv()
benv_inst.data_from_pars("parameters.don")
benv_inst.run_once()

benvals = benv_inst.get_benv_vals()

benvals = [str(i[0])+'  :  '+str(i[1]) for i in benvals]

os.chdir(pwd)
iop.flat_file_write("results.srt", benvals)

cmv.cmd('mv results.srt benv_data')
