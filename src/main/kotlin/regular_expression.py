
from linecache import checkcache


def allCharactersSame(s, checkChar) :
    n = len(s)
    for i in range(1, n) :
        if s[i] != checkChar :
            return False
    return True

def isSatisfiedRegularExpression(checkString, pattern):
    
    if (checkString == pattern):
        return True
    elif (pattern == ".*"):
        return True
    else:
        stringLength = len(checkString)
        patternLength = len(pattern)
        if (patternLength > stringLength):
            return False
        else:
            if (pattern.find("*") != -1):
              splitString = pattern.split("*")[0]
              splitStringLen = len(splitString)
              if (splitStringLen == 1 and stringLength > 1):
                return allCharactersSame(checkString, splitString) 
              else:
                  if(checkString.startswith(splitString)):
                      splitSecond = checkString.split(splitString)[1]
                      if (splitSecond == ''):
                          return True
                      else:
                          return allCharactersSame(splitSecond,splitSecond[0])
            else:
                return False
                

print("aab,cc,dd".split("aab,cc"))

print(isSatisfiedRegularExpression("aabbbbbc", "aab*"))