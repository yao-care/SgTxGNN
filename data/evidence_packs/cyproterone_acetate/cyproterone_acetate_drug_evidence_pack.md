# Cyproterone acetate 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Cyproterone acetate | |
| DrugBank ID | DB04839 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | migraine disorder | 99.66% | L4 | 0 | 3 | S1 | Research Question |
| 2 | migraine with brainstem aura | 99.58% | L5 | 0 | 2 | S0 | Hold |
| 3 | Prinzmetal angina | 99.52% | L5 | 0 | 0 | S0 | Hold |
| 4 | antithrombin deficiency type 2 | 99.48% | L5 | 0 | 0 | S0 | Hold |
| 5 | heparin cofactor 2 deficiency | 99.45% | L5 | 0 | 0 | S0 | Hold |
| 6 | factor 5 excess with spontaneous thrombosis | 99.45% | L5 | 0 | 0 | S0 | Hold |
| 7 | migraine with or without aura, susceptibility to | 99.34% | L4 | 0 | 20 | S1 | Research Question |
| 8 | amenorrhea (disease) | 99.28% | L3 | 4 | 14 | S2 | Proceed with Guardrails |
| 9 | breast fibrocystic disease | 99.15% | L4 | 0 | 4 | S1 | Research Question |
| 10 | thrombophilia | 99.03% | L5 | 0 | 18 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Cyproterone acetate | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Cyproterone acetate | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Cyproterone acetate, disease=migraine disorder | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Cyproterone acetate, disease=migraine disorder | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Cyproterone acetate, disease=migraine disorder | success | 3 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Cyproterone acetate, disease=migraine with brainstem aura | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Cyproterone acetate, disease=migraine with brainstem aura | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Cyproterone acetate, disease=migraine with brainstem aura | success | 2 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Cyproterone acetate, disease=Prinzmetal angina | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Cyproterone acetate, disease=Prinzmetal angina | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Cyproterone acetate, disease=Prinzmetal angina | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Cyproterone acetate, disease=antithrombin deficiency type 2 | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Cyproterone acetate, disease=antithrombin deficiency type 2 | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Cyproterone acetate, disease=antithrombin deficiency type 2 | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Cyproterone acetate, disease=heparin cofactor 2 deficiency | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Cyproterone acetate, disease=heparin cofactor 2 deficiency | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Cyproterone acetate, disease=heparin cofactor 2 deficiency | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Cyproterone acetate, disease=factor 5 excess with spontaneous thrombosis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Cyproterone acetate, disease=factor 5 excess with spontaneous thrombosis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Cyproterone acetate, disease=factor 5 excess with spontaneous thrombosis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Cyproterone acetate, disease=migraine with or without aura, susceptibility to | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Cyproterone acetate, disease=migraine with or without aura, susceptibility to | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Cyproterone acetate, disease=migraine with or without aura, susceptibility to | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Cyproterone acetate, disease=amenorrhea (disease) | success | 4 |  |
| 25 | ictrp | 2026-03-10 | drug=Cyproterone acetate, disease=amenorrhea (disease) | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Cyproterone acetate, disease=amenorrhea (disease) | success | 14 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Cyproterone acetate, disease=breast fibrocystic disease | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Cyproterone acetate, disease=breast fibrocystic disease | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Cyproterone acetate, disease=breast fibrocystic disease | success | 4 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Cyproterone acetate, disease=thrombophilia | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Cyproterone acetate, disease=thrombophilia | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Cyproterone acetate, disease=thrombophilia | success | 18 |  |