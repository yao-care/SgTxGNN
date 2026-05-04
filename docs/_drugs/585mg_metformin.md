---
layout: default
title: 585Mg Metformin
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 0
---

# 585Mg Metformin
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

# Metformin: 資料品質問題 — 老藥新用分析待執行

## One-Sentence Summary

本候選藥品記錄的 INN 欄位為異常字串「585MG METFORMIN)」，其中包含劑量數值與多餘括號，顯示資料進入管線前即已損壞。TxGNN 模型未返回任何預測新適應症，新加坡 HSA 亦無對應上市紀錄，因此無法完成完整的老藥新用評估。

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | 無法取得 |
| Predicted New Indication | 無 |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5（僅模型紀錄，無實際研究連結） |
| Singapore Market Status | 未上市 |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

TxGNN 未返回任何預測適應症，因此無法建立機轉關聯性論述。

Query Log 顯示 DrugBank 查詢成功取得 1 筆結果（`result_status: success`），表示底層藥物在 DrugBank 中可被識別，極可能對應 Metformin（二甲雙胍，雙胍類口服降血糖藥）。然而，INN 欄位中混入劑量字串「585MG」及多餘的閉括號「)」，導致藥名正規化（normalizer）與 DrugBank 映射流程無法正確識別藥物 ID，進而使 KG 與 DL 預測步驟均未能產出候選適應症。

此問題屬於**上游資料品質問題**，應在資料清洗層修正後重新執行 Evidence Pack 管線，而非在報告層補救。

---

## Clinical Trial Evidence

目前無相關臨床試驗（因預測適應症為空，無法查詢對應試驗）。

---

## Literature Evidence

目前無相關文獻（因預測適應症為空，無法查詢對應文獻）。

---

## Singapore Market Information

新加坡 HSA 無此候選藥品的上市登記紀錄。

> **注意**：Metformin 為全球廣泛上市的第一線 2 型糖尿病用藥，新加坡應有對應的 HSA 登記。INN 欄位異常可能導致查詢比對失敗，建議以正確藥名「metformin」重新查詢 HSA 資料庫。

---

## Safety Considerations

請參閱藥品仿單的警告與注意事項。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
藥品 INN 欄位「585MG METFORMIN)」為異常字串，導致預測管線、法規查詢、安全性擷取三個流程全部失敗，本 Evidence Pack 不具備可評估的內容。

**To proceed, the following is needed:**

- **修正 INN 欄位**：將「585MG METFORMIN)」更正為標準 INN「metformin」，追查資料源頭（HSA 原始資料或前處理腳本）中的解析邏輯，防止同類問題重複發生
- **取得 DrugBank ID**：DrugBank 查詢已回傳 1 筆結果，從該結果取得正確的 `DB:XXXXXX` ID 並寫入 Evidence Pack
- **重跑 KG + DL 預測**：以正確藥物 ID 重新執行 `run_kg_prediction.py`，取得 TxGNN 預測適應症清單
- **重查 HSA 上市資料**：以「metformin」為鍵值重新查詢新加坡 HSA 登記，補齊法規章節
- **補充安全性資料**：下載新加坡仿單 PDF，解析警語、禁忌與 MOA（對應 DG001、DG002 資料缺口）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

