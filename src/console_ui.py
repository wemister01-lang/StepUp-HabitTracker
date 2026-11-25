from src.models import Habit

class ConsoleUI:
    def __init__(self, tracker):
        self.tracker = tracker

    def show_menu(self):
        print("Додати звичку")
        print("Показати всі звички")
        print("Виконані звички")
        print("Невиконані звички")
        print("Статистика")
        print("Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            name = input("Назва звички: ").strip()
            description = input("Опис звички: ").strip()
            if not name:
                print("Ви не ввели назву!")
            elif not description:
                print("Ви не ввели опис!")
            else:
                habit = Habit(name, description, False)
                self.tracker.add_habit(habit)
                print("Звичку успішно додано!")

        elif choice == "2":
            print("Твої звички: ")
            for habit in self.tracker.get_habits():
                print(habit.name)
            
        elif choice == "3":
            print("Виконані звички: ")
            self.tracker.get_completed_habits()
        elif choice == "4":
            print("Невиконані звички")
            self.tracker.get_uncompleted_habits()
        elif choice == "5":
            print("Статистика звичок: ")
            print("Усього звичок: ", self.tracker.count_habits())
            print("Усього виконаних завдань: ", self.tracker.count_completed_habits())
            print("Усього невиконаних завдань: ", self.tracker.count_uncompleted_habits())
            print("Відсоток виконань: ", self.tracker.get_completion_percentage())
        elif choice == "6":
            print("Ти вибрав вихід")
        else:
            print("Невідомий пункт меню")

        return choice
    
    def run(self):
        while True:
            choice = self.show_menu()
            if choice == "6":
                break

           
   
