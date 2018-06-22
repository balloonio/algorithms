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
    TreeNode* sortedArrayToBST(vector<int>& nums) {

        if( nums.empty() )
            return NULL;

        
        int mid = nums.size()/2;
        TreeNode * n = new TreeNode( nums[mid] );
        if( mid == 0 )
        {
            n->left = NULL;
        }
        else
        {
            vector<int> v( nums.begin(), nums.begin()+ mid );
            n->left = sortedArrayToBST( v );
        }

        if( mid == nums.size()-1 )
        {
            n->right = NULL;
        }        
        else
        {
            vector<int> v( nums.begin()+mid+1, nums.end() );
            n->right = sortedArrayToBST( v );
        }
        return n;
    }
};