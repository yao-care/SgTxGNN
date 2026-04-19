# Dexketoprofen 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Dexketoprofen | |
| DrugBank ID | DB09214 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | tendinitis | 99.90% | L3 | 0 | 1 | S1 | Research Question |
| 2 | fibromyalgia | 99.88% | L5 | 0 | 0 | S0 | Hold |
| 3 | myositis fibrosa | 99.88% | L5 | 0 | 0 | S0 | Hold |
| 4 | idiopathic granulomatous myositis | 99.88% | L5 | 0 | 0 | S0 | Hold |
| 5 | rheumatoid arthritis | 99.88% | L4 | 0 | 0 | S1 | Research Question |
| 6 | migraine disorder | 99.87% | L1 | 8 | 20 | S3 | Proceed with Guardrails |
| 7 | headache disorder | 99.86% | L1 | 12 | 20 | S3 | Proceed with Guardrails |
| 8 | migraine with brainstem aura | 99.86% | L2 | 0 | 8 | S2 | Proceed with Guardrails |
| 9 | exostosis | 99.85% | L5 | 0 | 0 | S0 | Hold |
| 10 | congenital hypotrichosis milia | 99.83% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Dexketoprofen | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Dexketoprofen | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Dexketoprofen, disease=tendinitis | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Dexketoprofen, disease=tendinitis | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Dexketoprofen, disease=tendinitis | success | 1 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Dexketoprofen, disease=fibromyalgia | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Dexketoprofen, disease=fibromyalgia | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Dexketoprofen, disease=fibromyalgia | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Dexketoprofen, disease=myositis fibrosa | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Dexketoprofen, disease=myositis fibrosa | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Dexketoprofen, disease=myositis fibrosa | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Dexketoprofen, disease=idiopathic granulomatous myositis | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Dexketoprofen, disease=idiopathic granulomatous myositis | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Dexketoprofen, disease=idiopathic granulomatous myositis | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Dexketoprofen, disease=rheumatoid arthritis | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Dexketoprofen, disease=rheumatoid arthritis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Dexketoprofen, disease=rheumatoid arthritis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Dexketoprofen, disease=migraine disorder | success | 8 |  |
| 19 | ictrp | 2026-03-09 | drug=Dexketoprofen, disease=migraine disorder | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Dexketoprofen, disease=migraine disorder | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Dexketoprofen, disease=headache disorder | success | 12 |  |
| 22 | ictrp | 2026-03-09 | drug=Dexketoprofen, disease=headache disorder | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Dexketoprofen, disease=headache disorder | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Dexketoprofen, disease=migraine with brainstem aura | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Dexketoprofen, disease=migraine with brainstem aura | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Dexketoprofen, disease=migraine with brainstem aura | success | 8 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Dexketoprofen, disease=exostosis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Dexketoprofen, disease=exostosis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Dexketoprofen, disease=exostosis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Dexketoprofen, disease=congenital hypotrichosis milia | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Dexketoprofen, disease=congenital hypotrichosis milia | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Dexketoprofen, disease=congenital hypotrichosis milia | success | 0 |  |