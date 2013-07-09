__author__ = 'saimanoj'


class TreeNode(object):
    """Class that holds every Node of the Tree.

    Attributes:
        data: contains data of this node, of any type.
        parent: TreeNode object corresponding to parent of this node.
        children: List of all TreeNode objects that are children of this node.
        height: height of this node from root.
    """

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []
        self.height = -1


class RootNode(TreeNode):
    """Extends TreeNode and represents Root Node of the Tree.

    Attributes:
        data, parent and children are same as TreeNode.
        parent is always None for a RootNode.
    """

    def __init__(self, data):
        TreeNode.__init__(self, data, None)
        self.height = 0


class Tree(object):
    """Represents a Tree using TreeNode and RootNode classes.
        Root Node is always present in our Tree. It is never removed. Though
         its value can be changed.

    Attributes:
        root: RootNode object representing root of the tree.
        node_count: Total no. of nodes currently in the tree.
        height_tree: Height of the whole tree, i.e. max height of all nodes.
    """

    def __init__(self, data):
        self.root = RootNode(data)
        self.node_count = 1
        self.tree_height = 0

    def add(self, parent, child):
        child.parent = parent
        parent.children.append(child)
        self.node_count += 1
        child.height = parent.height + 1
        assert self.tree_height >= child.height - 1
        if child.height > self.tree_height:
            self.tree_height = child.height
        assert self.tree_height >= child.height

    def remove(self, node):
        """
            Removes only leaf nodes. Checks whether node is root or node,
            because some times root node may not have any children but
            removing it is not valid.
        """

        if node.children:
            return
        if not node.parent or isinstance(node, RootNode):
            return
        assert node in node.parent.children
        node.parent.children.remove(node)
        if node.height == self.tree_height:
            nodes = self.get_all_nodes()
            change_required = True
            for x in nodes:
                assert x.height <= self.tree_height
                if x.height == self.tree_height:
                    change_required = False
                    break
            if change_required:
                self.tree_height -= 1
        self.node_count -= 1
        del node

    def get_all_nodes(self):
        nodes = [self.root]
        for node in nodes:
            if node.children:
                nodes.extend(node.children)

        return nodes

