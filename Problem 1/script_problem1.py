#Say "Hello, World!" With Python
print ("Hello, World!")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

#Print Function
if __name__ == '__main__':
    n = int(input())
if n > 0:
    for i in range(1, n + 1):
        print(i, end="")

#Loops
if __name__ == '__main__':
    n = int(input())
    if n >= 0:
      for i in range(n):
        print(i ** 2)

#Write a Function
def is_leap(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

#Python If-Else
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n % 2 == 1: 
    print("Weird")
else:
    if 2 <= n <= 5:  
        print("Not Weird")
    elif 6 <= n <= 20:  
        print("Weird")
    else:  
        print("Not Weird")

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
print(coordinates)

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    voti_unici = list(set(arr))
    voti_unici.sort(reverse=True)
    if len(voti_unici) >= 2:
        sec_voto = voti_unici[1] 
        print(sec_voto)

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average_mark = sum(student_marks.get(query_name, [])) / len(student_marks.get(query_name, []))
    print(f"{average_mark:.2f}")

#Lists
if __name__ == '__main__':
    N = int(input())
    my_list = []

for _ in range(N):
    command = input().split()
    action = command[0]

    if action == "insert":
        i = int(command[1])
        e = int(command[2])
        my_list.insert(i, e)
    elif action == "print":
        print(my_list)
    elif action == "remove":
        e = int(command[1])
        my_list.remove(e)
    elif action == "append":
        e = int(command[1])
        my_list.append(e)
    elif action == "sort":
        my_list.sort()
    elif action == "pop":
        my_list.pop()
    elif action == "reverse":
        my_list.reverse()

#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)

result = hash(t)
print(result)

#Nested List
if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    
    lowest_grade = min(students, key=lambda x: x[1])[1]

    
    students = [student for student in students if student[1] != lowest_grade]

    
    second_lowest = min(students, key=lambda x: x[1])[1]

    
    second_lowest_students = sorted([student[0] for student in students if student[1] == second_lowest])

    for student in second_lowest_students:
        print(student)

#sWAP cASE
def swap_case(s):
    return s.swapcase()

#String Split and Join
def split_and_join(line):
    # write your code here
    words = line.split(" ")
    hyphen_joined = "-".join(words)
    return hyphen_joined
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#Mutations
def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    modified_string = ''.join(string_list)
    return modified_string

#Find a string
def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)
    for i in range(len(string) - sub_len + 1):
        substring_in_string = string[i:i + sub_len]
        if substring_in_string == sub_string:
            count += 1
    
    return count

#String Validators
if __name__ == '__main__':
    s = input()
    has_alphanumeric = any(c.isalnum() for c in s)
    has_alpha = any(c.isalpha() for c in s)
    has_digit = any(c.isdigit() for c in s)
    has_lower = any(c.islower() for c in s)
    has_upper = any(c.isupper() for c in s)

    print(has_alphanumeric)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)

#Text Wrap

def wrap(string, max_width):
    wrapped_text = textwrap.wrap(string, width=max_width)
    return "\n".join(wrapped_text)

#Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
def create_door_mat(N, M):
    pattern = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
    welcome = 'WELCOME'.center(M, '-')
    return '\n'.join(pattern + [welcome] + pattern[::-1])

if __name__ == '__main__':
    N, M = map(int, input().split())
    door_mat = create_door_mat(N, M)
    print(door_mat)

#String Formatting

def print_formatted(number):
    # your code goes here
    width = len(bin(number)) - 2  
    for i in range(1, number + 1):
        decimal = i
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

#What's Your Name?
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print("Hello {} {}! You just delved into python.".format(first, last))

#Text Alignment
# Enter your code here. Read input from STDIN. Print output to STDOUT
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Alphabet Rangoli

a = "abcdefghijklmnopqrstuvwxyz"
def print_rangoli(size):
    
    lines = []
    for row in range(size):
        print_ = "-".join(a[row:size])
        lines.append(print_[::-1] + print_[1:])
    width = len(lines[0])
    
    for row in range(size-1, 0, -1):
        print(lines[row].center(width, '-'))
        
    for row in range(size):
        print(lines[row].center(width, '-'))


