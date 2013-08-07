#! /usr/bin/python
import os;from sys import *;from fcntl import *;from termios import *
R,C,s,u,b,r,c=(lambda x:2-x//3),(lambda x:x%3),' ',0,['x','o'],1,1
def m():
 ot,nt=tcgetattr(stdin.fileno()),tcgetattr(stdin.fileno());nt[3]=nt[3] & ~ICANON & ~ECHO;tcsetattr(stdin.fileno(),TCSANOW,nt);of=fcntl(stdin.fileno(),F_GETFL);fcntl(stdin.fileno(),F_SETFL,of|os.O_NONBLOCK)
 try:
  while 1:
   try:c=stdin.read(1);break
   except IOError:pass
 finally:tcsetattr(stdin.fileno(),TCSAFLUSH,ot);fcntl(stdin.fileno(),F_SETFL,of);return c
def pp(t):print "\n\n"+"\n".join([(" ".join([t[w][l] for l in range(3)])) for w in range(3)]),
t=[[s]*3,[s]*3,[s]*3];pp(t)
while 1:
 if sum(["".join(["".join(w) for w in t]).count(p) for p in b])==9: print "Tie!";break
 i=m()
 if not i.isdigit(): continue
 if i=='0':
  if r+c=='':continue
  else: t[r][c]=b[u];u=1-u;r=c=''
 else:
  if r+c!='':t[r][c]=s
  i=int(i)-1
  if t[R(i)][C(i)] not in b:r,c=R(i),C(i);t[r][c]='_'
 pp(t)
 if (t[1][1] in b)and((t[1][1]==t[0][0]and t[1][1]==t[2][2])or(t[1][1]==t[0][2]and t[1][1]==t[2][0])or(t[1][1]==t[0][1]and t[1][1]==t[2][1])or(t[1][1]==t[1][0]and t[1][1]==t[1][2])): w=t[1][1]
 elif ((t[0][0]==t[1][0]and t[0][0]==t[2][0])or(t[0][0]==t[0][1]and t[0][0]==t[0][2]))and(t[0][0]) in b: w=t[0][0]
 elif ((t[0][2]==t[1][2]and t[0][2]==t[2][2])or(t[2][0]==t[2][1]and t[2][0]==t[2][2]))and(t[2][2]) in b: w=t[2][2]
 else: continue
 print w.upper()+" Won!";break
while 1:pass
