# Histidine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Histidine | |
| DrugBank ID | DB00117 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | gastroparesis (disease) | 99.55% | L5 | 0 | 0 | S0 | Hold |
| 2 | sclerosing cholangitis | 99.27% | L4 | 0 | 8 | S1 | Hold |
| 3 | congenital prothrombin deficiency | 98.80% | L5 | 0 | 0 | S0 | Hold |
| 4 | familial visceral myopathy | 98.67% | L5 | 0 | 0 | S0 | Hold |
| 5 | potassium deficiency disease | 98.67% | L5 | 0 | 5 | S0 | Hold |
| 6 | dyspepsia | 98.54% | L4 | 1 | 5 | S1 | Research Question |
| 7 | unclassified intestinal pseudoobstruction | 98.12% | L5 | 0 | 0 | S0 | Hold |
| 8 | myopathic intestinal pseudoobstruction | 98.12% | L5 | 0 | 0 | S0 | Hold |
| 9 | primary aldosteronism | 98.10% | L5 | 1 | 3 | S0 | Hold |
| 10 | intestinal obstruction | 98.06% | L5 | 2 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Histidine | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Histidine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Histidine, disease=gastroparesis (disease) | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Histidine, disease=gastroparesis (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Histidine, disease=gastroparesis (disease) | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Histidine, disease=sclerosing cholangitis | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Histidine, disease=sclerosing cholangitis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Histidine, disease=sclerosing cholangitis | success | 8 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Histidine, disease=congenital prothrombin deficiency | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Histidine, disease=congenital prothrombin deficiency | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Histidine, disease=congenital prothrombin deficiency | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Histidine, disease=familial visceral myopathy | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Histidine, disease=familial visceral myopathy | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Histidine, disease=familial visceral myopathy | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Histidine, disease=potassium deficiency disease | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Histidine, disease=potassium deficiency disease | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Histidine, disease=potassium deficiency disease | success | 5 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Histidine, disease=dyspepsia | success | 1 |  |
| 19 | ictrp | 2026-03-10 | drug=Histidine, disease=dyspepsia | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Histidine, disease=dyspepsia | success | 5 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Histidine, disease=unclassified intestinal pseudoobstruction | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Histidine, disease=unclassified intestinal pseudoobstruction | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Histidine, disease=unclassified intestinal pseudoobstruction | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Histidine, disease=myopathic intestinal pseudoobstruction | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Histidine, disease=myopathic intestinal pseudoobstruction | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Histidine, disease=myopathic intestinal pseudoobstruction | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Histidine, disease=primary aldosteronism | success | 1 |  |
| 28 | ictrp | 2026-03-10 | drug=Histidine, disease=primary aldosteronism | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Histidine, disease=primary aldosteronism | success | 3 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Histidine, disease=intestinal obstruction | success | 2 |  |
| 31 | ictrp | 2026-03-10 | drug=Histidine, disease=intestinal obstruction | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Histidine, disease=intestinal obstruction | success | 0 |  |