'''
@author: zygielj
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s
in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print:
Longest substring in alphabetical order is: abc
'''
def longestSubstrincInAlphaOrder(string):
    options = []    
    for x in range(0, len(string)):
        for y in range(1, len(string)+1):
            if list(string[x:y]) == sorted(string[x:y]) and (len(string[x:y]) > 0): 
                options.append(string[x:y]) 
    return max(options, key=len)     

print('Longest substring in alphabetical order is: {}'.format(longestSubstrincInAlphaOrder(s)))