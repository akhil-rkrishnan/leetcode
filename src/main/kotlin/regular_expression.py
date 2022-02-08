
from linecache import checkcache
import re


def isSatisfiedRegularExpression(p, s):
    
    k = 0; j = 0
    pLen = len(p); sLen = len(s)
    passed = True
    if (p == ".*"):
        return passed
    if (p.find("*") == -1 and p.find(".") == -1):
        if (p != s):
            return not passed
    c = ""
    while (k < pLen):

        if (j < sLen and (p[k] == s[j] or p[k] == ".")):
            k = k + 1; j = j + 1
        elif (p[k] == "*"):
            c = p[k-1]
            if (j == sLen):
                k = k + 1
                # break
            
            while (j < sLen):
                if (s[j] == c or c == "."):
                    j = j + 1
                elif(k + 1 < pLen and (p[k + 1] == s[j] or p[k + 1] == ".")):
                    k = k + 2; j = j + 1; break
                elif (k + 1 < pLen and p[k + 1] == "*"):
                    k = k + 1; j = j + 1; break
                else:
                    print("IN-1")
                    passed = False
                    k = pLen
                    break      
           
        elif(k + 1 < pLen and p[k + 1] == "*"):
            k = k + 2
        
        elif (p[k] == c):
            k = k + 1

        else:
            passed = False   
            print("IN-2")         
            break

    if (j != sLen):
        passed = False
        print("IN-3")

    return passed

string = "bbbba"
pattern = ".*a*a"      

# string = "aaa"
# pattern = "a*a" 

# string = "ab"
# pattern = ".*c"  

# string = "aa"
# pattern = "a*"

print(isSatisfiedRegularExpression(pattern, string))