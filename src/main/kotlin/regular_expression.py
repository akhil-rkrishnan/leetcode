

def isSatisfiedRegularExpression(s, p):
    
    k = 0; j = 0
    pLen = len(p); sLen = len(s)
    passed = True
    
    if (p == ".*" or p == ""):
        return passed
    if (p.find("*") == -1 and p.find(".") == -1):
        if (p != s):
            return not passed

    c = ""
    while (k < pLen):

        if (j < sLen and (p[k] == s[j] or p[k] == ".")):
            print("IN-M")
            k = k + 1; j = j + 1
        elif (p[k] == "*"):
            c = p[k-1]
            if (j == sLen):
                k = k + 1
                print("Recursion")
                return isSatisfiedRegularExpression(s[j - 1], p[k:])
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
        
        elif (p[k] == c or p[k] == "."):
            k = k + 1

        else:
            passed = False   
            k = k + 1
            print("IN-2")         
            break

    if (j != sLen):
        passed = False
        print("IN-3")
       
    return passed

string = "a"
pattern = ".*..a*"

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

# string = "aaa"
# pattern = "a*a" 

# string = "ab"
# pattern = ".*c"  

# string = "aa"
# pattern = "a*"

print(isSatisfiedRegularExpression(string, pattern))
