"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def timeSpentMax(calls):
    """
    This function returns the telephone number that spent the longest time 
    on the phone during September 2016.
    """
    timeSpent = {}
    for call in calls:
        date = call[2].replace('-', ' ').split()
        if date[1] == '09' and date[2] == '2016':
            # calling telephone number
            if call[0] not in timeSpent:
                timeSpent[call[0]] = int(call[3])
            else:
                timeSpent[call[0]] += int(call[3])
        
            # answering telephone number
            if call[1] not in timeSpent:
                timeSpent[call[1]] = int(call[3])
            else:
                timeSpent[call[1]] += int(call[3])
    
    # find maximum
    numMax, timeMax = list(timeSpent.items())[0]
    
    for num, time in timeSpent.items():
        if time > timeMax:
            numMax = num
            timeMax = time
    
    result = '{} spent the longest time, {} seconds, on the phone during '\
    'September 2016'.format(numMax, timeMax)
    
    return result

print(timeSpentMax(calls))
# Time complexity O(n^2)        



