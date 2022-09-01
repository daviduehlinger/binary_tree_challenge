import sys
import binary_tree

if __name__ == '__main__':
    values = []
    print('\nEnter 0 to stop inserting values or <Ctrl+C> to exit.')
    while True:
        try:
            n = int(input('Enter the value of the node that will be inserted in the tree: '))
            if n == 0:
                break
            else:
                values.append(n)
        except ValueError:
            print(f'\nThe value of the node must be an integer.\n')
        except KeyboardInterrupt:
            sys.exit('\nBye !!!')
    try:
        if len(values) > 1:
            bt = binary_tree.Tree(values[0])
            bt.add_node(node=bt.root, values=values[1:])
            bt.preorder()
            bt.inorder()
            bt.postorder()
            deepestLevel = bt.deepestLevel(root=bt.root)
            print(f'\nThe deepest level of the tree is {deepestLevel}')
            print(f'\nThe deepest node have the value {bt.deepestNode(bt.root, deepestLevel)}')
    except:
        sys.exit('\nAn error has occurred.')
