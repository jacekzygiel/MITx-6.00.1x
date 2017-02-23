'''
@author: zygielj
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels 
contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
'''

def countVowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']    
    return sum(1 for letter in string if letter in vowels)

print('Number of vowels: {}'.format(countVowels(s)))