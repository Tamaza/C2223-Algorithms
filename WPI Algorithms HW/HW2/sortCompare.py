######################################################################################
#
#
#  Name:Irakli Grigolia
#  Date:25.03.18
#
#  This project compares quicksort, mergesort and bubblesort.  The steps
#  are as follows:
#    1) write/test the partition routine for quicksort. (20 points)  The rest of the code is given.
#    2) write/test the merging part of the mergesort. (20 points) The rest of the code is given.
#    3) write/test bubblesort. (10 points) No code is given.
#    4) In your main program, compare the sorts using stored lists of 10 and 50 items (in-order, reverse order
#       and random.  Name the lists order10.txt, reverse10.txt, random10.txt
#       order50.txt, reverse50.txt and random50.txt.  Be sure
#       to print out the initial and sorted arrays so we can see that your module
#       sorted properly. (10 points)
#    5) In your report, create a table 1 that shows the times in seconds of the
#       lists (rows) and sorts (columns). (10 points)
#    6) In your report, create a table 2 that shows the order of growth in Big O
#       notation for time and space of Quicksort, Mergesort and Bubblesort (Best case,
#       worst case and average case) (5 points)
#    6) write/test a variation on quicksort (it must be named as vqS) that makes the following
#       improvements:
#         chooses pivot by taking a small sample size (3 items) and using
#         median for pivot. (10 points)
#    7) write/test a variation on mergesort (it must be named as vmS) that makes the following
#        improvement:
#         Use insertion sort for small arrays (10 items or less). (10 points)
#    8) run your new modules on your stored lists and add your findings to a
#       table 3 in your report.  (10 points)
#   
#
####################################################################################
import time
import random

#print ("Read in  3 types of lists of 10 and 50 items")
#print ("One list should be in order, one list in reverse order and one random.")

def qS(items):
   
   qSHelp(items,0,len(items)-1)

def qSHelp(items,first,last):
   if first<last:

       pivot = partition(items,first,last)

       qSHelp(items,first,pivot-1)
       qSHelp(items,pivot+1,last)


def partition(items,first,last):
   pivotvalue = items[first]

   lSide = first+1
   rSide = last

   finished=False

   while not finished:

      while lSide <= rSide and items[lSide] <= pivotvalue:
           lSide = lSide+ 1

      while items[rSide] >= pivotvalue and rSide >= lSide:
           rSide= rSide -1

      if rSide < lSide:
           finished = True
      else:
           sub= items[lSide]
           items[lSide] = items[rSide]
           items[rSide] = sub

   sub = items[first]
   items[first] = items[rSide]
   items[rSide] = sub
   

   return rSide
   
   


def mS(items):
    
    
       if len(items)>1:
           mid = len(items)//2
           lefthalf = items[:mid]
           righthalf = items[mid:]

           mS(lefthalf)
           mS(righthalf)
        
           i=0
           j=0
           k=0
           while i < len(lefthalf) and j < len(righthalf):
               if lefthalf[i] < righthalf[j]:
                   items[k]=lefthalf[i]
                   i=i+1
               else:
                   items[k]=righthalf[j]
                   j=j+1
               k=k+1

           while i < len(lefthalf):
               items[k]=lefthalf[i]
               i=i+1
               k=k+1

           while j < len(righthalf):
               items[k]=righthalf[j]
               j=j+1
               k=k+1
            

            

    
def bS(items):
  
  for i in range( len( items ) ):
    for k in range( len( items ) - 1, i, -1 ):
      if ( items[k] < items[k - 1] ):
        swap( items, k, k - 1 )
        
 
def swap( items, x, y ):
  tmp = items[x]
  items[x] = items[y]
  items[y] = tmp
  



def swap1(array,a,b):
    array[a],array[b] = array[b],array[a]
    
def partition1(array,start,end):
    median = (end - 1 - start) // 2
    median = median + start
    left = start + 1
    if (array[median] - array[end-1])*(array[start]-array[median]) >= 0:
        swap1(array,start,median)
    elif (array[end - 1] - array[median]) * (array[start] - array[end - 1]) >=0:
         swap1(array,start,end - 1)
    pivot = array[start]
    for right in range(start,end):
        if pivot > array[right]:
            swap1(array,left,right)
            left = left + 1
    swap1(array,start,left-1)
    return left-1
def quickSortHelper(array,start,end):
    if start < end:
        splitPoint = partition1(array,start,end)
        quickSortHelper(array,start,splitPoint)
        quickSortHelper(array,splitPoint+1,end)
def vqS(array):
    quickSortHelper(array,0,len(array))

            
def iS(array):
    for i in range(1,len(array)):

     currentvalue = array[i]
     position = i

     while position>0 and array[position-1]>currentvalue:
         array[position]=array[position-1]
         position = position-1

     array[position]=currentvalue

def vmS(items):
   if (len(items)<=10):
      iS(items)
   else:
      if len(items)>1:
           mid = len(items)//2
           lefthalf = items[:mid]
           righthalf = items[mid:]

           vmS(lefthalf)
           vmS(righthalf)
        
           i=0
           j=0
           k=0
           while i < len(lefthalf) and j < len(righthalf):
               if lefthalf[i] < righthalf[j]:
                   items[k]=lefthalf[i]
                   i=i+1
               else:
                   items[k]=righthalf[j]
                   j=j+1
               k=k+1

           while i < len(lefthalf):
               items[k]=lefthalf[i]
               i=i+1
               k=k+1

           while j < len(righthalf):
               items[k]=righthalf[j]
               j=j+1
               k=k+1

