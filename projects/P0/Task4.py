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
    numsMakingCallsList = []
    for call in calls:
        if call[0] not in numsMakingCallsList:
            numsMakingCallsList.append(call[0])
    return numsMakingCallsList

def numsOtherFuncs(calls, texts):
    """
    This function finds unique numbers that send texts, receive texts
    or receive incoming calls.
    """
    numsOtherFuncsList = []
    
    # numbers that send receive texts
    for text in texts:
        if text[0] not in numsOtherFuncsList:
            numsOtherFuncsList.append(text[0])
        if text[1] not in numsOtherFuncsList:
            numsOtherFuncsList.append(text[1])
    
    # numbers that receive incoming calls
    for call in calls:
        if call[1] not in numsOtherFuncsList:
            numsOtherFuncsList.append(call[1])
    
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
    
    
    
    
