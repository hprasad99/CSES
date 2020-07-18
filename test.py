s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas'] 
  
# using list comprehension 
listToStr = ' '.join([str(elem) for elem in s]) 
  
print(listToStr)