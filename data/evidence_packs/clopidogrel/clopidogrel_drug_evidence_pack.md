# Clopidogrel 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Clopidogrel | |
| DrugBank ID | DB00758 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | migraine with brainstem aura | 99.44% | L3 | 0 | 16 | S2 | Research Question |
| 2 | migraine disorder | 99.44% | L2 | 8 | 20 | S2 | Proceed with Guardrails |
| 3 | osteoarthritis | 99.25% | L5 | 1 | 13 | S0 | Hold |
| 4 | tendinitis | 99.17% | L5 | 0 | 2 | S0 | Hold |
| 5 | myositis fibrosa | 99.13% | L5 | 0 | 0 | S0 | Hold |
| 6 | idiopathic granulomatous myositis | 99.13% | L5 | 0 | 0 | S0 | Hold |
| 7 | rheumatoid arthritis | 99.03% | L4 | 0 | 20 | S1 | Hold |
| 8 | osteoarthritis susceptibility | 99.01% | L5 | 0 | 1 | S0 | Hold |
| 9 | pseudoachondroplasia | 98.93% | L5 | 0 | 0 | S0 | Hold |
| 10 | fibromyalgia | 98.93% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Clopidogrel | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Clopidogrel | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Clopidogrel, disease=migraine with brainstem aura | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Clopidogrel, disease=migraine with brainstem aura | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Clopidogrel, disease=migraine with brainstem aura | success | 16 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Clopidogrel, disease=migraine disorder | success | 8 |  |
| 7 | ictrp | 2026-03-10 | drug=Clopidogrel, disease=migraine disorder | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Clopidogrel, disease=migraine disorder | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Clopidogrel, disease=osteoarthritis | success | 1 |  |
| 10 | ictrp | 2026-03-10 | drug=Clopidogrel, disease=osteoarthritis | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Clopidogrel, disease=osteoarthritis | success | 13 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Clopidogrel, disease=tendinitis | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Clopidogrel, disease=tendinitis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Clopidogrel, disease=tendinitis | success | 2 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Clopidogrel, disease=myositis fibrosa | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Clopidogrel, disease=myositis fibrosa | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Clopidogrel, disease=myositis fibrosa | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Clopidogrel, disease=idiopathic granulomatous myositis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Clopidogrel, disease=idiopathic granulomatous myositis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Clopidogrel, disease=idiopathic granulomatous myositis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Clopidogrel, disease=rheumatoid arthritis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Clopidogrel, disease=rheumatoid arthritis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Clopidogrel, disease=rheumatoid arthritis | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Clopidogrel, disease=osteoarthritis susceptibility | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Clopidogrel, disease=osteoarthritis susceptibility | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Clopidogrel, disease=osteoarthritis susceptibility | success | 1 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Clopidogrel, disease=pseudoachondroplasia | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Clopidogrel, disease=pseudoachondroplasia | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Clopidogrel, disease=pseudoachondroplasia | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Clopidogrel, disease=fibromyalgia | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Clopidogrel, disease=fibromyalgia | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Clopidogrel, disease=fibromyalgia | success | 0 |  |