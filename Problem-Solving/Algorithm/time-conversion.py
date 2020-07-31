#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour, minute, second = s.split(":")
    second = second[:2]
    if (s.find("PM") != -1) and (int(hour) < 12):
        hour = int(hour) + 12
        hour = str(hour)
    else:
        if (s.find("AM") != -1) and int(hour) == 12:
            hour = "00"
    return (hour +":"+ minute +":"+ second)

if __name__ == '__main__':

    s = input()
    result = timeConversion(s)

    print(result)
 