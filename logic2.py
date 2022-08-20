"""
•	Propositional logic is also called Boolean logic as it works on 0 and 1.
•	In propositional logic, we use symbolic variables to represent the logic, and we can use any symbol for a representing a proposition, such A, B, C, P, Q, R, etc.
•	Propositions can be either true or false, but it cannot be both.
•	Propositional logic consists of an object, relations or function, and logical connectives.
•	These connectives are also called logical operators.
•	The propositions and connectives are the basic elements of the propositional logic.
•	Connectives can be said as a logical operator which connects two sentences.
•	A proposition formula which is always true is called tautology, and it is also called a valid sentence.
•	A proposition formula which is always false is called Contradiction.
•	A proposition formula which has both true and false values is called
•	Statements which are questions, commands, or opinions are not propositions such as "Where is Rohini", "How are you", "What is your name", are not propositions.


Syntax: 
    
Sr. No	Subject	Syntax
1	Simple undividable statement represent true or false (not both)  and it is Boolean in nature	Upper Case letters A, B, C, P, Q, R are used to represent statements
2	Logical Connectors or operators used to connect two statements	^, v, →, ↔, ¬ are used to represent AND, OR,
3	Complex conditions	Complex conditions are handled by coding connectors within parenthesis.



"""


import itertools

print('Rules: ')
print('1) To enter "AND" use "+"')
print('2) To enter "OR" use "*"')
print('3) To enter "NOT" use "-"')
print('4) You can also use braces ()')

logical_expression = input('Enter the logical expression: ').strip()
# to remove all white spaces from the expression

variables = []
for c in logical_expression:
    if c not in ['+', '*', '-', '(', ')', ' '] + variables:
        variables.append(c)
# to get a list of only variables
n = len(variables)

truth_table = list(itertools.product([0,1], repeat=n))
print("\nTruth Table:\n")
for var in variables:
    print(' ' + var + ' ', end='')
print("  " + logical_expression)

satisfiable = False
for row in truth_table:
    temp_expr = logical_expression
    for i in range(len(variables)):
        temp_expr = temp_expr.replace(variables[i], str(row[i]))
    temp_expr = temp_expr.replace("+", "|").replace("*", "&").replace("-", "~")
    result = eval(temp_expr)

    if result:
        satisfiable = True

    for val in row:
        print(' ' + str(val) + ' ', end='')
    print("    " + str(result))

if satisfiable:
    print('\nThe entered propositional logic expression is Satisfiable')
else:
    print('\nThe entered propositional logic expression is not Satisfiable')
