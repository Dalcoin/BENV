Prerequesites:

1.) Must add the latest "pmod" package to the folder (delete the phelp.py if matplotlib is not installed)
2.) Must add "benv.py" to the standard pmod package (found in the script_application folder)


Set-up: ccm

1) Compile the binaries by running the compile script. Type "python compile.py" into the shell

2)  Add EoS to 'eos' folder. [(e.g.) 'e1_n2lo_450.don' & 'e0_n2lo_450.don'] 
    As long as the names are exactly the same but one is e0 and the other is e1 
    the program will find the files. Multiple files are allows as long as the names 
    are unique. If 'ex' is in the file name both e1 and e0 are in the same file with 
    the same densities vs. e/a. 

3)  Set the skval looping with the skval.don file (see documentation for all the details)

4)  Set the initial parameters with the 'parameters.don' files (see documentation for all the details)

5)  Run the program with 'python exe.py'

6)  Find the results in 'results.srt' found in the 'data' folder



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

