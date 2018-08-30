// 算法描述
// 只需计算有多少个排列在当前排列A的前面即可。如何算呢?举个例子，[3,7,4,9,1]，在它前面的必然是某位置i对应元素比原数组小，而i左侧和原数组一样。也即[3,7,4,1,X]，[3,7,1,X,X]，[3,1或4,X,X,X]，[1,X,X,X,X]。
// 而第i个元素，比原数组小的情况有多少种，其实就是A[i]右侧有多少元素比A[i]小，乘上A[i]右侧元素全排列数，即A[i]右侧元素数量的阶乘。i从右往左看，比当前A[i]小的右侧元素数量分别为1,1,2,1，所以最终字典序在当前A之前的数量为1×1!+1×2!+2×3!+1×4!=39，故当前A的字典序为40。

// 具体步骤：

// 用permutation表示当前阶乘，初始化为1,result表示最终结果，初始化为0。由于最终结果可能巨大，所以用long类型。
// i从右往左遍历A，循环中计算A[i]右侧有多少元素比A[i]小，计为smaller，result += smaller * permutation。之后permutation *= A.length - i，为下次循环i左移一位后的排列数。
// 已算出多少字典序在A之前，返回result+1。

public class Solution {
    /**
     * @param A: An array of integers
     * @return: A long integer
     */
    public long permutationIndex(int[] A) {
        // write your code here
        long permutation = 1;
        long result = 0;
        for (int i = A.length - 2; i >= 0; --i) {
            int smaller = 0;
            for (int j = i + 1; j < A.length; ++j) {
                if (A[j] < A[i]) {
                    smaller++;
                }
            }
            result += smaller * permutation;
            permutation *= A.length - i;
        }
        return result + 1;
    }
}