######################################################################################
#     This is your main program that tests the classes you have written.
#     name: Irakli Grigolia
# 
#
####################################################################################
import time
import random
from sortCompare import qS,mS,bS,vqS,vmS


items = [55,27,90,18,78,30,44,56,21,67]
print("before quick sorting",items)
start_time_quickSort = time.clock()
qS(items)
end_time_quickSort = time.clock()
print("Quick Sort CPU time (seconds): "  +str(end_time_quickSort - start_time_quickSort))
print("after  quick sorting:",items)

items = [55,27,90,18,78,30,44,56,21,67]
print("before merge sorting",items)
start_time_mSort = time.clock()
mS(items)
end_time_mSort = time.clock()
print("Merge Sort CPU time (seconds): "  +str(end_time_mSort - start_time_mSort))
print("after  merge sorting",items)


items = [55,27,90,18,78,30,44,56,21,67]
print("before bubble  sorting",items)
start_time_bSort = time.clock()
bS(items)
end_time_bSort = time.clock()
print("Bubble Sort CPU time (seconds): "  +str(end_time_bSort - start_time_bSort))
print("after  bubble sorting",items)

items = [55,27,90,18,78,30,44,56,21,67]
print("before vqS :",items)
start_time_vqSort=time.clock()
vqS(items)
end_time_vqSort=time.clock()
print("vqS CPU time (seconds): "  +str(end_time_vqSort - start_time_vqSort))
print("after  vqS",items)


list=[] 
def ConverttoList(name):
    with open(name, 'r') as handle:
        for line in handle:
            values = line.strip().split(',')

    
    for i in range(len(values)):
        list.append(int(values[i]))       
    
    return list

list1=ConverttoList("order10.txt")
time1=time.clock()
vmS(list1)
duration1=(time.clock()-time1)
print("duration is:",duration1)








