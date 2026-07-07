# 🐾 PawPal+
A smart pet care planning app built with Python and Streamlit that helps busy pet owners stay on top of daily routines.

## Scenario
Pet owners struggle to stay consistent with pet care tasks like feeding, walks, medications and grooming. PawPal+ solves this by letting owners track tasks, set priorities, and generate a daily plan automatically.

## Setup
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

## What I Built
- Task class to represent care activities with priority and time
- Pet class to store pet info and manage its task list
- Owner class to manage multiple pets
- Scheduler class to sort, filter and detect conflicts across all pets
- Streamlit UI connected to all backend logic
- 3 passing automated tests

## 🖥️ Sample Output
🐾 Daily Plan for Faith's pets:
⏳ [HIGH] Buddy — Morning Walk (30 mins) at 08:00
⏳ [HIGH] Buddy — Feeding (10 mins) at 09:00
⏳ [HIGH] Luna — Feeding (10 mins) at 08:30
⏳ [MEDIUM] Buddy — Playtime (20 mins) at 15:00
⏳ [MEDIUM] Luna — Grooming (15 mins) at 14:00

## 🧪 Testing PawPal+

Run the test suite:
python -m pytest tests/test_pawpal.py -v

Sample test output:
============== test session starts ===============
tests/test_pawpal.py::test_task_completion PASSED [ 33%]
tests/test_pawpal.py::test_add_task_increases_count PASSED [ 66%]
tests/test_pawpal.py::test_sorting_by_priority PASSED [100%]
=============== 3 passed in 0.69s ================

Confidence Level: ⭐⭐⭐⭐ (4/5)

## 📐 Smarter Scheduling
| Feature | Method | Notes |
|---|---|---|
| Task sorting | sort_by_priority() | High before medium before low |
| Filtering | filter_by_pet() | Filter tasks by pet name |
| Conflict detection | detect_conflicts() | Flags tasks at same time |
| Recurring tasks | Task.frequency | Once, daily, or weekly |

## 📸 Demo Walkthrough
1. Run streamlit run app.py
2. Enter owner name and pet name in the sidebar
3. Select species and click Create Profile
4. Add tasks with title, duration, priority and time
5. Click Build Schedule to see your daily plan
6. Tasks appear sorted by priority automatically

## 💭 How the Plan is Chosen
The scheduler sorts tasks by priority so high priority tasks always appear first. This ensures critical care like feeding and medication is never pushed behind optional activities like playtime.