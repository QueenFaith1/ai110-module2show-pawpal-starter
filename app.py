import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

# Initialize session state
if "owner" not in st.session_state:
    st.session_state.owner = None

st.title("🐾 PawPal+")
st.subheader("Smart Pet Care Planner")

# Owner and Pet Info
with st.sidebar:
    st.header("Setup")
    owner_name = st.text_input("Owner Name")
    pet_name = st.text_input("Pet Name")
    species = st.selectbox("Species", ["dog", "cat", "bird", "rabbit"])
    
    if st.button("Create Profile"):
        pet = Pet(pet_name, species)
        owner = Owner(owner_name)
        owner.add_pet(pet)
        st.session_state.owner = owner
        st.success(f"Profile created for {owner_name} and {pet_name}!")

# Add Tasks
if st.session_state.owner:
    st.header("Add a Task")
    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task Title")
    with col2:
        duration = st.number_input("Duration (mins)", min_value=1, max_value=120, value=15)
    with col3:
        priority = st.selectbox("Priority", ["high", "medium", "low"])
    
    time = st.text_input("Time (HH:MM)", value="08:00")
    frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

    if st.button("Add Task"):
        task = Task(task_title, duration, priority, time, frequency)
        st.session_state.owner.pets[0].add_task(task)
        st.success(f"Task '{task_title}' added!")

    
    # Generate Schedule
    st.header("📅 Daily Schedule")
    if st.button("Build Schedule"):
        scheduler = Scheduler(st.session_state.owner)
        plan = scheduler.get_daily_plan()
        
        # Show conflicts
        conflicts = scheduler.detect_conflicts()
        if conflicts:
            for conflict in conflicts:
                st.warning(conflict)
        
        if plan:
            for pet_name, task in plan:
                status = "✅" if task.completed else "⏳"
                st.write(f"{status} **[{task.priority.upper()}]** {pet_name} — {task.title} ({task.duration} mins) at {task.time}")
        else:
            st.warning("No tasks yet! Add some tasks first.")