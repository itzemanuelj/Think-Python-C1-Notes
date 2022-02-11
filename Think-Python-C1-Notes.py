#Vocab For Unit 1
#input: Get data from the keyboard, a file, the network, or some other device.
#output: Display data on the screen, save it in a file, send it over the network, etc.
#math: Perform basic mathematical operations like addition and multiplication.
#conditional execution: Check for certain conditions and run the appropriate code.
#repetition: Perform some action repeatedly, usually with some variation.
#Programming languages are formal languages that have been designed to express computations.
#ambiguity: Natural languages are full of ambiguity, which people deal with by using contextual clues and other information. 
# Formal languages are designed to be nearly or completely unambiguous, which means that any statement has exactly one meaning, regardless of context.
#redundancy: In order to make up for ambiguity and reduce misunderstandings, natural languages employ lots of redundancy. As a result, they are often verbose.  
# Formal languages are less redundant and more concise.
#literalness: Natural languages are full of idiom and metaphor. If I say, “The penny dropped”, there is probably no penny and nothing dropping  (
# this idiom means that someone understood something after a period of confusion). Formal languages mean exactly what they say.

>>> 1 + 1
2

>>> print('Hello, World!')
Hello, World!
    
#Arithmetic operators

>>> 40 + 2
42

>>> 43 - 1
42

>>> 6 * 7
42

#The operator / performs division:

>>> 84 / 2
42.0

#You might wonder why the result is 42.0 instead of 42. I’ll explain in the next section.
#Finally, the operator ** performs exponentiation; that is, it raises a number to a power:

>>> 6**2 + 6
42

##In some other languages, ^ is used for exponentiation, but in Python it is a bitwise operator
#called XOR. If you are not familiar with bitwise operators, the result will surprise you:

>>> 6 ^ 2
4

#Values and types

>>> type(2)
<class 'int'>

>>> type(42.0)
<class 'float'>

type('Hello, World!')
<class 'str'>

>>> type('2')
<class 'str'>

>>> type('42.0')
<class 'str'>

#They’re strings.

>>> 1,000,000
(1, 0, 0)

#Glossary

#problem solving: The process of formulating a problem, finding a solution, and expressing it.
#high-level language: A programming language like Python that is designed to be easy for humans to read and write.
#low-level language: A programming language that is designed to be easy for a computer to run; also called “machine language” or “assembly language”.
#portability: A property of a program that can run on more than one kind of computer.
#interpreter: A program that reads another program and executes it
#prompt: Characters displayed by the interpreter to indicate that it is ready to take input from the user.
#print statement: An instruction that causes the Python interpreter to display a value onthe screen.
#operator: A special symbol that represents a simple computation like addition, multiplication, or string concatenation. value: One of the basic units of data,
#  like a number or string, that a program manipulates.
#type: A category of values. The types we have seen so far are integers (type int), floatingpoint numbers (type float), and strings (type str).
#integer: A type that represents whole numbers.
#floating-point: A type that represents numbers with fractional parts.
#string: A type that represents sequences of characters.
#natural language: Any one of the languages that people speak that evolved naturally.
#formal language: Any one of the languages that people have designed for specific purposes, such as representing mathematical ideas or computer programs; 
# all programming languages are formal languages. token: One of the basic elements of the syntactic structure of a program, analogous to aword in a natural language.
#syntax: The rules that govern the structure of a program.
#parse: To examine a program and analyze the syntactic structure.
#bug: An error in a program.
#debugging: The process of finding and correcting bugs.

#Exercises

#1. In a print statement, what happens if you leave out one of the parentheses, or both?
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?


#2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

#3. You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?
# SyntaxError: invalid syntax

#4. In math notation, leading zeros are ok, as in 02. What happens if you try this in Python?
# SyntaxError: invalid syntax

#5. What happens if you have two values with no operator between them?
# SyntaxError: invalid syntax

#1. How many seconds are there in 42 minutes 42 seconds?
>>> 42*60*42
105840
>>>

#2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
>>> 10/1.61
6.211180124223602
#3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? 
>>> 10/1.61/42*60+42
50.87311446317658
>>>
# What is your average speed in miles per hour?
3052.386867790595