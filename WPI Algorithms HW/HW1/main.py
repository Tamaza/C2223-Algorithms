@ -0,0 +1,434 @@
#######################################################################################
#
#
#  Name:Irakli Grigolia
#  Date: 19.03.2018
#
#  This project compares the implementation of a Priority Queue using two different
#  data structures, a heap and an unsorted list.  It then measures each module (by time)
#  and prints out the results.  It uses a random number generator to create
#  seven different size lists (10, 50, 500, 1000, 5000, 10000, 50000)
#  to be used for testing.
#
# Once you have your classes working, you will use your PQ_Heap class and PQ_List class
#   to create and compare a rudimentary job scheduler.  
#          1) create a file named sample_queue.txt with 10 random numbers (by hand)
#             we will create our own txt file to test your code.
#          2) Your job scheduler will do the following:
#               start clock
#               enqueue the jobs one at a time 
#               loop until all jobs are complete
#                  looks at top of queue and print it out (doesn't delete)
#                  Removes 1 job from the queue 
#               stop clock
#
# After you have your time trials complete, create a table that lists each module (rows)
# and time efficiency for worst case (Big O). 
#
#    Further instructions and the rubric is commented into the code below.
#    Leave all comments that we have created intact for grading.
#
####################################################################################
import time
import random

 
class PQ_Heap(object):    
    def __init__(self, sampleList):
        #print ("creates a min heap from passed in list")
        self._heap = []
        self._size = 0

        for i in range(0,len(sampleList)):
            self.enQueue(sampleList[i])
        
        print("Current priority queue stored is: " ,self._heap)    
