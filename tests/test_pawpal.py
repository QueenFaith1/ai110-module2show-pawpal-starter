from pawpal_system import Task, Pet, Owner, Scheduler

def test_task_completion():
    task = Task("Morning Walk", 30, "high", "08:00", "daily")
    task.mark_complete()
    assert task.completed == True

def test_add_task_increases_count():
    pet = Pet("Buddy", "dog")
    task = Task("Feeding", 10, "high", "09:00", "daily")
    pet.add_task(task)
    assert len(pet.tasks) == 1

def test_sorting_by_priority():
    owner = Owner("Faith")
    dog = Pet("Buddy", "dog")
    dog.add_task(Task("Playtime", 20, "low", "15:00", "once"))
    dog.add_task(Task("Feeding", 10, "high", "09:00", "daily"))
    owner.add_pet(dog)
    scheduler = Scheduler(owner)
    plan = scheduler.get_daily_plan()
    assert plan[0][1].priority == "high"