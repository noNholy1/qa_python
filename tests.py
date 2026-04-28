import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_duplicate_not_added(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('genre, expected_genre', [('Фантастика', 'Фантастика'),('Детективы', 'Детективы'),('Несуществующий', '')])
    def test_set_book_genre_only_for_existing_genre(self, collector, genre, expected_genre):
        collector.add_new_book('Тест')
        collector.set_book_genre('Тест', genre)
        assert collector.get_book_genre('Тест') == expected_genre

    def test_get_book_genre_existing_book(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_get_book_genre_no_genre_set(self, collector):
        collector.add_new_book('Книга без жанра')
        assert collector.get_book_genre('Книга без жанра') == ''

    def test_get_books_with_specific_genre_invalid_genre_returns_empty(self, collector):
        collector.add_new_book('Любая книга')
        collector.set_book_genre('Любая книга', 'Фантастика')
        assert collector.get_books_with_specific_genre('Роман') == []

    def test_get_books_genre_returns_dict(self, collector):
        collector.add_new_book('А')
        collector.set_book_genre('А', 'Мультфильмы')
        assert collector.get_books_genre() == {'А': 'Мультфильмы'}

    def test_get_books_for_children_includes_child_friendly_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        children_books = collector.get_books_for_children()
        assert 'Гарри Поттер' in children_books

    def test_get_books_for_children_ignores_books_without_genre(self, collector):
        collector.add_new_book('Без жанра')
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_noexistent_book_not_added(self, collector):
        collector.add_book_in_favorites('Мираж')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_removes_if_present(self, collector):
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_after_adding(self, collector):
        collector.add_new_book('Зеленая миля')
        collector.add_book_in_favorites('Зеленая миля')
        assert collector.get_list_of_favorites_books() == ['Зеленая миля']