#      
#        Create a min heap from passed in list - return the min heap (10 points)
        
    def enQueue(self, item):
       # print ("adds an item to the PQ and reheapifies")

        self._size += 1
        self._heap.append(item);

        index = len(self._heap) - 1

        
        
        while index > 0:
            if self._heap[index] < self._heap[(index-1)//2]:
                self._heap[index],self._heap[(index-1)//2] = self._heap[(index-1)//2],self._heap[index] # swap index and (index-1)//2   a,b=b,a
            else:
                break
            index = (index-1)//2

        print (item, " <-- new item")
        print("parent: ")
        if index > 0:
            print(self._heap[(index-1)//2])
        else:
            print("n/a")
        print("left child: ")
        if 2*index+1<len(self._heap):
            print(self._heap[2*index+1])
        else:
            print("n/a")
        print("right child: ")
        if 2*index+2<len(self._heap):
            print(self._heap[2*index+2])
        else:
            print("n/a")
            print("“After enQueue an item, current priority queue stored is:", self._heap)
    
#
# Add an item to the PQ and reheapify. Print out parent and children (if applicable)
# or n/a if not (10 points)
    def deQueue(self):
        #print ("removes the highest priority item from the PQ and reheapifies")
        self._heap[0] = self._heap[len(self._heap) - 1]
        self._heap.pop()
        index = 0;
        self._size -= 1

        
        while index < len(self._heap):
           if 2*index+1 < len(self._heap):
               leftChild = self._heap[2*index+1]
           else:
               leftChild = 999999999 # infinity
               
           if 2*index+2 < len(self._heap):
               rightChild = self._heap[2*index+2]
           else:
               rightChild = 999999999 # infinity

           if self._heap[index]<min(leftChild,rightChild):
               break
           if leftChild<rightChild:
               self._heap[index],self._heap[2*index+1] = self._heap[2*index+1],self._heap[index]
               index = 2*index+1
           elif leftChild>=rightChild:
               self._heap[index],self._heap[2*index+2] = self._heap[2*index+2],self._heap[index]
               index = 2*index+2
               print("After deQueue an item, current priority queue stored is: ", self._heap)
    #
    #       Remove the highest priority item from the PQ and reheapify (10 points)
            
    def sneakAPeek(self):
        print ("returns the highest priority in the PQ, but does not remove it")
        
        print("The highest priority item is: ", self._heap[0])
#
#       Return the highest priority item from the PQ, but don't remove it (2 points)

    def isEmpty(self):
        print ("returns T if PQ is empty, F if PQ has entries")
        if self._size == 0:
            print("True")    
            return True
        
        else:
            print("False")   
            return False
        
#       Return a T if PQ is empty, F if PQ is not empty (2 points)
#
    def size(self):
        print ("returns number of items in queue")
        print("Number of items in queue is ", self._size)
#       Return the number of items in the queue (2 points)

class PQ_List(object):    
    def __init__(self, sampleList):
        self.List = []
        self._size = 0
               
        for i in range(0,len(sampleList)):
            self.enQueue(sampleList[i])
        print ("creates an unsorted list from passed in list")    
        print("Current priority queue stored is:", self.List)
#      
#        Returns the list (2 points)
        
    def enQueue(self, new_item):
        self.List.append(new_item)
        self._size += 1
        print ("adds an item to the PQ")
        print("“After enQueue an item, current priority queue stored is: ", self.List)

#       Add an item to the PQ (5 points)
        
    def deQueue(self):
        self._size -= 1
        index = 0
        minVal = self.List[0]
        for i in range(0,len(self.List)):
            if minVal>self.List[i]:
                minVal=self.List[i]
                index=i
        self.List.pop(index)
        print("After deQueue an item, current priority queue stored is: ", self.List)
       

#       Remove the highest priority item from the PQ (5 points)
        
    def sneakAPeek(self):
     index = 0
     minVal = self.List[0]
     for i in range(0,len(self.List)):
            if minVal>self.List[i]:
                minVal=self.List[i]
                
     print("The highest priority item is: ", minVal)
#print ("returns the highest priority in the PQ, but does not remove it")

#
#       Return the highest priority item from the PQ, but don't remove it (2 points)
       
    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False
        print ("returns T if PQ is empty, F if PQ has entries")
        
#       Return a T if PQ is empty, F if PQ is not empty (2 points)
#       
    def size(self):
        print ("returns number of items in queue")
        print("Number of items in queue is ", self._size)
#       Return the number of items in the queue (2 points)



#print ("Then time each module as it uses each list (using time.clock) and print")
#print ("out results in a table")
num_list = []
print(num_list)
def List_generator(size):
    num_list = [random.randint(1,50000) for x in range(0, size)]
    return num_list
#Use a pseudo random number generator to generate 7 different size lists (10 points)


    
#print ("Create 7 lists of different sizes (10, 50, 500, 1000, 5000, 10000, 50000) to use for testing.")
#print ("Use a pseudo random number generator to generate lists (1-50000)")
#Use a pseudo random number generator to generate 7 different size lists (10 points)

List1 = List_generator(10)
List2 = List_generator(50)
List3 = List_generator(500)
List4 = List_generator(1000)
List5 = List_generator(5000)
List6 = List_generator(10000)
List7 = List_generator(50000)

sampleList=[]
def ConverttoList():
    with open("sample_queue.txt", 'r') as handle:
        for line in handle:
            values = line.strip().split(',')

    
    for i in range(len(values)):
        sampleList.append(int(values[i]))       
    print(sampleList)
    return sampleList
  
#change this code to create lists as described above and time each function


txtList = ConverttoList()


#For each module, start the clock, call module, stop clock

start=time.clock()
my_heapPQ = PQ_Heap(sampleList) #print first 10 numbers, use size to prove the rest is there
elapsed=(time.clock()-start)


   

start1=time.clock()
my_heapPQ.enQueue(1500)
elapsed1=(time.clock()-start1)

start2=time.clock()
my_heapPQ.deQueue()
elapsed2=(time.clock()-start2)

start3=time.clock()
my_heapPQ.sneakAPeek()
elapsed3=(time.clock()-start3)

start4=time.clock()
my_heapPQ.isEmpty()
elapsed4=(time.clock()-start4)

start5=time.clock()
my_heapPQ.size()
elapsed5=(time.clock()-start5)

start6=time.clock()
my_listPQ = PQ_List(sampleList) #print first 10 numbers, use size to prove the rest is there
elapsed6=(time.clock()-start6)



start7=time.clock()
my_listPQ.enQueue(1500)
elapsed7=(time.clock()-start7)

start8=time.clock()
my_listPQ.deQueue()
elapsed8=(time.clock()-start8)

start9=time.clock()
my_listPQ.sneakAPeek()
elapsed9=(time.clock()-start9)

start10=time.clock()
my_listPQ.isEmpty()
elapsed10=(time.clock()-start10)

start11=time.clock()
my_listPQ.size()
elapsed11=(time.clock()-start11)




print(" time statistics for PQ  Heap and List :")


    
print("                        Heap                       List"                    )
print("PQ_Heap:             "  ,  elapsed ,"        ",elapsed6                   )
print("enQueue:             "  ,  elapsed1,"        ",elapsed7                   )
print("deQueue:             "  ,  elapsed2,"        ",elapsed8                   )
print("sneakAPeek:          "  ,  elapsed3,"        ",elapsed9                   )
print("isEmpty:             "  ,  elapsed4,"        ",elapsed10                  )
print("size:                "  ,  elapsed5,"        ",elapsed11                  )

          



    
#Time each module for each list, and print the results in a table
# (rows - modules, columns - heap, list) (10 points) 


#   Once you have your classes working, you will use your PQ_Heap class and PQ_List class
#   to create and compare a rudimentary job scheduler.  
#          1) create a file named sample_queue.txt with 10 random numbers (by hand)
#             we will create our own txt file to test your code.
#          2) Your 2 job schedulers will do the following:
#               start clock
#               enqueue the jobs one at a time 
#               loop until all jobs are complete
#                  looks at top of queue and print it out (doesn't delete)
#                  Removes 1 job from the queue 
#               stop clock


#Time both your schedulers and print out results for each here (5 points)


def heapTester(list):
    start=time.clock()
    Heap = PQ_Heap([])
    for i in range(0,len(list)):
        Heap.enQueue(list[i])

    for i in range(0,len(list)):
        Heap.sneakAPeek()
        Heap.deQueue()
        
    duration=(time.clock()-start)
    return duration

def listTester(list):
    start=time.clock()
    List = PQ_List([])
    for i in range(0,len(list)):
        List.enQueue(list[i])

    for i in range(0,len(list)):
        List.sneakAPeek()
        List.deQueue()
        
    duration=(time.clock()-start)
    return duration

def tester(list):

    time1=time.clock()
    my_newPQ = PQ_Heap(list) 
    end=(time.clock()-time1)
    print("time for init is :",end)
    
    time2=time.clock()
    my_heapPQ.enQueue(1)
    end1=(time.clock()-start2)
    print("time for enQueue is:",end1)
    time4=time.clock()
    my_heapPQ.deQueue()
    end2=(time.clock()-start3)
    print("time for deQueue is :",end2)

    time4=time.clock()
    my_heapPQ.sneakAPeek()
    end3=(time.clock()-start4)
    print("time for sneakAPeek is :",end3)

    time5=time.clock()
    my_heapPQ.isEmpty()
    end4=(time.clock()-start5)
    

    time6=time.clock()
    my_heapPQ.size()
    end5=(time.clock()-start6)
    




print ("From sample_queue.txt results: ", " Heap_time = ", heapTester(txtList),"    List_time = ", listTester(txtList))

# PQ_Heap O(lg(N))
# PQ_List O(N)



#Once you have your time trials complete, create a table that lists each module (rows)
#and time efficiency for worst case (Big O) and print here. (10 points)  


#print ("Size = ",10, " Heap_time = ", heapTester(List1),"    List_time = ", listTester(List1))
#print ("Size = ",50, " Heap_time = ", heapTester(List2),"    List_time = ", listTester(List2))
#print ("Size = ",500, " Heap_time = ", heapTester(List3),"    List_time = ", listTester(List3))
#print ("Size = ",1000, " Heap_time = ", heapTester(List4),"    List_time = ", listTester(List4))
#print ("Size = ",5000, " Heap_time = ", heapTester(List5),"    List_time = ", listTester(List5))
#print ("Size = ",10000, " Heap_time = ", heapTester(List6),"    List_time = ", listTester(List6))
#print ("Size = ",50000, " Heap_time = ", heapTester(List7),"    List_time = ", listTester(List7))

print ( "\
Size =  10  Heap_time =  0.00013492865191690184     List_time =  7.694579879584384e-05\n\
Size =  50  Heap_time =  0.0008719308290089378     List_time =  0.0007384608652208635\n\
Size =  500  Heap_time =  0.014262323179648373     List_time =  0.0377016180498069\n\
Size =  1000  Heap_time =  0.03318041419449419     List_time =  0.11368322399250236\n\
Size =  5000  Heap_time =  0.10107468847891643     List_time =  2.600278974104639\n\
Size =  10000  Heap_time =  0.24180126103588728     List_time =  10.239751439542848\n\
Size =  50000  Heap_time =  1.2322534178886233     List_time =  262.14090489718075\n\
" )


# PQ_Heap O(lg(N))
# PQ_List O(N)

