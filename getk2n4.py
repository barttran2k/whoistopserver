from sv import sv
import json as json
import logging

f = open("data_dot2/dgkd",'r',encoding='utf-8')
contents = f.read()
dgkd = contents.split(" ")
    
# f = open("data_dot2/pttkat",'r',encoding='utf-8')
# contents = f.read()
# pttkat = contents.split(" ")

# f = open("data_dot2/ttpt",'r',encoding='utf-8')
# contents = f.read()
# ttpt = contents.split(" ")

# f = open("data_dot2/atmmt",'r',encoding='utf-8')
# contents = f.read()
# atmmt = contents.split(" ")

# f = open("data_dot2/gtatm",'r',encoding='utf-8')
# contents = f.read()
# gtatm = contents.split(" ")

# f = open("data_dot2/ktgt",'r',encoding='utf-8')
# contents = f.read()
# ktgt = contents.split(" ")

sbd = []
hvt_rr = []
for i in dgkd:
    # if i[0] not in sbd and 'AT15' in i[0]:
    #     sbd.append(i[0])
    print(i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9])
# for i in pttkat:
#     if i[0] not in sbd and 'AT15' in i[0]:
#         sbd.append(i[0])
        
# for i in atmmt:
#     if i[0] not in sbd and 'AT15' in i[0]:
#         sbd.append(i[0])
        
# for i in ttpt:
#     if i[0] not in sbd and 'AT15' in i[0]:
#         sbd.append(i[0])
        
# for i in gtatm:
#     if i[0] not in sbd and 'AT15' in i[0]:
#         sbd.append(i[0])
# for i in ktgt:
#     if i[0] not in sbd and 'AT15' in i[0]:
#         sbd.append(i[0])
# for i in ttcscn:
#     if i[0] not in sbd and 'AT15' in i[0]:
#         sbd.append(i[0])
    
# # print(sbd)
# # print(len(sbd))
# all_sv = []
# for i in sbd:
#     hvt = ''
#     sv_dgkd = 0
#     sv_pttkat = 0
#     sv_ttpt = 0
#     sv_atmmt = 0
#     sv_gtatm = 0
#     sv_ktgt = 0
#     sv_ttcscn  = 0
#     for j in dgkd:
#         if j[0] == i:
#             hvt = j[1]
#             sv_dgkd = j[3]

#     for j in pttkat:
#         if j[0] == i:
#             sv_pttkat = j[3]
    
#     for j in atmmt:
#         if j[0] == i:
#             sv_atmmt = j[3]
            
#     for j in ttpt:
#         if j[0] == i:
#             sv_ttpt = j[3]
            
#     for j in gtatm:
#         if j[0] == i:
#             sv_gtatm = j[3]
            
#     for j in ktgt:
#         if j[0] == i:
#             sv_ktgt = j[3]
    
#     for j in ttcscn:
#         if j[0] == i:
#             sv_ttcscn = j[3]
#     st = sv(i,hvt,sv_dgkd,sv_pttkat,sv_ttpt,sv_atmmt,sv_gtatm,sv_ttcscn,sv_ktgt)   
  
#     all_sv.append({'sbd':i,'HVT': hvt,'DTB':st.getDTB()})
    
# newlist = sorted(all_sv, key=lambda d: d['DTB'], reverse=True)
# w = open('data_dot2/all_sv','w',encoding='utf-8')
# for  i in newlist:
#     name = i['HVT']
  
#     output = i['sbd']+'\t|\t'+f'{name:<25}'+'\t\t\t\t|\t'+str(i['DTB'])+'\n'
#     w.write(str(output))
    