class Solution {
public:
    int singleNumber(vector<int>& nums) {
        for(int i = 1; i < nums.size(); ++i)
        {
            nums[0] ^= nums[i];
        }
        return nums[0];
    }
};

/*
 15 / 15 test cases passed.
 Status: Accepted
 Runtime: 16 ms
 You are here!
 Your runtime beats 51.58% of cpp submissions.
*/