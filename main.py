from storage.storage_manager import StorageManager
from src.habit_tracker import HabitTracker
from src.console_ui import ConsoleUI

storage = StorageManager()
tracker = HabitTracker(storage)

ui = ConsoleUI(tracker)
ui.run()

