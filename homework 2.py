#Exercise 1
#Given a list as a parameter,write a function that returns a list of numbers that are less than ten

#For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

def MergeAndSort(l1,l2):
  outputList = l1+l2 
  outputList.sort() 
  return outputList 


def LessThan10(l1):
  outputList = [] 
  for item in l1: 
    if(item<10): 
      outputList.append(item) 
  return outputList 

List1 = [10,9,8]
List2 = [1,2,3]
List3 = [1,11,14,5,8,9]

Output1 = MergeAndSort(List1,List2) 
Output2 = LessThan10(List3) 

print("Merged and Sorted List ",Output1) 
print("Less than 10 in the List ",Output2) 

#Exercise 2
#Write a function that takes in two lists and returns the two lists merged together and sorted
#Hint: You can use the .sort() method

def sort(list1, list2):
    final_list = list1 + list2
    final_list.sort()
    return(final_list)
  

list1 = [25, 18, 9, 41, 26, 31]
list2 = [25, 45, 3, 32, 15, 20]
print(sort(list1, list2))