import unittest

from main import get_list_by_N, print_map, check_all_same_markers_in_row

class TestMain(unittest.TestCase):
    def test_get_list_by_N(self):
        result = get_list_by_N(2)
        expected = [None, None, None, None]
        self.assertEqual(result, expected)

        result = get_list_by_N(3)
        expected = [None] * 9
        self.assertEqual(result, expected)

    def test_print_map(self):
        n = 3
        play_list = [None] * n * n
        result = print_map(n, play_list)
        expected = (
            " 1 | 2 | 3 \n" +
            "-----------\n" +
            " 4 | 5 | 6 \n" +
            "-----------\n" +
            " 7 | 8 | 9 "
        )
        self.assertEqual(result, expected)

        play_list = [
            None, None, None,
            None, True, False,
            None, None, None
        ]
        result = print_map(n, play_list)
        expected = (
            " 1 | 2 | 3 \n" +
            "-----------\n" +
            " 4 | o | x \n" +
            "-----------\n" +
            " 7 | 8 | 9 "
        )
        self.assertEqual(result, expected)
        
        n = 4
        play_list = [None] * n * n
        result = print_map(n, play_list)
        expected = (
            "  1 |  2 |  3 |  4 \n" +
            "-------------------\n" +
            "  5 |  6 |  7 |  8 \n" +
            "-------------------\n" +
            "  9 | 10 | 11 | 12 \n"
            "-------------------\n" +
            " 13 | 14 | 15 | 16 "            
        )
        self.assertEqual(result, expected)

        play_list = [
            None, None, None, None,
            None, True, None, None,
            None, None, True, None,
            None, None, None, False
        ]
        result = print_map(n, play_list)
        expected = (
            "  1 |  2 |  3 |  4 \n" +
            "-------------------\n" +
            "  5 |  o |  7 |  8 \n" +
            "-------------------\n" +
            "  9 | 10 |  o | 12 \n"
            "-------------------\n" +
            " 13 | 14 | 15 |  x "            
        )
        self.assertEqual(result, expected)                        

    def test_check_markers(self):
        # vertical
        n = 3
        position = 7
        play_list = [
            False, False, True,
            False, True, None,
            None, True, True,
        ]
        result = check_all_same_markers_in_row(n, position, play_list, False)
        expected_number = 1
        self.assertEqual(result, 1)

        # horizontal
        position = 7
        play_list = [
            False, False, False,
            False, True, True,
            None, True, True,
        ]
        result = check_all_same_markers_in_row(n, position, play_list, True)
        expected_number = 1
        self.assertEqual(result, 1)        

        # diagonal
        position = 1
        play_list = [
            None, False, False,
            False, True, True,
            None, True, True,
        ]
        result = check_all_same_markers_in_row(n, position, play_list, True)
        expected_number = 1
        self.assertEqual(result, 1)        
        
        # diagonal
        n = 4
        position = 1
        play_list = [
            None, None, None, False,
            None, True, None, False,
            None, None, True, False,
            None, None, None, True
        ]
        result = check_all_same_markers_in_row(n, position, play_list, True)
        expected_number = 1        
        self.assertEqual(result, 1)        
