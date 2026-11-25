from src.models import Habit

class HabitTracker:
    def __init__(self, storage):
        self.storage = storage
        self.habits = []

    def add_habit(self, habit):
        self.habits.append(habit)

    def get_habits(self):
        return self.habits

    def edit_habit(self, habit, new_name, new_description):
        habit.name = new_name
        habit.description = new_description

    def mark_completed(self, habit):
        habit.completed = True

    def get_completion_percentage(self):
        total = self.count_habits()
        if total == 0:
            return 0
        completed = self.count_completed_habits()

        percentage = completed/total * 100
        return percentage

    def delete_habit(self, habit):
        self.habits.remove(habit)

    def count_habits(self):
        return len(self.habits)

    def count_completed_habits(self):
        count = 0
        for i in self.habits:
            if i.completed:
                count += 1
        
        return count

    def count_uncompleted_habits(self):
        count = 0
        for i in self.habits:
            if not i.completed:
                count += 1

        return count

    def search_habits(self, name):
        found_habits = []
        for habit in self.habits:
            if name in habit.name:
                found_habits.append(habit)

        return found_habits

    def get_completed_habits(self):
        for habits in self.habits:
            if habits.completed:
                print(habits.name)

    def get_uncompleted_habits(self):
        for habits in self.habits:
            if not habits.completed:
                print(habits.name)
