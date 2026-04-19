# Ampicillin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Ampicillin | |
| DrugBank ID | DB00415 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | laryngitis | 99.97% | L3 | 1 | 20 | S1 | Research Question |
| 2 | gonococcal urethritis | 99.36% | L2 | 0 | 20 | S2 | Hold |
| 3 | Ureaplasma urethritis | 99.36% | L5 | 0 | 8 | S0 | Hold |
| 4 | chronic rhinosinusitis | 99.34% | L3 | 9 | 20 | S1 | Research Question |
| 5 | chronic ethmoidal sinusitis | 99.33% | L3 | 0 | 8 | S1 | Research Question |
| 6 | gingivitis | 99.28% | L3 | 2 | 20 | S1 | Research Question |
| 7 | paranasal sinus neoplasm (disease) | 99.20% | L5 | 0 | 3 | S0 | Hold |
| 8 | bacterial arthritis | 99.11% | L3 | 2 | 20 | S2 | Proceed with Guardrails |
| 9 | conjunctivitis | 99.04% | L3 | 1 | 20 | S1 | Research Question |
| 10 | pericoronitis | 99.04% | L3 | 0 | 20 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Ampicillin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Ampicillin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Ampicillin, disease=laryngitis | success | 1 |  |
| 4 | ictrp | 2026-03-09 | drug=Ampicillin, disease=laryngitis | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Ampicillin, disease=laryngitis | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Ampicillin, disease=gonococcal urethritis | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Ampicillin, disease=gonococcal urethritis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Ampicillin, disease=gonococcal urethritis | success | 20 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Ampicillin, disease=Ureaplasma urethritis | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Ampicillin, disease=Ureaplasma urethritis | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Ampicillin, disease=Ureaplasma urethritis | success | 8 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Ampicillin, disease=chronic rhinosinusitis | success | 9 |  |
| 13 | ictrp | 2026-03-09 | drug=Ampicillin, disease=chronic rhinosinusitis | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Ampicillin, disease=chronic rhinosinusitis | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Ampicillin, disease=chronic ethmoidal sinusitis | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Ampicillin, disease=chronic ethmoidal sinusitis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Ampicillin, disease=chronic ethmoidal sinusitis | success | 8 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Ampicillin, disease=gingivitis | success | 2 |  |
| 19 | ictrp | 2026-03-09 | drug=Ampicillin, disease=gingivitis | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Ampicillin, disease=gingivitis | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Ampicillin, disease=paranasal sinus neoplasm (disease) | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Ampicillin, disease=paranasal sinus neoplasm (disease) | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Ampicillin, disease=paranasal sinus neoplasm (disease) | success | 3 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Ampicillin, disease=bacterial arthritis | success | 2 |  |
| 25 | ictrp | 2026-03-09 | drug=Ampicillin, disease=bacterial arthritis | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Ampicillin, disease=bacterial arthritis | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Ampicillin, disease=conjunctivitis | success | 1 |  |
| 28 | ictrp | 2026-03-09 | drug=Ampicillin, disease=conjunctivitis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Ampicillin, disease=conjunctivitis | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Ampicillin, disease=pericoronitis | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Ampicillin, disease=pericoronitis | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Ampicillin, disease=pericoronitis | success | 20 |  |