# Axitinib 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Axitinib | |
| DrugBank ID | DB06626 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | renal cell carcinoma associated with neuroblastoma | 99.90% | L5 | 0 | 0 | S0 | Hold |
| 2 | unclassified renal cell carcinoma | 99.90% | L3 | 2 | 0 | S1 | Research Question |
| 3 | renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions | 99.90% | L3 | 1 | 0 | S1 | Research Question |
| 4 | childhood kidney cell carcinoma | 99.87% | L2 | 2 | 2 | S2 | Proceed with Guardrails |
| 5 | liposarcoma | 99.87% | L4 | 0 | 1 | S1 | Research Question |
| 6 | renal carcinoma | 99.85% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 7 | ovarian myxoid liposarcoma | 99.84% | L5 | 0 | 0 | S0 | Hold |
| 8 | angiolipoma | 99.83% | L5 | 0 | 0 | S0 | Hold |
| 9 | collecting duct carcinoma | 99.81% | L3 | 1 | 20 | S2 | Research Question |
| 10 | familial spontaneous pneumothorax | 99.78% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Axitinib | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Axitinib | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Axitinib, disease=renal cell carcinoma associated with neuroblastoma | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Axitinib, disease=renal cell carcinoma associated with neuroblastoma | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Axitinib, disease=renal cell carcinoma associated with neuroblastoma | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Axitinib, disease=unclassified renal cell carcinoma | success | 2 |  |
| 7 | ictrp | 2026-03-09 | drug=Axitinib, disease=unclassified renal cell carcinoma | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Axitinib, disease=unclassified renal cell carcinoma | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Axitinib, disease=renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions | success | 1 |  |
| 10 | ictrp | 2026-03-09 | drug=Axitinib, disease=renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Axitinib, disease=renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Axitinib, disease=childhood kidney cell carcinoma | success | 2 |  |
| 13 | ictrp | 2026-03-09 | drug=Axitinib, disease=childhood kidney cell carcinoma | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Axitinib, disease=childhood kidney cell carcinoma | success | 2 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Axitinib, disease=liposarcoma | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Axitinib, disease=liposarcoma | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Axitinib, disease=liposarcoma | success | 1 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Axitinib, disease=renal carcinoma | success | 50 |  |
| 19 | ictrp | 2026-03-09 | drug=Axitinib, disease=renal carcinoma | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Axitinib, disease=renal carcinoma | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Axitinib, disease=ovarian myxoid liposarcoma | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Axitinib, disease=ovarian myxoid liposarcoma | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Axitinib, disease=ovarian myxoid liposarcoma | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Axitinib, disease=angiolipoma | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Axitinib, disease=angiolipoma | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Axitinib, disease=angiolipoma | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Axitinib, disease=collecting duct carcinoma | success | 1 |  |
| 28 | ictrp | 2026-03-09 | drug=Axitinib, disease=collecting duct carcinoma | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Axitinib, disease=collecting duct carcinoma | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Axitinib, disease=familial spontaneous pneumothorax | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Axitinib, disease=familial spontaneous pneumothorax | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Axitinib, disease=familial spontaneous pneumothorax | success | 0 |  |