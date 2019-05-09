"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def numsMakingCalls(calls):
    """
    This functions finds unqiue numbers that make outgoing calls.
    """
    numsMakingCallsList = set()
    for call in calls:
        numsMakingCallsList.add(call[0])
    return numsMakingCallsList

def numsOtherFuncs(calls, texts):
    """
    This function finds unique numbers that send texts, receive texts
    or receive incoming calls.
    """
    numsOtherFuncsList = set()
    
    # numbers that send receive texts
    for text in texts:
        numsOtherFuncsList.add(text[0])
        numsOtherFuncsList.add(text[1])
    
    # numbers that receive incoming calls
    for call in calls:
        numsOtherFuncsList.add(call[1])
    
    return numsOtherFuncsList

def main():
    numsMakingCallsList = numsMakingCalls(calls)
    numsOtherFuncsList = numsOtherFuncs(calls, texts)
    
    numsTM = []
    for num in numsMakingCallsList:
        if num not in numsOtherFuncsList:
            numsTM.append(num)
    numsTM.sort()
    print('These numbers could be telemarketers:',
          *numsTM, sep = '\n')

if __name__ == '_main_':
    main()    
    
main()    

# Time complexity of O(n^2)
    
    
    
    
