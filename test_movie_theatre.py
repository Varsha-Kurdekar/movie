import sys
import os
sys.path.append(os.getcwd())

from movie_theatre import MovieTheatre

def test_best_show_slot():
    theatre = MovieTheatre()
    assert theatre.best_show_slot() == "10AM"

def test_crowd_level():
    theatre = MovieTheatre()
    assert theatre.analyze_crowd("4PM") == "HIGH"