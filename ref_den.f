       
        
       program ref_den
       implicit real*8(a-h,o-z)
       dimension :: e0(100), e1(100), esym(100)
       dimension :: xkf(100), den(100), den_r(100)
       dimension :: frac(100), coef(100,4), ee(100), ee2(100)
       
       open(111,file='ex_nxlo.don')
       open(151,file='out_skin_tables.srt')
       open(515,file='par.don')
       open(525,file='serv_par.txt')
c       open(000,file='dump.don')
       open(707,file='alt_ex_nxlo.don')
       
       open(999,file='list_ref_dens.srt')
       
       read(525,*) n0, n1, it1, it2, it3       
       
       read(515,*) n, it0, n_read, it2, it3,    
     1             mic,isnm,isym_emp,k0,rho0,fff
       
       pi = 3.14159d0
       n2 = n-1
               
c  Generates the interpolated neutron matter EoS
c  parametrization of empirical EoS for symmmetric nuclear matter

       pi2=pi**2 
       fact=(3.d0*pi2/2.d0)**(2.d0/3.d0) 
       hbc=197.327d0
       hbc2=hbc**2
       xm=938.926d0 
       tfact=(3.d0*hbc2/10.d0/xm)
       totfact=fact*tfact
c
       alpha=-29.47-46.74*(k0+44.21)/(k0-166.11)
       beta=23.37*(k0+254.53)/(k0-166.11)
       sigma=(k0+44.21)/210.32
       gam=0.72d0
       alph=0.2d0 
       a1=119.14d0
       b1=-816.95d0
       c1=724.51d0
       d1=-32.99d0
       d2=891.15d0
       ff1=a1*2.d0*(0.5d0)**(5.d0/3.d0)
       ff2=d1*2.d0*(0.5d0)**(5.d0/3.d0) + 
     1     d2*2.d0*(0.5d0)**(8.d0/3.d0) 
       
       gam_4 = 4.0
       do i=1,n
          read(111,*) xkf(i), e0(i), e1(i)
          den(i) = gam_4*(xkf(i)**3)/(6.d0*pi**2)    

c         phenom_eos_section
          datapt = den(i)
          rat=datapt/rho0
          ee(i)=ff1*(datapt)**(2.d0/3.d0) + b1*datapt +
     1    c1*(datapt)**(alph+1.d0) + ff2*(datapt)**(5.d0/3.d0) 

          ee2(i)=totfact*(datapt)**(2.d0/3.d0) + (alpha/2.d0)*(rat)+
     1    (beta/(sigma + 1.d0))*(rat)**(sigma) 

          if(mic.eq.1) go to 3355 
          
             if(isnm.eq.1) then
                e0(i)=ee(i) 
             else 
                e0(i)=ee2(i) 
             end if 
         
c             if(datapt.le.0.0019.and.e0(i).gt.0.d0) then
c                e0(i)=0.d0 
c             end if
               
             esym_t=22.d0*rat**gam + 12.d0*rat**(2.d0/3.d0)       
             go to 3355 

3355      continue
          
          if(isym_emp.eq.0) then
             esym(i)=(e1(i)-e0(i)) 
          else 
             esym(i)=esym_t      
          end if      
            
c          write(000,*) xkf(i), den(i), e0(i), e1(i), esym(i) 
       end do 

       if(mic .NE. 1 .OR. isym_emp .NE. 0) then
          do i=1,n
             write(707,*) xkf(i) den(i) e0(i), e1(i), esym(i)
          end do
       end if
       
       call dcsakm(n,esym,den,frac,coef)
       
       m=n0*n1
       do i=1,m
          read(151,*) ia, iz, radz, radn, skn, chrgr, be, esymc
          den_r(i) = dcsval(esymc,n2,frac,coef) 
c          write(000,*) esymc, den_r(i),m
          write(999,*) den_r(i)
       end do
        
       end  
