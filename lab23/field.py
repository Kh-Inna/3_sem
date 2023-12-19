def field(items, *args):
    assert len(args) > 0
    for i in items:
        if all(arg in i for arg in args):
            for arg in args:
                print(i[arg], end=" ")
    print("")

if __name__ == '__main__':
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    field(goods, 'title')
    field(goods, 'title', 'price')