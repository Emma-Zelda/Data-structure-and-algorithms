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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def countUniqueNums(texts, calls):
    """
    This function counts unique telephon numbers in all records.
    """
    unique = []             
    # find unique numbers in texts
    for text in texts:
        if text[0] not in unique: 
            unique.append(text[0])
        if text[1] not in unique:
            unique.append(text[1])
    
    # find unique numbers in calls
    for call in calls:
        if call[0] not in unique:
            unique.append(call[0])
        if call[1] not in unique:
            unique.append(call[1])

    return len(unique)

print(countUniqueNums(texts, calls))
# Time complexity O(n^2)




