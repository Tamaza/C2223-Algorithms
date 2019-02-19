HW2.ReadMe by Irakli Grigolia

In this program I implement 4 different kinds of sorts(quick sort,merge sort,bubble sort, and insertion sort).Insertion sort is just a helper fucntion.
We implement quick sort with 2 different methods:simple partion and three way partion.
Also we use insertion sort only with merge sort and only when the size of the list is less or equal to 10.

To read list from a file I have a function called "ConverttoList(name)". So if we want to read a list from a file as a list we have to do the following
list=ConverttoList("name")-> and "name" is the name of the text file.We have to use name "list" because that is the name of the list where my fucntion stores the list after it reads it
from the textfile.

I have two "swap(items, x, y)" functions to help to swap elemets easily,"partion1(array,start,end)" and "quicksorthelper(array,start,end)"  as helper functions for vqS.

Also for vmS I implemented insertion sort called iS(array),I check for the length of the intial array if its is less or equal to 10 it calls "iS(array)" function  for an array given, 
otherwise ,it uses merge sort and after every division it calls vmS on left and right parts of the array which was divided in two, and so on until it finds list size of 10.

In order to run this program just open the Proj2_main.py file and press f5,ofcourse you need to have seperate .py file with all the functions.
