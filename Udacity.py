# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url', 
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
first = page.find('"',start_link)+1
last = page.find ('"', first)
url = page [first:last]
print url
_________________________________________________________________

# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

x = 3.14159

#ENTER CODE BELOW HERE
a = str(x).find ('.')
b = str(x)[0:a]
c = str(x)[a+1]
d = c.find('5')+1
e = c.find('6')+1
f = c.find('7')+1
g = c.find('8')+1
h = c.find('9')+1
print int(b)+d+ e + f + g + h
_______________
#BEST SOLUTION:
num = x+0.5
s = str(num)
point = s.find ('.')
print s[:point]
_________________________________________________________________

#factorial

def factorial(n):
    result = 1
    while n>=1:
        result = result * n
        n = n - 1
    return result
print factorial(4)
_________________________________________________________________

# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(search, target):
    last_pos = -1
    while True:
        position = search.find(target, last_pos + 1)
        if position == -1:
            return last_pos
        last_pos = position
#print find_last('aaaa', 'a')
#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 3






_____________________________________________________________________

# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(string):
    res = ''
    n = 0
    while n <= len(string) - 1:
        if string[n] == '<':
            end_q = string.find('>')
            string = ' ' + string[end_q + 1:]
            n = 0
        if string[n] != '<':
            res += string[n]
            n += 1
    return res.split()
    
print remove_tags('This is a <a href="http://www.udacity.com">link</a>.<p>')

print remove_tags('''<h1>Title</h1><p>This is a <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                    <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

#print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']
_________________________________________________________________



# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. It can 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement):
    
    return [match, replacement]
        



def apply_converter(converter, string):
    a = None
    while a != string:
        a = string
        pos = string.find(converter[0])
        if pos != -1:
            string = string[:pos] + converter[1] + string[pos + len(converter[0]):]
    return string
    



# For example,

c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
#>>> ab
___________________________________________________________________________________________________________________________________________________________________________________________________

DAYSOld

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#count days in years between dates
        def year_days (year1, year2):
            days_y = 0
            this_year = 0
            while year1 != year2:
                if year1 % 4 == 0 and year1 % 100 != 0:
                    if year1 % 400 != 0:
                                   this_year = 366
                    else:
                         this_year = 365
                else:
                     this_year = 365
                days_y = days_y + this_year
                year1 = year1 + 1
            return days_y
#count days in months (from 1 january to second date - from 1 january to first date)           
        def month_days (month1, month2):
            days_m = 0
            january = 1
            day = 0
            from_1 = 0
            from_2 = 0
            while january < month1:
                if year1 % 4 == 0 and year1 % 100 != 0:
                    if year1 % 400:
                                   day=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                    else:
                         day=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                else:
                     day=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                from_1 = from_1 + day[january - 1]
                january = january + 1
                
            january = 1
            while january < month2:
                if year2 % 4 == 0 and year2 % 100 != 0:
                    if year2 % 400:
                                   day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                    else:
                         day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                else:
                     day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                from_2 = from_2 + day[january - 1]
                january = january + 1
            days_m = from_2 - from_1
            return days_m
# count days                    
        def days_days (day1, day2):
            if day1 == day2:
                            return 0
            else:
                 return day2 - day1
        
        num_of_days = year_days (year1, year2) + month_days (month1, month2) + days_days (day1, day2)
        return num_of_days