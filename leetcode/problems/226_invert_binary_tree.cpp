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
    TreeNode* invertTree(TreeNode* root) {
        
        if (root == NULL)
            return NULL;
        
        TreeNode *temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        root->left = invertTree(root->left);
        root->right = invertTree(root->right);
        
        return root;
    }
};

/*
 Status: Accepted
 Runtime: 0 ms
 Submitted: 1 year ago
 You are here!
 Your runtime beats 39.74% of cpp submissions.
*/