#Capitalize!
# Complete the solve function below.
def solve(s):
    ans = s.split(' ')
    ans1 = (((i.capitalize() for i in ans)))
    return ' '.join(ans1)

#The minion game
def minion_game(string):
    # your code goes here
    s=len(string)
    vowel = 0
    consonant = 0
     
    for i in range(s):
        if string[i] in 'AEIOU':
           vowel+=(s-i)
        else:
           consonant+=(s-i)
                
    if vowel < consonant:
        print('Stuart ' + str(consonant))
    elif vowel > consonant:
        print('Kevin ' + str(vowel))
    else:
        print('Draw')

#Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    l = len(string)//k
    for i in range(l):
        print(''.join(dict.fromkeys(string[i*k:(i*k)+k])))

#Introduction to Sets
def average(array):
    # your code goes here
    s = set(array)
    return sum(s)/len(s)

#Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
set1 = set(list(map(int, input().split())))
n = int(input())
set2 = set(list(map(int, input().split())))
#print (set1)
#print (set2)

n1 = set1.difference(set2)
n2 = set2.difference(set1)
L = [str(x) for x in n1] + [str(x) for x in n2]
L.sort(key = int)
#print (L)
print ('\n'.join(L))

#No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
sc_ar = input().split()

A = set(input().split())
B = set(input().split())

print (sum([(i in A) - (i in B) for i in sc_ar]))

#Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
num  = int(input())
country = set([])
for i in range(num):
    country.add(input())
print(len(list(country)))

#Set .union() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english_subscribers = set(map(int, input().split()))

m = int(input())
french_subscribers = set(map(int, input().split()))

total_subscribers = len(english_subscribers.union(french_subscribers))

print(total_subscribers)

#Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
inglesi = set(map(int, input().split()))

m = int(input())
francesi = set(map(int, input().split()))

tutti = len(inglesi.intersection(francesi))

print(tutti)

#Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
inglesi = set(map(int, input().split()))

m = int(input())
francesi = set(map(int, input().split()))

solo_inglesi = len(inglesi.difference(francesi))

print(solo_inglesi)

#Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
inglesi = set(map(int, input().split()))

m = int(input())
francesi = set(map(int, input().split()))

inglesi_o_francesi = len(inglesi.symmetric_difference(francesi))

print(inglesi_o_francesi)

#Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
SET_A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operazione = input().split()
    set_nuovo = set(map(int, input().split()))
    eval('SET_A.{}({})'.format(operazione[0], set_nuovo))

print(sum(SET_A))

#The Captain's Room
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = input() 

room_ls = input().split()

from collections import Counter
room_counts = Counter(room_ls)

captain_room = room_counts.most_common()[-1][0]
print(captain_room)

#Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    a = int(input())
    set_a = set(map(int, input().split()))

    b = int(input())
    set_b = set(map(int, input().split()))

    if len(set_a - set_b) == 0:
        print("True")
    else:
        print("False")

#Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split())
conta = 0
valore = 0

for i in range(int(input())):
    if a.issuperset(set(input().split())):
        conta += 1
    else:
        valore += 1
if valore != 0:
    print('False')
else:
    print('True')

#Set .discard(), .remove() & .pop()

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))
occurrences = {}

for num in s:
    if num in occurrences:
        occurrences[num] += 1
    else:
        occurrences[num] = 1

for _ in range(int(input())):
    s1 = input().split()
    command = s1[0]

    if command == 'pop':
        if occurrences:
            key = next(iter(occurrences))
            occurrences[key] -= 1
            if occurrences[key] == 0:
                del occurrences[key]
    else:
        element = int(s1[1])
        if element in occurrences:
            if command == 'remove':
                del occurrences[element]
            elif command == 'discard':
                occurrences[element] -= 1
                if occurrences[element] == 0:
                    del occurrences[element]

#collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

scarpe = int(input())
taglie = collections.Counter(map(int, input().split()))

guadagno = 0

for _ in range(int(input())):
    size, price = map(int, input().split())
    if taglie[size]:
        guadagno += price
        taglie[size] -= 1

print(guadagno)

#DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for i in range(1, n + 1):
    d[input()].append(str(i))
for i in range(m):
    print(' '.join(d[input()]) or -1)

#Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N, studenti = int(input()), namedtuple('Student', input())

