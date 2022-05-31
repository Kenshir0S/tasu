from datetime import datetime
import json
from pandas import json_normalize
import pandas as pd
import altair as alt

from main import db_file_name as db


db_file = db

def create_model(day, category, in_out, price):
    day = day.strftime("%Y-%m-%d")
     
    if in_out == "1":
        if price == 0:
            pass
        else:
            price *= -1

    dic = {
        "date": day,
        "category": category,
        "in_out": in_out,
        "price": price
    }
        
    with open(db_file, "r") as f:
        json_datas = json.load(f)
    dic["id"] = len(json_datas)
    json_datas.append(dic)
    with open(db_file, "w") as f:
        json.dump(json_datas, f, indent=4, ensure_ascii=False)
        
    return True

     
def read_model(kind, interval):
    detail_list = []
    
    with open(db_file, "r") as f:
        json_datas = json.load(f)

    if kind == 0:
        for data in json_datas:
            if not data:
                continue
            detail_list.append(data)
        return detail_list
        
    if kind == 1:
        interval = datetime.strptime(interval, "%Y")
        inter_year = interval.year
        for data in json_datas:
            if not data:
                continue
            date = datetime.strptime(data["date"], "%Y-%m-%d")
            year = date.year
            if year == inter_year:
                detail_list.append(data)
        return detail_list
    
    if kind == 2:
        interval = datetime.strptime(interval, "%Y%m")
        inter_year = interval.year
        inter_month = interval.month
        for data in json_datas:
            if not data:
                continue
            date = datetime.strptime(data["date"], "%Y-%m-%d")
            year = date.year
            month = date.month
            if year == inter_year:
                if month == inter_month:
                    detail_list.append(data)
        return detail_list
        
    if kind == 3:
        inter_year = interval.year
        inter_month = interval.month
        inter_day = interval.day
        for data in json_datas:
            if not data:
                continue
            date = datetime.strptime(data["date"], "%Y-%m-%d")
            year = date.year
            month = date.month
            day = date.day
            if year == inter_year:
                if month == inter_month:
                    if day == inter_day:
                        detail_list.append(data)
        return detail_list
        
    if kind == 4:
        for data in json_datas:
            if not data:
                continue
            cate = data["category"]
            if cate == interval:
                detail_list.append(data)
        return detail_list
        
        
def update_model(id, day, category, in_out, price):
    with open(db_file, "r") as f:
        json_datas = json.load(f)

    default_day = json_datas[id]["date"]
    if not day:
        day = default_day
    else:
        day = day.strftime("%Y-%m-%d")
        
    default_category = json_datas[id]["category"]
    if not category:
        category = default_category

    default_in_out = json_datas[id]["in_out"]
    if not in_out:
        in_out = default_in_out

    default_price = json_datas[id]["price"]
    if not price:
        price = default_price

    if in_out == "1":
        price *= -1
    
    update_dic = {
        "date": day,
        "category": category,
        "in_out": in_out,
        "price": price
    }
                        
    json_datas[id].update(update_dic)
    with open(db_file, "w") as f:
        json.dump(json_datas, f, indent=4, ensure_ascii=False)
        
    return True
            
            
def delete_model(id):
    with open(db_file, "r") as f:
        json_datas = json.load(f)
    
    for data in json_datas:
        if not data:
                continue
        if data["id"] == id:
            with open(db_file, "r") as f:
                json_datas = json.load(f)
            json_datas[id].clear()
            with open(db_file, "w") as f:
                json.dump(json_datas, f, indent=4, ensure_ascii=False)
                
    return True

        
def total_model(kind, interval):
    inout = []
    
    with open(db_file, "r") as f:
        json_datas = json.load(f)

    if kind == 0:
        for data in json_datas:
            if not data:
                continue
            inout.append(data["price"])
        total = sum(inout)
        return total
        
    if kind == 1:
        interval = datetime.strptime(interval, "%Y")
        inter_year = interval.year
        for data in json_datas:
            if not data:
                continue
            date = datetime.strptime(data["date"], "%Y-%m-%d")
            year = date.year
            if year == inter_year:
                inout.append(data["price"])
        total = sum(inout)
        return total
    
    if kind == 2:
        interval = datetime.strptime(interval, "%Y%m")
        inter_year = interval.year
        inter_month = interval.month
        for data in json_datas:
            if not data:
                continue
            date = datetime.strptime(data["date"], "%Y-%m-%d")
            year = date.year
            month = date.month
            if year == inter_year:
                if month == inter_month:
                    inout.append(data["price"])
        total = sum(inout)
        return total
        
    if kind == 3:
        inter_year = interval.year
        inter_month = interval.month
        inter_day = interval.day
        for data in json_datas:
            if not data:
                continue
            date = datetime.strptime(data["date"], "%Y-%m-%d")
            year = date.year
            month = date.month
            day = date.day
            if year == inter_year:
                if month == inter_month:
                    if day == inter_day:
                        inout.append(data["price"])
        total = sum(inout)
        return total
        
    if kind == 4:
        for data in json_datas:
            if not data:
                continue
            cate = data["category"]
            if cate == interval:
                inout.append(data["price"])
        total = sum(inout)
        return total

def get_category_name():
    cate = []
    
    with open(db_file, "r") as f:
        json_datas = json.load(f)
    
    for data in json_datas:
        if not data:
            continue
        cate.append(data["category"])
        
    return list(set(cate))

def return_df(kind, interval):
    j_data = read_model(kind, interval)
    df = json_normalize(j_data)
    return df

def chart_data(df):
    df = df.sort_values("date")
    df = df.pivot_table(index="date", columns="category", values="price")
    df = df.apply(lambda x: x.sum(), axis=1)
    df = pd.DataFrame(df, columns=["price"]).reset_index()
    df["total"] = 0
    total = 0
    for i, price in enumerate(df["price"]):
        total += price
        df["total"][i] = total
    chart = alt.Chart(df).mark_line(clip=True).encode(
            x='date:T',
            y='total:Q'
        ).interactive()
    return chart