######################################################################################
#
#
#  Name:Irakli Grigolia
#  Date:14.04.2018
#
#  This project compares two approaches to solving the cut rod problem.  A top down
#  approach and a bottom up approach.
#
#   
#
####################################################################################
import time
import random

INT_MIN=-999999 
def topDownCutRod(pricelist,n):
    N = len(pricelist)
    NN = n
    r = [0 for x in range (N+2)]
    s = [0 for x in range (N+2)]
    ss = [0 for x in range (N+2)]
    for i in range (0,N+2):
        r[i]=INT_MIN


    #print (r,N,pricelist)    
    print("the topdown optimal price is:", topDownMemoization(pricelist,n,r,s,ss))

    f = [0 for x in range(N+2)]
    a = 0

    while n>0:
        a=a+1
        #print("price of piece used:",(r[n]-r[s[n]]))
        f[ss[n]]=f[ss[n]]+1
        n=s[n]

        
    print(a,"piece(s) were used")

    array=[]
    for i in range(0,N):
        array.append(f[i])
    print (array)
    array.clear()
        
    
 
def topDownMemoization(pricelist,n,r,s,ss):
    #print(r,n)
    if r[n]>= 0:
        return r[n]
    if n==0:
        q=0
    else:
        q=INT_MIN
        for i in range(0,n):
            
            k=pricelist[i]+topDownMemoization(pricelist,n-i-1,r,s,ss)
            if q<k:
                q=k
                s[n]=n-i-1
                ss[n]=i
    r[n]=q
    return q
   
   
def BottumCutRod(pricelist,n):
  q=INT_MIN
  r = [0 for x in range (n+1)]
  s = [0 for x in range (n+1)]
  r[0]=0
  
  for j in range (0,n):
      #q=INT_MIN
      w=0
      for i in range(0,j+1):
          if q<pricelist[i]+r[j-i]:
              q=pricelist[i]+r[j-i]
              s[j+1]=i+1
            
      r[j+1]=q
      

      
  print("bottom up optimal price is :",q)
  
  return r,s




def PrintCutRod(pricelist,n):
    a=0
    N = n
    r,s = BottumCutRod(pricelist,n)

    array=[]
    f=[0 for x in range(len(pricelist)+1)]

    while n > 0:
        a=a+1
        f[s[n]-1] = f[s[n]-1] + 1
        n -= s[n]
    #print (array)
    array=[]
    for i in range(0,len(pricelist)):
        array.append(f[i])
    print (array)
    return array
 
