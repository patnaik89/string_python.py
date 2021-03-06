"How to create set"
"Set operations(union,intersections)"
"(A-B),(B-A),(A+B),(B+A),(A union B),(B union A),(A intersection B),(B intersection A)"
"create tuple"
"create nested tuple"
"create dynamic tuple"


# create set
x = {"apple","banana","cherry"}
print(x)
{'apple','banana','cherry'}   # output set


# A-B
A = {'a','b','c','d'}
B = {'c','f','g'}
print(A.difference(B))
{'d','a','b'}     # output 

#B-A 
print(B.difference(A))
{'f','g'}

# A intersection B
A = {2,3,5,4}
B = {2,5,80}
print(A.intersection(B))
{2, 5}  #output

# B intersection A
print(B.intersection(A))
{2,5}     # ouput

# A union B
A = {'a','c','d'}
B = {'c','d','e'}
print(A.union(B))
{'d', 'a', 'c', 'e'}   # output

# B union A
print(B.union(A))
{'d', 'a', 'c', 'e'}     # output
 
# A+B
A = {"apple","orange","cherry"}
B = {"banana"}
A.add("banana")
print(A)
{'apple', 'orange', 'banana', 'cherry'}   #output

# B+A
A = {"orange"}
B = {"apple","cherry","banana"}
B.add("orange")
print(B)
{'apple', 'banana', 'cherry', 'orange'}      # output

# create tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
('apple', 'banana', 'cherry')       # ouput

# create nested tuple
tuple1 = (0,1,2,3)
tuple2 = ('book','pen')
tuple3 = (tuple1,tuple2)
print(tuple3)
((0, 1, 2, 3), ('book', 'pen'))    # output
