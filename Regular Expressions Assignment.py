#!/usr/bin/env python
# coding: utf-8

# In[74]:


import re
import regex as re


# In[75]:


#Sample Text- 'Python Exercises, PHP exercises.'
#Expected Output: Python:Exercises::PHP:exercises:

sample_text='Python Exercises, PHP exercises.'
pattern=re.sub("\s",":",sample_text)
print(pattern)


# In[83]:


#Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
#Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
#Expected output-
#0      hello world
#1             test
#2    four five six

import pandas as pd
import regex as re

dictionary= {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four five:; six...']}
df= pd.DataFrame(dictionary)
df
pattern = df['SUMMARY'].str.replace(r'[^a-z\s]','',regex=True)
print (pattern)



# In[74]:


#Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

sample_text='abds, ahdd, akdaksj, abcd, skdh, ejrhehe'
pattern=re.compile(r'\b\w{4}\b')
result = re.findall(pattern,sample_text)
print (result)


# In[75]:


#Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

sample_text='The five defining characteristics of a poem include: meter. rhyme. form.'
pattern= re.compile(r'\b\w{3,5}\b')
result = re.findall(pattern,sample_text)
print(result)


# In[76]:


#Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
#Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
#Expected Output:
#example.com
#hr@fliprobo.com
#github.com
#Hello Data Science World

sample_text='"example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"'
pattern= re.compile(r'[()]')
result = re.sub(pattern,"",sample_text)
print(result)


# In[116]:


#Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
#Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
#Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
#Note- Store given sample text in the text file and then to remove the parenthesis area from the text.

import re

filename = r'C:\Users\sheba\OneDrive\Documents\Internship 2024\sample.txt'

def parentheses_area(filename):
    
    with open(filename,'r') as file:
        text = file.read()
        modified_text=re.sub(r'\s*\([^)]*\)','',text)
        return modified_text

new_sample_text = parentheses_area(filename)

print("Parentheses area removed:")
print(new_sample_text)
   


# In[9]:


#Write a regular expression in Python to split a string into uppercase letters.
#Sample text: “ImportanceOfRegularExpressionsInPython”
#Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]

sample_text='ImportanceOfRegularExpressionsInPython'
pattern=re.findall(r'[A-Z][^A-Z]*',sample_text)
print (pattern)


# In[74]:


#Create a function in python to insert spaces between words starting with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
#Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython

import re

def insert_spaces(text):
    pattern = r'([A-Z][a-z0-9]+|\d+)'
    return re.sub(pattern, r' \1', text).strip()

sample_text = "RegularExpressionIsAnImportantTopicInPython"
result = insert_spaces(sample_text)
print(result)


# In[125]:


#Create a function in python to insert spaces between words starting with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
#Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython

import re

def insert_spaces(text):
    
    pattern = r'([A-Z][a-z]*\d+|\d+)'
    #pattern = r'([A-Z][a-z0-9]+|\d+)'
    return re.sub(pattern, r' \1', text).strip()

sample_text = 'RegularExpression1IsAn2ImportantTopic3InPython'
result = insert_spaces(sample_text)
print(result)


# In[117]:


#Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
#Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv

import pandas as pd

url='https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv'
df=pd.read_csv(url)
df['first_five_letters']=df['Country'].str[:5]
print(df.head())


# In[41]:


#Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re

def check_string(string):
    
    pattern=re.compile(r'^[a-zA-Z0-9_]+$')
    return bool(pattern.match(string))

sample_text=input("Enter String: ")

if check_string(sample_text):
    print("Match found")
else:
    print("Match not found")    


# In[46]:


#Write a Python program where a string will start with a specific number. 

import re

def check_starts_w_number(s,number):
    
    pattern=re.compile(r'^'+str(number)+'.*$')
    return bool(pattern.match(s))

sample_text=input("Enter string with a number:")
num=int(input("Enter Number:"))

if check_starts_w_number(sample_text,num):
    print("The string starts with a specific number")
else:
    print("The string does not start with a specific number")


# In[48]:


#Write a Python program to remove leading zeros from an IP address

import re

ip_address= input("Enter IP address: ")
pattern=re.sub('\.[0]','.',ip_address)
print("Removed leading zeros:",pattern)


# In[101]:


#Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
#Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
#Expected Output- August 15th 1947
#Note- Store given sample text in the text file and then extract the date string asked format.

import re

filename= r'C:\Users\sheba\OneDrive\Documents\Internship 2024\sample_text.txt'

with open(filename,'r') as file:
    text=file.read()
    
pattern=r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)\s+\d{4}\b'  
result=re.findall(pattern,text)

print (f"Extracted Date:", result)


# In[107]:


sample_text='"The quick brown fox jumps over the lazy dog."'
searched_words=['fox','dog','horse']

def search_literal_strings(text):
    
    for pattern in searched_words:
        
        if re.search(pattern,text):
            print(f'"{pattern}"in text')
        else:
            print(f'"{pattern}" not found in text')

sample_text = 'The quick brown fox jumps over the lazy dog.'
search_literal_strings(sample_text)          


# In[111]:


#Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox'

