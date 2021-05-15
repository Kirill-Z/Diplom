      SUBROUTINE REGA (M,MH,XC,SX,Z,B,F,R,A,RR,KGA) 
! на основе матрицы коэфф. парной корреляции Z(MH) вычисляется вектор коэфф. A(M)
! линейной регрессии по модифицированному методу Гаусса
! Первая переменная - зависимая, остальные M-1 - независмые
      DIMENSION Z(MH,MH),B(MH,MH),F(MH),R(MH),A(MH),SX(MH),XC(MH)
c
c Z - матрица коэфф. парной коррел. (входная)
c XC - вектор средних значений переменных ММ
c SX - вектор сред.-квадр. отклонений переменных ММ
c B,F,R -рабочие массивы
c A - вектор коэфф.
c KGA - признак наличия решения (=0) или отсутствия (=1)
c M -  число коэфф. в  конкретном частном описании
c MH -  число коэфф. в  полном частном описании
c
      KGA=1
      do 1 I=1,MH
      F(I)=0.
      R(I)=0.
      A(I)=0.
      do 1 J=1,MH
      B(I,J)=0.
    1 continue
      do 11 I=2,M
      F(I-1)=Z(1,I)
      do 11 J=2,M
   11 B(I-1,J-1)=Z(I,J)
      M1=M-1
c      write(6,201) M,M1
      do 12 K=1,M1
   12 R(K)=K
c      write(6,200) F(1),B(1,1)
c      write(6,200) Z
      do 13 K=1,M1
      SM=0. 
! выбор максимального коэффициента корреляции
           do 14 I=K,M1
           do 14 J=K,M1
           if(abs(B(I,J)).le.SM) goto 14
           SM=abs(B(I,J))
           IM=I
           JM=J 
   14      continue      
c      write(6,200) SM
      if(SM.eq.0.) goto 16
      if(IM.eq.K) goto 101
           do 17 I=K,M1
           SM=B(K,I)
           B(K,I)=B(IM,I)
           B(IM,I)=SM
   17      continue      
      SM=F(K)
      F(K)=F(IM)
      F(IM)=SM
c      write(6,200) SM,F
  101 if(JM.eq.K) goto 102         
           do 18 I=1,M1
           SM=B(I,K)
           B(I,K)=B(I,JM)
           B(I,JM)=SM
   18      continue      
      SM=R(K)
      R(K)=R(JM)
      R(JM)=SM
c      write(6,200) SM,R
  102 SM=1/B(K,K)
      K1=K+1
!
      IF(K1.gt.M1) GO TO 30
           do 19 I=K1,M1   
   19      B(K,I)=B(K,I)+SM
   30  F(K)=F(K)*SM
c      write(6,200) SM,F
           do 20 I=1,M1   
           if(I.eq.K) goto 20
           SM=B(I,K)
           K1=K+1
      IF(K1.gt.M1) GO TO 31
                 do 21 J=K1,M1
   21            B(I,J)=B(I,J)-B(K,J)*SM
   31        F(I)=F(I)-F(K)*SM
   20      continue 
c      write(6,200) SM,F
   13 continue 
c
      do 22 K=1,M1
      if(K.eq.R(K)) goto 22
      K1=K+1  
      IF(K1.gt.M1) GO TO 22
           do 23 I=K1,M1   
           if(R(I).ne.K) goto 23
           SM=F(K)
           F(K)=F(I)
           F(I)=SM
           SM=R(I)
           R(I)=R(K)
           R(K)=SM
           goto 22
   23      continue 
   22 continue 
c      write(6,200) SM,F
      W1=0.
      RR=0.
      do 24 I=2,M
   24 RR=abs(F(I-1)*Z(I,1)+RR)
      RR=sqrt(RR)
      do 25 I=2,M
      A(I)=F(I-1)*SX(1)/SX(I)
      W1=A(I)*XC(I)+W1     
   25 continue 
      A(1)=XC(1)-W1
c      write(6,200) RR,A(1)
      goto 27
   16 continue 
      KGA=0.
   27 continue 
c      write(6,200) A 
c      write(6,200) RR
  200 format (10f16.8)
  201 format (10i6)
      END SUBROUTINE REGA
