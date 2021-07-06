import unittest

target = __import__("remove_duplicates_from_linked_list")

class TestRemoveDuplicatesFromLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = target.Linked_list()
        self.list.head = target.Node(12)

        n1 = target.Node(12)
        n2 = target.Node(11)
        n3 = target.Node(11)
        n4 = target.Node(12)
        self.list.head.next = n1
        n1.next = n2
        n2.next = n3
        n3.next = n4       

    def test_case(self):
        self.list.remove_duplicates()
        result_list = target.Linked_list()
        result_list.head = target.Node(12)
        n1 = target.Node(11)
        result_list.head.next = n1
        result = target.compare_lists(self.list, result_list)
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()