from lib.book import Books
class Book_Repository:

    def __init__(self, database_connection):
        self.database_connection = database_connection

    def all(self):
            books_data = self.database_connection.execute("SELECT * FROM books")
            list = []
            for i in books_data:
                item = Books(i['id'], i['title'], i['author_name'])
                list.append(item)
            
            return list