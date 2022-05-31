import streamlit as st

import views


def rooting():
    menu_list = ["Home", "Create", "Update", "Delete", "Total"]
    choice = st.sidebar.selectbox("作業を選択してください", menu_list, index=0)

    if choice == "Home":
        views.read()

    if choice == "Create":
        views.create()

    if choice == "Update":
        views.update()

    if choice == "Delete":
        views.delete()

    if choice == "Total":
        views.total()