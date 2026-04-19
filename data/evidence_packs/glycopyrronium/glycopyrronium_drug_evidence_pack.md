# Glycopyrronium 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Glycopyrronium | |
| DrugBank ID | DB00986 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | irritable bowel syndrome | 98.84% | L4 | 0 | 1 | S1 | Research Question |
| 2 | cauda equina syndrome | 98.51% | L5 | 0 | 0 | S0 | Hold |
| 3 | obsolete neurogenic bladder (disease) | 97.73% | L4 | 0 | 0 | S1 | Research Question |
| 4 | neurocirculatory asthenia | 96.91% | L5 | 0 | 0 | S0 | Hold |
| 5 | migraine disorder | 96.08% | L5 | 0 | 1 | S0 | Hold |
| 6 | migraine with brainstem aura | 95.68% | L5 | 0 | 0 | S0 | Hold |
| 7 | open-angle glaucoma | 95.61% | L5 | 0 | 0 | S0 | Hold |
| 8 | autonomic nervous system disease | 95.55% | L3 | 2 | 18 | S2 | Proceed with Guardrails |
| 9 | primary hereditary glaucoma | 95.30% | L5 | 0 | 0 | S0 | Hold |
| 10 | dysthymic disorder | 93.68% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Glycopyrronium | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Glycopyrronium | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Glycopyrronium, disease=irritable bowel syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Glycopyrronium, disease=irritable bowel syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Glycopyrronium, disease=irritable bowel syndrome | success | 1 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Glycopyrronium, disease=cauda equina syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Glycopyrronium, disease=cauda equina syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Glycopyrronium, disease=cauda equina syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Glycopyrronium, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Glycopyrronium, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Glycopyrronium, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Glycopyrronium, disease=neurocirculatory asthenia | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Glycopyrronium, disease=neurocirculatory asthenia | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Glycopyrronium, disease=neurocirculatory asthenia | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Glycopyrronium, disease=migraine disorder | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Glycopyrronium, disease=migraine disorder | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Glycopyrronium, disease=migraine disorder | success | 1 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Glycopyrronium, disease=migraine with brainstem aura | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Glycopyrronium, disease=migraine with brainstem aura | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Glycopyrronium, disease=migraine with brainstem aura | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Glycopyrronium, disease=open-angle glaucoma | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Glycopyrronium, disease=open-angle glaucoma | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Glycopyrronium, disease=open-angle glaucoma | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Glycopyrronium, disease=autonomic nervous system disease | success | 2 |  |
| 25 | ictrp | 2026-03-10 | drug=Glycopyrronium, disease=autonomic nervous system disease | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Glycopyrronium, disease=autonomic nervous system disease | success | 18 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Glycopyrronium, disease=primary hereditary glaucoma | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Glycopyrronium, disease=primary hereditary glaucoma | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Glycopyrronium, disease=primary hereditary glaucoma | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Glycopyrronium, disease=dysthymic disorder | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Glycopyrronium, disease=dysthymic disorder | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Glycopyrronium, disease=dysthymic disorder | success | 0 |  |