# 玉山人工智慧挑戰公開賽 程式碼繳交範例
請各組參賽者繳交程式碼與readme，需依照以下格式繳交:

## 資料夾結構:
- 繳交檔案需至少區分為Preprocess以及Model兩個資料夾，如有其他不屬兩者的程式，可另行增加資料夾或檔案存放。
- 須提供用到的套件與其版本(requirements.txt)
- 需提供readme檔案說明每個資料夾/檔案的用途
- 程式碼可使用.py檔或者.ipynb檔格式繳交
- 如果為非python程式碼
```
範例: (參考用，符合上述規則即可)
.
├ Preprocess
│ ├ x.py
│ ├ y.py
│ └ Readme
├ Model
│ ├ train.py
│ ├ inference.py
│ └ Readme
├ main.py
├ requirements.txt
└ Readme
```
## 程式碼檔案內容:
- 需於檔案最上方說明該程式碼之用途、input、output
- 每個class需撰寫docstring，說明該class之用途、input、output、attributes、method等
- 每個function需撰寫docstring，同樣說明該function之用途、input、output
  - class method 同樣需要說明
- 可參照範例程式
