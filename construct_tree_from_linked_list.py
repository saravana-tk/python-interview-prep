from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def count_nodes(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count

        def build_bst(start, end):
            nonlocal head
            if start > end:
                return None

            mid = (start + end) // 2

            left = build_bst(start, mid - 1)

            root = TreeNode(head.val)
            root.left = left

            head = head.next

            root.right = build_bst(mid + 1, end)

            return root

        total_nodes = count_nodes(head)
        return build_bst(0, total_nodes - 1)

# ---------- Helper to print BST in level-order ----------
from collections import deque

def print_tree_level_order(root):
    if not root:
        print("[]")
        return
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    # Trim trailing None values for clean output
    while result and result[-1] is None:
        result.pop()
    print(result)

# ---------- Linked list creation ----------
def create_linked_list(arr):
    if not arr:
        return None
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# ---------- Run ----------
if __name__ == "__main__":
    input_list = [-3, 1, 0, 3]
    head = create_linked_list(input_list)

    sol = Solution()
    bst_root = sol.sortedListToBST(head)

    print("BST in level-order:")
    print_tree_level_order(bst_root)