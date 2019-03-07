def is_palindrom(string):
    if len(string) % 2 == 0:
        half = string[0:len(string)//2]
        reverse_half = string[len(string):len(string)//2-1:-1]
        return half == reverse_half
    else:
        half = string[0:len(string)//2]
        reverse_half = string[len(string):(len(string)//2):-1]
        return half == reverse_half

def check_palindrome():
    for i in range(100000,999999):
        test_string = str(i)[2:6]
        if is_palindrom(test_string):
            test_string = str(i+1)[1:6]
            if is_palindrom(test_string):
                test_string = str(i+2)[1:5]
                if is_palindrom(test_string):
                    test_string = str(i+3)
                    if is_palindrom(test_string):
                        print("Found a matching number: " + str(i))

if __name__ == '__main__':
    # Question 2
    print("Running Question 2:")
    check_palindrome()