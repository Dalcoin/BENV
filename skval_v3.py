# Program Skval: Version 3.0
# Written by Randy Millerson

import subprocess
import sys

#Parameter Input and sorting
par_in = open('serv_par.txt','r')
par_lines = par_in.readlines()

start_pos = par_lines[0].strip("\n")

start_split = start_pos.split(" ")

z_rep = int(start_split[0])
a_rep = int(start_split[1])
reset = int(start_split[2])
aug = int(start_split[3])
mirror = int(start_split[4])

p=a_rep*z_rep

counter = 0

n=z_rep+1
m=a_rep+1

#Vector Initialization

skin_list=[]
A_list = []
Z_list = []
Opt_pars = []

#Main loop: running the fortran/python optimization loop

for j in range(1,m):
    for i in range(1,n):

#       #Inner Loop start
        #Input atomic parameter parsing
        file_in = open('values.in2016', 'r')
        lines = file_in.readlines()

        l1 = lines[0].strip("\n")
        l2 = lines[1].strip("\n")
        l3 = lines[2].strip("\n")

        s1 = l1.split(" ")
        s2 = l2.split(" ")
        s3 = l3.split(" ")

        x0=str(s2[0])+" "
        x1=str(s2[1])

        A=float(s3[0])
        Anum=A
        Z=float(s3[1])
        Znum=Z
        Nnum=Anum-Znum

        A_list.append(Anum)
        Z_list.append(Znum)

        #reset values check
        if(counter == 0):
            A_rst = Anum
            Z_rst = Znum
            A_reset = str(Anum) + " "
            Z_reset = str(Znum) 
            Atom_reset = A_reset + Z_reset

#A, Z modification 

# If we are doing increments of aug:
        if(mirror==1):
            Z=Z+aug
        if(mirror==0):
            A=A+aug
# If we are doing increments by one.
# This needs to be turned into an option:

#       Z=Z+1 

#       Bash script: Shell IO parsing:

        subprocess.call("make",shell=True)
        subprocess.call("python nm_run.py",shell=True)
        subprocess.call("f90 $F90FLAGS -o run -s -w nskin_v3.f eb_v3.f $LINK_FNL",shell=True)
        subprocess.call("./run",shell=True)
          
#       Result parsing from output file:

        file_skin = open('skin.srt', 'r')
        lines_skin = file_skin.readlines()
        l_sk = lines_skin[0].strip("\n")
        sk = l_sk.split(" ")
        sk = filter(None, sk)

        pr = float(sk[0])
        nr = float(sk[1])
        nskin = float(sk[2])
        chrx = float(sk[3])
        aegen = float(sk[4])
        esymc = float(sk[5])

        temp_list=[]
        temp_list.append(pr)
        temp_list.append(nr)
        temp_list.append(nskin)
        temp_list.append(chrx)
        temp_list.append(aegen)
        temp_list.append(esymc)
        skin_list.append(temp_list)

        #Troubleshoot Shell Display:
 
        print(temp_list)
        print(skin_list)
        print(Anum,Znum,Nnum)

        #Rewriting A and Z

        kube=str(s1[0])
#       print(kube)
        kubes = kube+" "+kube+" "+kube+"\n"
        x=x0+x1+"\n"

        A=str(A)+" "
        Z=str(Z)
        Atom=A+Z
        
        
#       Reconstructing the values.in2016 file
         
        file_out = open('values.in2016', 'w')

        file_out.write(kubes)
        file_out.write(x)
        file_out.write(Atom)
        file_in.close()
        file_out.close()
        counter = counter + 1

#       Parsing optimized paramter values

        file_opt_par = open('opt_par.etr', 'r')
        opt_par_lines = file_opt_par.readlines()
        opt_par_str = opt_par_lines[0].strip("\n")
        opt_par_vals = opt_par_str.split(" ")
        opt_par_vals = filter(None,opt_par_vals)

        Opt_pars.append(opt_par_vals)

