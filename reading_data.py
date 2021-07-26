"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""

data = []

file_name = input('Provide a name of a file of data: ')

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            add_it = new[:-1].split(',') # remove trailing \n
            data.append(add_it)
finally:
    fh.close() # close file even if fail

grades_data =  []
if data:
    for student in data:
        try:
            name = student[0:-1]
            grades = int(student[-1])
            grades_data.append([name, [grades]])
        except ValueError:
            grades_data.append([student[:], []])
