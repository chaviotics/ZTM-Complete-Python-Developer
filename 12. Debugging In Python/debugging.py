# debugging

# linting
# detect issues/errors of our code

# install pylint

# use ide / editor with packages 
# use auto formatting / pep 8
# use colors

# read errors

# 4 + 'gdf'

# get to know errors like TypeError, Syntax Error

# If you see an error that you've never seen before, you try to read it in the documentation

import pdb

def add(num1, num2):
    # print(num1, num2)
    pdb.set_trace()
    return num1 + num2

print(add(4, 'hi'))