import streamlit as st

st.title("📝 To-Do List App")

# Store tasks in session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add task
st.subheader("Add Task")
new_task = st.text_input("Enter a new task")

if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success("Task added!")
    else:
        st.warning("Please enter a task")

# Show tasks
st.subheader("Your Tasks")

if len(st.session_state.tasks) == 0:
    st.write("No tasks yet")
else:
    for i, task in enumerate(st.session_state.tasks):
        st.write(f"{i+1}. {task}")

# Delete task
st.subheader("Delete Task")

if len(st.session_state.tasks) > 0:
    task_num = st.number_input("Enter task number to delete", min_value=1, max_value=len(st.session_state.tasks), step=1)

    if st.button("Delete Task"):
        st.session_state.tasks.pop(task_num - 1)
        st.success("Your Task deleted!")