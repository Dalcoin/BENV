# Program Opti: Version 3.0
# Modified by: Randy Millerson

import scipy.optimize as sciopt 	#import SciPy module with optimization routines
import subprocess 					#module for calling subprocesses
import time							#module with timing functions
  

# start the FORTRAN server process
server = subprocess.Popen("./xeb_server", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr = subprocess.STDOUT)

file_par = open('par.don', 'r')
lines_par = file_par.readlines()
file_par.close()
l_par = lines_par[0].strip("\n")
s_par = l_par.split(" ")
s_par = filter(None,s_par)

garbage = int(s_par[0])
n_opt = int(s_par[1])

function_call_counter = 0	#counts the number of energy() evaluations

# definition of function to minimize
def energy(v): # v is a list of parameters. Modified Woods-Saxon Distribution v = [rp, cp, wp, rn, cn, wn]
        global n_opt
	global function_call_counter
	#write the "EVALUATE ENERGY" command (icmd = 0)  and parameter values into the STDIN of the FORTRAN server
        if(n_opt != 3):
        	server.stdin.writelines(["0\n" + str(v[0]) + "\n" + str(v[1]) + "\n" + str(0.0) + "\n" + str(v[2]) + "\n" + str(v[3]) + "\n" + str(0.0) + "\n"])
        if(n_opt == 3):
                server.stdin.writelines(["0\n" + str(v[0]) + "\n" + str(v[1]) + "\n" + str(v[2]) + "\n" + str(v[3]) + "\n" + str(v[4]) + "\n" + str(v[5]) + "\n"])        
	#wait for FORTRAN server responce and read the energy value from from its STDOUT 
	en = float(server.stdout.readline())
	
	function_call_counter += 1	#increase the counter
	
	#print out parameters and energy every n iterations
	if True: #set to False to disable printing
		n = 10
		if n == 1 or (function_call_counter % n) == 1:
			print v, en	
	return en 	#return the value of the energy

	
# Here goes the main program ----------------->
if(n_opt != 3):
	v = [7.0,0.3,7.0,0.3] #set up the initial guess for parameters
if(n_opt == 3):
	v = [7.0,0.3,3.0,7.0,0.3,3.0]
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

if(n_opt != 3):
	outputfile.writelines([str(nma[0]),"  ",str(nma[1]),"  ",str(0.0),"  ",str(nma[2]),"  ",str(nma[3]),"  ",str(0.0),"\n"])
if(n_opt == 3):
        outputfile.writelines([str(nma[0]),"  ",str(nma[1]),"  ",str(nma[2]),"  ",str(nma[3]),"  ",str(nma[4]),"  ",str(nma[5]),"\n"])
outputfile.close()


