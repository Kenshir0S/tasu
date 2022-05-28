import sys
from datetime import datetime
import os
import json


file_name = "datas.json"

def create_inout():
    day = input("日付を入力してください。例)20220527: ")
    if not day:
        day = datetime.today().date().strftime("%Y-%m-%d")
    else:
        while not day.isdigit():
            day = input("日付を入力してください。例)20220527: ")
        day = datetime.strptime(day, "%Y%m%d").date()
        day = day.strftime("%Y-%m-%d")
    print(day)
        
    category = input("カテゴリを入力してください。: ")
    if not category:
        category = "なし"
    print(category)
        
    in_out = input("収入:0 支出:1 を入力してください。: ")
    while in_out != '0' and in_out != '1':
        in_out = input("収入:0 支出:1 を入力してください。: ")
    print(in_out)
    
    price = input("金額を入力してください。: ")
    while not price.isdigit():
        price = input("金額を入力してください。: ")
    if in_out == "1":
        if int(price) < 0:
            price = int(price)
        else:
            price = int(price) * -1
    else:
        if int(price) < 0:
            price = int(price) * -1
        else:
            price = int(price)
    print(f"¥{price:,}")
        
    dic = {
        "date": day,
        "category": category,
        "in_out": in_out,
        "price": price
    }
        
    with open(file_name, "r") as f:
        json_datas = json.load(f)
    dic["id"] = len(json_datas)
    json_datas.append(dic)
    with open(file_name, "w") as f:
        json.dump(json_datas, f, indent=4, ensure_ascii=False)
        
        
def show_inout(kind, interval):
    with open(file_name, "r") as f:
        json_datas = json.load(f)

    if kind == 0:
        for data in json_datas:
            if not data:
                continue
            print(data)
        
    if kind == 1:
        interval = datetime.strptime(interval, "%Y")
        inter_year = interval.year
        for data in json_datas:
            if not data:
                continue
            date = datetime.strptime(data["date"], "%Y-%m-%d")
            year = date.year
            if year == inter_year:
                print(data)
    
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
                    print(data)
        
    if kind == 3:
        interval = datetime.strptime(interval, "%Y%m%d")
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
                        print(data)
        
    if kind == 4:
        for data in json_datas:
            if not data:
                continue
            cate = data["category"]
            if cate == interval:
                print(data)
        
        
def edit_inout(id):
    id = int(id)
    with open(file_name, "r") as f:
        json_datas = json.load(f)
        
    day = input("更新後の日付を入力してください。例)20220527: ")
    default_day = json_datas[id]["date"]
    if not day:
        day = default_day
    else:
        while not day.isdigit():
            day = input("更新後の日付を入力してください。例)20220527: ")
        day = datetime.strptime(day, "%Y%m%d").date()
        day = day.strftime("%Y-%m-%d")
    print(f"{default_day} -> {day}")
        
    category = input("更新後のカテゴリを入力してください。: ")
    default_category = json_datas[id]["category"]
    if not category:
        category = default_category
    print(f"{default_category} -> {category}")
        
    in_out = input("更新後の収入:0 支出:1 を入力してください。: ")
    default_in_out = json_datas[id]["in_out"]
    if not in_out:
        in_out = default_in_out
    else:
        while in_out != '0' and in_out != '1':
            in_out = input("更新後の収入:0 支出:1 を入力してください。: ")
    print(f"{default_in_out} -> {in_out}")
    
    price = input("更新後の金額を入力してください。: ")
    default_price = json_datas[id]["price"]
    if not price:
        price = default_price
    else:
        while not price.isdigit():
            price = input("更新後の金額を入力してください。: ")
    if in_out == "1":
        price = int(price) * -1
    else:
        price = int(price)
    print(f"{default_price} -> {price}")
    
    update_dic = {
        "date": day,
        "category": category,
        "in_out": in_out,
        "price": price
    }
                        
    json_datas[id].update(update_dic)
    with open(file_name, "w") as f:
        json.dump(json_datas, f, indent=4, ensure_ascii=False)
                
    print(f"id={id}を更新しました。")
            
            
def delete_inout(id):
    with open(file_name, "r") as f:
        json_datas = json.load(f)
    
    for data in json_datas:
        if not data:
                continue
        if data["id"] == int(id):
            with open(file_name, "r") as f:
                json_datas = json.load(f)
            json_datas[int(id)].clear()
            with open(file_name, "w") as f:
                json.dump(json_datas, f, indent=4, ensure_ascii=False)
                
    print(f"id={id}を削除しました。")

        
