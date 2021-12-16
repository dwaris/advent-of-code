import numpy as np
f = open("day16/input.txt","r")
def packetparse(binstring,versionlist):
  if binstring == '0'*len(binstring):
    return 0
  version = int(binstring[0:3],2)
  versionlist.append(version)
  type = int(binstring[3:6],2)
  if type==4:
    i = 6
    litbin = ""
    while binstring[i] == '1':
      litbin += binstring[i+1:i+5]
      i+=5
    litbin += binstring[i+1:i+5]
    finalval = (int(litbin,2))
    return (i+5,finalval)
  else:
    id = binstring[6]
    valuelist = []
    finval = 0
    if id=='0':
      binlength = int(binstring[7:22],2)
      currentlength = 0
      i = 22
      while currentlength < binlength:
        count,val = packetparse(binstring[i:],versionlist)
        valuelist.append(val)
        i+=count
        currentlength += count
      size = 22+currentlength
    elif id=='1':
      numbins = int(binstring[7:18],2)
      currentbins = 0
      currentlen = 0
      i = 18
      while currentbins < numbins:
        count,val = packetparse(binstring[i:],versionlist)
        valuelist.append(val)
        currentlen+=count
        i+=count
        currentbins+=1

      size = 18+currentlen
    if type == 0: finval = sum(valuelist)
    if type ==1: finval = np.prod(valuelist)
    if type ==2: finval = min(valuelist)
    if type ==3: finval = max(valuelist)
    if type ==5:
      if valuelist[0]>valuelist[1]: finval = 1
      else: finval = 0
    if type ==6:
      if valuelist[0]<valuelist[1]: finval = 1
      else: finval = 0
    if type ==7:
      if valuelist[0]==valuelist[1]: finval = 1
      else: finval = 0
    return (size,finval)
binconv = ""
versionlist = []
for line in f:
  for char in line.strip():
    strbin = bin(int(char,16))[2:]
    while len(strbin)<4: strbin = '0'+strbin
    binconv += strbin

_,value = packetparse(binconv,versionlist)

result_1 = np.sum(versionlist)
result_2 = value

print(f"Result 1: {result_1}\nResult 2: {result_2}")
