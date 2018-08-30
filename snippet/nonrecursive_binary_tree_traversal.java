// 先序遍历
// 思路
// 遍历顺序为根、左、右

// 如果根节点非空，将根节点加入到栈中。
// 如果栈不空，弹出出栈顶节点，将其值加加入到数组中。
// 如果该节点的右子树不为空，将右子节点加入栈中。
// 如果左子节点不为空，将左子节点加入栈中。
// 重复第二步，直到栈空。

public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<Integer> preorder = new ArrayList<Integer>();
        
        if (root == null) {
            return preorder;
        }
        
        stack.push(root);
        while (!stack.empty()) {
            TreeNode node = stack.pop();
            preorder.add(node.val);
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.left != null) {
                stack.push(node.left);
            }
        }
        
        return preorder;
    }
}

// 中序遍历
// 思路
// 遍历顺序为左、根、右

// 如果根节点非空，将根节点加入到栈中。
// 如果栈不空，取栈顶元素（暂时不弹出），
// 如果左子树已访问过，或者左子树为空，则弹出栈顶节点，将其值加入数组，如有右子树，将右子节点加入栈中。
// 如果左子树不为空，则将左子节点加入栈中。
// 重复第二步，直到栈空。

public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: Inorder in ArrayList which contains node values.
     */
    public ArrayList<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        ArrayList<Integer> result = new ArrayList<>();
        
        while (root != null) {
            stack.push(root);
            root = root.left;
        }
    
        while (!stack.isEmpty()) {
            TreeNode node = stack.peek();
            result.add(node.val);
            
            if (node.right == null) {
                node = stack.pop();
                while (!stack.isEmpty() && stack.peek().right == node) {
                    node = stack.pop();
                }
            } else {
                node = node.right;
                while (node != null) {
                    stack.push(node);
                    node = node.left;
                }
            }
        }
        return result;
    }
}

// 后序遍历
// 思路
// 遍历顺序为左、右、根

// 如果根节点非空，将根节点加入到栈中。
// 如果栈不空，取栈顶元素（暂时不弹出），
// 如果（左子树已访问过或者左子树为空），且（右子树已访问过或右子树为空），则弹出栈顶节点，将其值加入数组，
// 如果左子树不为空，切未访问过，则将左子节点加入栈中，并标左子树已访问过。
// 如果右子树不为空，切未访问过，则将右子节点加入栈中，并标右子树已访问过。
// 重复第二步，直到栈空。

public ArrayList<Integer> postorderTraversal(TreeNode root) {
    ArrayList<Integer> result = new ArrayList<Integer>();
    Stack<TreeNode> stack = new Stack<TreeNode>();
    TreeNode prev = null; // previously traversed node
    TreeNode curr = root;

    if (root == null) {
        return result;
    }

    stack.push(root);
    while (!stack.empty()) {
        curr = stack.peek();
        if (prev == null || prev.left == curr || prev.right == curr) { // traverse down the tree
            if (curr.left != null) {
                stack.push(curr.left);
            } else if (curr.right != null) {
                stack.push(curr.right);
            }
        } else if (curr.left == prev) { // traverse up the tree from the left
            if (curr.right != null) {
                stack.push(curr.right);
            }
        } else { // traverse up the tree from the right
            result.add(curr.val);
            stack.pop();
        }
        prev = curr;
    }

    return result;
}