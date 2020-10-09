Prerequesites:

1.) Must add the latest "pmod" package to the folder (delete 'phelp.py' if matplotlib is not installed)
2.) Must add "benv.py" to the standard pmod package (found in the 'script_application folder')
3.) Must add "compile.py" to the standard package (found in 'program_scaffolding')

Set-up: ccm

1) Compile the binaries by running the compile script. Type "python compile_BENV.py" into the shell

2)  Add EoS to 'eos' folder. [(e.g.) 'e1_n2lo_450.don' & 'e0_n2lo_450.don'] 
    As long as the names are exactly the same but one is e0 and the other is e1 
    the program will find the files. Multiple files are allowed as long as the names 
    are unique. If 'ex' is in the file name both e1 and e0 are in the same file with 
    the same densities vs. e/a. 

3)  Set the skval looping with the skval.don file (see documentation for all the details)

4)  Set the initial parameters with the 'parameters.don' files (see documentation for all the details)

5)  Run the program with 'python exe_BENV.py'

6)  Find results in the 'dat' folder

    a) Find the density functional parameters in 'Pars.srt' 
    b) Find the nuclear values in 'Vals.srt'


Examples: 

A par example:
       
    6 2 0 9 9 1 1 0 220 0.16 65
      

A skval loop example:

    A  Z  inc  inv
    4  2  1    0    

     
pair examples:
     
    16,8
    40,20
    208.82


"results.srt" ordering:

The order of the output data found in 'results.srt' is as follows:

parameters.don
rp  cp  wp  rn  cn  wn  

characteristics
nr  pr  ns  cr  be  sc  A  Z    


rp : radial parameter (proton)
cp : diffuse parameter (proton)
wp : folding parameter (proton)
rn : radial parameter (neutron)
cn : diffuse parameter (neutron)
wn : folding parameter (neutron)
nr : neutron r.m.s. radius 
pr : proton r.m.s. radius
ns : neutron skin 
cr : charge radius 
be : binding energy
sc : symmetry-energy coefficient 
A  : Atomic mass 
Z  : Atomic number 