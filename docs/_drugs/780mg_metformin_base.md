---
layout: default
title: 780Mg Metformin Base
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 0
---

# 780Mg Metformin Base
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

# 780MG METFORMIN BASE): 資料品質不足，無法完成老藥新用評估

> ⚠️ **注意**：本報告因輸入資料存在嚴重品質問題，無法按標準格式完整輸出。以下為資料缺口分析與建議行動。

---

## One-Sentence Summary

此 Evidence Pack 的藥物欄位（INN）包含非標準字串 `"780MG METFORMIN BASE)"`，疑似為劑量規格混入藥名欄位導致的解析錯誤，而非正確的國際非專利名稱。
由於藥物識別失敗，系統未能取得任何 TxGNN 預測指徵、新加坡上市資料或安全性資料，**目前無法執行老藥新用評估**。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| 輸入藥名（原始） | `780MG METFORMIN BASE)` ← 疑似解析錯誤 |
| 推測正確藥物 | Metformin（Metformin HCl，雙胍類降血糖藥） |
| 預測新適應症 | 無（predicted_indications 為空） |
| TxGNN 預測分數 | 無資料 |
| 證據等級 | L5（模型預測資料缺失） |
| 新加坡市場狀態 | 未上市（0 筆核准） |
| 許可證數量 | 0 |
| 建議決策 | **Hold** |

---

## Why is This Prediction Reasonable?

由於 `predicted_indications` 陣列為空，本節無法執行機轉關聯性分析。

若確認本案藥物為 **Metformin**，其作用機轉（AMPK 活化、肝醣新生抑制）在老藥新用領域具有豐富研究基礎（癌症、PCOS、NAFLD、神經退化性疾病等），**具備評估潛力**。但在藥物識別問題解決前，不應進行任何預測解讀。

---

## Clinical Trial Evidence

目前無相關臨床試驗資料（predicted_indications 為空，無法查詢）。

---

## Literature Evidence

目前無相關文獻資料（predicted_indications 為空，無法查詢）。

---

## Singapore Market Information

本次查詢未取得任何新加坡核准記錄（total_licenses: 0）。

若藥物識別確認為 Metformin，應重新執行查詢——Metformin 在新加坡為廣泛上市藥物，預期應有多筆 HSA 核准記錄。

---

## Safety Considerations

請參閱仿單警語與禁忌事項。安全性資料查詢未能返回結果，可能與藥物識別失敗有關。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
藥物識別欄位（INN）包含格式錯誤字串，導致 DrugBank 映射、TxGNN 預測、新加坡上市查詢及安全性評估全部失敗。在資料修正完成前，本案無任何可評估的預測證據。

**To proceed, the following is needed:**

1. **修正藥物識別問題（Blocking）**
   - 確認正確 INN：若為 Metformin，應輸入 `metformin`（全小寫、無括號、無劑量規格）
   - 重新觸發 Evidence Pack 生成流程

2. **補充 DrugBank ID（High）**
   - Metformin DrugBank ID 為 `DB00331`
   - 補入後可取得完整 MOA、藥物分類、安全性資料

3. **重新執行 TxGNN 預測**
   - 確認藥物識別後，重新生成 `predicted_indications`

4. **補充新加坡 HSA 資料（High）**
   - Metformin 在新加坡應有上市記錄，需重新查詢確認

5. **補充仿單安全資料（Blocking）**
   - 依 DG001 補救措施：下載仿單 PDF 解析警語與禁忌
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

