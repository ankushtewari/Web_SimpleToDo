import streamlit as st
import file_functions


def add_todo():
    todos = file_functions.get_todos()
    todo = st.session_state["new_todo"]
    todo.strip()
    if len(todo) > 0:
        todo = todo + '\n'
        todos.append(todo)
        file_functions.write_todos(todos)
        st.session_state["new_todo"] = ""


todos = file_functions.get_todos()
st.title("My To Do App")
st.subheader("This is a simple to do app")

for index, todo in enumerate(todos):
    k = str(index) + todo
    checkbox = st.checkbox(todo, key=k)
    if checkbox:
        todos.pop(index)
        file_functions.write_todos(todos)
        del st.session_state[k]
        st.rerun()

st.text_input(label="", placeholder="Add a new to-do and press enter", key="new_todo",
              on_change=add_todo)
