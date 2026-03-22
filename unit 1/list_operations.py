my_list = [10, 5, 20, 15, 2]

print("Original List:", my_list)

my_list.append(25)         
my_list.insert(2, 12)       
print("List after adding elements:", my_list)

my_list.remove(5)          
popped_element = my_list.pop()  
print("List after removing elements:", my_list)
print("Popped element:", popped_element)

my_list.sort()              
print("Sorted List:", my_list)

my_list.reverse()
print("Reversed List:", my_list)