sample_text='The quick brown fox jumps over the lazy dog.'
searched_word='fox'

def find_literal_strings(text,pattern):
    
    match = re.search(pattern,text)
    if match:
        s = match.start()
        e = match.end()
        print(f'Found "{pattern}" from {s} to {e}')
    else:
            print(f'"{pattern}" not found in text')

sample_text = 'The quick brown fox jumps over the lazy dog.'
find_literal_strings(sample_text,searched_word)  


# In[51]:


#Write a Python program to find the substrings within a string.
#Sample text : 'Python exercises, PHP exercises, C# exercises'
#Pattern : 'exercises'.

sample_text='Python exercises, PHP exercises, C# exercises'
pattern='exercises'
result=re.findall(pattern,sample_text)
print(result)


# In[64]:


#Write a Python program to find the occurrence and position of the substrings within a string.

import re

def find_substring_positions(text, substring):
    
    positions = []
        
    for match in re.finditer(substring, text):
        positions.append(match.start())
    
    return positions

sample_text = "Python exercises, PHP exercises, C# exercises"
search_substring = "exercises"

substring_positions = find_substring_positions(sample_text, search_substring)

print(f"The substring '{search_substring}' occurs at positions: {substring_positions}")


# In[80]:


#Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy formaimport datetime

from datetime import datetime

old_format='2024-04-24'
print("Old Format: ",old_format)

datetime_obj = datetime.strptime(old_format,"%Y-%m-%d")
new_format = datetime_obj.strftime("%d-%m-%Y")
print("New Format:",new_format)


# In[16]:


#Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
#Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
#Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']

sample_text='01.12 0132.123 2.31875 145.8 3.01 27.25 0.25'
pattern=re.compile(r'\b\d+\.\d{1,2}\b')
decimal_numbers=re.findall(pattern,sample_text)
print (decimal_numbers)


# In[86]:


#Write a Python program to separate and print the numbers and their position of a given string.

sample_text='There are 100 cows on this farm'

for m in re.finditer("\d+",sample_text):
    print(m.group(0))
    print("Index Postion:",m.start())


# In[88]:


#Write a regular expression in python program to extract maximum/largest numeric value from a string.
#Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
#Expected Output: 950

sample_text='My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
num_values=re.findall(r'\d+',sample_text)
max_number=max(map(int,num_values))
print(max_number)


# In[71]:


#Create a function in python to insert spaces between words starting with capital letters.
#Sample Text: “RegularExpressionIsAnImportantTopicInPython"
#Expected Output: Regular Expression Is An Important Topic In Python

def insert_spaces(text):
    pattern = re.sub(r'([A-Z])',r'\1', text).strip()
    return result
    
sample_text='RegularExpressionIsAnImportantTopicInPython'
output=insert_spaces(sample_text)
print(output) 


# In[99]:


#Python regex to find sequences of one upper case letter followed by lower case letters
sample_text=input("Enter text:")
pattern=re.findall(r'[A-Z][a-z]+',sample_text)
print(pattern)


# In[24]:


#Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
#Sample Text: "Hello hello world world"
#Expected Output: Hello hello world

def remove_duplicate(text):
    new_sentence=re.sub(r'\b(\w+)(\s+\1)+\b',r'\1',text)
    return new_sentence

sample_text='Hello hello world world'
result=remove_duplicate(sample_text)
print (result)


# In[34]:


#Write a python program using RegEx to accept string ending with alphanumeric character.

import re

def check_string(string):
    pattern= re.compile(r'^.*[a-zA-Z0-9]$')
  
    if pattern.match(string):
        return True
    else:
        return False
    
sample_text=input("Enter Words:")

if check_string(sample_text):    
        print("Ends with alphanumeric character")    
else:
        print("Does not end with alphanumeric character")


# In[5]:


#Write a python program using RegEx to extract the hashtags.
#Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
#Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']

sample_text='"""RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""'
pattern=r'#\w+'
result=re.findall(pattern,sample_text)
print(result)


# In[6]:


#Write a python program using RegEx to remove <U+..> like symbols
#Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
#Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
#Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders

sample_text='"@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"'
pattern=r'<U\+[0-9A-Fa-f]+>'
result=re.sub(pattern,'',sample_text)
print(result)


# In[121]:


#Write a python program to extract dates from the text stored in the text file.
#Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
#Note- Store this sample text in the file and then extract dates.

filename = r'C:\Users\sheba\OneDrive\Documents\Internship 2024\extract_date.txt'

def extract_dates (filename):
    with open(filename,'r') as file:
        text = file.read()
        pattern = r'\b(\d{2}-\d{2}-\d{4})\b'
        dates = re.findall(pattern,text)
        return dates

print (extract_dates(filename))
    


# In[8]:


#Create a function in python to remove all words from a string of length between 2 and 4.
#The use of the re.compile() method is mandatory.
#Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.

def remove_words(text):
    
    pattern=re.compile(r'\b\w{2,4}\b')
    new_string=re.sub(pattern,'',text)
    return new_string

sample_text='The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly.'
result=remove_words(sample_text)
print(result)


# In[ ]:




