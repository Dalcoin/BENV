# Program Opti: Version 3.0
# Modified by: Randy Millerson

import scipy.optimize as sciopt 	#import SciPy module with optimization routines
import subprocess 					#module for calling subprocesses
import time							#module with timing functions
  

# start the FORTRAN server process
server = subprocess.Popen("./xeb_server", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr = subprocess.STDOUT)

# Get optiosn from 'par' file 
with open('par.don', 'r') as file_par:
    lines_par = file_par.readlines()
       
l_par = lines_par[0].strip("\n")
s_par = filter(None,l_par.split(" "))

n_opt = int(s_par[1])
nread = int(s_par[2]) 

function_call_counter = 0	#counts the number of energy() evaluations

# definition of function to minimize
def energy(v): # v is a list of parameters. Modified Woods-Saxon Distribution v = [rp, cp, wp, rn, cn, wn]
    global n_opt
    global function_call_counter
    nl = "\n"
	#write the "EVALUATE ENERGY" command (icmd = 0)  and parameter values into the STDIN of the FORTRAN server
    if(nread != 2):
        if(n_opt == 2 or n_opt == 4):
            server.stdin.writelines(["0\n"+str(v[0])+nl+str(v[1])+nl+str(0.0)+nl+str(v[2])+nl+str(v[3])+nl+str(0.0)+nl])
        if(n_opt == 3):
            server.stdin.writelines(["0\n"+str(v[0])+nl+str(v[1])+nl+str(v[2])+nl+str(v[3])+nl+str(v[4])+nl+str(v[5])+nl])     
    else:
        if(n_opt == 2 or n_opt == 4):
            server.stdin.writelines(["0\n"+str(0.0)+nl+str(0.0)+nl+str(0.0)+nl+str(v[0])+nl+str(v[1])+nl+str(0.0)+nl])
        if(n_opt == 3):
            server.stdin.writelines(["0\n"+str(0.0)+nl+str(0.0)+nl+str(0.0)+nl+str(v[0])+nl+str(v[1])+nl+str(v[2])+nl])  
         
      
    #wait for FORTRAN server responce and read the energy value from from its STDOUT 
    en = float(server.stdout.readline())
    function_call_counter += 1 #increase the counter
    #print out parameters and energy every n iterations
    if True: #set to False to disable printing
        n = 10
        if n == 1 or (function_call_counter % n) == 1:
            print v, en	
    return en #return the value of the energy


# Here goes the main program ----------------->
if(nread != 2):
    if(n_opt != 3):
        v = [7.0,0.3,7.0,0.3] #set up the initial guess for parameters
    if(n_opt == 3):
        v = [7.0,0.3,3.0,7.0,0.3,3.0]
else:
    if(n_opt != 3):
        v = [7.0,0.3] #set up the initial guess for parameters
    if(n_opt == 3):
        v = [7.0,0.3,3.0]    
#v = [3.0,0.4,3.0,0.4]   #O,N,Mg,Al
#v = [6.0,0.4,6.0,0.4]   #Pb


if False: 		#set this to True, if you want to run the FORTRAN  routine once and quit.
	print v 	#otherwise this section is ignored. Useful for testing purposes
	en = energy(v)
	print en

 	server.communicate("1\n0\n0\n0\n0\n0\n0\n") # issue a "STOP" command to the server, wait for it to finish

	print "YAY!! :D"
	quit()


time_0 = time.time() #start timing	
	
#call the minimization routine
res = sciopt.minimize(
			fun = energy,  				#target function to be minimized. energy() in our case
			
			x0 = v, 					#initial guess for solution
			
			method = 'Nelder-Mead',
			
			tol = 1e-6					#max relative error between consecutive iterations
				)

#And the result is:...
print res

time_1 = time.time() #timing
#print "total time:", time_1 - time_0
#print "function evaluation:", function_call_counter
#print "time per function evaluation:", (time_1 - time_0)/function_call_counter

server.communicate("1\n0\n0\n0\n0\n0\n0\n") # issue a "STOP" command (icmd = 1) to the FORTRAN server, wait for it to finish

outputfile = open("opt_par.etr", "w")
nma=res.x

#Alternate Optimization
#outputfile.writelines([str(res.x), "\n", str(res.fun), "\n"])  #Single variable optimization 
#outputfile.writelines([str(res.x),"\n",str(nma[0])," ",str(nma[1])," ",str(nma[2])," ",str(nma[3]),"\n"]) #3pf optimization

spc = "   "

if(nread != 2):
    if(n_opt != 3):
        outputfile.writelines([str(nma[0]),spc,str(nma[1]),spc,str(0.0),spc,str(nma[2]),spc,str(nma[3]),spc,str(0.0),"\n"])
    if(n_opt == 3):
        outputfile.writelines([str(nma[0]),spc,str(nma[1]),spc,str(nma[2]),spc,str(nma[3]),spc,str(nma[4]),spc,str(nma[5]),"\n"])
else:
    if(n_opt != 3):
        outputfile.writelines([str(nma[0]),spc,str(nma[1]),spc,str(0.0),spc,str(nma[0]),spc,str(nma[1]),spc,str(0.0),"\n"])
    if(n_opt == 3):
        outputfile.writelines([str(nma[0]),spc,str(nma[1]),spc,str(nma[2]),spc,str(nma[0]),spc,str(nma[1]),spc,str(nma[2]),"\n"])

outputfile.close()

