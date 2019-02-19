######################################################################################
#     This is your main program that tests the classes you have written.
#
#      Here is the Rubric:
#
#       Write/test the bottom up rod cutting solution.  You must print out the
#       the full solution (optimal price and pieces used) otherwise, no points
#       will be given.  (35 points)
#
#       Write/test the top down rod cutting solution.   You must print out the
#       the full solution (optimal price and pieces used) otherwise, no points
#       will be given.  (35 points)
#
#       Compare the two approaches using two lists.  Name the lists price1.txt
#       and price2.txt. (5 points)
#
#       Time the approaches, and create Table 1 that shows the times in seconds for
#       all possible n in pricelist 1 and 2.  Add to your report. (5 points)
#
#       In your report, create Table 2 that shows the order of growth in Big O notation
#       for time and space for both algorithms. (5 points)
#
#       Create a user interface menu.
#           The user interface asks the user what pricelist to use (1 or 2)
#           and what size to cut the rod. (5 points)
#           There is also an option to run through all n and both pricelists at once (5 points)
#           This is in a loop.  The user has an option to quit. (5 points)
#
####################################################################################
import time
import random
from cutrodproblem import topDownCutRod, BottumCutRod ,PrintCutRod


#need to change the template to read in two files that contain the 2 price lists.

#files are named price1.txt and price2.txt

#Create a User Inteface:
#In a loop, 
#The user is asked which pricelist(1 or 2) to use and what size to cut the rod (n).
#There is an option for the user to quit by entering q.
#If the user chooses an n larger than the pricelist can handle, the user is asked to try again.

pricelist = [3,5,8,9,10,17,17,18]


start_time_topDownCutRod = time.clock()
topDownCutRod(pricelist,8)
end_time_topDownCutRod = time.clock()
print("topDownCutRod CPU time (seconds): "  +str(end_time_topDownCutRod - start_time_topDownCutRod))
print(pricelist)

pricelist = [3,5,8,9,10,17,17,18]

start_time_BottumCutRod = time.clock()
BottumCutRod(pricelist,8)
end_time_BottumCutRod = time.clock()
print("BottumCutRod CPU time (seconds): "  +str(end_time_BottumCutRod - start_time_BottumCutRod))
print(pricelist)

PrintCutRod(pricelist,8)
#print("!")

list2=[]
list1=[]
sampleList=[]
def ConverttoList(name):
    with open(name, 'r') as handle:
        for line in handle:
            values = line.strip().split(',')

    
    for i in range(len(values)):
        sampleList.append(int(values[i]))       
    print(sampleList)
    return sampleList


def interface():
  
    
   x= (input('which list you want to use?:price1 or price2 ? or type "both"  if you want to run through both lists '))
   if x=="price1":
       ConverttoList("price1.txt")
   else:
       if x=="price2":
           ConverttoList("price2.txt")
       else:
          if x=='q':

              exit()
          else:
              if x!= "price1" and  x!="price2" and x!="both":
                  print("error! type 'price1' or price2 ")
                  interface()
              else:
                  if x=="both":  
                      a=ConverttoList("price1.txt")
                      for n in range(1,len(a)+1):
                          print("price1.txt    size of a rod = ",n)
                          start_time_topDownCutRod3=time.clock()
                          topDownCutRod(sampleList,n)
                          end_time_topDownCutRod3 = time.clock()
                          print("topDownCutRod CPU time (seconds): "  +str(end_time_topDownCutRod3- start_time_topDownCutRod3))


                          start_time_BottumCutRod3 = time.clock()
                          #BottumCutRod(sampleList)
                          PrintCutRod(sampleList,n)
                          end_time_BottumCutRod3 = time.clock()
                          #PrintCutRod(sampleList)
                          print("BottumCutRod CPU time (seconds): "  +str(end_time_BottumCutRod3 - start_time_BottumCutRod3))
                          print('\n')
                      list1.clear()
                      sampleList.clear()
                      

                      
                      a=ConverttoList("price2.txt")
                      for n in range(1,len(a)+1):
                          print("price2.txt    size of a rod = ",n)
                          start_time_topDownCutRod4=time.clock()
                          topDownCutRod(sampleList,n)
                          end_time_topDownCutRod4 = time.clock()
                          
                          print("topDownCutRod CPU time (seconds): "  +str(end_time_topDownCutRod3- start_time_topDownCutRod3))


                          start_time_BottumCutRod3 = time.clock()
                          #BottumCutRod(sampleList)
                          PrintCutRod(sampleList,n)
                          end_time_BottumCutRod3 = time.clock()
                          #PrintCutRod(sampleList)
                          print("BottumCutRod CPU time (seconds): "  +str(end_time_BottumCutRod3 - start_time_BottumCutRod3))
                          print('\n')
                      list1.clear()
                      sampleList.clear()
                    
                  interface()

                          #sampleList.clear()
                          #converttoList("price2.txt")

                      
                      
              
              
   
   
       
   y=(int)(input('what size of rod you want to cut '))
  # print("----------",y)
   #print("----------",len(sampleList))
   if y>len(sampleList):
       
       print("error! the rod is not that long,use number from 1 to ",len(sampleList))
       sampleList.clear()
       interface()
   else:
       
       for i in range(0,y):
           list1.append(sampleList[i])
       
   start_time_topDownCutRod2= time.clock()
   for i in range(0,len(list1)):
       print(list1[i])
       
   topDownCutRod(list1,y)
   end_time_topDownCutRod2 = time.clock()
   print("topDownCutRod CPU time (seconds): "  +str(end_time_topDownCutRod2- start_time_topDownCutRod2))

   start_time_BottumCutRod2 = time.clock()
   BottumCutRod(list1,y)
   end_time_BottumCutRod2 = time.clock()
   print("BottumCutRod CPU time (seconds): "  +str(end_time_BottumCutRod2 - start_time_BottumCutRod2))
   PrintCutRod(list1,y)
   list1.clear()
   sampleList.clear()
   interface()
   
   

       
       
  
   
def console():

   
    running = 1
    while running == 1:
        user = input(str('Enter "q"  to exit or press "enter"   to continue : '))
        for i in range(0,len(sampleList)):
                       sampleList.clear()
        if user == 'q':
            exit()
        else:
            interface()
        
    
console()  
