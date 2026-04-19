# Amphotericin B 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Amphotericin B | |
| DrugBank ID | DB00681 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | paranasal sinus neoplasm (disease) | 97.45% | L4 | 0 | 12 | S0 | Hold |
| 2 | chronic rhinosinusitis | 97.44% | L1 | 2 | 20 | S2 | Research Question |
| 3 | chronic ethmoidal sinusitis | 97.44% | L3 | 0 | 11 | S1 | Research Question |
| 4 | bacterial pneumonia | 95.57% | L4 | 3 | 20 | S0 | Hold |
| 5 | meningococcal infection | 94.30% | L5 | 0 | 5 | S0 | Hold |
| 6 | endocardial fibroelastosis | 93.61% | L5 | 0 | 0 | S0 | Hold |
| 7 | punctate epithelial keratoconjunctivitis | 93.30% | L4 | 0 | 1 | S0 | Hold |
| 8 | bacterial arthritis | 93.27% | L3 | 0 | 20 | S1 | Research Question |
| 9 | endocarditis | 92.91% | L3 | 0 | 20 | S2 | Proceed with Guardrails |
| 10 | pneumocystosis | 91.61% | L4 | 0 | 20 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Amphotericin B | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Amphotericin B | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Amphotericin B, disease=paranasal sinus neoplasm (disease) | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Amphotericin B, disease=paranasal sinus neoplasm (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Amphotericin B, disease=paranasal sinus neoplasm (disease) | success | 12 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Amphotericin B, disease=chronic rhinosinusitis | success | 2 |  |
| 7 | ictrp | 2026-03-10 | drug=Amphotericin B, disease=chronic rhinosinusitis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Amphotericin B, disease=chronic rhinosinusitis | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Amphotericin B, disease=chronic ethmoidal sinusitis | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Amphotericin B, disease=chronic ethmoidal sinusitis | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Amphotericin B, disease=chronic ethmoidal sinusitis | success | 11 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Amphotericin B, disease=bacterial pneumonia | success | 3 |  |
| 13 | ictrp | 2026-03-10 | drug=Amphotericin B, disease=bacterial pneumonia | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Amphotericin B, disease=bacterial pneumonia | success | 20 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Amphotericin B, disease=meningococcal infection | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Amphotericin B, disease=meningococcal infection | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Amphotericin B, disease=meningococcal infection | success | 5 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Amphotericin B, disease=endocardial fibroelastosis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Amphotericin B, disease=endocardial fibroelastosis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Amphotericin B, disease=endocardial fibroelastosis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Amphotericin B, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Amphotericin B, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Amphotericin B, disease=punctate epithelial keratoconjunctivitis | success | 1 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Amphotericin B, disease=bacterial arthritis | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Amphotericin B, disease=bacterial arthritis | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Amphotericin B, disease=bacterial arthritis | success | 20 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Amphotericin B, disease=endocarditis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Amphotericin B, disease=endocarditis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Amphotericin B, disease=endocarditis | success | 20 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Amphotericin B, disease=pneumocystosis | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Amphotericin B, disease=pneumocystosis | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Amphotericin B, disease=pneumocystosis | success | 20 |  |