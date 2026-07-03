# PawPal+ System
# Core classes for managing pet care tasks

from dataclasses import dataclass, field
from typing import List
from datetime import datetime, timedelta

@dataclass
class Task:
    title: str
    duration: int  # in minutes
    priority: str  # "high", "medium", "low"
    time: str = "08:00"  # HH:MM format
    frequency: str = "once"  # "once", "daily", "weekly"
    completed: bool = False

    def mark_complete(self):
        """Mark task as complete."""
        self.completed = True

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)

class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Get all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))
        return all_tasks

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_by_priority(self):
        """Sort all tasks by priority."""
        priority_order = {"high": 1, "medium": 2, "low": 3}
        all_tasks = self.owner.get_all_tasks()
        return sorted(all_tasks, key=lambda x: priority_order.get(x[1].priority, 3))

    def get_daily_plan(self):
        """Generate a daily plan sorted by priority."""
        return self.sort_by_priority()