import os


from pmod import benv               # 'benv' is not a standard pmod module and must be added
from pmod import ioparse as iop
from pmod import cmdline as cml 

skval, eos = True, True

cmv = cml.path_parse('linux')
success, pwd = cmv.cmd('pwd')

benvals_list = []

benv_instance = benv.benv()
intial_pars, inital_vals = benv_instance.data_from_pars()
benvals = benv.benv_run_once(benv_instance)
benvals_list.append(benvals)

if(skval):
    skval_lines = benv_instance.get_skval_data('skval.don')
    data, type, parincl = benv_instance.format_skval_data(skval_lines)
       
    if(type == 'loop'):
        loops = True         
        if(parincl):
            pass
        else:
            pass
    elif(type == 'pair'): 
        pairs = True
        if(parincl):

        else:
        
    else:
        pass 


benvals = benv.benv_run_once(benv_instance)


benvals = [str(i[0])+'  :  '+str(i[1]) for i in benvals]

os.chdir(pwd)
iop.flat_file_write("results.srt", benvals)

cmv.cmd('mv results.srt benv_data')
