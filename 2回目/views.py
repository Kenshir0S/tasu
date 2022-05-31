import streamlit as st

import models


def read():
    kind = st.selectbox(label="全体:0 年別:1 月別:2 日別:3 カテゴリ別:4", options=["0", "1", "2", "3", "4"], index=0)
    kind = int(kind)
    if kind == 0:
        interval = 0
        df = models.return_df(kind, interval)
        _, col = st.columns([2, 4.5])
        col.dataframe(df, width=1000)
        chart_data = models.chart_data(df)
        st.altair_chart(chart_data, use_container_width=True)
    
    elif  kind == 1:
        interval = st.text_input(label="年を入力してください", value="2022")
        df = models.return_df(kind, interval)
        _, col = st.columns([2, 4.5])
        col.dataframe(df, width=1000)
        if "date" in df.keys():
            chart_data = models.chart_data(df)
            st.altair_chart(chart_data, use_container_width=True)
    
    elif  kind == 2:
        interval = st.text_input(label="年月を入力してください", value="202204")
        df = models.return_df(kind, interval)
        _, col = st.columns([2, 4.5])
        col.dataframe(df, width=1000)
        if "date" in df.keys():
            chart_data = models.chart_data(df)
            st.altair_chart(chart_data, use_container_width=True)
    
    elif kind == 3:
        interval = st.date_input(label="カレンダーから選択してください")
        df = models.return_df(kind, interval)
        _, col = st.columns([2, 4.5])
        col.dataframe(df, width=1000)
    
    else:
        category_names = models.get_category_name()
        interval = st.selectbox(label="カテゴリ名を選択してください", options=category_names)
        df = models.return_df(kind, interval)
        _, col = st.columns([2, 4.5])
        col.dataframe(df, width=1000)
        if "date" in df.keys():
            chart_data = models.chart_data(df)
            st.altair_chart(chart_data, use_container_width=True)

def create():
    st.write("""
                ### 新規作成
                """)
    day = st.date_input(label="日付:")
    st.write('input: ', day)
    category = st.text_input(label="カテゴリ名:", value="なし")
    st.write('input: ', category)
    in_out = st.selectbox(label="0(収入) or 1(支出):", options=["0", "1"], index=0)
    st.write('input: ', in_out)
    price = st.number_input(label="金額:", min_value=0, step=1)
    st.write('input: ', price)
    if st.button("作成"):
        result = models.create_model(day, category, in_out, price)
        if result is not None:
            st.success("新規作成しました！")
        else:
            st.error("新規作成できませんでした…")
            
def update():
    st.write("""
                ### 内容更新
                """)
    id = st.number_input(label="ID:", min_value=0, step=1)
    st.write('input: ', id)
    day = st.date_input(label="日付:")
    st.write('input: ', day)
    category = st.text_input(label="カテゴリ名:", value="なし")
    st.write('input: ', category)
    in_out = st.selectbox(label="0(収入) or 1(支出):", options=["0", "1"], index=0)
    st.write('input: ', in_out)
    price = st.number_input(label="金額:", min_value=0, step=1)
    st.write('input: ', price)
    if st.button("更新"):
        result = models.update_model(id, day, category, in_out, price)
        if result:
            st.success("変更内容を更新しました！")
        else:
            st.error("変更内容を更新できませんでした…")
            
def delete():
    st.write("""
                ### 内容削除
                """)
    id = st.number_input(label="ID:", min_value=0, step=1)
    st.write('input: ', id)
    if st.button("削除"):
        result = models.delete_model(id)
        if result:
            st.success("内容を削除しました！")
        else:
            st.error("内容を削除できませんでした…")
                
def total():
    st.write("""
                ### 集計結果
                """)
    kind = st.selectbox(label="全体:0 年別:1 月別:2 日別:3 カテゴリ別:4", options=["0", "1", "2", "3", "4"], index=0)
    kind = int(kind)
    if kind == 0:
        interval = 0
        total = models.total_model(kind, interval)
        st.markdown(f"## ¥{total:,}")
    
    elif  kind == 1:
        interval = st.text_input(label="年を入力してください", value="2022")
        total = models.total_model(kind, interval)
        st.markdown(f"## ¥{total:,}")
    
    elif  kind == 2:
        interval = st.text_input(label="年月を入力してください", value="202204")
        total = models.total_model(kind, interval)
        st.markdown(f"## ¥{total:,}")
    
    elif kind == 3:
        interval = st.date_input(label="カレンダーから選択してください")
        total = models.total_model(kind, interval)
        st.markdown(f"## ¥{total:,}")
    
    else:
        category_names = models.get_category_name()
        interval = st.selectbox(label="カテゴリ名を選択してください", options=category_names)
        total = models.total_model(kind, interval)
        st.markdown(f"## ¥{total:,}")