      SUBROUTINE NORM (N1,N2,N,M,MH,X,X1,XC,SX)
! ���᫥��� �।���, ��ᯥ�ᨨ � ��ନ஢�� ������ �室���� ���ᨢ�
      DIMENSION X(N,MH),XC(MH),SX(MH),X1(N,MH)
c
c X - �室��� ࠡ�稩 ���ᨢ
c XC - ����� �।��� ���祭�� ��६����� ��
c SX - ����� �।.-�����. �⪫������ ��६����� ��
c X1 - ��ନ஢���� ���祭�� ���ᨢ� X
c M -  �᫮ �����. �  �����⭮� ��⭮� ���ᠭ��
c MH -  �᫮ �����. �  ������ ��⭮� ���ᠭ��
c N1- ��砫� �����饩 �롮ન �� ��饩
c N2- ����� �����饩 �롮ન
c N  - ����� ��饩 �롮ન (�᫮ ��砥�)
c
      N3=N2-N1+1
      do 1 J=1,M
      XC(J)=0.
          do 2 I=N1,N2
    2     XC(J)=XC(J)+X(I,J)
      XC(J)=XC(J)/float(N3)
      SX(J)=0.
          do 3 I=N1,N2
    3     SX(J)=SX(J)+(X(I,J)-XC(J))**2
      SX(J)=sqrt(SX(J)/float(N3))
          do 4 I=N1,N2
    4     X1(I,J)=(X(I,J)-XC(J))/SX(J)
    1 continue       
      END SUBROUTINE NORM
