//用 Morris 算法实现 O(1) 额外空间遍历二叉树

// 节点定义
class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    pubic TreeNode(int val) {
        this.val = val;
        this.left = this.right = null;
    }
}

// 用 Morris 算法进行中序遍历(Inorder Traversal)
// 1. 如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。
// 2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
//     1. 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。
//     2. 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空（恢复树的形状）。输出当前节点。当前节点更新为当前节点的右孩子。
// 3. 重复1、2两步直到当前节点为空。

public class Solution {
    /**
     * @param root: A Tree
     * @return: Inorder in ArrayList which contains node values.
     */

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> nums = new ArrayList<>();
        TreeNode cur = null;

        while (root != null) {
            if (root.left != null) {
                cur = root.left;
                while (cur.right != null && cur.right != root) {
                    cur = cur.right;
                }

                if (cur.right == root) {
                    nums.add(root.val);
                    cur.right = null;
                    root = root.right;
                } else {
                    cur.right = root;
                    root = root.left;
                }               
            } else {
                nums.add(root.val);
                root = root.right;
            }
        }

        return nums;
    } 

}

// 用 Morris 算法实现先序遍历(Preorder Traversal)
// 1. 如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。
// 2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
//     1. 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。**输出当前节点**（与中序遍历唯一一点不同）。当前节点更新为当前节点的左孩子。
//     2. 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空。当前节点更新为当前节点的右孩子。
// 3. 重复1、2两步直到当前节点为空。

public class Solution {
    /**
     * @param root: A Tree
     * @return: Preorder in ArrayList which contains node values.
     */
    public List<Integer> preorderTraversal(TreeNode root) {
        // morris traversal
        List<Integer> nums = new ArrayList<>();
        TreeNode cur = null;
        while (root != null) {
            if (root.left != null) {
                cur = root.left;
                // find the predecessor of root node
                while (cur.right != null && cur.right != root) {
                    cur = cur.right;
                }
                if (cur.right == root) {
                    cur.right = null;
                    root = root.right;
                } else {
                    nums.add(root.val);
                    cur.right = root;
                    root = root.left;
                }
            } else {
                nums.add(root.val);   
                root = root.right;
            }
        }
        return nums;
    } 
}

// 用 Morris 算法实现后序遍历(Postorder Traversal)
// * 后序遍历其实可以看作是和前序遍历左右对称的，此处，我们同样可以利用这个性质，基于前序遍历的算法，可以很快得到后序遍历的结果。我们只需要将前序遍历中所有的左孩子和右孩子进行交换就可以了。

public class Solution {
    /**
     * @param root: A Tree
     * @return: Postorder in ArrayList which contains node values.
     */
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> nums = new ArrayList<>();
        TreeNode cur = null;
        while (root != null) {
            if (root.right != null) {
                cur = root.right;
                while (cur.left != null && cur.left != root) {
                    cur = cur.left;
                }
                if (cur.left == root) {
                    cur.left = null;
                    root = root.left;
                } else {
                    nums.add(root.val);
                    cur.left = root;
                    root = root.right;
                }
            } else {
                nums.add(root.val);
                root = root.left;
            }
        }
        Collections.reverse(nums);
        return nums;
    } 
}