# qa_python
# Тесты для BooksCollector

Для удобства добавил фикстуру `collector`.
Также исправил тест, который использовался для примера (использовался метод get_books_rating, который нигде не применялся. Исправил на get_books_genre)

## Список тестов

### add_new_book
- **test_add_new_book_add_two_books** – добавление двух корректных книг; проверка, что словарь содержит ровно 2 элемента.
- **test_add_new_book_duplicate_not_added** – повторное добавление той же книги не увеличивает словарь.

### set_book_genre
- **test_set_book_genre_only_for_existing_genre** – параметризованный тест: жанр устанавливается только если он присутствует в списке допустимых (`Фантастика`, `Детективы`, несуществующий жанр игнорируется).

### get_book_genre
- **test_get_book_genre_existing_book** – для книги с установленным жанром возвращается правильное значение.
- **test_get_book_genre_no_genre_set** – для книги без жанра возвращается пустая строка.

### get_books_with_specific_genre
- **test_get_books_with_specific_genre_invalid_genre_returns_empty** – запрос книг по жанру, которого нет в списке допустимых, возвращает пустой список.

### get_books_genre
- **test_get_books_genre_returns_dict** – метод возвращает словарь со всеми книгами и жанрами.

### get_books_for_children
- **test_get_books_for_children_ignores_books_without_genre** – книга без указанного жанра не попадает в список для детей.

### add_book_in_favorites
- **test_add_book_in_favorites_noexistent_book_not_added** – попытка добавить в избранное книгу, отсутствующую в `books_genre`, не меняет список избранного.

### delete_book_from_favorites
- **test_delete_book_from_favorites_removes_if_present** – книга успешно удаляется из избранного, если она там была.

### get_list_of_favorites_books
- **test_get_list_of_favorites_books_after_adding** – после добавления книги в избранное, она появляется в возвращаемом списке.

## Особенности
- Один тест (`test_set_book_genre_only_for_existing_genre`) **параметризован** для проверки разных жанров.
- Названия тестов следуют шаблону `test_метод_сценарий`.