print("{:.2f}".format(sum([int(studenti(*input().split()).MARKS) for _ in range(N)]) / N))

#Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

a = OrderedDict()

N = int(input())

for i in range(N):
    inp = input()

    if type(inp) != int:
        isplit = inp.split()
        cost = isplit[-1]
        item = isplit[:-1]
        item = " ".join(item)
        cost = "".join(cost)
        cost = int(cost)

        if item in a:
            current = a[item]
            current += cost
            a[item] = current
        else:
            a[item] = cost


for key, value in a.items():
    print(key, value)

#Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
lista = []

for i in range(n):
    lista.append(input().strip())

conta = Counter(lista)

print(len(conta))
print(*conta.values())

#Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()

for _ in range(int(input())):
    oper, val, *args = input().split() + ['']
    eval(f'd.{oper} ({val})')

print(*d)

#Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
ris = []
T = int(input())

for _ in range(T):
    n = int(input())
    sl = list(map(int, input().split()))

    for _ in range(n-1):
        if sl[0] >= sl[len(sl)-1]:
            a = sl[0]
            sl.pop(0)
        elif sl[0] < sl[len(sl)-1]:
            a = sl[len(sl)-1]
            sl.pop(len(sl)-1)
        else:
            pass

        if len(sl) == 1:
            ris.append("Yes")

        if((sl[0] > a) or (sl[len(sl)-1] > a)):
            ris.append("No")
            break

print("\n".join(ris))

#Company Logo
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    conta_lett = {}
    for lett in s:
        if lett.isalpha():  
            conta_lett[lett] = conta_lett.get(lett, 0) + 1
    
    sorted_lett = sorted(conta_lett.keys(), key=lambda lett: (-conta_lett[lett], lett))
    
    for lett in sorted_lett[:3]:
        print(lett, conta_lett[lett])

#Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

mese, giorno, anno = map(int, input().split())

print(calendar.day_name[calendar.weekday(anno, mese, giorno)].upper())

#Time delta
import math
import os
import random
import re
import sys
from datetime import datetime

format = '%a %d %b %Y %H:%M:%S %z'

for _ in range(int(input())):
    time1 = datetime.strptime(input(), format)
    time2 = datetime.strptime(input(), format)

    print(int(abs((time1 - time2).total_seconds())))

#Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except ZeroDivisionError as z:
        print(f'Error Code: {z}')
    except ValueError as v:
        print(f'Error Code: {v}')

#Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = input().split()

io = list()

for _ in range(int(X)):
    ip = map(float, input().split())
    io.append(ip)

for i in zip(*io): 
    print( sum(i)/len(i) ) 

#Athlete sort
import math
import os
import random
import re
import sys



if __name__ == "__main__":
    
    n, m = input().strip().split(' ')
    
    n, m = [int(n), int(m)]
    arr = []
    
    for arr_i in range(n):
         
       arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
       arr.append(arr_t)
    
    k = int(input().strip())
    
    sorted_arr = sorted(arr, key = lambda x : x[k])
    
    for row in sorted_arr:
        print(' '.join(str(y) for y in row))

#ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT
def sort_String(s):
    minus = []
    maius = []
    disp = []
    pari = []
    for lett in s:
        if lett.islower():
            minus.append(lett)
        elif lett.isupper():
            maius.append(lett)
        elif lett.isdigit():
            if int(lett)%2==0:
                pari.append(lett)
            else:
                disp.append(lett)
    return (''.join(sorted(minus)+sorted(maius)+sorted(disp)+sorted(pari)))
    
if __name__=='__main__':
    
    S = input()
    print (sort_String(S))

#Map and Lambda Function
cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib_list = []
    
    if n >= 1:
        fib_list.append(0)
    if n >= 2:
        fib_list.append(1)

    for i in range(2, n):
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
    
    return fib_list   

#Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

class main():
    def __init__(self):
        self.n = int(input())
        
        for i in range(self.n):
            self.s = input()
            print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', self.s)))
            
            
if __name__ == '__main__':
    ogg = main()

#Re.split()
regex_pattern = r"[\,\.]"    # Do not delete 'r'.

#Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

class main():
    def __init__(self):
        self.s = input()
        self.li = re.search(r'([a-zA-Z0-9])\1+', self.s)
        
    def output(self):
        print(self.li.group(1) if self.li else -1)
        

