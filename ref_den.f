       
        
       program ref_den
       implicit real*8(a-h,o-z)
       dimension :: e0(100), e1(100), esym(100)
       dimension :: xkf(100), den(100), den_r(100)
       dimension :: frac(100), coef(100,4)
       
       open(111,file='ex_nxlo.don')
       open(151,file='out_skin_tables.srt')
       open(515,file='par.don')
       open(525,file='serv_par.txt')
c       open(000,file='dump.don')
       
       open(999,file='list_ref_dens.srt')
       
       read(525,*) n0, n1, it1, it2, it3       
       
       read(515,*) n, it0, it1, it2, it3
       
       pi = 3.14159d0
       n2 = n-1
       
       gam = 4.0
       do i=1,n
          read(111,*) xkf(i), e0(i), e1(i)
          den(i) = gam*(xkf(i)**3)/(6.d0*pi**2)    
          esym(i) = e1(i) - e0(i)
c          write(000,*) xkf(i), den(i), e0(i), e1(i), esym(i) 
       end do 
       
       call dcsakm(n,esym,den,frac,coef)
       
       m=n0*n1
       do i=1,m
          read(151,*) ia, iz, radz, radn, skn, chrgr, be, esymc
          den_r(i) = dcsval(esymc,n2,frac,coef) 
c          write(000,*) esymc, den_r(i),m
          write(999,*) den_r(i)
       end do
        
       end  
