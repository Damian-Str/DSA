/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// Recursive

 /*
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> output = new ArrayList<Integer>();
        inOrder(root, output);
        return output;
    }

    private void inOrder(TreeNode node, List<Integer> output) {
        if(node == null) return;

        inOrder(node.left, output);
        output.add(node.val);
        inOrder(node.right, output);
    }
}*/

// Iterative

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> output = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();

        TreeNode current = root;

        while(current != null || !stack.isEmpty() ) {
            while(current != null) {
                stack.push(current);
                current = current.left;
            }

            current = stack.pop();
            output.add(current.val);
            
            current = current.right;
        }
        return output;
    }
}