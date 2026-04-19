# Clobetasol 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Clobetasol | |
| DrugBank ID | DB11750 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | primary cutaneous T-cell lymphoma | 99.51% | L3 | 0 | 20 | S2 | Proceed with Guardrails |
| 2 | lymphosarcoma | 98.88% | L3 | 1 | 20 | S2 | Research Question |
| 3 | cystic teratoma | 98.88% | L5 | 0 | 0 | S0 | Hold |
| 4 | Crohn's colitis | 98.88% | L4 | 0 | 13 | S1 | Hold |
| 5 | spinal cord dermoid cyst | 98.87% | L5 | 0 | 0 | S0 | Hold |
| 6 | disease of orbital part of eye adnexa | 98.86% | L5 | 0 | 0 | S0 | Hold |
| 7 | disease of orbital region | 98.77% | L4 | 3 | 0 | S1 | Hold |
| 8 | dermoid cyst of ovary | 98.74% | L5 | 0 | 0 | S0 | Hold |
| 9 | candidiasis | 98.60% | L4 | 2 | 20 | S1 | Hold |
| 10 | polyp of vocal cord | 98.59% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Clobetasol | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Clobetasol | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Clobetasol, disease=primary cutaneous T-cell lymphoma | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Clobetasol, disease=primary cutaneous T-cell lymphoma | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Clobetasol, disease=primary cutaneous T-cell lymphoma | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Clobetasol, disease=lymphosarcoma | success | 1 |  |
| 7 | ictrp | 2026-03-10 | drug=Clobetasol, disease=lymphosarcoma | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Clobetasol, disease=lymphosarcoma | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Clobetasol, disease=cystic teratoma | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Clobetasol, disease=cystic teratoma | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Clobetasol, disease=cystic teratoma | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Clobetasol, disease=Crohn's colitis | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Clobetasol, disease=Crohn's colitis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Clobetasol, disease=Crohn's colitis | success | 13 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Clobetasol, disease=spinal cord dermoid cyst | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Clobetasol, disease=spinal cord dermoid cyst | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Clobetasol, disease=spinal cord dermoid cyst | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Clobetasol, disease=disease of orbital part of eye adnexa | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Clobetasol, disease=disease of orbital part of eye adnexa | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Clobetasol, disease=disease of orbital part of eye adnexa | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Clobetasol, disease=disease of orbital region | success | 3 |  |
| 22 | ictrp | 2026-03-10 | drug=Clobetasol, disease=disease of orbital region | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Clobetasol, disease=disease of orbital region | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Clobetasol, disease=dermoid cyst of ovary | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Clobetasol, disease=dermoid cyst of ovary | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Clobetasol, disease=dermoid cyst of ovary | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Clobetasol, disease=candidiasis | success | 2 |  |
| 28 | ictrp | 2026-03-10 | drug=Clobetasol, disease=candidiasis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Clobetasol, disease=candidiasis | success | 20 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Clobetasol, disease=polyp of vocal cord | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Clobetasol, disease=polyp of vocal cord | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Clobetasol, disease=polyp of vocal cord | success | 0 |  |