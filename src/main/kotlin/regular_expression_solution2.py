
import re


def isMatch(s, p):
    
    k = 0; j = 0
    patternLength = len(p); stringLength = len(s)
    passed = True
    
    if (p == ".*" or p == ""):
        return passed

    elif (p.find("*") == -1 and p.find(".") == -1):
        if (p != s):
            return not passed    

    tempChar = ""
    while (k < patternLength):
        if (j < stringLength and p[k] == s[j]):
            print("\n IN-1", p[k], s[j])
            k = k + 1; j = j + 1
        elif (p[k] == "*"):
            print("\n IN-2")
            tempChar = p[k - 1]
            while (j < stringLength):
                print("IN-3", tempChar, s[j])
                if (tempChar == s[j]):
                    j = j + 1
                else:
                    print("IN-4")
                    k = k + 1
                    if (k >= patternLength and j < stringLength):
                        print("IN-5")
                        passed = False
                    break

            if (j == stringLength):
                k = k + 1
                return isMatch(s[j - 1:], p[k:])
            else:
                if (k + 1 < patternLength):
                    return isMatch(s[j: ], p[k + 1])
                            
        elif (k + 1 < patternLength and p[k + 1] == "*"):
            print("IN-6")
            k = k + 2                
        elif (p[k] == "."):
            print("IN-7")
            j = j + 1             

        else:
            print("IN-8")
            passed = False
            break

    return passed


string = "bccd"
pattern = "b*ccd"
 

# string = "a"
# pattern = ".*..a*"

#True
# string = "ab"
# pattern = ".*..c*"

# True
# string = "ab"
# pattern = ".*.."

# string = "aaa"
# pattern = "ab*ac*a"

# string = "bbbba"
# pattern = ".*a*a"      

string = "aaaaaabbbb"
pattern = "a*bb" 

# string = "bbb"
# pattern = "bb"  

string = "aaaaaa"
pattern = "a*aa"
print("Checking regular expression")
print(isMatch(string, pattern))