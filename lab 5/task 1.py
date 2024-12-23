class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return 'Название книги: ', self.title, 'Автор: ',self.author, 'Год: ', self.year
book1=book('1984','Джордж Оруэлл',1948)
print(book1.get_info())


