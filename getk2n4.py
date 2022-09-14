from email import header
from sv_k2n4 import sv
import json as json
import logging


def change_to_4(x):
    if "F" == x:
        return 0
    if "D" == x:
        return 1
    if "D+" == x:
        return 1.5
    if "C" == x:
        return 2
    if "C+" == x:
        return 2.5
    if "B" == x:
        return 3
    if "B+" == x:
        return 3.5
    if "A" == x:
        return 3.8
    if "A+" == x:
        return 4
    else:
        return 0


dgkd = []
pttkat = []
ttpt = []
atmmt = []
gtatm = []
ktgt = []

f = open("data_dot2/dgkd", 'r', encoding='utf-8')
for line in f.readlines():
    contents = line.strip()
    dgkd.append(contents.split(","))

f = open("data_dot2/pttk", 'r', encoding='utf-8')
for line in f.readlines():
    contents = line.strip()
    pttkat.append(contents.split(","))

f = open("data_dot2/ttpt", 'r', encoding='utf-8')
for line in f.readlines():
    contents = line.strip()
    ttpt.append(contents.split(","))

f = open("data_dot2/atmmt", 'r', encoding='utf-8')
for line in f.readlines():
    contents = line.strip()
    atmmt.append(contents.split(","))

f = open("data_dot2/gtatm", 'r', encoding='utf-8')
for line in f.readlines():
    contents = line.strip()
    gtatm.append(contents.split(","))

f = open("data_dot2/ktgt", 'r', encoding='utf-8')
for line in f.readlines():
    contents = line.strip()
    ktgt.append(contents.split(","))

sbd = []
hvt_rr = []
for i in dgkd:
    if i[0] not in sbd and 'AT15' in i[0]:
        sbd.append(i[0])
for i in pttkat:
    if i[0] not in sbd and 'AT15' in i[0]:
        sbd.append(i[0])

for i in atmmt:
    if i[0] not in sbd and 'AT15' in i[0]:
        sbd.append(i[0])

for i in ttpt:
    if i[0] not in sbd and 'AT15' in i[0]:
        sbd.append(i[0])

for i in gtatm:
    if i[0] not in sbd and 'AT15' in i[0]:
        sbd.append(i[0])
for i in ktgt:
    if i[0] not in sbd and 'AT15' in i[0]:
        sbd.append(i[0])
sbd.sort()
# print(sbd)
# # print(len(sbd))
all_sv = []
for i in sbd:
    hvt = ''
    sv_dgkd = 0
    sv_pttkat = 0
    sv_ttpt = 0
    sv_atmmt = 0
    sv_gtatm = 0
    sv_ktgt = 0
    sv_ttcscn = 0
    for j in dgkd:
        if j[0] == i:
            hvt = j[1]
            numb = j[2].strip().split(' ')

            if len(numb) > 1:
                sv_dgkd += 0
            else:
                sv_dgkd = change_to_4(numb[0])
    # print(sv_dgkd)
    for j in pttkat:
        if j[0] == i:
            numb = j[2].strip().split(' ')

            if len(numb) > 1:
                sv_pttkat += 0
            else:
                sv_pttkat = change_to_4(numb[0])
    # print(sv_dgkd)
    for j in atmmt:
        if j[0] == i:
            numb = j[2].strip().split(' ')

            if len(numb) > 1:
                sv_atmmt += 0
            else:
                sv_atmmt = change_to_4(numb[0])
    # print(sv_dgkd)
    for j in ttpt:
        if j[0] == i:
            numb = j[2].strip().split(' ')

            if len(numb) > 1:
                sv_ttpt += 0
            else:
                sv_ttpt = change_to_4(numb[0])

    for j in gtatm:
        if j[0] == i:
            numb = j[2].strip().split(' ')

            if len(numb) > 1:
                sv_gtatm += 0
            else:
                sv_gtatm = change_to_4(numb[0])
    # print(sv_gtatm)
    
    for j in ktgt:
        if j[0] == i:
            numb = j[2].strip().split(' ')

            if len(numb) > 1:
                sv_ktgt += 0
            else:
                sv_ktgt = change_to_4(numb[0])
    # print(sv_ktgt)
    st = sv(i, hvt, sv_dgkd, sv_pttkat, sv_ttpt, sv_atmmt, sv_gtatm, sv_ktgt)

    all_sv.append({'sbd': i, 'HVT': hvt,"sv_dgkd":sv_dgkd, "sv_pttkat":sv_pttkat, "sv_ttpt":sv_ttpt, "sv_atmmt":sv_atmmt, "sv_gtatm":sv_gtatm, "sv_ktgt":sv_ktgt, 'DTB': st.getDTB()})
# for i in all_sv:
#     if i['sbd'] == "AT150524":
#         print(i)
newlist = sorted(all_sv, key=lambda d: d['DTB'], reverse=True)
w = open('data_dot2/all_sv', 'w', encoding='utf-8')
header = f'{"SBD":<8}'+'\t|\t'+f'{"Ho ten":<25}'+'\t\t\t\t|\t'+"DTB"+'\t|\t'+"DGKD"+'\t|\t'+"PTTKAT"+'\t|\t'+"TTPT"+'\t|\t'+"ATMMT"+'\t|\t'+"GTATM"+'\t|\t'+"KTGT"+'\t|\t'+'\n'
w.write(str(header))
for i in newlist:
    name = i['HVT']
    output = i['sbd']+'\t|\t'+f'{name:<25}'+'\t\t\t\t|\t'+str(i['DTB'])+'\t|\t'+str(i['sv_dgkd'])+'\t|\t'+str(i['sv_pttkat'])+'\t|\t'+str(i['sv_ttpt'])+'\t|\t'+str(i['sv_atmmt'])+'\t|\t'+str(i['sv_gtatm'])+'\t|\t'+str(i['sv_ktgt'])+'\t|\t'+'\n'
    # print(str(output))
    w.write(str(output))
