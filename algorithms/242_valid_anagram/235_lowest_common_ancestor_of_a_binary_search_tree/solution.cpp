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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        bool foundP = false;
        bool foundQ = false;
        return findComm(root, p, q, &foundP, &foundQ);
    }
private:
    TreeNode* findComm(TreeNode* root, TreeNode* p, TreeNode* q, bool* foundP, bool* foundQ)
    {
        if(root == NULL)
            return NULL;
        
        bool tempP = *foundP;
        bool tempQ = *foundQ;
        bool dummyF = false;
        TreeNode* r = findComm(root->left, p, q, foundP, foundQ);
        //returned LCA, then pass along back to top level
        if(r != NULL)
            return r;
        
        if(tempP != *foundP)
        {
            //P found in left branch, then dont let right branch know P is found
            r = findComm(root->right, p, q, &dummyF, foundQ);
        }
        else if(tempQ != *foundQ)
        {
            //Q found in left branch, then dont let right branch know Q is found
            r = findComm(root->right, p, q, foundP, &dummyF);
        }
        else
        {
            //neither Q nor P was found yet, pass along
            r = findComm(root->right, p, q, foundP, foundQ);
        }
        //returned LCA, then pass along back to top level
        if(r != NULL)
            return r;
        
        if(root == p)
            *foundP = true;
        if(root == q)
            *foundQ = true;
        
        //under current root, if both P and Q already found, this is LCA
        if(*foundQ && *foundP)
            return root;
        return NULL;
    }
};

/*
 Status: Accepted
 Runtime: 44 ms
 Submitted: 1 year ago
 You are here!
 Your runtime beats 29.04% of cpp submissions.
*/