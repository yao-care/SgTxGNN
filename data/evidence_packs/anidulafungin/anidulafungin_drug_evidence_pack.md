# Anidulafungin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Anidulafungin | |
| DrugBank ID | DB00362 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | impetigo | 98.85% | L5 | 0 | 0 | S0 | Hold |
| 2 | malignant pleural mesothelioma | 98.75% | L5 | 0 | 0 | S0 | Hold |
| 3 | staphylococcal scalded skin syndrome | 98.73% | L5 | 0 | 0 | S0 | Hold |
| 4 | pleural empyema (disease) | 98.52% | L4 | 0 | 1 | S0 | Hold |
| 5 | malignant visceral pleura tumor | 98.45% | L5 | 0 | 0 | S0 | Hold |
| 6 | bullous impetigo | 98.40% | L5 | 0 | 0 | S0 | Hold |
| 7 | malignant epithelioid mesothelioma | 98.37% | L5 | 0 | 0 | S0 | Hold |
| 8 | sarcomatoid mesothelioma | 98.26% | L5 | 0 | 0 | S0 | Hold |
| 9 | hordeolum | 98.23% | L5 | 0 | 0 | S0 | Hold |
| 10 | Clostridium infectious disease | 98.22% | L5 | 0 | 1 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Anidulafungin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Anidulafungin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Anidulafungin, disease=impetigo | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Anidulafungin, disease=impetigo | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Anidulafungin, disease=impetigo | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Anidulafungin, disease=malignant pleural mesothelioma | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Anidulafungin, disease=malignant pleural mesothelioma | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Anidulafungin, disease=malignant pleural mesothelioma | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Anidulafungin, disease=staphylococcal scalded skin syndrome | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Anidulafungin, disease=staphylococcal scalded skin syndrome | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Anidulafungin, disease=staphylococcal scalded skin syndrome | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Anidulafungin, disease=pleural empyema (disease) | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Anidulafungin, disease=pleural empyema (disease) | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Anidulafungin, disease=pleural empyema (disease) | success | 1 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Anidulafungin, disease=malignant visceral pleura tumor | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Anidulafungin, disease=malignant visceral pleura tumor | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Anidulafungin, disease=malignant visceral pleura tumor | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Anidulafungin, disease=bullous impetigo | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Anidulafungin, disease=bullous impetigo | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Anidulafungin, disease=bullous impetigo | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Anidulafungin, disease=malignant epithelioid mesothelioma | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Anidulafungin, disease=malignant epithelioid mesothelioma | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Anidulafungin, disease=malignant epithelioid mesothelioma | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Anidulafungin, disease=sarcomatoid mesothelioma | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Anidulafungin, disease=sarcomatoid mesothelioma | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Anidulafungin, disease=sarcomatoid mesothelioma | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Anidulafungin, disease=hordeolum | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Anidulafungin, disease=hordeolum | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Anidulafungin, disease=hordeolum | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Anidulafungin, disease=Clostridium infectious disease | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Anidulafungin, disease=Clostridium infectious disease | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Anidulafungin, disease=Clostridium infectious disease | success | 1 |  |