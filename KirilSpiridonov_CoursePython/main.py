lst = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

lst.pop()
print(lst) 
print(len(lst))
print(sum(lst))
print(max(lst))
print(min(lst))
print(lst.index(5))
print(lst.count(5))
lst.remove(3)
print(lst)
lst.clear()
print(lst)
print(sorted(lst)[: :-1])


fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "apple", True, 3.14]

print(fruits)
print(numbers)
print(mixed_list)

print(fruits[0])     
print(fruits[1])    
print(fruits[2])

#Slicing:

print(numbers[1:4])   
print(numbers[:3])    
print(numbers[2:])

#Lists are mutable:  
fruits[1] = "grape"
print(fruits)


#Adding elements:      

#Append: To add an element to the end of the list, we use the append() method.
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print(fruits)  


#Insert: To insert an element at a specific position, we use the insert() method.
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 10)
print(numbers)        

#Removing elements:      

#Remove: To remove the first occurrence of an element, we use the remove() method.
fruits = ["apple", "banana", "orange", "banana"]
fruits.remove("banana")
print(fruits)        

#Pop: To remove an element at a specific index and return its value, we use the pop() method.
numbers = [1, 2, 3, 4, 5]
popped = numbers.pop(3)
print(numbers)        
print(popped)        

#Del: To remove an element at a specific index, we can use the del statement.
fruits = ["apple", "banana", "orange"]
del fruits[1]
print(fruits)         

#Finding elements:

#Index: To find the index of the first occurrence of an element, we use the index() method.

fruits = ["apple", "banana", "orange"]
index = fruits.index("banana")
print(index)       

#Count: To count the number of occurrences of an element, we use the count() method.
fruits = ["apple", "banana", "orange", "banana"]
count = fruits.count("banana")
print(count)        

#Sorting and reversing:    
  
#Sort: To sort the list in ascending order, we use the sort() method.
numbers = [5, 2, 4, 1, 3]
numbers.sort()
print(numbers)       

#Reverse: To reverse the order of elements in the list, we use the reverse() method.
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)      

