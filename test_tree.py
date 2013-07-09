__author__ = 'saimanoj'

import unittest
import ds.tree


class TreeTests(unittest.TestCase):

    def test_add_node(self):
        t = ds.tree.Tree('/')
        self.assertEqual(t.root.data,'/')
        node_a = ds.tree.TreeNode('a')
        t.add(t.root, node_a)
        node_b = ds.tree.TreeNode('b')
        t.add(t.root, node_b)
        node_c = ds.tree.TreeNode('c')
        t.add(t.root, node_c)
        node_d = ds.tree.TreeNode('d')
        t.add(node_c, node_d)

        # t.remove(node_d)
        nodes = t.get_all_nodes()
        for node in nodes:
            print node.data

        self.assertEqual(True, True)

