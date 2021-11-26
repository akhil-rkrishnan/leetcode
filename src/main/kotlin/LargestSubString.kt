fun main() {
    val length = LargestSubstring().lengthOfLongestSubstring("")
    println("Output - $length")
}

class LargestSubstring {
    fun lengthOfLongestSubstring(s: String): Int {
        val strLength = s.length
        if (strLength > 0) {
            val isAllSame = checkAllSame(s)
            if (isAllSame) {
                return 1
            } else {
                return largest(s)
            }
        } else {
            return 0
        }

    }

    fun largest(s: String): Int {
        val arrayList = ArrayList<String>()
        var largestValue = 0
        var index = 0
        var strLength = s.length
        while (index < strLength) {
            val valAtposition = s.get(index).toString()
            if (!arrayList.contains(valAtposition)) {
                arrayList.add(valAtposition)
                index++
            } else if (!valAtposition.equals(s.get(index - 1).toString())) {
                index = findTheLatestCharIndex(s, valAtposition, index) + 1
                if (largestValue < arrayList.size) {
                    largestValue = arrayList.size
                }
                arrayList.clear()
            } else {
                if (largestValue < arrayList.size) {
                    largestValue = arrayList.size
                }
                arrayList.clear()
            }
            if (index == strLength) {
                if (largestValue < arrayList.size) {
                    largestValue = arrayList.size
                }
                arrayList.clear()
            }
        }
        return largestValue
    }

    fun findTheLatestCharIndex(s: String, ch: String, currentIndex: Int): Int{
        for ( i in currentIndex-1 downTo 0) {
            if (s.get(i).toString().equals(ch)) {
                return i;
            }
        }
        return currentIndex
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