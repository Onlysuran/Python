#conding:utf-8

class Book:
    lang = 'learn python with suran'

    def __init__(self, author):
        self.author = author
    
    def get_name(self):
        return self.author

def new_book():
    return "数据准备和特征工程"

python = Book('suran')
author_name = python.get_name()
print(author_name)
published = new_book()
print(published)
