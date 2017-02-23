'''
@author: zygielj
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
'''

def countStringOccurrence(string):
    bob = 'bob'
    return sum(1 for x in range(0, len(string)-len(bob)+1) if bob in string[x:x+len(bob)])
   
print('Number of times bob occurs is: {}'.format(countStringOccurrence(s)))