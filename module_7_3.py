class WordsFinder():

    file_names = []
    all_words = {}
    y = ',', '.', '=', '!', '?', ';', ':'

    def __init__(self, *file_name):
        for i in file_name:
            self.file_names.append(i)

    def get_all_words(self):
        a = []
        for f in self.file_names:
            with open(f, 'r+', encoding= 'utf-8') as file:
                for line in file:
                    s = str(line.lower())
                    for char in self.y:
                        if char in s:
                            s = s.replace(char,' ')
                        elif '-' in s:
                            s = s.replace('-', ' ')
                    for h in s.split():
                        self.a = a.append(h)
                self.all_words[f] = a
        return self.all_words

    def find(self, word):
        res = {}
        s = str(word.lower())
        for file_names, words in self.get_all_words().items():
            if s in words:
                res[file_names] = words.index(s) + 1
        return res

    def count(self, word):
        res = {}
        s = str(word.lower())
        for file_names, words in self.get_all_words().items():
            if s in words:
                res[file_names] = words.count(s)
        return res


finder2 = WordsFinder('test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
