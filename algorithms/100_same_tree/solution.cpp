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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if( p == NULL && q == NULL )
            return true;
        else if( p == NULL || q == NULL )
            return false;
        else if( p->val != q->val )
            return false;
        else
            return isSameTree( p->left, q->left ) && isSameTree( p->right, q->right );
    }
};

/*
 54 / 54 test cases passed.
 Status: Accepted
 Runtime: 0 ms
 You are here!
 Your runtime beats 27.96% of cpp submissions.
*/