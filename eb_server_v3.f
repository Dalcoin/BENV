
c      Program EB_run: Version 3.0
c      Modified by: Randy Millerson

c---------------------------------------------------------------------------------------------------

       PROGRAM eb_run_once
       implicit real*8 (a-h, o-z)

c      SERVER INTIALIZATION
      
c       open (unit=000,file='dump.don')
       open (unit=8,file='values.in2016')
       open (unit=14,file='par.don')
                       
       read(8,*) n1,n2,n3
       read(8,*) x1,x2
       read(8,*) ta,tz 

       call init(n1, n2, n3, x1, x2, ta, tz)
      
c-------------------------------------------------
c             SERVER MAIN LOOP                   |
c-------------------------------------------------

c      read the command and parameters
c      if command is 0 (or rather "not 1"), evaluate energy and repeat
c      if command is 1, stop the server

       icmd = 0
       do 100 while (icmd .ne. 1)
       
          read(*,*) icmd, rp, cp, wp, rn, cn, wn        
          
          if (icmd .ne. 1) then
              en = energy(rp, cp, wp, rn, cn, wn)
c         write the energy value to STDOUT
              write(*, *) en
          endif 
 100   continue           
            
       stop
       END PROGRAM
