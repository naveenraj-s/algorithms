from collections import Counter
#initialization #1
test = Counter([1,1,2,3,3,5,0,9,9,7])
#initialization #2
test1 = Counter({1:2,2:2,3:3})
print(test) # Elements are stored as Keys and the no. of occurrences of key stored as Values
print(test.items()) # Get key and values as tuple list
print(test.values()) # Get all the values from the counter dict
print(test.keys()) # Get all the keys from counter dict
print(test.most_common(4)) # Print top 4 elements with more common occurrences
print(test.elements()) # Converts in to iterable object
print(test.update({1:1})) # Updates the number of occurrences in the counter object
print (test)
print (test + test1) # Sum two counters
print(test[11])

# Othere collections
# NamedTupule
# Ordered Dict
# Defaul Dict
# Chain Map
# Deque - Can be add and remove from both the ends
