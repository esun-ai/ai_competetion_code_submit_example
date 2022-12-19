# 玉山人工智慧挑戰公開賽 程式碼繳交範例
請各組參賽者繳交程式碼與readme，需依照以下格式繳交:

## 資料夾結構:
- 繳交檔案需至少區分為***Preprocess***以及***Model***兩個資料夾，分別存放資料前處理以及模型相關程式
  - 如有其他不屬兩者的程式，可另行增加資料夾或檔案存放(需於readme中說明)。
- 需提供用到的套件與其版本(***requirements.txt***)
- 需提供***readme檔案***說明每個資料夾/檔案的用途
  - 需提供可復現模型結果之超參數設定以及資源配置 (若有使用GPU再提供資源配置即可)
- 程式碼限使用.py檔繳交
- 若使用非python之程式碼，以提供可閱讀且可執行之檔案為主

範例: (參考用，符合上述規則即可)
```
.
├ Preprocess
│ ├ x.py
│ ├ y.py
│ └ README
├ Model
│ ├ train.py
│ ├ inference.py
│ └ README
├ main.py
├ requirements.txt
└ README
```
## 程式碼檔案內容:
- 需於檔案最上方說明該程式碼之用途、input、output
- 每個class需撰寫docstring，說明該class之用途、input、output、attributes、method等
- 每個function需撰寫docstring，同樣說明該function之用途、input、output
  - class method 同樣需要說明
- 可參照範例程式
