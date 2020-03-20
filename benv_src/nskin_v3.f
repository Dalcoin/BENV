
c      Program nucquant: Version 4.0
c      Modified by: Randy Millerson

       program nucquant
       implicit real*8(a-h,o-z)
       common/paspoi/pas(200),poi(200),x(200),w(200)
       common/binding/totbe,binde1,binde2,binde3
       common/maineos/xdata(75),zdata(75),nxdata,
     3                 xsnm(75), ydata(75),nxnm,
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
       common/esymc/esym_coef
       common/rhoeval/rhoneu,rhopro,rhotot,alphapar
         
          
       open(unit=117,file='opt_par.etr')
       open(unit=8,file='nucleus.don')
       open(unit=999,file='skin.srt')
c       open(unit=000,file='dump.don')
              

c    number of integration points
       read(8,*) n1,n2,n3
       read(8,*) x1,x2
       read(8,*) ta,tz
       tn=ta-tz

       read(117,*) rp, cp, wp, rn, cn, wn


c      Build model from EoS
       call init(n1, n2, n3, x1, x2, ta, tz)

       call xnormalize(pi,rp,cp,tz,wp)
       ap=xnorm                  
       call xnormalize(pi,rn,cn,tn,wn)
       an=xnorm
         
c      calculate radii
       call rms(ap,rp,cp,wp,an,rn,cn,wn,pi,tz,tn,ta,64)

c      calculate charge radii 
       call chrms(ap,rp,cp,wp,pi,tz,64)

c      calculate symmetry energy coefficient 
       call sym_eng_coef(ap,rp,cp,wp,an,rn,cn,wn)
       en = energy(rp, cp, wp, rn, cn, wn)

       write(999,1344) fint2,fint1,fint2-fint1,chr,en,esym_coef
c       write(*,1344) fint2,fint1,fint2-fint1,chr,en,esym_coef

 1344  FORMAT(F10.4,F10.4,F10.4,F10.4,F10.4,F10.4)
 4000  format(1x,'neutron skin=',f10.4)
 5555  format(1x,'neutron radius',f10.4)
 2000  format(1x,'neutron density function')
 1000  format(1x,'proton density function')
 5000  format(1x,'*************************************************')
       end
