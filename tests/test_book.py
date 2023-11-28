from lib.book import Books

def test_constructs_with_field():
    book = Books(3, "Emma", "Jane Austen")
    assert book.id == 3
    assert book.title == "Emma"
    assert book.author_name == "Jane Austen"