"""    
given a list of expression trees and sequence in the format
    "<expression tree> / <sequence of operations>"
    EXPRESSION TREE
        non-empty, A-Z variables
        derivatve chain: E -> E | (E)
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

        for reversing, reverse the entire inputString and then swap parentheses
"""
def simplify(inputString):
    #find the first non-parentheses character after counting opening/closing parentheses
    #then remove closing parentheses until balance is restored
    openP = 0
    startIdx = 0
    for idx, val in enumerate(inputString):
        if val == "(":
            openP += 1
        elif val == ")":
            openP -= 1
        else:
            startIdx = idx
            break
    
    outStr = ""     #the new, simplified inputStringing
    endIdx = 0      #the end of the first simplification

    for i in range(startIdx, len(inputString)):
        #break from the loop if all parentheses are closed
        if openP <= 0:
            endIdx = i 
            break

        #if it's a character, add to the new inputStringing
        if inputString[i] not in ["(", ")"]:
            outStr += inputString[i]
        #else, keep track of open parentheses accordingly
        elif inputString[i] == '(':
            openP += 1
        elif inputString[i] == ')':
            openP -= 1
    
    #now append everything else
    outStr += inputString[endIdx::]

    return outStr

def reverse(inputString):
    #swap parentheses using the intermediary character ' ', then reverse
    return inputString.replace("(", " ").replace(")", "(").replace(" ", ")")[::-1]

test1 = "A(BC)/RSR"

while True:
    #grab the expression tree and operations, format correctly
    try:
        inputString =raw_input().replace(" ", "")
    except (EOFError):
        break

    if inputString == "test":
        inputString = test1
    #split the inputStringing into its components
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

    #now iterate through the operations with some optimization:
    #if both ends have been simplified, just check if they are an even
    #or odd number of reversals left and do zero or one of those
    simplifiedFront = False
    simplifiedBack = False
    treeReversed = False
    for idx, op in enumerate(operations):
        #if both ends are simplified, just reverse and return
        if simplifiedFront and simplifiedBack:
            numRs = 0
            for j in range(idx, len(operations)):
                if operations[j] == "R":
                    numRs += 1
            #if there are an odd number of times left to reverse, just do it once
            if numRs % 2 != 0:
                operations = reverse(operations)
                break
            else:
                break

        elif op == "R":
            expressionTree = reverse(expressionTree)
            treeReversed = not treeReversed
        elif op == "S":
            #only need to simplify both sides once
            if not treeReversed and not simplifiedFront:
                expressionTree = simplify(expressionTree)
                simplifiedFront = True
            elif treeReversed and not simplifiedBack:
                expressionTree = simplify(expressionTree)
                simplifiedBack = True

    #the operations are finished, so print the inputStringing
    print expressionTree
