def trifeca(word): 
    """ Checks whether word contains three consecutive double-letter pairs. """
    pairs = 0

    i = 0
    pairs = 0
    while i < len(word):
        if i+1 == len(word):
            return False
        
        if word[i] == word[i+1]:
            pairs = pairs+1
            i = i+2
        else:
            i = i+1
            pairs = 0
        
        if pairs == 3:
            return True
    return False

if __name__ == '__main__':
    # Question 1
    example1 = 'aabbcc'
    return_value = trifeca(example1)
    print("Question 1 solution example1: " + example1 + ", result: " + str(return_value))

    example2 = 'abccddee0123'
    return_value = trifeca(example2)
    print("Question 1 solution example2: " + example2 + ", result: " + str(return_value))

    example3 = 'llkkbmm'
    return_value = trifeca(example3)
    print("Question 1 solution example3: " + example3 + ", result: " + str(return_value))
