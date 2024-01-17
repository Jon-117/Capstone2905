"""
Basics of Python
Lab 2, Parts 1 & 2
"""


class Author:
    def __init__(self, name: str, books_published: list):
        self.name = name
        self.books_published = books_published

    def publish_book(self, book_name: str):
        if book_name not in self.books_published:
            self.books_published.append(book_name)
        else:
            print(f"{book_name} already published")

    def __str__(self):
        listed_books = ''
        for book in self.books_published:
            listed_books += book + '\n'
        return f"{self.name} wrote:\n{listed_books}"


author_list = ['Charlie Carr', 'Rebecca Nicole Graham']
book_list1 = ["Rizz: Lifestyle or Life Science", "Big Chunga: Biography of the One and Only", "Curling, A Primer"]
book_list2 = ['Niblitz Galactica', 'British College', 'Worldhopping for Dummies',
              "Contagious Thoughts: The Mind Virus Technique"]


def main():
    author = Author('Jon', [])
    print(author.name)
    print(author.books_published)
    print('*' * 30)
    books = ['Killer Warlocks in Bangladesh', 'chalie bit me, vol 1', 'all about chaos', "Girl, don't touch my toenuts",
             "Chibledy Gibgrutz: An Anthology"]
    for book in books:
        author.publish_book(book)
    print(author)

    author2 = Author(author_list[0], book_list1)
    author3 = Author(author_list[1], book_list2)

    print(author2)
    print(author3)

    author3.publish_book('Punny Title')
    author3.publish_book('Punny Title')


if __name__ == '__main__':
    main()
