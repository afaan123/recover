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

def findInputs(ex):
    inputs=[]
    for c in ex:
        if c!='+' and c!='*' and c!='-' and c!='(' and c!=')' and c!=' ' and c not in inputs:
            inputs.append(c)
    return inputs

def evaluate(ex,row):
    input_no=0
    replaced=[]
    for c in ex:
        if c!='+' and c!='*' and c!='-' and c!='(' and c!=')' and c!=' ' and c not in replaced :
            ex=ex.replace(c,str(row[input_no]))
            input_no+=1
            replaced.append(c)
    ex=ex.replace('+','&')
    ex=ex.replace('*','|')
    ex=ex.replace('-','~')
    result=eval(ex)
    return result

def compute_results(truthtable,ex):
    outputs=[]
    for row in truth_table:
        outputs.append(evaluate(ex,row))
    return outputs

n=int(input('Enter number of inputs: '))
print('Rules: ')
print('1) To enter "AND" use "+"')
print('2) To enter "OR" use "*"')
print('3) To enter "NOT" use "-"')
logical_expression=input('Enter the logical expression: ')

truth_table = list(itertools.product([0,1],repeat=n))
table_outputs=compute_results(truth_table,logical_expression)

print('')
print('Truth Table:')
print('')
for c in findInputs(logical_expression):
    print(c,end='  ')
print('Output')

for i in range(len(truth_table)):
    for val in truth_table[i]:
        print(val,end='  ')
    print('  ',table_outputs[i])
print('')

if table_outputs.count(1)>=1:
    print('The entered propositional logic expression is Satisfiable')
else:
    print('The entered propositional logic expression is Not Satisfiable')








