import unittest

from main import get_list_by_N, create_map_by_N, check_all_same_markers_in_row

class TestMain(unittest.TestCase):
    def test_get_list_by_N(self):
        result = get_list_by_N(2)
        expected = [None, None, None, None]
        self.assertEqual(result, expected)

        result = get_list_by_N(3)
        expected = [None] * 9
        self.assertEqual(result, expected)

    def test_create_map_by_N(self):
        n = 3
        play_list = [None] * n * n
        result = create_map_by_N(n, play_list)
        expected = "\n".join([
            " 1 | 2 | 3 ",
            "-----------",
            " 4 | 5 | 6 ",
            "-----------",
            " 7 | 8 | 9 "
        ])
        self.assertEqual(result, expected)

        play_list = [
            None, None, None,
            None, True, False,
            None, None, None
        ]
        result = create_map_by_N(n, play_list)
        expected = "\n".join([
            " 1 | 2 | 3 ",
            "-----------",
            " 4 | o | x ",
            "-----------",
            " 7 | 8 | 9 "
        ])
        self.assertEqual(result, expected)

        n = 4
        play_list = [None] * n * n
        result = create_map_by_N(n, play_list)
        expected = "\n".join([
            "  1 |  2 |  3 |  4 ",
            "-------------------",
            "  5 |  6 |  7 |  8 ",
            "-------------------",
            "  9 | 10 | 11 | 12 ",
            "-------------------",
            " 13 | 14 | 15 | 16 "
        ])
        self.assertEqual(result, expected)

        play_list = [
            None, None, None, None,
            None, True, None, None,
            None, None, True, None,
            None, None, None, False
        ]
        result = create_map_by_N(n, play_list)
        expected = "\n".join([
            "  1 |  2 |  3 |  4 ",
            "-------------------",
            "  5 |  o |  7 |  8 ",
            "-------------------",
            "  9 | 10 |  o | 12 ",
            "-------------------",
            " 13 | 14 | 15 |  x "
        ])
        self.assertEqual(result, expected)

    def test_mark_where_it_is_already_marked(self):
        n = 3
        position = 1
        play_list = [
            False, False, True,
            False, True, None,
            False, True, True,
        ]
        result = check_all_same_markers_in_row(n, position, play_list, False)
        expected_number = 0
        self.assertEqual(result, expected_number)

    def test_vertical_mark(self):
        n = 3
        position = 7
        play_list = [
            False, False, True,
            False, True, None,
            None, True, True,
        ]
        result = check_all_same_markers_in_row(n, position, play_list, False)
        expected_number = 1
        self.assertEqual(result, expected_number)

        # vertical N=4
        n = 4
        position = 9
        play_list = [
            False, False, True, None,
            False, True, None, None,
            None, True, True, None,
            None, True, True, None,
        ]
        result = check_all_same_markers_in_row(n, position, play_list, False)
        expected_number = 1
        self.assertEqual(result, expected_number)

    def test_horizontal_mark(self):
        # horizontal
        n = 3
        position = 7
        play_list = [
            False, False, False,
            False, True, True,
            None, True, True
        ]
        result = check_all_same_markers_in_row(n, position, play_list, True)
        expected_number = 1
        self.assertEqual(result, expected_number)

        # horizontal, no win even though there's 3 consecutive makers in row
        n = 3
        position = 7
        play_list = [
            False, False, False,
            False, True, True,
            None, True, None
        ]
        result = check_all_same_markers_in_row(n, position, play_list, True)
        expected_number = 0
        self.assertEqual(result, expected_number)

        # horizontal N=4
        n = 4
        position = 9
        play_list = [
            False, False, False, None,
            False, True, True, None,
            None, True, True, None,
            None, None, None, None
        ]
        result = check_all_same_markers_in_row(n, position, play_list, True)
        expected_number = 1
        self.assertEqual(result, expected_number)

    def test_left_up_diagonal_mark(self):
        n = 3
        position = 1
        play_list = [
            None, False, False,
            False, True, True,
            None, True, True,
        ]
        result = check_all_same_markers_in_row(n, position, play_list, True)
        expected_number = 1
        self.assertEqual(result, expected_number)

        # left-up diagonal N=4 in True
        n = 4
        position = 1
        play_list = [
            None, None, None, False,
            None, True, None, False,
            None, None, True, False,
            None, None, None, None
        ]
        result = check_all_same_markers_in_row(n, position, play_list, True)
        expected_number = 1
        self.assertEqual(result, expected_number)

    def test_left_up_diagonal_mark_not_from_vertex(self):
        n = 4
        position = 2
        play_list = [
            None, None, None, False,
            None, True, False, False,
            None, None, True, False,
            None, None, None, None
        ]
        result = check_all_same_markers_in_row(n, position, play_list, False)
        expected_number = 1
        self.assertEqual(result, expected_number)

        # another left-up diagonal N=4 in True not from vertex
        n = 4
        position = 12
        play_list = [
            None, True, False, None,
            None, False, True, False,
            None, False, True, None,
            False, None, None, True
        ]
        result = check_all_same_markers_in_row(n, position, play_list, True)
        expected_number = 1
        self.assertEqual(result, expected_number)

    def test_left_up_diagonal_mark_should_be_in_a_line(self):
        n = 4
        position = 13
        play_list = [
            None, True, True, None,
            None, False, True, True,
            False, False, True, None,
            None, None, None, True
        ]
        result = check_all_same_markers_in_row(n, position, play_list, True)
        expected_number = 0
        self.assertEqual(result, expected_number)

    def test_right_up_diagonal_mark(self):
        # right-up diagonal N=4 in False
        n = 4
        position = 7
        play_list = [
            None, None, None, None,
            None, True, None, False,
            None, False, True, False,
            False, None, None, True
        ]
        result = check_all_same_markers_in_row(n, position, play_list, False)
        expected_number = 1
        self.assertEqual(result, expected_number)

    def test_right_up_diagonal_mark_not_from_vertex(self):
        n = 4
        position = 9
        play_list = [
            None, None, False, None,
            None, False, None, False,
            None, False, True, False,
            False, None, None, True
        ]
        result = check_all_same_markers_in_row(n, position, play_list, False)
        expected_number = 1
        self.assertEqual(result, expected_number)

        # another right-up diagonal N=4 in False not from vertex
        n = 4
        position = 14
        play_list = [
            None, None, False, None,
            None, False, None, True,
            None, False, True, False,
            False, None, None, True
        ]
        result = check_all_same_markers_in_row(n, position, play_list, True)
        expected_number = 1
        self.assertEqual(result, expected_number)

    def test_right_up_diagonal_mark_should_be_in_a_line(self):
        n = 4
        position = 5
        play_list = [
            None, True, False, None,
            None, False, None, True,
            None, False, True, False,
            False, None, None, True
        ]
        result = check_all_same_markers_in_row(n, position, play_list, True)
        expected_number = 0
        self.assertEqual(result, expected_number)


    def test_vertical_and_horizontal_mark(self):
        n = 3
        position = 1
        play_list = [
            None, False, False,
            False, True, True,
            False, True, True,
        ]
        result = check_all_same_markers_in_row(n, position, play_list, False)
        expected_number = 2
        self.assertEqual(result, expected_number)

    def test_two_diagonals_mark(self):
        n = 3
        position = 5
        play_list = [
            False, True, False,
            True, None, True,
            False, True, False,
        ]
        result = check_all_same_markers_in_row(n, position, play_list, False)
        expected_number = 2
        self.assertEqual(result, expected_number)
