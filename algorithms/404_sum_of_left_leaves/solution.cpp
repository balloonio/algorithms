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
    int sumOfLeftLeaves(TreeNode* root) {
        return sumLeft( root, false );
    }
    
    int sumLeft( TreeNode* root, bool isLeft )
    {
        if( root == NULL )
            return 0;
        if( !isParent(root) )
            return isLeft?root->val:0;
        return sumLeft( root->left, true ) + sumLeft( root->right, false );
    }
    
    bool isParent( TreeNode* root )
    {
        if( root == NULL )
            return false;
        return (root->left != NULL) || (root->right != NULL);
    }
};