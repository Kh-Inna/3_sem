import unittest
from main import *

class TestJoinOperations(unittest.TestCase):
    def test_one_to_many(self):
        result = one_to_many_(chapters, books)
        self.assertTrue(len(result) > 0)  # Проверка, что результат не пустой

    def test_many_to_many(self):
        result = many_to_many_(chapters, chapters_books, books)
        self.assertTrue(len(result) > 0)  # Проверка, что результат не пустой

class TestTaskResults(unittest.TestCase):
    def test_get_result_1(self):
        data = [("Кратные интегралы", 3, "Математический анализ"), ("Анализ векторный", 3, "Курс математического анализа"), ("Предел функции", 1, "Сборник задач для ВТУЗОВ")]
        result = get_result_1(data)
        self.assertEqual(result, [("Анализ векторный", 3, "Курс математического анализа")])  # Проверка корректности результата

    def test_get_empty_result_1(self):
        data = []  # пустой список
        result = get_result_1(data)
        self.assertEqual(result, [])  # ожидаемый результат - пустой список

    def test_get_result_2(self):
        data = [("Кратные интегралы", 3, "Математический анализ"), ("Анализ векторный", 3, "Курс математического анализа"), ("Предел функции", 1, "Сборник задач для ВТУЗОВ")]
        result = get_result_2(data)
        self.assertEqual(result, [("Сборник задач для ВТУЗОВ", 1), ("Математический анализ", 3), ("Курс математического анализа", 3)])  # Проверка корректности результата

    def test_get_result_3(self):
        data = [
            ("Анализ векторный", 3, "Сборник задач по векторному анализу1"),
            ("Дифференциалы", 2, "Сборник задач для ВТУЗОВ"),
            ("Дифференциалы", 2, "Сборник задач по курсу математического анализа"),
            ("Кратные интегралы", 3, "Математический анализ"),
            ("Кратные интегралы", 3, "Ряды и кратные интегралы"),
            ("Предел функции", 1, "Сборник задач для ВТУЗОВ"),
            ("Предел функции", 1, "Сборник задач по курсу математического анализа"),
            ("Ряды", 2, "Сборник задач для ВТУЗОВ"),
            ("Ряды", 2, "Сборник задач по курсу математического анализа")]
        result = sorted(data, key=itemgetter(0))  # ожидаемый результат - отсортированный по имени библиотеки
        self.assertEqual(result, get_result_3(data))

if __name__ == '__main__':
    unittest.main()