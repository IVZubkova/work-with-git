import requests

class Publication:
    __udc = '0.0.0' #приватный атрибут
    default_format = 'hardcover'
    default_edition = 'basic_edition'

    def __init__(self, title, author, year, publisher):
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher

    #метод класса
    def get_short_info(self):
        return f'{self.title} by {self.author}'

    #метод класса, кот будет работать одинаково со всеми экземплярами класса
    @classmethod #декоратор
    def get_default_edition(self):
        return self.default_format, self.default_edition

    def get_udc(self):
        return self.__udc

    #private method
    def __set_udc(self, udc):
        self.__udc = udc

    @staticmethod
    def get_phrase_of_a_day():
        r = requests.get('https://citbase.ru/random', timeout=30)
        # with open('response.html', 'w') as f:
        #     f.write(r.text)
        txt = r.text
        tag_beg = '<pre>'
        tag_end = '</pre>'
        beg = txt.find(tag_beg) + len(tag_beg)
        end = txt.find(tag_end)
        txt = txt[beg:end]
        return txt



class Book(Publication):
    def get_book_udc(self):



        return self.__udc


if __name__ == '__main__':
    # pub = Publication('Статья', 'Иванов Иван Иванович', 2024, 'Зеленоград 24')
    book = Book('Мастер и Маргарита', 'Булгаков М.А', 2020, 'АСТ')
    # # print(pub.get_short_info())#вызываем от экземпляра
    # # print(Publication.get_default_edition())#вызываем от класса
    # # print(pub.get_udc())
    # print(book.get_udc())
    # print(book.get_book_udc()) #класс наследник не получает доступ к приватным атрибутам класса родителя
    print(Publication.get_phrase_of_a_day())

