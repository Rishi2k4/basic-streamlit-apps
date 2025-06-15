import streamlit as st

st.set_page_config(page_title="📝 To-Do List", layout="centered")

st.title("📝 To-Do List App")
st.caption("Track your daily tasks with Streamlit!")

# Initialize task list
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "completed" not in st.session_state:
    st.session_state.completed = []

# Add new task
new_task = st.text_input("Add a new task:")
if st.button("➕ Add Task"):
    if new_task.strip():
        st.session_state.tasks.append(new_task.strip())
        st.success(f"Task added: {new_task}")
    else:
        st.warning("Please enter a valid task.")

st.divider()

# Display tasks with checkboxes
st.subheader("Your Tasks")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.1, 0.9])
        if col1.checkbox("", key=f"task_{i}"):
            st.session_state.completed.append(task)
            st.session_state.tasks.pop(i)
            st.experimental_rerun()
        else:
            col2.write(f"🔹 {task}")
else:
    st.info("No tasks added yet.")

# Show completed tasks
if st.session_state.completed:
    with st.expander("✅ Completed Tasks"):
        for task in st.session_state.completed:
            st.markdown(f"- ~~{task}~~")

# Reset button
if st.button("🔄 Reset All"):
    st.session_state.tasks.clear()
    st.session_state.completed.clear()
    st.success("All tasks cleared.")
