
from linecache import checkcache
import re


def isSatisfiedRegularExpression(p, s):
    
    k = 0; j = 0
    pLen = len(p); sLen = len(s)
    passed = True
    if (p == ".*"):
        return passed
    if (p.find("*") == -1):
        if (p != s):
            return not passed

    while (k < pLen):

        if (j < sLen and p[k] == s[j]):
            k = k + 1; j = j + 1
        elif (p[k] == "*"):
            c = p[k-1]
            if (j == sLen):
                break
            while (j < sLen):
                if (s[j] == c):
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
            
        # elif(k + 1 < pLen and p[k + 1] == "."):
        #     k = k + 1
        else:
            passed = False   
            print("IN-2")         
            break
   
    return passed
        
string = "abcd"
pattern = "f*"             

print(isSatisfiedRegularExpression(pattern, string))