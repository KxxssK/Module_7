info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
strings_positions = {}

def custom_write(file_name, string):
    n = 0
    f = open(file_name, 'a', encoding = 'utf-8')
    for i in string:
        strings_positions[(n,f.tell())] = i
        n += 1
        f.write(f'{i}\n')
    f.close()

    return strings_positions

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

