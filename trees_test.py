#/usr/bin/python3
# encoding: utf-8
import unittest
import trees
import dbutils

class TreeTest(unittest.TestCase):

    def testAdd0(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        self.__ae('R', tree, 1, 2)

    def testAdd1(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')

        self.__ae('R', tree, 1, 4)
        self.__ae('A', tree, 2, 3)

    def testAdd2(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')
        tree.add('A', 'A1')

        self.__ae('R', tree, 1, 6)
        self.__ae('A', tree, 2, 5)
        self.__ae('A1', tree, 3, 4)

    def testAdd3(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')
        tree.add('A', 'A1')

        self.__ae('R', tree, 1, 6)
        self.__ae('A', tree, 2, 5)
        self.__ae('A1', tree, 3, 4)

    def testAdd4(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')
        tree.add('A', 'A1')
        tree.add('A', 'A2')

        self.__ae('R', tree, 1, 8)
        self.__ae('A', tree, 2, 7)
        self.__ae('A1', tree, 3, 4)
        self.__ae('A2', tree, 5, 6)

    def testAdd5(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')
        tree.add('A', 'A1')
        tree.add('A', 'A2')
        tree.add('R', 'B')

        self.__ae('R', tree, 1, 10)
        self.__ae('A', tree, 2, 7)
        self.__ae('A1', tree, 3, 4)
        self.__ae('A2', tree, 5, 6)
        self.__ae('B', tree, 8, 9)

    def testAdd6(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')
        tree.add('A', 'A1')
        tree.add('A', 'A2')
        tree.add('R', 'B')
        tree.add('B', 'B1')

        self.__ae('R', tree, 1, 12)
        self.__ae('A', tree, 2, 7)
        self.__ae('A1', tree, 3, 4)
        self.__ae('A2', tree, 5, 6)
        self.__ae('B', tree, 8, 11)
        self.__ae('B1', tree, 9, 10)

    def testAdd7(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')
        tree.add('A', 'A1')
        tree.add('A', 'A2')
        tree.add('R', 'B')
        tree.add('B', 'B1')
        tree.add('B', 'B2')

        self.__ae('R', tree, 1, 14)
        self.__ae('A', tree, 2, 7)
        self.__ae('A1', tree, 3, 4)
        self.__ae('A2', tree, 5, 6)
        self.__ae('B', tree, 8, 13)
        self.__ae('B1', tree, 9, 10)
        self.__ae('B2', tree, 11, 12)

    def testAdd8(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')
        tree.add('A', 'A1')
        tree.add('A', 'A2')
        tree.add('R', 'B')
        tree.add('B', 'B1')
        tree.add('B', 'B2')
        tree.add('A', 'A3')

        self.__ae('R', tree, 1, 16)
        self.__ae('A', tree, 2, 9)
        self.__ae('A1', tree, 3, 4)
        self.__ae('A2', tree, 5, 6)
        self.__ae('B', tree, 10, 15)
        self.__ae('B1', tree, 11, 12)
        self.__ae('B2', tree, 13, 14)
        self.__ae('A3', tree, 7, 8)

    def testAdd9(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')
        tree.add('A', 'A1')
        tree.add('A', 'A2')
        tree.add('R', 'B')
        tree.add('B', 'B1')
        tree.add('B', 'B2')
        tree.add('A', 'A3')

        self.__ae('R', tree, 1, 16)
        self.__ae('A', tree, 2, 9)
        self.__ae('A1', tree, 3, 4)
        self.__ae('A2', tree, 5, 6)
        self.__ae('B', tree, 10, 15)
        self.__ae('B1', tree, 11, 12)
        self.__ae('B2', tree, 13, 14)
        self.__ae('A3', tree, 7, 8)

    def testAdd10(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')
        tree.add('A', 'A1')
        tree.add('A', 'A2')
        tree.add('R', 'B')
        tree.add('B', 'B1')
        tree.add('B', 'B2')
        tree.add('A', 'A3')
        tree.add('A2', 'A21')

        self.__ae('R', tree, 1, 18)
        self.__ae('A', tree, 2, 11)
        self.__ae('A1', tree, 3, 4)
        self.__ae('A2', tree, 5, 8)
        self.__ae('B', tree, 12, 17)
        self.__ae('B1', tree, 13, 14)
        self.__ae('B2', tree, 15, 16)
        self.__ae('A3', tree, 9, 10)
        self.__ae('A21', tree, 6, 7)

    def testAdd11(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')
        tree.add(None, 'C')

        self.__ae('R', tree, 1, 4)
        self.__ae('A', tree, 2, 3)
        self.__ae('C', tree, 5, 6)

    def testRemove0(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')
        tree.remove('A')

        self.__ae('R', tree, 1, 2)

    def testRemove1(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')
        tree.add('A', 'A1')
        tree.add('A', 'A2')
        tree.remove('A1')

        self.__ae('R', tree, 1, 6)
        self.__ae('A', tree, 2, 5)
        self.__ae('A2', tree, 3, 4)

    def testRemove2(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')
        tree.add('A', 'A1')
        tree.add('A', 'A2')
        tree.add('R', 'B')
        tree.add('B', 'B1')
        tree.add('B', 'B2')
        tree.remove('A1')

        self.__ae('R', tree, 1, 12)
        self.__ae('A', tree, 2, 5)
        self.__ae('A2', tree, 3, 4)
        self.__ae('B', tree, 6, 11)
        self.__ae('B1', tree, 7, 8)
        self.__ae('B2', tree, 9, 10)

    def testRemove3(self):
        tree = trees.Trees()
        tree.add(None, 'R')
        tree.add('R', 'A')
        tree.add('A', 'A1')
        tree.add('A', 'A2')
        tree.add('R', 'B')
        tree.add('B', 'B1')
        tree.add('B', 'B2')
        tree.remove('A')

        self.__ae('R', tree, 1, 12)
        self.__ae('A1', tree, 2, 3)
        self.__ae('A2', tree, 4, 5)
        self.__ae('B', tree, 6, 11)
        self.__ae('B1', tree, 7, 8)
        self.__ae('B2', tree, 9, 10)


    def __ae(self, name, tree, lft, rght):
        p = tree.get_by_name(name)

        self.assertEqual(lft, p['lft'])
        self.assertEqual(rght, p['rght'])

    def tearDown(self):
        db = dbutils.DBUtils()
        data = db.save('truncate trees', None)
        db.close()

if __name__ == '__main__':
    unittest.main()
