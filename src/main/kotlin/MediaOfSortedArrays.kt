import java.util.*

fun main() {
    print(MediaOfSortedArrays().findMedianSortedArrays(intArrayOf(2), intArrayOf()))
}

class MediaOfSortedArrays {
    // This take time and space; doesn't satisfy olog(n+m)
    fun findMedianSortedArrays(nums1: IntArray, nums2: IntArray): Double {
        var arrayList = nums1.toMutableList()
        arrayList.addAll(nums2.toMutableList())
        arrayList.sort()
        val length = arrayList.size
        var median = 0
        if (length % 2 == 1) {
            median = (length / 2)
            return arrayList.get(median).toDouble()
        } else {
            val median = length / 2
            return ((arrayList.get(median).toDouble() + arrayList.get(median - 1).toDouble()) / 2.0)
        }
    }
}