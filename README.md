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
No affiliation is asserted nor implied.

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




