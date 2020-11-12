

------------------------|
    BENV Source Info    |
------------------------|

Version : BENV 5.0
Author : Randy Millerson


Description:

The Binding Energy and Nucleon Values (BENV) program computes
the total energy of a nucleus using a Semi-Emperical Mass
Formula inspired Energy Density Functional. The program takes
the nuclear Equation of State (EoS) as a direct input into
the program. For further details on the EDF employed, and the
predictions derived therefrom, see the publication: 

"Nuclear Forces in the Medium: Insight From the Equation of State"
F. Sammarruca and R. Millerson, Front. Phys. 7, 213 (2019)


Methodology:

The input takes two nuclear EoS, one for symmetric nuclear matter (SNM)
and the other of neutron nuclear matter (NM). Both express the energy
per particle as functions of Fermi-momenta which are converted to density:

 kf  e0   e1
 .   .    .
 .   .    .
 .   .    .
 .   .    .

Note that the Fermi-momenta corrospond to the density within SNM. For
functions which convert between Fermi-momenta and density, see the
"eos" functionality contained within "pmod": lib -> probLib -> pmod


The nuclear matter EoS is approximated with the parabolic approximation:

 e(rho, alpha) = e0 + esym*alpha*alpha

 where,

 alpha = (rhon-rhop)/(rhon+rhop)

 esym = e1 - e0

 rhon = neutron density
 rhop = proton density

The density functional must be chosen, default is
the Thomas-Fermi (Woods-Saxon) distribution, all
options are shown below:

- Two-Parameter Thomas-Fermi (Woods-Saxon) distribution (2PF)
- Two-Parameter Folded-Yukawa distribution (2PY)
- Three-Parameter Thomas-Fermi distribution (3PF)

For the controls to select the density functional, see input
file formatting below.

------------------------|
    BENV Source Files   |
------------------------|

Subroutines and Functions:

eb_v3.f


Computing Nucleus Parameters:

eb_server_v3.f  :  Server which connects to the python script for minimizing the E/A
nskin_v3.f      :  Computes the nucleonic values using the optimized EDF parameters
nm_run.py       :  Python minimization script


Computing the Hadronic density distribution:

dens_v3.f  :   Computes the Hadronic density distribution
               using the optimized EDF parameters.


------------------------|
    BENV Directions     |
------------------------|

Run modes: 

This program is intended to be run with the BENV python class.
However, this program may easily used as is. The "compile.sh"
shell script may be used to facilitate the compilation
process, the groups required for each compiled binary are given
below.

Binaries:

xeb_server : eb_server_v3.f , eb_v3.f
aux        : nskin_v3.f , eb_v3.f
zed        : dens_v3.f , eb_v3.f

All of the above use the IMSL FNL (Fortran Numerical Library).

Run as follows:

To compute the optimized EDF parameters run "nm_run.py"

To compute the nucleus values run "aux"

To compute the density distribution run "zed"

Note that the following flow computes each desired value set
for a single given EoS and a single nucleus (A,Z).



------------------------|
    BENV Input Files    |
------------------------|

"par.don"                                                                                                              
"nucleus.don"                                                                                                           
"denopts.don"
"denpars.don"

The details on the input of each of these files given below:

"par.don" : Contains the controls for the nuclear EoS input
            and which distribution function to select,
            options for various phenomenological EoS.

"nucleus.don" : Contains the controls for the nucleus for
                which the energy-per-nucleon is calculated.
                Also contains controls for the numeric
                tolerences used in the integrations.

"denopts.don" : Contains controls for the density distribution
                as computed from the EDF parameters and for
                a given nucleus

"denpars.don" : Input EDF parameters, derived from "nm_run.py"


--------------------------------------------------------------|

Complete descripts of the input files are given below.


--------------------------------------------------------------|


"par.don" parameters:

Sample Input:   6   2  0  9  9  1  1  0  220  0.16   65.
Format is:      I1 I2 I3 I4 I5 I6 I7 I8   I9   F10  F11

I1: number of points if a single EOS is chosen
I2: Choice of density function:
	2: 2pf
	3: 3pf
	4: Folded-Yukawa
I3: Choice of EOS input:
	0: "ex_nxlo.don": e0 and e1 same length; format: "den  e0  e1"
	1: "e0_nxlo.don" & "e1_nxlo.don": various lengths, adjusted e0 kf to den: "den  e0"  &  "den  e1"
	2: "e0_nxlo.don" only: "den  e0" [Note this input only is valid if Z = N | 2Z = 2N = A]
I4: Number of points e0 if differing length EOS
I5: Number of points e1 if differing length EOS
I6: Microscopic options: 1 for True, 0 for False
I7: SNM Phenomenological EoS option: 1 for set parameterized choice, 0 for saturation density dependent option 
I8: Emperical Symmetry Energy option: 1 for True, 0 for False
I9: SNM curvature parameter, for use if option 0 SNM Phenomenological EoS is chosen
F10: saturation density, for use if option 0 SNM Phenomenological EoS is chosen
F11: nuclear surface parameter: determined to range from 60-70 MeV fm^(-5).

The BENV variable names which corrospond to each of the above parameters are given below for reference:

n  nden nread n0 n1 mic isnm iemp k0  rho0  fff
11 2    0     19 19 0   1    0    220 0.16  65.
I1 I2   I3    I4 I5 I6  I7   I8    I9  F10  F11


--------------------------------------------------------------|


"nucleus.don" parameters:

Sample Input:   64 64 64
                0.0 20.0
                208.0 82.0
Format is:      I1 I2 I3
                F4 F5
                F6 F7

I1,I2,I3: Gaussian Quadrature Points
F4: Radial Integration Start Point: Low limit (fm)
F5: Radial Integration Terminal Point: Upper limit (fm)
F6: Atomic Mass Number
F7: Atomic Number


--------------------------------------------------------------|


"denopts.don" parameters:

Sample Input:   2 12.0 30 208.0 82.0
Format is:     I1 F2   I3 F4    F5

I1: Choice of density function (see "par.don")
F2: Radial Integration: Upper limit (fm)
I3: Number of radial points in output
F4: Atomic Mass Number
F5: Atomic Number


--------------------------------------------------------------|

"denopts.don" parameters:

Sample Input:  6.265  0.765  0.0  6.359  0.821  0.0
Format is:     F1     F2     F3   F4     F5     F6

F1: Proton Radial Parameter    (rp)
F2: Proton Diffuse Parameter   (cp)
F3: Proton Folding Parameter   (wp)
F4: Neutron Radial Parameter   (rn)
F5: Neutron Diffuse Parameter  (cn)
F6: Neutron Folding Parameter  (wn)

This file is typically produced as the output of the 'xeb_server' binary


--------------------------------------------------------------|



------------------------|
   BENV Output Files    |
------------------------|

--------------------------------------------------------------|

"opt_par.etr"

Sample Output: 6.84521  0.42469  0.00000  6.92377  0.49904  0.00000
Format is:     rp       cp       wp       rn       cn       wn

See "denopts.don" parameters

--------------------------------------------------------------|

"skin.srt"

Sample Output: 5.7614    5.5948    0.1665    5.6602   -7.7337   21.7263    0.0808
Format is:     NR        PR        NS        CHR       BE       SEC        RD

NR  :  Neutron Radius
PR  :  Proton  Radius
NS  :  Neutron Skin
CHR :  Charge  Radius
BE  :  Binding Energy
SEC :  Sym. Eng. Coef
RD  :  Ref. Density  
A   :  Mass    number
Z   :  Atomic  number


--------------------------------------------------------------|