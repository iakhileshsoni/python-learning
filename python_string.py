# [start : end : step]

"""
-8 -7 -6 -5 -4 -3 -2 -1
"R  A  M  M  O  H  A  N"
 0  1  2  3  4  5  6  7
"""

name1 = '  Ram Mohan  '
# print(name1[0:])    # 0, 1, 2, 3, 4 , 5
# print(name1[::-1])  # -1, -2, -3, -4, -5


first_letter = name1[0]
last_letter = name1[-1]
word = first_letter + " " + last_letter
print(word)

# Length of the string 
print(f"Length of the given name, {name1} is : ", len(name1))

# Upper case of the string 
print(f"Upper case of the given name {name1} is :", name1.upper())

# Lower case of the string 
print(f"Lower case of the given name {name1} is :", name1.lower())

# Removing whitespace 
print(f"After removing whitespace the word {name1} is : ", name1.strip())

# replace - string.replace("replace to", "replace with")
name2 = "Ram"
print(name2.replace("Ram", "Mohan"))

# split - string.split("<operator/symbol>")
name3 = "Ram, Mohan"
print(name3.split(","))


name4 = 'Ram Mohan'
result = "".join([name4[0], name4[7], name4[-1]])
print(f"After combining the word {name4} is :", result)



"""
String Introduction
String Indexing
String Slicing
String Methods :
    1. len()
    2. upper()
    3. lower()
    4. strip()
    5. replace()
    6. split()
    7. join()

"""