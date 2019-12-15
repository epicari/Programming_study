#
# HackerRank Tutorials Day 13: Abstract Classes
#
# @abstractmethod를 쓰려면 abc를 import 해야 함
# 내용은 pass 처리, 추상 클래스에서 내용 작성하도록
#

from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(self): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print("Title: " + title + "\nAutor: " + author + "\nPrice: " + self.price)  

if __name__ == '__main__':

    title=input()
    author=input()
    price=int(input())
    new_novel=MyBook(title,author,price)
    new_novel.display()

