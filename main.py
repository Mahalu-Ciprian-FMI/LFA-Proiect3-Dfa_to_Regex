f=open('dfa.in','r') #deschidem fisierul

from collections import defaultdict;
from copy import deepcopy;
for i,line in enumerate(f): #citim din fisier linie cu linie,si actualizam DFA-ul de tip tuplu.
    if i==0:
        Q=line.split()
    if i==1:
        sigma=line.split()
    if i==2:
        start=line.strip()
    if i==3:
        final=line.split()
    delta=defaultdict(lambda:'null');
    j=0;
    if(i>=3):
        v=f.readlines()
        k=[];
        for j in range(0,len(v)):
            k=v[j].split()
            delta[(k[0],k[1])]=k[2]
#new start + remove old
for i in Q:
    for j in Q:
        for k in sigma:
            if(i in final or delta[(j,k)]==i):
                delta[('p0','e')]=i;
                start='p0';
counter=0;
#new final + remove old
if(len(final)!=1):
    for i in final:
        final.remove(i);
        delta[(i,'e')]='p1';
    sigma.append('e');
else:
    for i in Q:
        for j in sigma:
            if(delta[(final[0],j)]==i):
                delta[(final[0],'e')]='p1';
                sigma.append('e');
    final.remove(final[0]);
oldQ=Q;
Q.append('p0');
Q.append('p1');
sigma=set(sigma);
sigma=list(sigma);
print(sigma);

#   a . vid =vid
#   a . lambda =a
#   a* . a =a*
#   {a1,a2,...,an}*  = (a1+a2+...+an)* = (a1* . a2* . ... .an*) , oricare ar fi n
#   a1 . (a2+a3) =(a1.a2)+(a1.a3)

rows=len(Q);
columns=pow(rows,2);
newQ=[];
M={};

for i in range(rows):
    for j in range(rows):
        M[(i,j)]='r'+str(i) + str(j);
# predecesor=[q for q,delta[q] in delta.items() if q in delta[q].keys() and delta[q][q]!='e' and q!= l for l in Q];
# succesor=[q for q,delta[q] in delta[l for l in Q].items() if (delta[q]!='e' and q!=l for l in Q)];
# def get_if_loop(a,state):
#     if(delta[state][state]!='e'):
#         return delta[state][state];
#     else:
#         return '';
# for q in oldQ:
#     for i in predecesor:
#             for j in succesor:
#                 inter_loop = get_if_loop(q)
#                 # print('i : ', i, ' j : ', j)
#                 delta[i][j] = '+'.join(('(' + delta[i][j] + ')', ''.join(('(' + delta[i][q] + ')', '(' + inter_loop + ')' + '', '(' + delta[q][j] + ')'))));
#     new_delta = {r: {c: v for c, v in val.items() if c != q} for r, val in delta.items() if r != q}  # remove inter node
#     delta = deepcopy(new_delta);
#
# start_bucla = new_delta[start][start]
# init_to_final = new_delta[start][final[0]] + '(' + new_delta[final[0]][final[0]] + ')' + ''
# final_to_init = new_delta[final[0]][start]
# re = '(' + '(' + start_bucla + ')' + '+' + '(' + init_to_final + ')' + '(' + final_to_init + ')' + ')' + '' + '(' + init_to_final + ')'
# # re = '(' + re + ')'
# print('Regular Expression : ', re);

for i in range(rows):
    for j in range(1,columns):
        if(i!=j):
            (print(i))
        else:
            for q in oldQ:
                for j in sigma:
                    M[(i,j)]=str(M[(i,j)])+ '+' +'e';





