# Alemtuzumab 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Alemtuzumab | |
| DrugBank ID | DB00087 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | hepatic infarction | 94.44% | L5 | 0 | 0 | S0 | Hold |
| 2 | syndrome with combined immunodeficiency | 93.73% | L2 | 13 | 12 | S2 | Proceed with Guardrails |
| 3 | hepatic veno-occlusive disease | 93.14% | L4 | 3 | 6 | S0 | Hold |
| 4 | kidney pelvis sarcomatoid transitional cell carcinoma | 93.09% | L5 | 0 | 0 | S0 | Hold |
| 5 | infiltrating bladder urothelial carcinoma sarcomatoid variant | 92.93% | L5 | 0 | 0 | S0 | Hold |
| 6 | prostatic urethra urothelial carcinoma | 92.85% | L5 | 0 | 0 | S0 | Hold |
| 7 | renal pelvis papillary urothelial carcinoma | 92.81% | L5 | 0 | 0 | S0 | Hold |
| 8 | peliosis hepatis | 92.20% | L5 | 0 | 0 | S0 | Hold |
| 9 | acquired hemophagocytic lymphohistiocytosis associated with malignant disease | 89.93% | L4 | 0 | 1 | S1 | Research Question |
| 10 | hemophagocytic syndrome associated with an infection | 89.93% | L3 | 2 | 10 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Alemtuzumab | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Alemtuzumab | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Alemtuzumab, disease=hepatic infarction | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Alemtuzumab, disease=hepatic infarction | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Alemtuzumab, disease=hepatic infarction | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Alemtuzumab, disease=syndrome with combined immunodeficiency | success | 13 |  |
| 7 | ictrp | 2026-03-10 | drug=Alemtuzumab, disease=syndrome with combined immunodeficiency | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Alemtuzumab, disease=syndrome with combined immunodeficiency | success | 12 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Alemtuzumab, disease=hepatic veno-occlusive disease | success | 3 |  |
| 10 | ictrp | 2026-03-10 | drug=Alemtuzumab, disease=hepatic veno-occlusive disease | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Alemtuzumab, disease=hepatic veno-occlusive disease | success | 6 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Alemtuzumab, disease=kidney pelvis sarcomatoid transitional cell carcinoma | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Alemtuzumab, disease=kidney pelvis sarcomatoid transitional cell carcinoma | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Alemtuzumab, disease=kidney pelvis sarcomatoid transitional cell carcinoma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Alemtuzumab, disease=infiltrating bladder urothelial carcinoma sarcomatoid variant | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Alemtuzumab, disease=infiltrating bladder urothelial carcinoma sarcomatoid variant | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Alemtuzumab, disease=infiltrating bladder urothelial carcinoma sarcomatoid variant | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Alemtuzumab, disease=prostatic urethra urothelial carcinoma | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Alemtuzumab, disease=prostatic urethra urothelial carcinoma | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Alemtuzumab, disease=prostatic urethra urothelial carcinoma | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Alemtuzumab, disease=renal pelvis papillary urothelial carcinoma | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Alemtuzumab, disease=renal pelvis papillary urothelial carcinoma | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Alemtuzumab, disease=renal pelvis papillary urothelial carcinoma | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Alemtuzumab, disease=peliosis hepatis | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Alemtuzumab, disease=peliosis hepatis | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Alemtuzumab, disease=peliosis hepatis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Alemtuzumab, disease=acquired hemophagocytic lymphohistiocytosis associated with malignant disease | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Alemtuzumab, disease=acquired hemophagocytic lymphohistiocytosis associated with malignant disease | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Alemtuzumab, disease=acquired hemophagocytic lymphohistiocytosis associated with malignant disease | success | 1 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Alemtuzumab, disease=hemophagocytic syndrome associated with an infection | success | 2 |  |
| 31 | ictrp | 2026-03-10 | drug=Alemtuzumab, disease=hemophagocytic syndrome associated with an infection | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Alemtuzumab, disease=hemophagocytic syndrome associated with an infection | success | 10 |  |