import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books(self):
        book1 = data.Book(["kendall", "kylie"], "Hunger Games")
        book2 = data.Book(["David"], "Almost")
        book3 = data.Book(["Hey", "Annika"], "Normal People")
        expected = lab6.selection_sort_books([book1, book3, book2])
        result = [data.Book(['David'], 'Almost'), data.Book(['kendall', 'kylie'], 'Hunger Games'), data.Book(['Hey', 'Annika'], 'Normal People')]
        self.assertEqual(expected, result)

    def test_selection_sort_books_2(self):
        book1 = data.Book(["Annika"], "I love electrical engineering")
        book2 = data.Book(["Daivd", "bob"], "Everything")
        expected  = [data.Book(["Daivd", "bob"], "Everything"), data.Book(["Annika"], "I love electrical engineering")]
        result = lab6.selection_sort_books([book1, book2])
        self.assertEqual(expected, result)

    # Part 2
    def test_swap_case(self):
        result = lab6.swap_case("Hey!")
        expected = "hEY!"
        self.assertEqual(expected, result)

    def test_swap_case_2(self):
        result = lab6.swap_case("CUIDATE, por favor!!")
        expected = "cuidate, POR FAVOR!!"
        self.assertEqual(expected, result)

    # Part 3
    def test_str_translate(self):
        result = lab6.str_translate("Lalalala", 'a', 'e')
        expected = ('Lelelele')
        self.assertEqual(result, expected)

    def test_str_translate_2(self):
        result = 'ji jow jave you been jayden'
        expected = lab6.str_translate('hi how have you been hayden', 'h', 'j')
        self.assertEqual(result, expected)

    # Part 4
    def test_histogram(self):
        result = lab6.histogram("This is so so so cool")
        expected = {'This': 1, 'is': 1, 'so': 3, 'cool':1}
        self.assertEqual(result, expected)

    def test_histogram_2(self):
        result = lab6.histogram("oh my goodness, oh my gosh!")
        expected = {'oh': 2, 'my': 2, 'goodness,':1, 'gosh!':1}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
