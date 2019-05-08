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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def firstText(texts):
    """
    This function returns first record of the texts.
    """
    text = texts[0]
    result = 'First record of texts, {} texts {} at time {}'.format(text[0],
                                     text[1], text[2])
    return result

print(firstText(texts))
# Time complexity of O(1)


def lastCall(calls):
    """
    This function returns last record of the calls.
    """
    call = calls[-1]
    result = 'Last record of calls, {} calls {} at time {}, ' \
    'lasting {} seconds'.format(call[0], call[1], call[2], call[3])
    
    return result

print(lastCall(calls))
# Time complexity of O(1)

