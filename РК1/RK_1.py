from operator import itemgetter

class Chapter:
    """Глава"""
    def __init__(self, id, title, semester, book_id):
        self.id = id
        self.title = title
        self.semester = semester
        self.book_id = book_id

class Book:
    """Книга"""
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

class ChapterBook:
    """
    'Главы книги' для реализации связи многие-ко-многим
    """
    def __init__(self, book_id, chapter_id):
        self.book_id = book_id
        self.chapter_id = chapter_id

# Книги
books = [
    Book(1, 'Математический анализ', 'В.А.Зорич'),
    Book(2, 'Курс математического анализа', 'Л.Д.Кудрявцев'),
    Book(3, 'Сборник задач для ВТУЗОВ', 'А.В.Ефимов, Б.П.Демидович'),
    Book(11, 'Ряды и кратные интегралы', 'А.А.Гусак'),
    Book(22, 'Сборник задач по векторному анализу', 'Е.Н.Кожевников'),
    Book(33, 'Сборник задач по курсу математического анализа', 'Г.Н.Берман'),
]

# Главы
chapters = [
    Chapter(1, 'Кратные интегралы', 3, 1),
    Chapter(2, 'Анализ векторный', 3, 2),
    Chapter(3, 'Предел функции', 1, 3),
    Chapter(4, 'Дифференциалы', 2, 3),
    Chapter(5, 'Ряды', 2, 3),
]

chapters_books = [
    ChapterBook(1,1),
    ChapterBook(2,2),
    ChapterBook(3,3),
    ChapterBook(3,4),
    ChapterBook(3,5),
    ChapterBook(11,1),
    ChapterBook(22,2),
    ChapterBook(33,3),
    ChapterBook(33,4),
    ChapterBook(33,5),
]

def main():
    """Основная функция"""
    # Соединение данных один-ко-многим 
    one_to_many = [(c.title, c.semester, b.title) 
        for b in books 
        for c in chapters 
        if c.book_id==b.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(b.title, cb.book_id, cb.chapter_id) 
        for b in books 
        for cb in chapters_books 
        if b.id==cb.book_id]
    many_to_many = [(c.title, c.semester, book_title) 
        for book_title, book_id, chapter_id in many_to_many_temp
        for c in chapters if c.id==chapter_id]

    print('Задание В1')
    array = sorted(one_to_many, key=itemgetter(2))
    res_11 = []
    for i in range(len(array)):
        if array[i][0].startswith("А"):
            res_11.append(array[i])
    print(res_11)

    print('\nЗадание В2')
    res_12_unsorted = []
    i = 0
    for b in books:
        b_chapter = list(filter(lambda i: i[2]==b.title, one_to_many))        
        if len(b_chapter) > 0:
            b_semester = [page for _,page,_ in b_chapter]
            # Выбор минимального семестра
            b_semester_min = min(b_semester)
            res_12_unsorted.append((b.title, b_semester_min))
    # Сортировка по минимальному семестру
    res_12 = sorted(set(res_12_unsorted), key=itemgetter(1))
    print(res_12)

    print('\nЗадание В3')
    # Сортировка по главам
    res_13 = sorted(many_to_many, key=itemgetter(0))
    print (res_13)

if __name__ == '__main__':
    main()