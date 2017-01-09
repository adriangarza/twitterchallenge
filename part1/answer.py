"""    
given a list of expression trees and sequence in the format
    "<expression tree> / <sequence of operations>"
    EXPRESSION TREE
        non-empty, A-Z variables
        derivatve chain: E -> E \ (E)
    OPERATIONS
        R: reverse, but keep parentheses intact
        S: simplify, look at the FIRST element and remove:
            parentheses around it
            parentheses around sub-expression trees
            i.e (AB) C / S -> ABC
    IDEAS
        remove all spaces
        if there are any S markers, only simplify once
        no Rs: don't do anything
        odd number of Rs in a row: reverse
        even number of Rs in a row: do nothing


    PSEUDO
        create scanner in main(), infinitely read lines
        feed it into answer(), print what it returns
        remove spaces
        separate by slash
        concatenate Ss between Rs
        between every S, look forwards to the next S and do the odd/even R treatment

        for reversing, reverse the entire string and then swap parentheses
"""
def simplify(str):
    print "Adsd"
def reverse(str):
    print "ASdasd"

test1 = "(AB) C((DE)F) /SRRRSSRRSSS"

while True:
    #grab the expression tree and operations, format correctly
    inputString =raw_input().replace(" ", "")
    if inputString == "test":
        inputString = test1
    #split the string into its components
    expressionTree = inputString.split("/")[0]
    operations = list(inputString.split("/")[1])

    #optimize operations: remove sequential S operations
    for idx, val in enumerate(operations):
        if val == "S":
            while idx+1 < len(operations) and operations[idx+1] == "S":
                del operations[idx+1]
        #optimize reversals: remove them in pairs
        if val == "R":
            if idx+1 < len(operations) and operations[idx+1] == "R":
                del operations[idx]
                del operations[idx]

    print operations
