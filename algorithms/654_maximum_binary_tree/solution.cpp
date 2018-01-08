/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        if( nums.size() == 0)
            return NULL;
        int maxIndex = findMaxIndex( nums );
        vector<int> numsBefore( nums.begin()+0, nums.begin()+maxIndex );
        vector<int> numsAfter( nums.begin()+maxIndex+1, nums.begin()+nums.size());
        TreeNode * np = new TreeNode( nums[maxIndex] );
        np->left = constructMaximumBinaryTree( numsBefore );
        np->right = constructMaximumBinaryTree( numsAfter );
        return np;
    }
    
    int findMaxIndex( vector<int>& nums )
    {
        int currMax = nums[0];
        int currMaxIndex = 0;
        for( int i = 0; i < nums.size(); ++i )
        {
            if( nums[i] > currMax )
                currMaxIndex = i;
        }
        return currMaxIndex;
    }
};