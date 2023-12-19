import random

def gen_random(num_count, begin, end):
    numbers = []
    for i in range(num_count):
        numbers.append(random.randint(begin, end))
    return numbers

# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.index = 0
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __next__(self):
        while self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            item_key = item.lower() if self.ignore_case else item
            if item_key not in self.seen:
                self.seen.add(item_key)
                return item
        raise StopIteration()

    def __iter__(self):
        return self
    
if __name__ == '__main__':
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    unique_data = Unique(data)
    print(list(unique_data))

    data = gen_random(10, 1, 3)
    unique_data = Unique(data)
    print(list(unique_data))

    data = ["a", "A", "b", "B", "a", "A", "b", "B"]
    unique_data = Unique(data)
    print(list(unique_data))

    data = ["a", "A", "b", "B", "a", "A", "b", "B"]
    unique_data = Unique(data, ignore_case=True)
    print(list(unique_data))