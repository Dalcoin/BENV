
c      Program Energy_time: Version 3.0
c      Modified by: Randy Millerson

       program energy_time
       implicit real*8(a-h,o-z)
       common/paspoi/pas(200),poi(200),x(200),w(200)
       common/binding/totbe,binde1,binde2,binde3
       common/maineos/xdata(75),zdata(75),nxdata,
     3                 xsnm(75), ydata(75),nsnm,
     1                 breakz(75),cscoefz(4,75),
     2                 breaky(75),cscoefy(4,75),
     4                 xdatas(100),xdatan(100)
       common/abc/xnorm
       common/charge/chr
       common/main/fint1,fint2,fint3
       common/azn/ta, tz, tn
       common/setup/n1, n2, n3, x1, x2
       common/factor/pi,pi2
       common/parz/n_den,mic,isnm,isym_emp,k0,rho0,fff

       dimension :: e0(100),e1(100),xkf(100),den(100)
       dimension :: den0(100), den1(100), ee(100), ee2(100)
       dimension :: coef0(4,100),coef1(4,100),caser0(100),caser1(100)

       open(unit=117,file='opt_par.etr')
       open(unit=8,file='values.in2016')
       open(unit=999,file='skin.srt')
       open(unit=525,file='ex_nxlo.don')
       open(unit=114,file='par.don')
c       open(unit=000,file='dump.don')

       pi=3.141592654d0
       pi2=pi*pi

c  parametrization of empirical EoS for symmmetric nuclear matter

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

       read(117,*) rp, cp, wp, rn, cn, wn
       read(114,*) m, n_den, n_read, n_0, n_1,
     1             mic,isnm,isym_emp,k0,rho0,fff

       m0 = n_0-1
       m1 = n_1-1
       m2 = m-1
c    number of integration points
       read(8,*) n1,n2,n3
       read(8,*) x1,x2
       read(8,*) ta,tz
       tn=ta-tz
       
c     this is where we setup the input
       call init(n1, n2, n3, x1, x2, ta,tz)
       en = energy(rp, cp, wp, rn, cn, wn)

       if(n_read .ne. 4 and n_read .ne. 5) then
          do i=1,m 
             den(i)=xdata(i)
             e0(i)=ydata(i)
             e1(i)=zdata(i)
          end do
       else if(n_read .eq. 4) then
          do i=1,n0
             den0(i)=xdata(i)
             e0(i)=ydata(i)
          end do
          do i=1,n1
             den1(i)=xdata(i)
             e1(i)=zdata(i)
          end do
       else if(n_read .eq. 5) then 
          do i,m 
             den(i) = xdata 
             e0(i) = ydata(i)
       end if

c     normalize the proton function
       call xnormalize(pi,rp,cp,tz,wp)
       ap=xnorm
       

       call xnormalize(pi,rn,cn,tn,wn)
       an=xnorm
c       write(000,*) an, ap
       
       call rms(ap,rp,cp,wp,an,rn,cn,wn,pi,tz,tn,ta,64)
       call chrms(ap,rp,cp,wp,pi,tz,64)

       
       sum=0.d0
       down_lim = 0.0d0
       upper_lim = 20.d0
       nrep = 90
 
       if(tn .ne. tz) then
          coef_int = ta/(tn-tz)**2
       else 
          coef_int = 0.d0
       end if

       call lgauss(nrep)
       call papoi(down_lim,upper_lim,1,nrep,1.d0,1)

       if(n_read .ne. 4 and n_read .ne. 5) then
          call dcsakm(m,den,e0,caser0,coef0)
          call dcsakm(m,den,e1,caser1,coef1)
       else if(n_read .eq. 4) then
          call dcsakm(n_0,den0,e0,caser0,coef0)
          call dcsakm(n_1,den1,e1,caser1,coef1)
       else if(n_read .eq. 5) then 
          call dcsakm(m,den,e0,caser0,coef0)
       end if

       do i =1,nrep
          dr = pas(i)
          ww = poi(i)
          if(n_den .EQ. 2) then
             rho_t = rho(dr,an,rn,cn) + rho(dr,ap,rp,cp)
             delt = (rho(dr,an,rn,cn) - rho(dr,ap,rp,cp))/rho_t
          else if(n_den .EQ. 3) then
             rho_t = rho_3pf(dr,an,rn,cn,wn) + rho_3pf(dr,ap,rp,cp,wp)
             delt = (rho_3pf(dr,an,rn,cn,wn) - 
     1               rho_3pf(dr,ap,rp,cp,wp))/rho_t
          else if(n_den .EQ. 4) then
             rho_t = rho_fy(dr,an,rn,cn,tn) + rho_fy(dr,ap,rp,cp,tz)
             delt = (rho_fy(dr,an,rn,cn,tn) -
     1               rho_fy(dr,ap,rp,cp,tz))/rho_t
          end if

          if(n_read .ne. 4 and n_read .ne. 5) then
             e0_eval = dcsval(rho_t,m2,caser0,coef0)
             e1_eval = dcsval(rho_t,m2,caser1,coef1)
          else if(n_read .eq. 4) then
             e0_eval = dcsval(rho_t,m0,caser0,coef0)
             e1_eval = dcsval(rho_t,m1,caser1,coef1)
          else if(n_read .eq. 5) then 
             e0_eval = dcsval(rho_t,m2,caser0,coef0)             
          end if
c         phenom_eos_section

          if(n_read .eq. 5) then 
              pt = e0_eval
              goto 4295

          rat=rho_t/rho0
          ee(i)=ff1*(rho_t)**(2.d0/3.d0) + b1*rho_t +
     1    c1*(rho_t)**(alph+1.d0) + ff2*(rho_t)**(5.d0/3.d0) 

          ee2(i)=totfact*(rho_t)**(2.d0/3.d0) + (alpha/2.d0)*(rat)+
     1    (beta/(sigma + 1.d0))*(rat)**(sigma) 

          if(mic.eq.1) go to 3355 
         
             if(isnm.eq.1) then
                e0_eval=ee(i) 
             else 
                e0_eval=ee2(i) 
             end if 
         
             if(rho_t.le.0.0019.and.e0_eval.gt.0.d0) then
                e0_eval=0.d0 
             end if
               
             esym=22.d0*rat**gam + 12.d0*rat**(2.d0/3.d0)        
             go to 3355 

3355      continue

          if(isym_emp.eq.0) then
             pt=(delt*delt)*(e1_eval-e0_eval) 
          else 
             pt=(delt*delt)*esym      
          end if    

4295      continue     
         
          val = rho_t*pt*(dr**2)*ww
          sum = sum + val
       end do
       esym_coef = sum*coef_int*4.d0*pi

c       write(6,5000)
c       write(6,*) rp,cp,rn,cn
c       write(6,*) chr
c       write(6,*) fint1,fint2,fint3
c       write(6,4000) fint2-fint1
c       write(6,5555) fint2

c      Fint2: Neutron radius
c      Fint1: Proton radius
c      chr  : Charge radius
c      Fint2-Fint1: Neutron Skin
c      en: Energy per Particle
c      esym_coef: Symmetry Energy Coefficient

       write(999,1344) fint2,fint1,fint2-fint1,chr,en,esym_coef
c       write(*,1344) fint2,fint1,fint2-fint1,chr,en,esym_coef

 1344  FORMAT(F10.4,F10.4,F10.4,F10.4,F10.4,F10.4)
 4000  format(1x,'neutron skin=',f10.4)
 5555  format(1x,'neutron radius',f10.4)
 2000  format(1x,'neutron density function')
 1000  format(1x,'proton density function')
 5000  format(1x,'*************************************************')
       stop
       end
