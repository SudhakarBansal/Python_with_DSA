# Words Frequency in a Sentence

# Input: "hello world hello"
# Output: {'hello': 2, 'world': 1}

def count_word_frequency(sentence:str)->dict:
    # Your code goes here
    dct = {}
    wordlst = sentence.split()
    for items in wordlst:
        if items in dct:
            dct[items] += 1
        else:
            dct[items]=1

    return dct


print(count_word_frequency(""))