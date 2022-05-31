# 家計簿管理アプリbyStreamlit

## 必要パッケージ

※必ずpipをインストールしてから、パッケージをインストールしてください。

pip (パッケージ管理システム)

python >= 3.7

pandas

streamlit (numpy, pandas, matplotlibが必要)

altair

## アプリ起動コマンド

streamlit run main.py

## 処理順序

main.py (画面表示設定、初期jsonファイル作成)

↓

rooting.py (ルーティング処理)

↓

views.py (modelとやり取りして、レンダリング)

↓ ↑

models.py (viewからの指示でjson(DB)とやり取りをして、必要な情報を返す)
