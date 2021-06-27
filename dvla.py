from itertools import product
import numpy as np
import requests
import math
import time
print(time.perf_counter())
file1 = open("numberplates1.txt","w")
regno="ro62r?u"
count=regno.count('?')
regnolen = len(regno)
alpha = "A","B","C","D","E","F","G","H","J","K","M","N","O","P","R","S","T","U","V","W","X","Y","Z"
numbero = "0","1","2","3","4","5","6","7","8","9",
unsurepos=[]
numpos=[]
charpos=[]
url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
listreg = list(regno)
a = np.array(listreg),(listreg)
arr=[]
unsurepos = ([pos for pos, char in enumerate(regno) if char =='?'])
comb = product((alpha),repeat = count)

for b in unsurepos:
    #print(a)
    if 2 <= b <= 3:
        #rint("is number")
        numpos.append(b)
    else: charpos.append(b)

n=numbero
l=alpha
co=[]

for c in range(regnolen):
    #print(b)
    if c in list(charpos):
        co.append(l)
    if c in list(numpos):
        co.append(n)

def myfunc2(*args, **kwargs):
    #print(args)
    for element in product(*args):
        #print(co)
        #print(element)
        arr.append(element)
myfunc2(*co)

arrlen = len(arr)
for d in range(arrlen):
    a = np.insert(a, 0, (listreg), axis=0)

for e in range(arrlen):
    for f, g in enumerate(unsurepos):
        a[e][g] = arr[e][f]

for b in range(arrlen):
    print(time.perf_counter())
    regnofin = ((a[b][0])+(a[b][1])+(a[b][2])+(a[b][3])+(a[b][4])+(a[b][5])+(a[b][6]))
    #print(regnofin)
    quotient = b / arrlen
    percentage = math. ceil(quotient * 100)
    print(str(percentage)+("%"))
    print(("remaining combinations to try ")+(str(arrlen-b)))
    payload = "{\n\t\"registrationNumber\": \"" + regnofin + "\"\n}"
    headers = {
        'x-api-key': 'pToXuWje3X8z6GWEC6pOb2otrmVvdCx58Xn5y8uK',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    if response.status_code == 200:
        print(data)
        str1=(data['registrationNumber'])
        str2=(data['make'])
        str3=(data['colour'])
        dom = str((data['yearOfManufacture']))
        print(str1)
        print(str2)
        print(str3)
        print(dom)
        print("\n")
        file1.write((str1) + "\n" + (str2) + "\n" + (str3) + "\n" + (dom) + "\n" + "\n" + "\n")
print(time.perf_counter())
file1.close()