if __name__ == '__main__':
    ogg = main()
    ogg.output()

#Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

class main():
    def __init__(self):
        self.s = input()
        self.c = 'qwrtypsdfghjklzxcvbnm'
        
    def output(self):
        self.ss = re.findall(r'(?<=[' + self.c + '])([aeiou]{2,})(?=[' + self.c +'])', self.s, flags = re.I)
        print('\n'.join(self.ss or ['-1']))
        
if __name__ == '__main__':
    ogg = main()
    ogg.output()

#Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

class main:
    def __init__(self):
        self.s = input()
        self.k = input()
        
    def output(self):
        pattern = re.compile(r'(?=('+self.k+'))')
        matches = list(pattern.finditer(self.s))
        if matches:
            for match in matches:
                start = match.start(1)
                end = match.end(1) - 1
                print('({}, {})'.format(start, end))
        else:
            print('(-1, -1)')

if __name__ == '__main__':
    ogg = main()
    ogg.output()

#Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

class main:
    def __init__(self):
        self.n = int(input())
        
        for _ in range(self.n):
            self.s = input()
            print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', self.s))
            
            
if __name__ == '__main__':
    ogg = main()

#Validating Roman Numerals
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XL|XC|L?X{0,3})(IX|IV|V?I{0,3}$)"	
# Do not delete 'r'.

#Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

class main():
    def __init__(self):
        self.n = int(input())
        
        for i in range(self.n):
            self.s = input()
            print('YES' if re.match(r'[789]\d{9}$', self.s) else 'NO')
            
            
if __name__ == '__main__':
    ogg = main()

#Validating and Parsing Email Addresses
# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils as em
import re

class main():
    def __init__(self):
        self.n = int(input())
        
        for i in range(self.n):
            self.s = em.parseaddr(input())
            
            if re.match(r'^[a-zA-Z](\w|-|\.|_)+@[a-zA-Z]+\.[a-zA-Z]{0,3}$', self.s[1]):
                print(em.formataddr(self.s))
        
if __name__ == '__main__':
    ogg = main()

#Hex Color Code

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

class main:
    def __init__(self):
        self.n = int(input())
        
        for _ in range(self.n):
            self.s = input()
            self.matchs = re.findall(':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', self.s)
            if self.matchs:
                print(*self.matchs, sep='\n')
            
if __name__ == '__main__':
    ogg = main()

#HTML Parser - Part 1
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):     
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for li in attrs:
            print('->', li[0], '>', li[1])
            
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for li in attrs:
            print('->', li[0], '>', li[1])
        

if __name__ == '__main__':
    n = int(input())
    s = ''
    for i in range(n):
        temp = input()
        s += temp   
    ogg = MyHTMLParser()
    ogg.feed(s)

#HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)
    def handle_data(self, data):
        if data == '\n':
            return
        print(">>> Data")
        print(data)
  
  
if __name__ == '__main__':
    html = ""       
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'

    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()

#Detect HTML Tags, Attributes and Attribute Values
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for li in attrs:
            print('->', li[0], '>', li[1])


if __name__ == '__main__':
    n = int(input())
    s = ''
    for _ in range(n):
        t = input()
        s += t
        
    ogg = MyHTMLParser()
    ogg.feed(s)

#Validating UID
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

class main():
    def __init__(self):
        self.n = int(input())
        
        for i in range(self.n):
            self.s = input()
            self.pattern = ''
            self.temp = all([re.search(r, self.s) for r in [r'[A-Za-z0-9]{10}',r'([A-Z].*){2}',r'([0-9].*){3}']]) and not re.search(r'.*(.).*\1', self.s)
            
            print('Valid' if self.temp else 'Invalid')
            
            
if __name__ == '__main__':
    ogg = main()

#Validating Credit Card Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

class main:
    def __init__(self):
        self.test = re.compile(r'^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$')
        for _ in range(int(input())):
            self.s = input()
            print("Valid" if self.test.search(self.s) else "Invalid")
            
            
if __name__ == '__main__':
    ogg = main()

#Validating Postal Codes
regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


#Matrix Script
import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

encoded_string = "".join([matrix[j][i] for i in range(m) for j in range(n)])
pat = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
print(re.sub(pat,' ',encoded_string))


