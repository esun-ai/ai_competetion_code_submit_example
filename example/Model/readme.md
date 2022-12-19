# 模型訓練
本資料夾內含兩個程式:
- train.py: 訓練模型
- inference.py: 使用訓練好的模型進行預測，並產生繳交的csv檔

## 參數設定
- 4-layer dnn
  - neuron: 128, 64, 32, 2
  - activation: relu，最後一層為softmax
  - loss: cross entropy
- batch size: 128
- epoch: 100
