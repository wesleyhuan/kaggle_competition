# Kaggle Competition Solutions

這個倉庫包含一系列Kaggle競賽的解決方案，涵蓋從初級到進階的機器學習工程實踐。

## 📋 項目結構

### Season 6
- **[beginer-level-eda-season-6-episode-1.ipynb](beginer-level-eda-season-6-episode-1.ipynb)**
  - 基礎EDA (Exploratory Data Analysis) 分析
  - 探索資料特徵和分佈
  - 包含資料視覺化和相關性分析
  - 為後續的資料預處理和特徵工程提供決策依據

- **[baseline-xgb-of-season-6-episode-1.ipynb](baseline-xgb-of-season-6-episode-1.ipynb)**
  - XGBoost模型訓練與優化
  - 使用OPTUNA進行超參數搜尋
  - 基於EDA結果進行資料預處理和特徵工程
  - 包含資料載入、預處理、模型訓練和提交步驟

- **[basic-eda-season-6-episode-2.ipynb](basic-eda-season-6-episode-2.ipynb)**
  - 基礎EDA分析 (Episode 2)
  - 探索資料特徵和分佈
  - 包含資料視覺化和相關性分析
  - 為後續的資料預處理和特徵工程提供決策依據

- **[baseline-xgb-season-6-episode-2.ipynb](baseline-xgb-season-6-episode-2.ipynb)**
  - XGBoost模型訓練與優化 (Episode 2)
  - 使用OPTUNA進行超參數搜尋
  - 基於EDA結果進行資料預處理和特徵工程
  - 包含資料載入、預處理、模型訓練和提交步驟

- **[basic-eda-season-6-episode-3.ipynb](basic-eda-season-6-episode-3.ipynb)**
  - 基礎EDA分析 (Episode 3)
  - 探索資料特徵和分佈
  - 包含資料視覺化和相關性分析
  - 為後續的資料預處理和特徵工程提供決策依據

- **[baseline-xgb-season-6-episode-3.ipynb](baseline-xgb-season-6-episode-3.ipynb)**
  - XGBoost模型訓練與優化 (Episode 3)
  - 使用OPTUNA進行超參數搜尋
  - 基於EDA結果進行資料預處理和特徵工程
  - 包含資料載入、預處理、模型訓練和提交步驟

### Season 5
- **[beginer-friendly-solution-season-5-episode-10.ipynb](beginer-friendly-solution-season-5-episode-10.ipynb)**
  - 初學者友善的完整解決方案
  - 詳細的步驟說明和思路
  - 涵蓋資料探索、視覺化、預處理、特徵工程
  - 包含模型選擇、調優和提交

- **[easy-and-simple-solution-season-5-episode-11.ipynb](easy-and-simple-solution-season-5-episode-11.ipynb)**
  - 簡潔易讀的解決方案
  - 重點關注程式碼可讀性
  - 標準的機器學習工作流程
  - 適合學習和參考

- **[easy-and-simple-solution-season-5-episode-12.ipynb](easy-and-simple-solution-season-5-episode-12.ipynb)**
  - 易懂的第12集解決方案
  - 逐步展示完整的分析過程
  - 包含模型對比和優化策略

- **[improve-solution-season-5-episode-12.ipynb](improve-solution-season-5-episode-12.ipynb)**
  - 第12集的改進版本
  - 跳過EDA部分（參考原始筆記本）
  - 引入進階技巧：
    - 從相關性矩陣增加特徵
    - Out-of-Fold (OOF) 預測集成
  - 專注於性能提升

## 🛠 工作流程

每個notebook通常遵循以下步驟：

1. **資料載入和探索**
   - 讀取資料集
   - 初步統計和檢查

2. **資料視覺化**
   - 特徵分佈分析
   - 相關性矩陣
   - 異常值檢測

3. **資料預處理和清洗**
   - 缺失值處理
   - 異常值處理
   - 資料標準化/歸一化

4. **特徵工程**
   - 特徵建立和選擇
   - 基於相關性的特徵提取

5. **模型選擇和訓練**
   - 多種模型對比
   - 超參數調優 (使用OPTUNA)
   - K-fold交叉驗證

6. **模型評估和優化**
   - Out-of-Fold預測
   - 集成策略
   - 性能提升技巧

7. **提交結果**
   - 生成提交檔案
   - Kaggle提交

## 📊 技術棧

- **Python** - 編程語言
- **Pandas** - 資料處理和分析
- **NumPy** - 數值計算
- **Scikit-learn** - 機器學習庫
- **XGBoost** - 梯度提升模型
- **Matplotlib/Seaborn** - 資料視覺化
- **OPTUNA** - 超參數優化框架

## 🎯 學習路徑

### 初級
1. 從 `beginer-level-eda-season-6-episode-1.ipynb` 開始學習EDA
2. 查看 `beginer-friendly-solution-season-5-episode-10.ipynb` 了解完整工作流

### 中級
3. 學習 `easy-and-simple-solution-season-5-episode-11.ipynb` 中的簡潔程式碼風格
4. 參考 `easy-and-simple-solution-season-5-episode-12.ipynb` 的另一個實現

### 高級
5. 研究 `baseline-xgb-of-season-6-episode-1.ipynb` 中的XGBoost優化
6. 學習 `improve-solution-season-5-episode-12.ipynb` 中的進階技巧

## 💡 關鍵技巧

- **超參數優化**: 使用OPTUNA自動化超參數搜尋過程
- **特徵工程**: 透過相關性矩陣識別重要特徵
- **模型集成**: Out-of-Fold預測用於更穩定的預測
- **交叉驗證**: K-fold交叉驗證保證模型泛化能力
- **程式碼可讀性**: 編寫清晰、易維護的程式碼以便長期使用

## 📝 注意事項

- 部分notebook基於Kaggle上的資料集
- 具體資料集連結和資訊見各個notebook檔案
- 這些解決方案用於學習和參考，不作為生產環境程式碼

## 🚀 快速開始

1. 複製或下載此倉庫
2. 安裝必要的相依套件：
   ```bash
   pip install pandas numpy scikit-learn xgboost optuna matplotlib seaborn
   ```
3. 打開相應的`.ipynb`檔案在Jupyter Notebook中執行
4. 按照notebook中的步驟執行程式碼單元

## 📚 參考資源

- [Kaggle官網](https://www.kaggle.com/)
- [Pandas文檔](https://pandas.pydata.org/)
- [OPTUNA文檔](https://optuna.readthedocs.io/)
- [XGBoost文檔](https://xgboost.readthedocs.io/)

## 📄 授權條款

這些程式碼用於學習和研究目的。

---

**持續改進中** - 這個倉庫會隨著新的解決方案和改進而定期更新。
