from pawpal_system import Task, Pet, Owner, Scheduler

# Create owner
owner = Owner("Faith")

# Create pets
dog = Pet("Buddy", "dog")
cat = Pet("Luna", "cat")

# Add tasks for dog
dog.add_task(Task("Morning Walk", 30, "high", "08:00", "daily"))
dog.add_task(Task("Feeding", 10, "high", "09:00", "daily"))
dog.add_task(Task("Playtime", 20, "medium", "15:00", "daily"))

# Add tasks for cat
cat.add_task(Task("Feeding", 10, "high", "08:30", "daily"))
cat.add_task(Task("Grooming", 15, "medium", "14:00", "weekly"))

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create scheduler
scheduler = Scheduler(owner)

# Print daily plan
print(f"\n🐾 Daily Plan for {owner.name}'s pets:\n")
plan = scheduler.get_daily_plan()
for pet_name, task in plan:
    status = "✅" if task.completed else "⏳"
    print(f"{status} [{task.priority.upper()}] {pet_name} — {task.title} ({task.duration} mins) at {task.time}")