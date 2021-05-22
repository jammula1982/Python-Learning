
## Defined a List
courses = ['Art','Engineering','Business Studides','Medical','Accountancy']

## Iterating througn the list and printing
for c in courses:
    print(c)

## Printing items from index 0 through 3, ** index 4 is not included.
# print(courses[0:4]) 

print(courses[:])

## Apending item and printing using APPEND function

courses.append('Data Analysis')
print(courses)

## Inserting an element to the list at 0th index
courses.insert(0,'Technology')
print(courses)

courses_engg = ['Computer','Information Technology', 'Electronics','Mechanical']

courses.append(courses_engg)
print(courses)
print(courses[-1])

## Popping the last element
courses.pop(-1)

courses.extend(courses_engg)
print(courses)
print(courses[-1])

#Reverse

courses.reverse()
print(courses)






