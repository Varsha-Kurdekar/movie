import pytest
from movie_theatre import MovieTheatre

def test_book_seats():
    theatre = MovieTheatre()
    theatre.book_seats("10AM", 10)
    assert theatre.show_slots["10AM"] == 50

def test_invalid_slot():
    theatre = MovieTheatre()
    with pytest.raises(ValueError):
        theatre.book_seats("11PM", 5)

def test_analyze_crowd_low():
    theatre = MovieTheatre()
    assert theatre.analyze_crowd("10AM") == "LOW"

def test_best_show_slot():
    theatre = MovieTheatre()
    assert theatre.best_show_slot() == "10AM"