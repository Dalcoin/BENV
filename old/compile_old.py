#
#import sys
#import os 
#import subprocess
#
#import pmod.cmdline as cml
#import pmod.cmdutil as cmu
#import pmod.ioparse as iop
#import pmod.strlist as strl
#
#'''
#This script faciliates compiling binaries from source ('src') folder
#and moving those binaries to the binaries folder ('bin').
#
#Info:
#
#    - Change 'linux' to 'windows' if running on windows
#
#'''
#
#
#
#
#def compile_benv(OS_INST = "linux", SRC_DIR = "src", BIN_DIR = "bin", spc="    "):
#
#    DIRPATH = ""
#    SRCPATH = ""
#    BINPATH = ""
#
#    movexeb = False
#    moveaux = False
#    exefail = False
#
#    print(" ")
#    print("The compile_benv routine is now starting...runtime messesges will be printed below:\n")
#
#    # Set internal command line and command line utility
#    try:
#        cmv = cml.PathParse(OS_INST)
#        cmt = cmu.cmdUtil(cmv)
#        if(cmt.CML_INIT == False):
#            print(spc+"Error: 'cmdUtil' could not be initialized\n")
#            return False
#        print(spc+"Success: Internal pathway routine has been successfully initialized")
#    except:
#        print(spc+"Error: an error occured while initializing internal pathway routine")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False
#
#    # Set start pathway
#    success, value = cmv.cmd("pwd")
#    if(not success):
#        print(spc+"Error: It looks like the BENV folder pathway could not be accessed")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False
#    else:
#        DIRPATH = value
#
#    # Checking for existing binaries in Bin directory
#    success, value = cmv.cmd("cd "+BIN_DIR)
#    if(not success):
#        print(spc+"Error: It looks like the binary folder, '"+BIN_DIR+"', could not be accessed")
#        print(spc+"       Check to see if the binary folder is present")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#
#    # Get list of content of Bin directory
#    success, value = cmv.cmd("ls")
#    if(not success):
#        print(spc+"Error: It looks like the binary folder, '"+BIN_DIR+"', content could not be accessed")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False
#    binarylist = value
#
#    # Check for pre-existing binary files and remove any if the exist
#    if("xeb_server" in binarylist):
#        print(spc+"Warning: An already existing 'xeb_server' binary is present in the binary folder")
#        print(spc+"         An attempt will be made to overwrite this file")
#        success, value = cmv.cmd("rm xeb_server")
#        if(not success):
#            print(spc+"Error: failure to delete existing 'xeb_server', the newly compile_benvd version may end up in the program folder")
#    if("aux" in binarylist):
#        print(spc+"Warning: An already existing 'aux' binary is present in the binary folder")
#        print(spc+"         An attempt will be made to overwrite this file")
#        success, value = cmv.cmd("rm aux")
#        if(not success):
#            print(spc+"Error: failure to delete existing 'aux'")
#            print(spc+"The newly compile_benvd version may end up in the program folder\n")
#
#    success, value = cmv.cmd("cd ..")
#    if(not success):
#        print(spc+"Error: It looks like the program folder, 'BENV', could not be accessed")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#
#    # Moving into the source file 
#    cmv = cml.PathParse(OS_INST)
#    success, value = cmv.cmd("cd "+SRC_DIR)    
#    if(not success):
#        print(spc+"Error: It looks like the source folder, '"+SRC_DIR+"', could not be accessed")
#        print(spc+"       Check to see if the source folder is present")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#
#    success, value = cmv.cmd("pwd")
#    if(not success):
#        print(spc+"Error: It looks like the source folder, '"+SRC_DIR+"', pathway could not be accessed")
#        print(spc+"       Check to see if the source folder is present")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False
#    else:
#        SRCPATH = value
#
#    success, value = cmv.cmd("ls")    
#    if(not success):
#        print(spc+"Error: It looks like the source folder, '"+SRC_DIR+"', content could not be accessed")
#        print(spc+"       Check to see if the source file properly formatted")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False
#    
#    if(isinstance(value,(list,tuple))):
#        if(len(value) > 0):
#            check_list = [i.rstrip() for i in value]
#            if("xeb_server" in check_list):
#                print(spc+"Warning: A binary for 'eb_server_v3.f' has been found and will be overwritten")            
#            if("aux" in check_list):
#                print(spc+"Warning: A binary for 'nskin_v3.f' has been found and will be overwritten")
#        else:
#            print("Error: It looks like the source folder, '"+SRC_DIR+"', is empty")      
#            print("ExitError: fatal error; 'compile_benv' could not be completed")
#            return False  
#    else:
#        print(spc+"Error: It looks like the source folder, '"+SRC_DIR+"', content could not be accessed")
#        print(spc+"       Check to see if the source file properly formatted")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False
#    
#    try:
#        os.chdir(SRCPATH)
#    except:
#        print(spc+"Error: failure to set the shell pathway to the source folder")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False     
#
#    success = cmt.convert_file_endline("compile_benv.sh", foldName = SRC_DIR)
#    if(success == False):
#        print(spc+"Warning: 'run.sh' shell script not formatted, errors may result from improper formatting\n")
#
#    try:
#        subprocess.call("chmod +x compile_benv.sh",shell=True) 
#    except:
#        print(spc+"Error: failure to set the 'compile_benv' shell script to an executable")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False     
#     
#    try:
#        subprocess.call("./compile_benv.sh",shell=True) 
#    except:
#        print(spc+"Error: failure to run the 'compile_benv' shell script")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False     
#         
#    success, value = cmv.cmd("ls")
#    if(not success):
#        print(spc+"Error: It looks like the source folder, '"+SRC_DIR+"', content could not be accessed after compiling")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False             
#          
#    if(isinstance(value,(list,tuple))):
#        if(len(value) > 0):
#            if("xeb_server" in value):
#                print(spc+"Success: A binary for 'eb_server_v3.f' has been found after compiling")
#                movexeb = True
#            else:
#                print(spc+"Error: It looks like 'eb_server_v3.f' wasn't properly compile_benvd")            
#            if("aux" in value):
#                print(spc+"Success: A binary for 'nskin_v3.f' has been found after compiling")
#                moveaux = True
#            else:
#                print(spc+"Error: It looks like 'nskin_v3.f' wasn't properly compile_benvd")  
#        else:
#            print("Error: It looks like the source folder, '"+SRC_DIR+"', is empty")      
#            print("ExitError: fatal error; 'compile_benv' could not be completed")
#            return False 
#    else:       
#        print(spc+"Error: It looks like the source folder, '"+SRC_DIR+"', content could not be accessed after compiling")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False 
#     
#    if(movexeb):
#        success, value = cmv.cmd("mv xeb_server ..")
#        if(not success):
#            print(spc+"Error: 'xeb_server' was not successfully moved into the BENV directory") 
#            movexeb = False 
#    if(moveaux):
#        success, value = cmv.cmd("mv aux ..")
#        if(not success):
#            print(spc+"Error: 'aux' was not successfully moved into the BENV directory") 
#            moveaux = False
#
#    success, value = cmv.cmd("cd ..") 
#    if(not success):
#        print(spc+"Error: It looks like the program folder, 'BENV', could not be reaccessed")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")        
#
#    if(movexeb):
#        success, value = cmv.cmd("mv xeb_server "+BIN_DIR)
#        if(not success):
#            print(spc+"Error: 'xeb_server' was not successfully moved into the binary directory; '"+BIN_DIR+"'") 
#            movexeb = False 
#    if(moveaux):
#        success, value = cmv.cmd("mv aux "+BIN_DIR)
#        if(not success):
#            print(spc+"Error: 'aux' was not successfully moved into the binary directory; '"+BIN_DIR+"'") 
#            moveaux = False
#                    
#    success, value = cmv.cmd("cd "+BIN_DIR) 
#    if(not success):
#        print(spc+"Error: It looks like the binary folder, '"+BIN_DIR+"', could not be accessed")
#        print(spc+"       Check to see if the binary folder is present")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")     
#
#    success, value = cmv.cmd("pwd")
#    if(not success):
#        print(spc+"Error: It looks like the binary folder, '"+BIN_DIR+"', pathway could not be accessed")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False
#    else:
#        BINPATH = value     
#      
#    try:
#        os.chdir(BINPATH)
#    except:
#        print(spc+"Error: failure to set the shell pathway to the binary folder")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False     
#
#    success = cmt.convert_file_endline("run.sh", foldName=BIN_DIR)
#    if(success == False):
#        print(spc+"Warning: 'run.sh' shell script not formatted, errors may result from improper formatting\n")
#
#    try:
#        subprocess.call("chmod +x run.sh",shell=True)
#    except:
#        print(spc+"Error: failure to set the 'run' shell script to an executable")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False   
#
#    success, value = cmv.cmd("ls")
#    if(not success):
#        print(spc+"Error: It looks like the binary folder, '"+BIN_DIR+"', content could not be accessed")
#        print(spc+"ExitError: fatal error; 'compile_benv' could not be completed")
#        return False
#           
#    if("xeb_server" in value):
#        print(spc+"Success: The 'xeb_server' binary is accounted for in the binary folder")
#    else:
#        print(spc+"Error: The 'xeb_server' binary is not accounted for in the binary folder")  
#        exefail = True 
#
#    if("aux" in value):
#        print(spc+"Success: The 'aux' binary is accounted for in the binary folder")       
#    else:
#        print(spc+"Error: The 'aux' binary is not accounted for in the binary folder")  
#        exefail = True 
#
#    if(exefail):
#        print(spc+"Error: compile_benv failed, the 'exe.py' script will not work as intended")   
#     
#    return True
#
#
#
# Main program 
#
#success = compile_benv()
#print(" ")
#
#if(success):
#    print("No fatal errors detected, see above for runtime messesges")
#else:
#    print("Fatal error detected! See above for runtime errors")
#print(" ")
