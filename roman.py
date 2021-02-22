# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals

Refer to the instructions on Canavs for more information.

"I have neither given nor received help on this assignment."
author: Xander Dyer (xdyer)
"""
__version__ = 1

#Dictionary of Roman Numerals (keys) and their values
rNum = {
    "I":1, "V":5, "X":10, "L":50,
    "C":100, "D":500, "M":1000
}


def valid_numeral(test_case):
    """
    Primary function that takes a string and returns whether it is a valid 
    roman numeral or not.
    """
    num = test_case
    
    #Checks string validity according to conditions in helper functions
    if checkNumeral(num) and check4x(num) and checkOrder(num):
            return True
    
    return False

def checkNumeral(string):
    """
    Helper function that determines if a string consists of alpha letter
    characters and if they one of the specific upper-case roman numeral. Takes
    a string as a parameter and returns true if the string only consists of
    valid upper-case roman numerals.
    """
    #Checks if characers are letters
    if not string.isalpha():
        return False
    
    #Checks if characters are Roman Numerals
    for ch in string:
        if (ch != "I" and ch != "V" and ch != "X" and ch!= "L" and ch != "C" 
        and ch != "D" and ch != "M"):
            return False
        
    return True

def check4x(string):
    """
    Helper function that determines if a string violates the rule of having 
    more than 4 repeating numerals or a sequence of 2 or 3 numerals that are
    powers of 10. takes a string as parameter and returns true only if both
    conditions are met.
    """
    count = 1
    #Iterates through string greater than 1 char
    if len(string) > 1:
        for i in range(1, len(string)):
            #Counts sequences of characters
            if string[i-1] != string[i]:
                count = 1
            else:
                count += 1
                #Behavior for rule 7
                if ((count > 1 and not checkPower(rNum.get(string[i-1])))
                    or count > 3):
                    return False
        return True
    return True


def checkOrder(string):
    """
    Helper function that determines if a string violates numeral rules five 
    and six. Takes a string as a parameter and returns true only if there are 
    small value symbols that precede large value symbols that are powers of 10
    AND within two symbols in size order.
    """
    #moves dictionary keys to an indexed list
    keys = rNum.keys()
    keys_list = list(keys)
    #print(keys_list)
    #Iterates through string greater than 1 char
    if len(string) > 1:
        for i in range(1, len(string)):
            #print(rNum.get(string[i-1]))
            curInd = keys_list.index(string[i-1])
            nxtInd = keys_list.index(string[i])
            #print(curInd)
            #print(nxtInd)
            #Checks powers of 10 and size order, consinues if valid
            if checkPower(rNum.get(string[i-1])) and abs(nxtInd - curInd) < 3:
                continue
            #Provides behavior for invalid numeral ordering
            if rNum.get(string[i-1]) < rNum.get(string[i]):
                return False    
    return True

def checkPower(x):
    """
    Helper function for checking if a number is a power of 10. Takes a number
    as a parameter and returns true if it is a power of 10.

    """
    #Behavior for power of 10: 0 and 1
    if x == 1 or x == 10:
        return True
    
    power = 1
    #Finds power of 10 closest to input number
    while power < x:
        power = power * 10
        
    #Checks if closest power of 10 is equal to input number
    return power == x

def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()





###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for Rule 1
def test1():
    #assert valid_numeral("abc") == True, ("The function does not validate" +
        #"supplied string properly")
    #assert valid_numeral("XVC") == True, ("The function does not validate" +
        #"supplied string properly")
    assert valid_numeral("abc!") == False, ("The function does not invalidate" +
        "supplied string properly")
    assert valid_numeral("") == False, ("The function does not invalidate" +
        "supplied string properly")

# Below are the tests for rule 2
def test2():
    # This comment explains what test2() is testing for, and is followed by code
    #assert checkNumeral("XVC") == True, ("The function does not validate" +
        #"supplied string properly")
    assert checkNumeral("XVCA") == False, ("The function does not invalidate" +
        "supplied string properly")
    assert checkNumeral("xvc") == False, ("The function does not invalidate" +
        "supplied string properly")
    #assert valid_numeral("XVC") == True, ("The function does not validate" +
        #"supplied string properly")
    assert valid_numeral("abc") == False, ("The function does not validate" +
        "supplied string properly")
    
# Below are the tests for rule 3
def test3():
    # This comment explains what test3() is testing for, and is followed by code
    assert check4x("III") == True, ("The function does not validate" + 
        "supplied string properly")
    assert check4x("IIII") == False, ("The function does not invalidate" + 
        "supplied string properly")
    assert check4x("X") == True, ("The function does not validate" + 
        "supplied string properly")
    assert check4x("XCVIIIIXCV") == False, ("The function does not invalidate" + 
        "supplied string properly")
    
# Below are the tests for rule 4
def test4():
    # This comment explains what test3() is testing for, and is followed by code
    assert checkOrder("XVXCVI") == False, ("The function does not invalidate" + 
        "supplied string properly")
    assert checkOrder("X") == True, ("The function does not validate" + 
        "supplied string properly")
    assert checkOrder("MDC") == True, ("The function does not validate" + 
        "supplied string properly")
    
# Below are the tests for rule 5
def test5():
    assert checkPower(10) == True, ("The function does not provide" + 
        "correct feedback for a number that is a power of 10")
    assert checkPower(100) == True, ("The function does not provide" + 
        "correct feedback for a number that is a power of 10")
    assert checkPower(25) == False, ("The function does not provide" + 
        "correct feedback for a number that is not a power of 10")
    assert checkOrder("XXXCVI") == True, ("The function does not validate" + 
        "supplied string properly")
    
# Below are the tests for rule 6
def test6():
    assert checkOrder("XM") == False, ("The function does not invalidate" + 
        "supplied string properly")
    assert checkOrder("XXXL") == True, ("The function does not validate" + 
        "supplied string properly")

# Below are the tests for rule 7 and other supplied test cases
def test7():
    assert valid_numeral("XVIII") == True, ("The function does not validate" + 
        "supplied string properly")
    assert valid_numeral("MCXIV") == True, ("The function does not validate" + 
        "supplied string properly")
    assert valid_numeral("CCCC") == False, ("The function does not invalidate" + 
        "supplied string properly")
    assert valid_numeral("CIL") == False, ("The function does not invalidate" + 
        "supplied string properly")
    assert valid_numeral("M2C") == False, ("The function does not invalidate" + 
        "supplied string properly")
    assert valid_numeral("ASDF") == False, ("The function does not invalidate" + 
        "supplied string properly")
    assert valid_numeral("VL") == False, ("The function does not invalidate" + 
        "supplied string properly")
    assert valid_numeral("XXX") == True, ("The function does not validate" + 
        "supplied string properly")
    assert valid_numeral("LLL") == False, ("The function does not invalidate" + 
        "supplied string properly")
    
    
    


    
###############################################################    
    
if __name__ == "__main__":
    main()    