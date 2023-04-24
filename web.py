import streamlit as st
import functions as fun

todos = fun.get_todos()


def add_todo():
    todo_this = (st.session_state["new_todo"])
    todos.append(todo_this+'\n')
    fun.write_todos(todos)


st.title("My todo app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fun.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="add a new todo",
              on_change=add_todo, key="new_todo")