def total_inout(kind, interval):
    inout = []
    
    with open(file_name, "r") as f:
        json_datas = json.load(f)

    if kind == 0:
        for data in json_datas:
            if not data:
                continue
            inout.append(data["price"])
        total = sum(inout)
        print(f"全体合計金額: ¥{total:,}")
        
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
        interval = interval.strftime("%Y年")
        print(f"{interval}合計金額: ¥{total:,}")
    
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
        interval = interval.strftime("%Y年%m月")
        print(f"{interval}合計金額: ¥{total:,}")
        
    if kind == 3:
        interval = datetime.strptime(interval, "%Y%m%d")
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
        interval = interval.strftime("%Y年%m月%d日")
        print(f"{interval}合計金額: ¥{total:,}")
        
    if kind == 4:
        for data in json_datas:
            if not data:
                continue
            cate = data["category"]
            if cate == interval:
                inout.append(data["price"])
        total = sum(inout)
        print(f"{interval}合計金額: ¥{total:,}")


def main():
    argv = sys.argv
    argc = len(argv)
    if argc != 2:
        print("USAGE: python3 file_name.py [command]")
        exit()
        
    if not (argv[1] == "-c" or argv[1] == "-e" or argv[1] == "-d" or argv[1] == "-t" or argv[1] == "-s" or argv[1] == "-h"):
        print("USAGE: python3 file_name.py -h(ヘルプ)")
        exit()
        
    if argv[1] == "-h":
        print("USAGE: python3 file_name.py [-c(登録)] or [-e(編集)] or [-d(削除)] or [-t(合計金額)] or [-s(表示)] or [-h(ヘルプ)]")
        exit()
    
    if not os.path.isfile(file_name):
        with open(file_name, "w") as f:
            json.dump([], f, indent=4, ensure_ascii=False)
            
    if argv[1] == "-c":
        create_inout()
    
    if argv[1] == "-e":
        id = input("どのidの内容を変更しますか？: ")
        while not id.isdigit():
            id = input("どのidの内容を変更しますか？: ")
        edit_inout(id)
        
    if argv[1] == "-d":
        id = input("どのidの内容を削除しますか？: ")
        while not id.isdigit():
            id = input("どのidの内容を削除しますか？: ")
        delete_inout(id)
        
    if argv[1] == "-t":
        kind = input("何についての合計金額を表示しますか？(全体:0 年別:1 月別:2 日別:3 カテゴリ別:4): ")
        while not kind.isdigit():
            kind = input("何についての合計金額を表示しますか？(全体:0 年別:1 月別:2 日別:3 カテゴリ別:4): ")
        kind = int(kind)
        if not (kind == 0 or kind == 1 or kind == 2 or kind == 3 or kind == 4):
            exit()
            
        if kind == 0:
            interval = 0
        if kind == 1:
            interval = input("年 (例: 2022): ")
            while not interval.isdigit() or len(interval) != 4:
                interval = input("年 (例: 2022): ")
        if kind == 2:
            interval = input("年月 (例: 202205): ")
            while not interval.isdigit() or len(interval) != 6:
                interval = input("年月 (例: 202205): ")
        if kind == 3:
            interval = input("年月日 (例: 20220527): ")
            while not interval.isdigit() or len(interval) != 8:
                interval = input("年月日 (例: 20220527): ")
        if kind == 4:
            interval = input("カテゴリ名 (例: 雑費): ")
            
        total_inout(kind, interval)
        
    if argv[1] == "-s":
        kind = input("何についての内容を表示しますか？(全体:0 年別:1 月別:2 日別:3 カテゴリ別:4): ")
        while not kind.isdigit():
            kind = input("何についての内容を表示しますか？(全体:0 年別:1 月別:2 日別:3 カテゴリ別:4): ")
        kind = int(kind)
        if not (kind == 0 or kind == 1 or kind == 2 or kind == 3 or kind == 4):
            exit()
            
        if kind == 0:
            interval = 0
        if kind == 1:
            interval = input("年 (例: 2022): ")
            while not interval.isdigit() or len(interval) != 4:
                interval = input("年 (例: 2022): ")
        if kind == 2:
            interval = input("年月 (例: 202205): ")
            while not interval.isdigit() or len(interval) != 6:
                interval = input("年月 (例: 202205): ")
        if kind == 3:
            interval = input("年月日 (例: 20220527): ")
            while not interval.isdigit() or len(interval) != 8:
                interval = input("年月日 (例: 20220527): ")
        if kind == 4:
            interval = input("カテゴリ名 (例: 雑費): ")
            
        show_inout(kind, interval)
    

if __name__ == '__main__':
    main()