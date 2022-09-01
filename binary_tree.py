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

    def __insertNode(self, node: Node, value: int) -> None:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.__insertNode(node.left, value)
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.__insertNode(node.right, value)

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
            self.__insertNode(node, value)

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

    def deepestLevel(self, root: Node) -> int:
        if not root:
            return 0
        return max(self.deepestLevel(root.left), self.deepestLevel(root.right)) + 1

    def deepestNode(self, root: Node, maxLevel, result=[]) -> int:
        if not root:
            return

        if maxLevel == 1:
            result.append(root.value)
        elif maxLevel > 1:
            self.deepestNode(root.left, maxLevel - 1)
            self.deepestNode(root.right, maxLevel - 1)

        return result