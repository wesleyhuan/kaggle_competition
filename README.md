# Kaggle Competition Solutions

這個倉庫包含一系列Kaggle競賽的解決方案，涵蓋從初級到進階的機器學習工程實踐。

## 📋 項目結構

### Season 6
- **[beginer-level-eda-season-6-episode-1.ipynb](beginer-level-eda-season-6-episode-1.ipynb)**
  - 學生考試成績資料集的基礎EDA分析
  - 探索學習時數、睡眠品質和出勤率等特徵分佈
  - 建議序數編碼和三個交互特徵：sleep_hours_quality、facility_rating_attendance、study_method_hours
  - 包含可重用的Preprocessor類別

- **[baseline-xgb-of-season-6-episode-1.ipynb](baseline-xgb-of-season-6-episode-1.ipynb)**
  - 學生考試成績預測的XGBoost迴歸模型
  - 使用OPTUNA進行超參數搜尋（30次試驗），最佳RMSE: 8.75
  - 創建三個交互特徵：sleep_hours_quality、facility_rating_attendance、study_method_hours
  - 包含中位數填補和序數編碼前處理

- **[basic-eda-season-6-episode-2.ipynb](basic-eda-season-6-episode-2.ipynb)**
  - 心臟病資料集的基礎EDA分析 (Episode 2)
  - 分析年齡、血壓、膽固醇、最大心率等特徵的相關性
  - 識別BP_Age_Product為重要交互特徵
  - 建議對分類特徵使用One-Hot編碼，對數值特徵使用標準化

- **[baseline-xgb-season-6-episode-2.ipynb](baseline-xgb-season-6-episode-2.ipynb)**
  - 心臟病預測的XGBoost迴歸模型 (Episode 2)
  - 使用OPTUNA進行超參數搜尋，輸出概率預測
  - 創建BP_Age_Product交互特徵
  - One-Hot編碼分類特徵，StandardScaler標準化數值特徵

- **[basic-eda-season-6-episode-3.ipynb](basic-eda-season-6-episode-3.ipynb)**
  - 客戶流失資料集的基礎EDA分析 (Episode 3)
  - 大型資料集（594K筆訓練樣本）的特徵分佈和相關性分析
  - 識別重要交互特徵 Monthly_Fee_Ratio
  - 包含可重用的Preprocessor類別

- **[baseline-xgb-season-6-episode-3.ipynb](baseline-xgb-season-6-episode-3.ipynb)**
  - 客戶流失預測的XGBoost迴歸模型 (Episode 3)
  - 使用OPTUNA進行超參數搜尋，最佳RMSE: 0.3082
  - 包含二元編碼、分類替換和One-Hot編碼前處理
  - 創建Monthly_Fee_Ratio交互特徵

- **[baseline-xgb-classification-season-6-episode-3.ipynb](baseline-xgb-classification-season-6-episode-3.ipynb)**
  - 客戶流失預測的XGBoost分類模型 (Episode 3)
  - 使用XGBClassifier搭配StratifiedKFold處理不平衡類別（1:4流失比例）
  - 使用OPTUNA進行超參數搜尋，最佳AUC: 0.9164
  - 輸出概率預測值（0.0-1.0）

- **[basic-eda-season-6-episode-4.ipynb](basic-eda-season-6-episode-4.ipynb)**
  - 農業灌溉資料集的基礎EDA分析 (Episode 4)
  - 21個特徵的分佈分析，包含土壤屬性、作物類型和灌溉資料
  - 建議對排序特徵使用序數映射（如Crop_Growth_Stage），對名義特徵使用One-Hot編碼
  - 提供溫度×日照時數等交互特徵建議

### Season 5
- **[beginer-friendly-solution-season-5-episode-10.ipynb](beginer-friendly-solution-season-5-episode-10.ipynb)**
  - 道路事故風險預測的初學者友善完整解決方案（517K筆訓練樣本）
  - 包含多項式特徵工程（車道數和曲率交互）
  - 分析不同n_estimators值（10-290）找出最佳設定，MAE: 0.0436
  - 涵蓋資料探索、視覺化、預處理、特徵工程到提交的完整流程

- **[easy-and-simple-solution-season-5-episode-11.ipynb](easy-and-simple-solution-season-5-episode-11.ipynb)**
  - 貸款違約預測的簡潔XGBoost分類解決方案
  - 創建衍生特徵：income_loan_ratio、total_debt、available_income
  - 使用OPTUNA（50次試驗）以AUC為指標進行超參數調優
  - 函數式前處理（非類別式），程式碼風格簡潔易讀

- **[easy-and-simple-solution-season-5-episode-12.ipynb](easy-and-simple-solution-season-5-episode-12.ipynb)**
  - 糖尿病預測的XGBoost分類解決方案
  - 創建6個醫學相關交互特徵：pulse_pressure、cholesterol_ratio、ldl_hdl_ratio等
  - 使用OPTUNA（50次試驗）和StratifiedKFold進行超參數調優
  - 輸出概率預測值

- **[improve-solution-season-5-episode-12.ipynb](improve-solution-season-5-episode-12.ipynb)**
  - 糖尿病預測的改進版本，OOF AUC: 0.7259
  - 跳過EDA部分（參考原始筆記本）
  - 引入進階技巧：
    - 基於醫學領域知識的強化特徵工程
    - Out-of-Fold (OOF) 預測集成提升泛化能力
  - 使用tree_method='hist'加速訓練，含早停機制

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
6. 比較 `baseline-xgb-season-6-episode-3.ipynb`（迴歸）和 `baseline-xgb-classification-season-6-episode-3.ipynb`（分類）的差異
7. 學習 `improve-solution-season-5-episode-12.ipynb` 中的進階技巧

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
