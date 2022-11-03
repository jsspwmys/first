import time
st=time.time()
def  selection(a):
      for i in range (len(a)-1):
          small=i
          for i in range (i+1,len[a]):
           if a [small]>a[j]:
             small=j
          a[i],a[small]=a[small],a[i]
def printarr (a):
    for i in range (len (a)):
        print(a[i])
a=[69,14,1,50,58]
print("Before selecting array elements are:")
PrintArr(a)
print("/ n after selecting array elements are:")
selection(a)
end=time.time()
print=end.start()
