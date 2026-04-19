# Azelaic acid 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Azelaic acid | |
| DrugBank ID | DB00548 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | demodicidosis of sebaceous gland | 98.05% | L5 | 0 | 0 | S0 | Hold |
| 2 | cutaneous candidiasis | 95.63% | L5 | 0 | 0 | S0 | Hold |
| 3 | lichen planus, familial | 95.45% | L5 | 0 | 0 | S0 | Hold |
| 4 | zinc, elevated plasma | 94.68% | L5 | 0 | 0 | S0 | Hold |
| 5 | isolated congenital adermatoglyphia | 94.03% | L5 | 0 | 0 | S0 | Hold |
| 6 | keratinization disease | 93.80% | L4 | 0 | 7 | S1 | Research Question |
| 7 | seborrheic dermatitis | 93.53% | L2 | 1 | 11 | S2 | Proceed with Guardrails |
| 8 | nail infection | 93.53% | L5 | 0 | 1 | S0 | Hold |
| 9 | tinea corporis | 93.07% | L4 | 0 | 3 | S0 | Hold |
| 10 | Beare-Stevenson cutis gyrata syndrome | 92.59% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Azelaic acid | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Azelaic acid | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Azelaic acid, disease=demodicidosis of sebaceous gland | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Azelaic acid, disease=demodicidosis of sebaceous gland | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Azelaic acid, disease=demodicidosis of sebaceous gland | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Azelaic acid, disease=cutaneous candidiasis | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Azelaic acid, disease=cutaneous candidiasis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Azelaic acid, disease=cutaneous candidiasis | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Azelaic acid, disease=lichen planus, familial | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Azelaic acid, disease=lichen planus, familial | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Azelaic acid, disease=lichen planus, familial | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Azelaic acid, disease=zinc, elevated plasma | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Azelaic acid, disease=zinc, elevated plasma | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Azelaic acid, disease=zinc, elevated plasma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Azelaic acid, disease=isolated congenital adermatoglyphia | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Azelaic acid, disease=isolated congenital adermatoglyphia | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Azelaic acid, disease=isolated congenital adermatoglyphia | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Azelaic acid, disease=keratinization disease | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Azelaic acid, disease=keratinization disease | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Azelaic acid, disease=keratinization disease | success | 7 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Azelaic acid, disease=seborrheic dermatitis | success | 1 |  |
| 22 | ictrp | 2026-03-09 | drug=Azelaic acid, disease=seborrheic dermatitis | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Azelaic acid, disease=seborrheic dermatitis | success | 11 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Azelaic acid, disease=nail infection | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Azelaic acid, disease=nail infection | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Azelaic acid, disease=nail infection | success | 1 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Azelaic acid, disease=tinea corporis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Azelaic acid, disease=tinea corporis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Azelaic acid, disease=tinea corporis | success | 3 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Azelaic acid, disease=Beare-Stevenson cutis gyrata syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Azelaic acid, disease=Beare-Stevenson cutis gyrata syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Azelaic acid, disease=Beare-Stevenson cutis gyrata syndrome | success | 0 |  |