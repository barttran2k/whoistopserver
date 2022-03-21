from sv import sv
import json as json
import logging
f = open("data/atcsdl.txt",'r',encoding='utf-8')
contents = f.read()
atcsdl = (json.loads(contents))
    
f = open("data/athdh.txt",'r',encoding='utf-8')
contents = f.read()
athdh = json.loads(contents)

f = open("data/csattt.txt",'r',encoding='utf-8')
contents = f.read()
csattt = json.loads(contents)

f = open("data/csltmm.txt",'r',encoding='utf-8')
contents = f.read()
csltmm = json.loads(contents)

f = open("data/ptpmud.txt",'r',encoding='utf-8')
contents = f.read()
ptpmud = json.loads(contents)

f = open("data/qlxdcs.txt",'r',encoding='utf-8')
contents = f.read()
qlxdcs = json.loads(contents)

f = open("data/ttcscn.txt",'r',encoding='utf-8')
contents = f.read()
ttcscn = json.loads(contents)

sbd = []
hvt_rr = []
for i in atcsdl:
    if i[0] not in sbd and 'AT15' in i[0]:
        sbd.append(i[0])
        
for i in athdh:
    if i[0] not in sbd and 'AT15' in i[0]:
        sbd.append(i[0])
        
for i in csltmm:
    if i[0] not in sbd and 'AT15' in i[0]:
        sbd.append(i[0])
        
for i in csattt:
    if i[0] not in sbd and 'AT15' in i[0]:
        sbd.append(i[0])
        
for i in ptpmud:
    if i[0] not in sbd and 'AT15' in i[0]:
        sbd.append(i[0])
for i in qlxdcs:
    if i[0] not in sbd and 'AT15' in i[0]:
        sbd.append(i[0])
for i in ttcscn:
    if i[0] not in sbd and 'AT15' in i[0]:
        sbd.append(i[0])
    
# print(sbd)
# print(len(sbd))
all_sv = []
for i in sbd:
    hvt = ''
    sv_atcsdl = 0
    sv_athdh = 0
    sv_csattt = 0
    sv_csltmm = 0
    sv_ptpmud = 0
    sv_qlxdcs = 0
    sv_ttcscn  = 0
    for j in atcsdl:
        if j[0] == i:
            hvt = j[1]
            sv_atcsdl = j[3]

    for j in athdh:
        if j[0] == i:
            sv_athdh = j[3]
    
    for j in csltmm:
        if j[0] == i:
            sv_csltmm = j[3]
            
    for j in csattt:
        if j[0] == i:
            sv_csattt = j[3]
            
    for j in ptpmud:
        if j[0] == i:
            sv_ptpmud = j[3]
            
    for j in qlxdcs:
        if j[0] == i:
            sv_qlxdcs = j[3]
    
    for j in ttcscn:
        if j[0] == i:
            sv_ttcscn = j[3]
    st = sv(i,hvt,sv_atcsdl,sv_athdh,sv_csattt,sv_csltmm,sv_ptpmud,sv_ttcscn,sv_qlxdcs)   
  
    all_sv.append({'sbd':i,'HVT': hvt,'DTB':st.getDTB()})
    
newlist = sorted(all_sv, key=lambda d: d['DTB'], reverse=True)
w = open('data/all_sv.txt','w',encoding='utf-8')
for  i in newlist:
    name = i['HVT']
  
    output = i['sbd']+'\t|\t'+f'{name:<20}'+'\t\t\t\t|\t'+str(i['DTB'])+'\n'
    w.write(str(output))
    