student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score":[56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

import pandas

student_dataFrame = pandas.DataFrame(student_dict)
print(student_dataFrame)

#Looping through a data frame
# for (key, value) in student_dataFrame.items():
#     print(value)

#pandas has an inbuilt loop, called iterrows
#Loop through rows of a data frame
for (index, row) in student_dataFrame.iterrows():
    print(row)
    #print(row.student)
    #if row.student == "Angela":
        print(row.score)

