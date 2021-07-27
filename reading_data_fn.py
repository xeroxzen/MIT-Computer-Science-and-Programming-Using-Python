# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:02:39 2021

@author: Andile Mbele
"""

def read_data(data):
    """

    >>> read_data([])
    Please input a filename to read from: grades_data.pdf
    >>> data
    [['Eric', 'Khumalo', '80'],
     ['Phumzile', 'Moyo', '100'],
     ['Nandipa', 'Siluma', '90'],
     ['Proud', 'Mpala', '70'],
     ['Anesu', 'Mapuranga', '75'],
     ['Arnold', 'Bhebhe'],
     ['Minolta', '80'],
     ['Andile', 'Jaden', 'Mbele', '75']]
    >>> grades_data
    [[['Eric', 'Khumalo'], [80]],
     [['Phumzile', 'Moyo'], [100]],
     [['Nandipa', 'Siluma'], [90]],
     [['Proud', 'Mpala'], [70]],
     [['Anesu', 'Mapuranga'], [75]],
     [['Arnold', 'Bhebhe'], []],
     [['Minolta'], [80]],
     [['Andile', 'Jaden', 'Mbele'], [75]]]
    >>> grades_data[-1]
    [['Andile', 'Jaden', 'Mbele'], [75]]
    >>> grades_data[6][0]
    ['Minolta']

    """
    file_name = input('Please input a filename to read from: ')

    try:
        fh = open(file_name, 'r')
    except IOError:
        print('cannot open', file_name)
        # we can include other assertions we may find relevant
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
