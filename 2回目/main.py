import os, json
import streamlit as st

import rooting


db_file_name = "datas.json"

def main():
    if not os.path.isfile(db_file_name):
            with open(db_file_name, "w") as f:
                json.dump([], f, indent=4, ensure_ascii=False)

    st.set_page_config(
        page_title = "家計簿管理アプリ",
        page_icon = ":yen:",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("家計簿管理アプリ :money_with_wings:")
    
    rooting.rooting()


if __name__ == "__main__":
    main()