import unittest
from Jewelry import Product
from ListColection import LstCollection
from memento import *
import os

class TestJewelry(unittest.TestCase):

    Product_A = Product(**{
        "title": "jewelry",
        "code": "40640123",
        "material": "gold",
        "type": "bracelets",
        "date_of_creation": "2002-12-06",
        "price": "201",
        "u_id": "123"
    })

    Product_B = Product(**{
        "title": "jjewelry",
        "code": "12345678",
        "material": "silver",
        "type": "rings",
        "date_of_creation": "2010-05-26",
        "price": "2",
        "u_id": "14"
    })

    Product_C = Product(**{
        "title": "jjjewelry",
        "code": "50607080",
        "material": "gold",
        "type": "rings",
        "date_of_creation": "2012-06-15",
        "price": "102",
        "u_id": "53"
    })

    Product_D = Product(**{
        "title": "jjjjewelry",
        "code": "40643050",
        "material": "platinum",
        "type": "earrings",
        "date_of_creation": "2002-10-16",
        "price": "15",
        "u_id": "3"
    })

    def setUp(self):
        self.test_empty_lst = LstCollection()
        self.data = [TestJewelry.Product_A, TestJewelry.Product_B, TestJewelry.Product_C,
                     TestJewelry.Product_D]
        self.test_lst = LstCollection(*self.data)
        self.caretaker = Jewerly(self.test_lst)
        self.caretaker.backup("Current collection.")

    def testAdd(self):
        self.test_empty_lst.append(TestJewelry.Product_A)
        self.assertListEqual([i for i in self.test_empty_lst], [TestJewelry.Product_A],
                             "Add method works improperly")
        self.test_empty_lst.append(TestJewelry.Product_B)
        self.assertListEqual([i for i in self.test_empty_lst], [TestJewelry.Product_A,
                                                                TestJewelry.Product_B],
                             "Add method works improperly")
        self.test_empty_lst.append(TestJewelry.Product_A)
        self.assertNotEqual([i for i in self.test_empty_lst],
                            [TestJewelry.Product_A, TestJewelry.Product_B],
                            "Add method works improperly")

    def test_sort(self):
        object_atters = [name for name in dir(TestJewelry.Product_D) if not name.startswith('__')
                    and not name.startswith('_') and name != "input_product"]
        for field in object_atters:
            self.data = sorted(self.data, key=lambda product: str(getattr(product, field)).lower())
            self.test_lst.sort(field)
            self.assertListEqual([i for i in self.test_lst], self.data, "Sort method works improperly")

        self.assertRaises(AttributeError, self.test_lst.sort, "impossible")

    def test_search(self):
        found1 = self.test_lst.search('2010')
        found2 = self.test_lst.search('jewelry')
        found3 = self.test_lst.search('jj')

        self.assertEqual(found1, [TestJewelry.Product_B],
                             "Search method works improperly")
        self.assertEqual(found2,  [TestJewelry.Product_A, TestJewelry.Product_C, TestJewelry.Product_D], "Search method works improperly")
        self.assertEqual(found3, [TestJewelry.Product_C, TestJewelry.Product_D], "Search method works improperly")

    def test_delete(self):
        id1, id2, id3 = "3", "53", "14"
        self.test_lst.delete(id1)
        self.assertListEqual([i for i in self.test_lst], [TestJewelry.Product_A, TestJewelry.Product_B,
                                                          TestJewelry.Product_C],
                             "Delete method works improperly")

        self.test_lst.delete(id2)
        self.assertListEqual([i for i in self.test_lst], [TestJewelry.Product_A, TestJewelry.Product_B],
                             "Delete method works improperly")

        self.test_lst.delete(id3)
        self.assertNotEqual([i for i in self.test_lst], [TestJewelry.Product_A, TestJewelry.Product_C],
                            "Delete method works improperly")


    def test_edit(self):
        to_edit1 = ("3", "material", "platinum")
        to_edit2 = ("3", "type", "rings")
        to_edit3 = ("123", "price", "50")
        to_edit4 = ("14", "title", "else")

        self.test_lst.edit(*to_edit1)
        self.assertEqual(getattr(TestJewelry.Product_D, to_edit1[1]), to_edit1[2], "Edit method works improperly")
        self.test_lst.edit(*to_edit2)
        self.assertEqual(getattr(TestJewelry.Product_D, to_edit2[1]), to_edit2[2], "Edit method works improperly")
        self.test_lst.edit(*to_edit3)
        self.assertEqual(getattr(TestJewelry.Product_A, to_edit3[1]), to_edit3[2], "Edit method works improperly")
        self.test_lst.edit(*to_edit4)
        self.assertEqual(getattr(TestJewelry.Product_B, to_edit4[1]), to_edit4[2], "Edit method works improperly")


    def testUndo(self):
        self.assertRaises(AttributeError, self.caretaker.undo)
        self.test_lst.append(self.test_lst[0])
        self.caretaker.backup("Add new element.")

        self.caretaker.undo()
        self.assertListEqual([str(i) for i in self.test_lst], [str(i) for i in self.data],
                             "Undo method works improperly")

    def testRedo(self):
        self.assertRaises(AttributeError, self.caretaker.redo)
        self.test_lst.append(self.test_lst[0])
        self.data.append(self.test_lst[0])
        self.caretaker.backup("Add new element.")

        self.caretaker.undo()
        self.caretaker.redo()
        self.assertListEqual([str(i) for i in self.test_lst], [str(i) for i in self.data],
                             "Redo method works improperly")

    def testMove(self):
        self.assertRaises(AttributeError, self.caretaker.move_on_moment, 4)
        self.test_lst.append(self.test_lst[0])
        self.caretaker.backup("Add new element.")

        self.caretaker.move_on_moment(1)
        self.assertListEqual([str(i) for i in self.test_lst], [str(i) for i in self.data],
                             "Undo method works improperly")

    def test_read_json_file(self):
        self.assertRaises(ValueError, self.test_lst.read_json_file, "wrong_file_name")

        self.test_empty_lst.read_json_file("data.json")
        self.assertEqual(len(self.test_empty_lst), 3, "Read_json_file method works improperly")

        self.test_empty_lst.read_json_file("data.json")
        self.assertNotEqual(len(self.test_empty_lst), 3, "Read_json_file method works improperly")

        self.test_empty_lst.lst.clear()

    def test_write_json_file(self):
        self.assertRaises(ValueError, self.test_lst.read_json_file, "wrong_file_name")

        self.test_lst.write_in_json_file('test.json')
        self.test_empty_lst.read_json_file('test.json')
        self.assertEqual(len(self.test_empty_lst), 4)

        os.remove("test.json")


if __name__ == '__main__':
    unittest.main()