#   End of Inner Loop

    #Outer Loop incremental value parsing
        
    file_inc = open('values.in2016', 'w')
    
    if(mirror==1):
        A_inc=str(A_rst+aug*j)+" "
        Z_inc=str(Z_rst+aug*j)
    if(mirror==0):
        A_inc=str(A_rst)+" "
        Z_inc=str(Z_rst+aug*j)        
    Atom_inc = A_inc+Z_inc
    file_inc.write(kubes)
    file_inc.write(x)
    file_inc.write(Atom_inc)
    file_inc.close()
    file_inc.close()

#   End of Outer Loop
    

# Parsing values to file in tabled format
file_sol = open('out_skin_tables.srt','w')

for k in range(0,p):
    skv=[]
    skv= skin_list[k]
    print(skv)
    for jj in range(len(skv)): skv[jj] = '%.3f' % float(skv[jj])
    A_tab = str(int(A_list[k]))+"  "
    Z_tab = str(int(Z_list[k]))+"  "
    skv1=str(skv[0])+"  "
    skv2=str(skv[1])+"  "
    skv3=str(skv[2])+"  "
    skv4=str(skv[3])+"  "
    skv5=str(skv[4])+"  "
    skv6=str(skv[5])+"\n"
    skvt=A_tab+Z_tab+skv1+skv2+skv3+skv4+skv5+skv6
    file_sol.write(skvt)
file_sol.close()

# Parsing Optimized parameter values in tabled format

file_opt_par_tables = open('out_pars_table.srt','w')

for k in range(0,p):
    par_parsing = []
    par_parsing = Opt_pars[k]
    for jj in range(len(par_parsing)): par_parsing[jj] = '%.5f' % float(par_parsing[jj])
    optpar1 = str(par_parsing[0]) + "  "
    optpar2 = str(par_parsing[1]) + "  "
    optpar3 = str(par_parsing[2]) + "  "
    optpar4 = str(par_parsing[3]) + "  "
    optpar5 = str(par_parsing[4]) + "  "
    optpar6 = str(par_parsing[5]) + "\n"
    optpartemp = optpar1+optpar2+optpar3+optpar4+optpar5+optpar6
    file_opt_par_tables.write(optpartemp)
file_opt_par_tables.close()    

# Resetting nucleus to its inital value    

if(reset == 1):
    file_reset = open('values.in2016', 'w')
    file_reset.write(kubes)
    file_reset.write(x)
    file_reset.write(Atom_reset)
    file_reset.close()

# Display Clean-Up
subprocess.call("clear", shell=True)
subprocess.call("rm skin.srt", shell=True)
subprocess.call("rm opt_par.etr", shell=True)
subprocess.call("rm run", shell=True)

# Change to False to run 'ref_den.f', if n_read == 5, ref_den.f will not work
if(True):
    sys.exit()

#Included in third update 
#Reference densities run command
subprocess.call("f90 $F90FLAGS -o run -s -w ref_den.f $LINK_FNL",shell=True)
subprocess.call("./run",shell=True)

#Parsing the output 

file_ref_den = open('list_ref_dens.srt', 'r')
ref_den_lines = file_ref_den.readlines()
ref_dens = []
for k in range(0,p):
    ref_den_line = ref_den_lines[k].strip("\n")
    ref_den_val = filter(None,ref_den_line.split(" "))
    ref_dens.append(ref_den_val[0])
file_ref_den.close()

#Combining reference densities into skin value table
   
file_opt_par_tables = open('out_skin_tables.srt','r')
file_out = open('out_skin_table.srt','w')
out_lines = file_opt_par_tables.readlines()
for k in range(len(out_lines)):
    out_lines_clean = out_lines[k].strip("\n")
    ref_den = '%.5f' % float(ref_dens[k])
    out_lines_final = out_lines_clean + "  " + str(ref_den) + "\n"
    file_out.write(out_lines_final)
file_opt_par_tables.close()
file_out.close()

#Final Screen clean-up

subprocess.call("rm out_skin_tables.srt", shell=True)
subprocess.call("rm list_ref_dens.srt", shell=True)
subprocess.call("rm run", shell=True)


