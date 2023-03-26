class Node:
    def __init__(self, value=[]):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, value=None) -> None:
        self.root = Node(value)

    def __is_empty(self):
        return self.root == None

    def __insert_node(self, node: Node, value: int) -> None:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.__insert_node(node.left, value)
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.__insert_node(node.right, value)

    def __inorder(self, node: None) -> None:
        if node is not None:
            self.__inorder(node.left)
            print(node.value, end=", ")
            self.__inorder(node.right)

    def __preorder(self, node: Node) -> None:
        if node is not None:
            print(node.value, end=", ")
            self.__preorder(node.left)
            self.__preorder(node.right)

    def __postorder(self, node: Node) -> None:
        if node is not None:
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(node.value, end=", ")

    def __search(self, node: Node, target: int) -> int:
        if node is None:
            return None
        if node.value == target:
            return node
        if target < node.value:
            return self.__search(node.left, target)
        else:
            return self.__search(node.right, target)

    # Public methods

    def add_node(self, node: Node, values: list) -> None:
        for value in values:
            self.__insert_node(node, value)

    def inorder(self):
        print("\nPrinting the tree inorder: ")
        self.__inorder(self.root)
        print("")

    def preorder(self):
        print("\nPrinting the tree preorder: ")
        self.__preorder(self.root)
        print("")

    def postorder(self):
        print("\nPrinting the tree postorder: ")
        self.__postorder(self.root)
        print("")

    def search(self, target: int) -> int:
        result = self.__search(self.root, target)
        if result.value:
            print(f'Found the node with value {result.value} in the Tree')
        else:
            print(f'Node not found with that value {target}.')

    def deepest_level(self, root: Node) -> int:
        if not root:
            return 0
        return max(self.deepest_level(root.left), self.deepest_level(root.right)) + 1

    def deepest_node(self, root: Node, max_level, result=[]) -> list:
        if not root:
            return []

        if max_level == 1:
            result.append(root.value)
        elif max_level > 1:
            self.deepest_node(root.left, max_level - 1)
            self.deepest_node(root.right, max_level - 1)

        return result
