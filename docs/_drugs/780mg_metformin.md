---
layout: default
title: 780Mg Metformin
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 0
---

# 780Mg Metformin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Metformin：資料不完整，無法產生老藥新用評估報告

---

## 一句話摘要

本 Evidence Pack 的藥物名稱欄位存在解析錯誤（原始值為 `"780MG METFORMIN)"`，疑似劑量資訊與藥物名稱混入同一欄位），導致 DrugBank ID 無法對應、預測適應症清單為空、新加坡藥監資料未收錄，**目前無法產生有效的老藥新用評估報告**。

---

## 快速概覽

| 項目 | 內容 |
|------|------|
| 資料狀態 | ⚠️ 藥物名稱解析錯誤 |
| 辨識藥物 | Metformin（推測，需確認） |
| 預測新適應症 | 無（predicted_indications 為空） |
| TxGNN 預測分數 | 無資料 |
| 證據等級 | 無法評估 |
| 新加坡市場狀態 | 未上市（資料缺失，待驗證） |
| 建議決策 | **Hold — 資料品質問題，需先修正輸入資料** |

---

## 資料品質問題說明

### 藥物名稱錯誤

Evidence Pack 中 `drug.inn` 欄位值為：

```
780MG METFORMIN)
```

此字串具有以下異常：
- 前綴 `780MG` 為劑量資訊，不應出現在 INN 名稱欄位
- 結尾有未閉合的右括號 `)`，疑似 PDF 或 OCR 解析殘留
- 正確的 INN 應為 **`metformin`**

### 連鎖影響

| 影響項目 | 狀態 |
|----------|------|
| DrugBank ID 對應 | 失敗（null） |
| MOA 資料 | 缺失（Data Gap） |
| TxGNN 預測 | 無輸出（predicted_indications 空陣列） |
| 安全性資料 | 全部缺失 |
| 新加坡藥監資料 | 無記錄 |

---

## 安全考量

目前所有安全性資料均缺失，無法評估：
- 藥物警語
- 禁忌症
- 藥物交互作用

> 請參閱原廠仿單之警語與注意事項。

---

## 結論與下一步

**決策：Hold**

**原因：**
輸入資料的藥物名稱欄位因解析錯誤包含劑量資訊與異常符號，導致整個評估流程無法執行，無任何預測適應症或安全性資料可供分析。

**繼續進行前，需完成以下事項：**

1. **修正藥物名稱**：將 `drug.inn` 從 `"780MG METFORMIN)"` 更正為 `"metformin"`，並重新執行資料擷取流程
2. **補充 DrugBank ID**：Metformin 的 DrugBank ID 為 `DB00331`，可直接填入重跑
3. **重新執行 TxGNN 預測**：修正輸入後，重新執行 KG + DL 預測流程以取得 predicted_indications
4. **確認新加坡上市狀態**：Metformin 在新加坡廣泛使用，需確認 HSA 登記資料是否因名稱錯誤而漏查
5. **補充 MOA 資料**（DG002）：從 DrugBank API 查詢 metformin 作用機轉
6. **補充警語與禁忌**（DG001）：查詢 HSA 或 DrugBank 的安全性資料

---

> ⚠️ **注意**：本報告因輸入資料品質問題而無法完整產生。建議優先排除資料解析錯誤後，重新提交 Evidence Pack。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