#XML 1 - Find the Score

def get_attr_number(node):
    # your code goes here
    return (sum(len(i.attrib) for i in node.iter()))

#XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if maxdepth == level:
        maxdepth += 1
        
    for child in elem:
        depth(child, level + 1)

#Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        # complete the function
        f(["+91 "+ a[-10:-5] + " " + a[-5:] for a in l])
    return fun

#Decorators 2 - Name Directory


def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key = lambda x: int(x[2])))
    return inner

#Arrays


def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr, float)[::-1]

#Shape and Reshape

import numpy as np

class main:
    def __init__(self):
        self.li = list(map(int, input().split()))
        self.np_li = np.array(self.li)
        
    def output(self):
        print(np.reshape(self.np_li, (3,3)))
        
if __name__ == '__main__':
    ogg = main()
    ogg.output()

#Transpose and Flatten

import numpy as np

class main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.np_array = np.array([input().split() for i in range(self.n)], int)
    
    def transposeArray(self):
        return np.transpose(self.np_array)
    
    def flattenArray(self):
        return self.np_array.flatten()
    
    def output(self):
        print(self.transposeArray())
        print(self.flattenArray())
        
if __name__ == '__main__':
    ogg = main()
    ogg.output()


#Concatenate

import numpy as np

class main:
    def __init__(self):
        self.n, self.m, self.p = map(int, input().split())
        self.firstArray = np.array([input().split() for i in range(self.n)], int)
        self.secondArray = np.array([input().split() for i in range(self.m)], int)
        
    def concatenateArray(self):
        return np.concatenate((self.firstArray, self.secondArray))
    
    def output(self):
        print(self.concatenateArray())
        
if __name__ == '__main__':
    ogg = main()
    ogg.output()


#Zeros and Ones

import numpy as np

shape = tuple(map(int, input().split()))

zero = np.zeros(shape, dtype=int)

uno = np.ones(shape, dtype=int)

print(zero)
print(uno)


#Eye and Identity

import numpy as np

print(str(np.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))



#Array Mathematics

import numpy as np

class main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.a = np.array([input().split() for i in range(self.n)], dtype=int)
        self.b = np.array([input().split() for i in range(self.n)], dtype=int)
        
    def Add(self):
        return np.add(self.a, self.b)
    
    def Subtract(self):
        return np.subtract(self.a, self.b)
    
    def Multiply(self):
        return np.multiply(self.a, self.b)
    
    def Divide(self):
        return self.a // self.b
    
    def Mod(self):
        return np.mod(self.a, self.b)
    
    def Power(self):
        return np.power(self.a, self.b)
    
    def output(self):
        print(self.Add())
        print(self.Subtract())
        print(self.Multiply())
        print(self.Divide())
        print(self.Mod())
        print(self.Power())
        
if __name__ == '__main__':
    ogg = main()
    ogg.output()

#Floor, Ceil and Rint

import numpy as np

np.set_printoptions(sign=' ')
a = np.array(input().split(),float)
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))


#Sum and Prod

import numpy as np

N, M = map(int, input().split())
A = np.array([input().split() for _ in range(N)],int)
print(np.prod(np.sum(A, axis=0), axis=0))

#Min and Max

import numpy as np
N, M = map(int, input().split())
print(np.array([input().split() for _ in range(int(N))], int).min(1).max())


#Mean, Var and Std

import numpy as np
N,M = map(int, input().split(" "))
A = np.array([input().split() for _ in range(N)],int)
print(np.mean(A, axis = 1))
print(np.var(A, axis = 0))
print(round(np.std(A, axis = None),11))

#Dot and Cross

import numpy as np

n = int(input())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)
print(np.dot(a, b))

#Inner and Outer

import numpy as np
A = np.array(input().split(), int)
B = np.array(input().split(), int)
print(np.inner(A,B), np.outer(A,B), sep='\n')


#Polynomials

import numpy as np

poly = [float(x) for x in input().split()]
x = float(input())
print(np.polyval(poly, x))


#Linear Algebra

import numpy as np

np.set_printoptions(legacy='1.13')

n = int(input())
array = np.array([input().split() for _ in range(n)], float)
print(np.linalg.det(array))

