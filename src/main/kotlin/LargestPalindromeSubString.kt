fun main() {
    println(LargestPalindromeSubString().longestPalindrome("abcabcb"))
    println(LargestPalindromeSubString().longestPalindrome("xaabacxcabaaxcabaax"))
    println(LargestPalindromeSubString().longestPalindrome("babad"))
    println(LargestPalindromeSubString().longestPalindrome("ab"))
    println(LargestPalindromeSubString().longestPalindrome("aaaaaaa"))
    println(LargestPalindromeSubString().longestPalindrome("x"))
}

class LargestPalindromeSubString {
    fun longestPalindromeWithHashMap(s: String): String {
        var largestIndex = 1
        var largestSubstring = s.get(0).toString()
        val hashMap = HashMap<Char, ArrayList<Int>>()
        s.forEachIndexed { index, char ->
            val getList = hashMap.get(char)
            if (getList == null) {
                hashMap.put(char, ArrayList<Int>().apply {
                    add(index)
                })
            } else {
                getList.add(index)
                hashMap.put(char, getList)
            }
        }
        hashMap.forEach { char, arrayList ->
            val listSize = arrayList.size
            if (listSize != 1) {
                for (startIndex in 0..listSize - 1) {
                    for (endIndex in (startIndex + 1)..listSize - 1) {
                        val newStr = s.substring(arrayList.get(startIndex), arrayList.get(endIndex) + 1)
                        if (newStr.reversed().equals(newStr)) {
                            if (newStr.length > largestIndex) {
                                largestIndex = newStr.length
                                largestSubstring = newStr
                            }
                        }
                    }
                }
            }
        }
        return largestSubstring
    }

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
            return longestPalindromeWithHashMap(s)
        }
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