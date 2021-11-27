fun main() {
    println(LargestPalindromeSubString().longestPalindrome("bacabab"))
}

class LargestPalindromeSubString {

    fun longestPalindrome(s: String): String {

        var stringLength = s.length

        if (stringLength == 1) {
            return s.get(0).toString()
        } else if (stringLength == 2) {
            val charAtFirst = s.get(0).toString()
            if (charAtFirst.equals(s.get(1).toString())) {
                return charAtFirst + charAtFirst
            }
            return charAtFirst
        } else if (checkAllSame(s) || s.reversed().equals(s)) {
            return s
        } else {
            return theLargestSubstring(s)
        }
    }

    fun theLargestSubstring(s: String): String {
        var i = 0
        val length = s.length
        var palindromeSubString = ""
        var largestLength = 0
        while (i < length) {
            val ch = s.get(i).toString()  //"aacabdkacaa"
            if (largestLength == 0) {
                palindromeSubString += ch
                largestLength = 1
            }
            if ((i + 1) != length) {
                var splitString = s.substring(i + 1, length)
                val indexOfRepeat = splitString.indexOf(ch)
                if (indexOfRepeat != -1) {
                    splitString = splitString.substring(0, indexOfRepeat + 1)
                    splitString = ch + splitString
                    val reversed = splitString.reversed()
                    if (splitString.equals(reversed)) {
                        if (splitString.length > largestLength) {
                            largestLength = splitString.length
                            palindromeSubString = splitString
                        }
                    }
                }
            }
            i++
        }
        return palindromeSubString
    }

    fun checkAllSame(s: String): Boolean {
        val ch = s.get(0)
        var i = 0
        while (i < s.length) {
            if (!s.get(i).equals(ch)) {
                return false
            }
            i++
        }
        return true
    }
}