import unittest

from src.models import Habit
from src.habit_tracker import HabitTracker
from storage.storage_manager import StorageManager

class TestHabitTracker(unittest.TestCase):

    def test_add_habit(self):
        storage = StorageManager()
        tracker = HabitTracker(storage)

        habit = Habit("Reading", "Read a book", False)
        tracker.add_habit(habit)
        self.assertEqual(1, tracker.count_habits())

    def test_count_completed_habits(self):
        storage = StorageManager()
        tracker = HabitTracker(storage)

        habit = Habit("Назва", "Опис", True)
        habit1 = Habit("Назва", "Опис", True)
        habit2 = Habit("Назва", "Опис", False)
        tracker.add_habit(habit)
        tracker.add_habit(habit1)
        tracker.add_habit(habit2)
        self.assertEqual(2, tracker.count_completed_habits())

    def test_count_uncompleted_habits(self):
        storage = StorageManager()
        tracker = HabitTracker(storage)

        habit = Habit("Назва", "Опис", True)
        habit1 = Habit("Назва", "Опис", False)
        habit2 = Habit("Назва", "Опис", False)
        tracker.add_habit(habit)
        tracker.add_habit(habit1)
        tracker.add_habit(habit2)
        self.assertEqual(2, tracker.count_uncompleted_habits())

    def test_completion_percentage(self):
        storage = StorageManager()
        tracker = HabitTracker(storage)

        habit = Habit("Назва", "Опис", True)
        habit1 = Habit("Назва", "Опис", False)
        habit2 = Habit("Назва", "Опис", False)
        habit3 = Habit("Назва", "Опис", True)
        tracker.add_habit(habit)
        tracker.add_habit(habit1)
        tracker.add_habit(habit2)
        tracker.add_habit(habit3)
        self.assertEqual(50.0, tracker.get_completion_percentage())

    def test_search_habits(self):
        storage = StorageManager()
        tracker = HabitTracker(storage)

        habit = Habit("Reading", "Read a book", False)
        habit1 = Habit("Running", "Go running", False)

        tracker.add_habit(habit)
        tracker.add_habit(habit1)
        result = tracker.search_habits("Reading")

        self.assertEqual(1, len(result))
        self.assertEqual("Reading", result[0].name)
       
if __name__ == "__main__":
    unittest.main()

