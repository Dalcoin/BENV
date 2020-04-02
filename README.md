# BENV (SEMF)

The BENV repo contains a set of programs for calculating the nuclear binding energies from the Semi-Emperical Mass Formula (SEMF) 
as well as programs to compute nuclei parameters such as the neutron and proton r.m.s radii, symmetry energy coefficient,
neutron skin, and charge radius for a given isotope (A,Z).   

## Methodology

Central to the methedology of the BENV program, is the nuclear EoS (equation of state) which is expressed through the energy-per-density 
of infinite nuclear matter. Using the parabolic approximation below:

<img src="https://render.githubusercontent.com/render/math?math=e(\rho) = e_{0} %2B \alpha^{2} (e_{1} - e_{0})">

The total energy can be expressed as a function of density,

where <img src="https://render.githubusercontent.com/render/math?math=(e_{1} - e_{0})"> is a quantity known as the symmetry energy and

<img src="https://render.githubusercontent.com/render/math?math=\alpha = \frac{\rho_{n}-\rho_{p}}{\rho_{n}%2b\rho_{p}}">

The program accepts EoS input of descrete values in the form:

<img src="https://render.githubusercontent.com/render/math?math=\rho_{a} \quad e_{0}(\rho_{a}) \quad e_{1}(\rho_{a})"> 

## Getting Started

### Dependencies 

The Fortran source code was compiled with the Absoft 64-bit Pro Fortran 15.0.0 compiler and the compile commands found in the
shell scrits reflect this.

The IMSL(R) Fortran Numerical Math Library (FNML) is referenced in the Fortran source code and must be installed. 
No affiliation is asserted nor implied. [ISML link](https://www.absoft.com/products/imsl-fortran-numerical-libraries/)

The OS used when testing this program is Red Hat Enterprise Linux Server release 6.6 (Santiago)

The program uses the PMOD python module [PMOD link](https://github.com/Dalcoin/PMOD)

The program uses the "benv.py" module [benv.py link](https://github.com/Dalcoin/PMOD/tree/master/script_applications/benv_scripts)

The "benv.py" module must be placed in the PMOD folder (named "pmod") and placed in the same directory as the "src" folder and compile.py script)

### Set-up

0) Place all files and folders in a directory from which the dependencies are accessible  

1) Run the "compile.py" script to generate the binaries and move them into the appropriate folders

2) Place the EoS files into the 'eos' folder

3) Run the exe.py script to compute the density function parameters and nuclei parameters

A successful compilation should produce the following: 

![successful compilation](https://github.com/Dalcoin/BENV/blob/master/successful_compile.JPG)

## Documentation

### EOS formatting: Using "benv.benv_eos_loop"

EoS files should be placed inside the 'eos' folder. Using the EoS loop function ("benv_eos_loop") the
script will attempt to find valid EoS matches from files with properly formatted names:

e0 : Symmetric nuclear matter EoS 
e1 : Neutron nuclear matter EoS

Nameing convensions:

1) e0 and e1 in the same file

   Files formatted with 'n' number of line. 
   Each line should contain three floats formatted as follows: 
   
   kf  e0  e1

   Files of this format must be named according to the following rules: 
  
   * contain the string 'ex' exactly once, in the name the characters may be either case
   * must NOT contain the string 'e0' or 'e1' in either case 

   Here kf is the fermi momentum corrosponding to a given density in *symmetric* matter
   for both e0 and e1   
     
 
2) e0 and e1 in seperate files:

   One of the files should have 'n0' number of lines and contain the e0 values

   Each line should contain two floats formatted as follows: 
   
   kf0  e0 

   Files of this first type must be named according to the following rules: 
  
   * contain the string 'e0' exactly once in the file's name, the characters may be of either case
   * must NOT contain the strings 'e1' or 'ex', in either case 

   here kf is the fermi momentum corrosponding to the e0 value 

   --------------------------------------------------------------------------------------

   The other file should have 'n1' number of lines and contain the e1 values

   Each line should contain two floats formatted as follows: 
   
   kf1  e1 

   Files of this first type must be named according to the following rules: 
  
   * contain the string 'e1' exactly once in the file's name, the characters may be of either case
   * must NOT contain the strings 'e0' or 'ex' in either case 

   here kf is the fermi momentum corrosponding to the e1 value 
   *unlike in the 'ex' format it is not adjusted to symmetric matter density* 

   --------------------------------------------------------------------------------------
   
   **n0 does not have to equal n1**

   There is an additional rule:

   * the to match an e0 and e1 file, the files must have the same name execpt for the '1' and '0'

   these work:
                      
      example_e0.don & example_e1.don  
      e0_1.don & e1_1.don  
                            
   these do not:
                         
      e0_ex.don & e1_ex.don  
      e0_new.don & e1_new_2.don  
                      


### SKVAL loop

The file 'skval.don' is intended to be formatted for the 'benv.skval_loop' function.

There are currently two modes in which the file can be parsed. Whichh is chosen is 
determined by the True or False value found after the appropriate text under the 
loop heading. The relevent section appears as follows:


>#----Loop----#  
>   
>INCloop:False  
>AZpairs:True  

Each boolean must be specified with 'True' for true or 'False' for false. Any other 
characters will not be properly understood. 

If INCloop is True, then the incloop looping will be attempted, else if 
AZpairs is True, then the program will search for nuclei denoted by two integers A and Z
formatted as 'A,Z'

1) The INCloop: Documentation to be added 

2) The AZpairs:

   The azpairs should be placed after the 'loop' section header. 
   Each A,Z pair should consist of two integers seperated by a comma 
   The first A, corrosponds to the mass number, the second Z, 
   corrosponds to the atomic number. 
 
   For example: 

   >#-------------#  
   >#--Formating--#-------#  
   >#-------------#
   >   
   >#----Loop----#
   >   
   >16,8   
   >40,20   
   >48,20   
   >56,28   
   >208,82   
 
 

