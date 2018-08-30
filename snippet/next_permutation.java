// 算法描述
// 如果上来想不出方法，可以试着找找规律，我们关注的重点应是原数组末尾。

// 从末尾往左走，如果一直递增，例如...9,7,5，那么下一个排列一定会牵扯到左边更多的数，直到一个非递增数为止，例如...6,9,7,5。对于原数组的变化就只到6这里，和左侧其他数再无关系。6这个位置会变成6右侧所有数中比6大的最小的数，而6会进入最后3个数中，且后3个数必是升序数组。

// 所以算法步骤如下：

// 从右往左遍历数组nums，直到找到一个位置i，满足nums[i] > nums[i - 1]或者i为0。
// i不为0时，用j再次从右到左遍历nums，寻找第一个nums[j] > nums[i - 1]。而后交换nums[j]和nums[i - 1]。注意，满足要求的j一定存在！且交换后nums[i]及右侧数组仍为降序数组。
// 将nums[i]及右侧的数组翻转，使其升序。

public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers that's next permuation
    */
    // 用于交换nums[i]和nums[j]
    public void swapItem(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    // 用于翻转nums[i]到nums[j]，包含两端的这一小段数组
    public void swapList(int[] nums, int i, int j) {
        while (i < j) {
            swapItem(nums, i, j);
            i ++; 
            j --;
        }
    }
    public void nextPermutation(int[] nums) {
        int len = nums.length;
        if ( len <= 1) {
            return;
        }
        int i = len - 1;
        while (i > 0 && nums[i] <= nums[i - 1]) {
            i --;
        }
        if (i != 0) {
            int j = len - 1;
            while (nums[j] <= nums[i - 1]) {
                j--;
            }
            swapItem(nums, j, i-1);
        }
        swapList(nums, i, len - 1);
    }
}