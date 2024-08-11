class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def is_empty(root):
    return root is None

def is_leaf(node):
    return node.left is None and node.right is None

def is_parent(node, child):
    if node is None:
        return False
    return node.left == child or node.right == child

def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)

        return max(left_height, right_height) + 1

def count_nodes(root):
    if root is None:
        return 0
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)

def preorder_traversal(root, result=[]):
    if root:
        result.append(root.val)
        preorder_traversal(root.left, result)
        preorder_traversal(root.right, result)
    return result

def inorder_traversal(root, result=[]):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)
    return result

def postorder_traversal(root, result=[]):
    if root:
        postorder_traversal(root.left, result)
        postorder_traversal(root.right, result)
        result.append(root.val)
    return result

def count_leaves(root):
    if root is None:
        return 0
    elif is_leaf(root):
        return 1
    else:
        return count_leaves(root.left) + count_leaves(root.right)

def count_internal_nodes(root):
    if root is None or is_leaf(root):
        return 0
    else:
        return 1 + count_internal_nodes(root.left) + count_internal_nodes(root.right)

def max_min_sum_avg(root):
    if root is None:
        return None, None, 0, 0
    
    max_val = root.val
    min_val = root.val
    sum_val = root.val
    count = 1

    if root.left:
        left_max, left_min, left_sum, left_count = max_min_sum_avg(root.left)
        max_val = max(max_val, left_max)
        min_val = min(min_val, left_min)
        sum_val += left_sum
        count += left_count

    if root.right:
        right_max, right_min, right_sum, right_count = max_min_sum_avg(root.right)
        max_val = max(max_val, right_max)
        min_val = min(min_val, right_min)
        sum_val += right_sum
        count += right_count

    avg_val = sum_val / count

    return max_val, min_val, sum_val, avg_val

# Hàm main để kiểm tra các chương trình con
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("1. Kiểm tra cây rỗng:", is_empty(root))
    print("2. Kiểm tra nút 5 có phải là nút lá không:", is_leaf(root.left.right))
    print("3. Kiểm tra nút 3 có phải là nút cha của nút 7 không:", is_parent(root.right, root.right.right))
    print("4. Chiều cao của cây:", height(root))
    print("5. Số nút của cây:", count_nodes(root))
    print("6. Duyệt tiền tự:", preorder_traversal(root))
    print("   Duyệt trung tự:", inorder_traversal(root))
    print("   Duyệt hậu tự:", postorder_traversal(root))
    print("7. Số nút lá của cây:", count_leaves(root))
    print("8. Số nút trung gian của cây:", count_internal_nodes(root))
    max_val, min_val, sum_val, avg_val = max_min_sum_avg(root)
    print("9. Nút có giá trị lớn nhất:", max_val)
    print("   Nút có giá trị nhỏ nhất:", min_val)
    print("   Tổng giá trị các nút:", sum_val)
    print("   Trung bình giá trị các nút:", avg_val)
