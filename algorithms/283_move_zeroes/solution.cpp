class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0, j = 0, k = 0;
        for(i = 0; i < nums.size(); i++)
        {
            if (nums[i] != 0)
                continue;
            for(j = i+1; j < nums.size(); j++)
            {
                if (nums[j] == 0)
                    continue;
                //swap nums[i] nums[j]
                nums[i] = nums[j];
                nums[j] = 0;
                break;
            }
        }
    }
};

/*
 Status: Accepted
 Runtime: 68 ms
 Submitted: 1 year ago
 You are here!
 Your runtime beats 6.06% of cpp submissions.
*/