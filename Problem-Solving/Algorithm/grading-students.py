#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade >= 38:
            next_mul = ((grade // 5) + 1) * 5
            if next_mul - grade < 3:
                rounded_grades.append(next_mul)
            else:
                rounded_grades.append(grade)
        else:
            rounded_grades.append(grade)
    return rounded_grades


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)