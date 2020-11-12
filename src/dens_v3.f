
c      Calculates the nuclear density as a function of radius

       program nucden
       implicit real*8(a-h,o-z)
       common/parz/nden
       common/abc/xnorm
       dimension :: step(100)
       dimension :: den(100)
       dimension :: rhop(100), rhon(100), rhot(100)

       open(450,file='denopts.don')
       read(450,*) nden, up_lim, nstep, ta, tz

       tn = ta - tz

       open(600,file='opt_par.etr')
       read(600,*) rp, cp, wp, rn, cn, wn

       dt = 0.d0

       open(999,file='rhos.don')

       pi = 3.14159d0

       if(nstep .gt. 0) then
          do i=1,nstep
             step(i) = up_lim*((i-1)/(nstep-1.0))
          end do
       else if((nstep .eq. 0) .or. (nstep .lt. 0)) then
          go to 5000 
       end if

c     normalize the proton function
       if(nden .EQ. 2 .OR. nden .EQ. 4) then
          call xnormalize(pi,rp,cp,tz,dt)
       else if(nden .EQ. 3) then
          call xnormalize(pi,rp,cp,tz,wp)
       end if
       ap=xnorm

c     normalize the neutron function
       if(nden .EQ. 2 .OR. nden .EQ. 4) then
          call xnormalize(pi,rn,cn,tn,dt)
       else if(nden .EQ. 3) then
          call xnormalize(pi,rn,cn,tn,wn)
       end if
       an=xnorm 

       if(nden .EQ. 2) then
          do i=1,nstep
             rhop(i) = rho(step(i),ap,rp,cp)
             rhon(i) = rho(step(i),an,rn,cn)
             rhot(i) = rhop(i) + rhon(i)
          end do
       else if(nden .EQ. 4) then
          do i=1,nstep
             rhop(i) = rho_fy(step(i),ap,rp,cp,tz)
             rhon(i) = rho_fy(step(i),an,rn,cn,tn)
             rhot(i) = rhop(i) + rhon(i)
          end do
       else if(nden .EQ. 3) then
          do i=1,nstep
             rhop(i) = rho_3pf(step(i),ap,rp,cp,wp)
             rhon(i) = rho_3pf(step(i),an,rn,cn,wn)
             rhot(i) = rhop(i) + rhon(i)
          end do
       end if

       write(999, 2332) 
       do i=1,nstep
          write(999, 2300) step(i), rhop(i), rhon(i), rhot(i) 
       end do 

2332   format(2x,"dens",5x,"rhop",5x,"rhon"5x,"rhot")
1000   format("                     ")
2300   format(F7.3,2x,F7.3,2x,F7.3,2x,F7.3)
5000   continue
       end program

