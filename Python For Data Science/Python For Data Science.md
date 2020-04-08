# Python for Data Science Cognitiveclass PY0101EN
# MODULE-1 PYTHON BASICS:
REVIEW QUESTION 1 
What is the result of the following operation in Python:

3 + 2 * 2
output-7

REVIEW QUESTION 2 
In Python, if you executed name = 'Lizz', what would be the output of print(name[0:2])?
output-Li

REVIEW QUESTION 3 
In Python, if you executed var = '01234567', what would be the result of print(var[::2])?
output-0246

REVIEW QUESTION 4 
In Python, what is the result of the following operation '1'+'2'
output-'12'

REVIEW QUESTION 5 
Given myvar = 'hello', how would you convert myvar into uppercase?
output-myvar.upper()

# MODULE-2 PYTHON DATA STRUCTURES
QUESTION 1
What is the syntax to obtain the first element of the tuple:
A=('a','b','c')
output-A[0]

QUESTION 2 
After applying the following method,L.append(['a','b']), the following list will only be one element longer.
output-True

QUESTION 3 
How many duplicate elements can you have in a set?
output-0, Set can only contain Unique Values

QUESTION 4 
Consider the following Python Dictionary:
Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}
what is the result of the following operation: Dict["D"]
output-(4,4,4)

QUESTION 5 
What is an important difference between lists and tuples?
output-Lists are mutable, tuples are not!

# MODULE-3 PYTHON PROGRAMMING FUNDAMENTALS:
QUESTION 1 
What is the output of the following lines of code:
x=1
if(x!=1):
    print('Hello')
else:
    print('Hi')
print('Mike')
output-Hi Mike

QUESTION 2 
What is the output of the following few lines of code ?
A=['1','2','3']
for a in A:
    print(2*a)
output-'11''22''33'

QUESTION 3 
Consider the function Delta, when will the function return a value of 1
def Delta(x):
if x==0:
    y=1;
else:
    y=0;
return(y)
output-when input is 0

QUESTION 4 
What is the correct way to sort the list 'B' using a method, the result should not return a new list, just change the list 'B'.
output-B.sort()

QUESTION 5 
what are the keys of the of the following {'a':1,'b':2}
output-a,b
# MODULE-4 WORKING WITH DATA IN PYTHON
QUESTION 1 
What do the following lines of code do?

with open("Example1.txt","r") as file1:
    FileContent=file1.readlines()
    print(FileContent)

 output- Read the file "Example1.txt"
 
 QUESTION 2 
What do the following lines of code do?

with open("Example2.txt","w") as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

output- Write to the file "Example2.txt"

QUESTION 3 
What do the following lines of code do?

with open("Example3.txt","a") as file1:
    file1.write("This is line C\n")
   
output- Append the file "Example3.txt" 

QUESTION 4 
What is the result of applying the following method df.head(), to the dataframe df
output-  prints the first 5 rows of the dataframe
# MODULE-5 WORKING WITH NUMPY ARRAYS
MULTIPLE CHOICE
1. What is the result of the following lines of code:
a=np.array([0,1,0,1,0])
b=np.array([1,0,1,0,1])
a*b
output-array([0, 0, 0, 0, 0])

2. What is the result of the following lines of code:
a=np.array([0,1])
b=np.array([1,0])
np.dot(a,b)
output-0

3. What is the result of the following lines of code:
a=np.array([1,1,1,1,1])
a+10
output- array([11, 11, 11, 11, 11])

4. What is the correct code to perform matrix multiplication on the matrix A and B
 output-np.dot(A,B)
# FINAL EXAM
1)What is the result of the following operation 3+2*2?
output-7

2) What is the type of the following variable: a=True?
output- bool

3) What is the result of the following operation int(3.2)?
output-3

4) Consider the string A='1234567', what is the result of the following operation: A[1::2]
output- '246'

5) Consider the string Name="Michael Jackson" , what is the result of the following operation Name.find('el')
output- 5

6) The variables A='1' and B='2' ,what is the result of the operation A+B?
output- '12'

7) Consider the variable F="You are wrong", Convert the values in the variable F to uppercase?
output- F.upper()

8) Consider the tuple tuple1=("A","B","C" ), what is the result of the following operation tuple1[-1]?
output- "C"

9) Consider the tuple A=((11,12),[21,22]), that contains a tuple and list. What is the result of the following operation A[1]:
output- [21,22]

10) Consider the tuple A=((11,12),[21,22]), that contains a tuple and list. What is the result of the following operation A[0][1]:
output- 12

11) What is the result of the following operation '1,2,3,4'.split(',')
output-  ['1','2','3','4'] 

12) Concatenate the following lists A=[1,'a'] and B=[2,1,'d']:
output- A+B

13) How do you cast the list 'A' to the set 'a'?
output- a=set(A)

14) Consider the Set: V={'A','B'}, what is the result of V.add('C')?
output- {'A','B','C'}

15) Consider the Set: V={'A','B','C' }, what is the result of V.add('C')?
output- {'A','B','C'}

16) What is the output of the following lines of code:

x="Go"
if(x!="Go"):
    print('Stop')
else:
    print('Go ')
print('Mike')

 output- Go Mike 
 
17) What is the output of the following lines of code:

x="Go"
if(x=="Go"):
    print('Go ')
else:
    print('Stop')
print('Mike')

 output- Go Mike 
 
18) How many iterations are performed in the following loop?
for n in range(3):
    print(n)
output- 3

19) What does the following loop print?
for n in range(3):
    print(n+1)
output- 1 2 3

20) What is the output of the following few lines of code ?
A=['1','2','3']
for a in A:
    print(2*a)
output- '11''22''33'

21) Consider the function add, what is the result of calling the following Add('1','1') (look closely at the return statement )

def Add(x,y):
    z=y+x
    return(y)
output- '1'

22) Consider the class Points, what are the data attributes:

class Points(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def print_point(self):
        print('x=',self.x,'y=',self.y)
output-  self.x self.y 

23) What is the result of running the following lines of code ?

class Points(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def print_point(self):
        print('x=',self.x,' y=',self.y)
p1=Points(1,2)
p1.print_point()

output-  x=1 y=2

24) What is the result of running the following lines of code ?

class Points(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def print_point(self):
        print('x=',self.x,' y=',self.y)
p2=Points(1,2)
p2.x=2
p2.print_point()
output- x=2 y=2 

25) Consider the following line of code: with open(example1,"r") as file1:
What mode is the file object in?
output-read