      SUBROUTINE CORA (N1,N2,N,M,MH,X,Z)
! ���᫥��� ������ ��୮� ���५�樨 �� ���祭�� �室���� ���ᨢ�
      DIMENSION X(N,MH),Z(MH,MH)
c
c X - �室��� ࠡ�稩 ���ᨢ (��ନ஢����)
c Z - ����� �����. ��୮� ���५.
c M -  �᫮ �����. �  �����⭮� ��⭮� ���ᠭ��
c MH -  �᫮ �����. �  ������ ��⭮� ���ᠭ��
c N1- ��砫� �����饩 �롮ન �� ��饩
c N2- ����� �����饩 �롮ન
c N  - ����� ��饩 �롮ન (�᫮ ��砥�)
c
!      write(6,201) M
      do 1 J=1,MH
      do 1 I=1,MH
    1 Z(I,J)=0.
      do 5 J=1,M
      do 5 I=1,M
      if(J-I) 7,9,8
    7 N3 =N2-N1+1
         do 6 K=N1,N2
    6    Z(I,J)=Z(I,J)+X(K,J)*X(K,I)
      Z(I,J)=Z(I,J)/float(N3)
      goto 5
    8 Z(I,J)=Z(J,I)
      goto 5
    9 Z(I,J)=1.
    5 continue       
c      write(6,200) Z
  200 format(10f8.3)
  201 format(10i8)
      END SUBROUTINE CORA
