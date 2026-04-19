# Isoleucine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Isoleucine | |
| DrugBank ID | DB00167 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | gastroparesis (disease) | 99.32% | L5 | 0 | 0 | S1 | Research Question |
| 2 | obsolete vitamin D deficiency | 98.35% | L5 | 0 | 0 | S0 | Hold |
| 3 | congenital prothrombin deficiency | 97.91% | L5 | 0 | 0 | S0 | Hold |
| 4 | dyspepsia | 97.74% | L4 | 0 | 4 | S1 | Research Question |
| 5 | renal tubular acidosis | 97.62% | L5 | 0 | 2 | S0 | Hold |
| 6 | sclerosing cholangitis | 97.23% | L5 | 0 | 3 | S0 | Hold |
| 7 | familial visceral myopathy | 96.80% | L5 | 0 | 0 | S0 | Hold |
| 8 | hypophosphatemic rickets | 95.83% | L5 | 0 | 0 | S0 | Hold |
| 9 | potassium deficiency disease | 95.49% | L5 | 0 | 4 | S0 | Hold |
| 10 | unclassified intestinal pseudoobstruction | 95.24% | L5 | 0 | 0 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Isoleucine | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Isoleucine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Isoleucine, disease=gastroparesis (disease) | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Isoleucine, disease=gastroparesis (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Isoleucine, disease=gastroparesis (disease) | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Isoleucine, disease=obsolete vitamin D deficiency | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Isoleucine, disease=obsolete vitamin D deficiency | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Isoleucine, disease=obsolete vitamin D deficiency | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Isoleucine, disease=congenital prothrombin deficiency | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Isoleucine, disease=congenital prothrombin deficiency | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Isoleucine, disease=congenital prothrombin deficiency | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Isoleucine, disease=dyspepsia | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Isoleucine, disease=dyspepsia | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Isoleucine, disease=dyspepsia | success | 4 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Isoleucine, disease=renal tubular acidosis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Isoleucine, disease=renal tubular acidosis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Isoleucine, disease=renal tubular acidosis | success | 2 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Isoleucine, disease=sclerosing cholangitis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Isoleucine, disease=sclerosing cholangitis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Isoleucine, disease=sclerosing cholangitis | success | 3 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Isoleucine, disease=familial visceral myopathy | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Isoleucine, disease=familial visceral myopathy | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Isoleucine, disease=familial visceral myopathy | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Isoleucine, disease=hypophosphatemic rickets | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Isoleucine, disease=hypophosphatemic rickets | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Isoleucine, disease=hypophosphatemic rickets | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Isoleucine, disease=potassium deficiency disease | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Isoleucine, disease=potassium deficiency disease | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Isoleucine, disease=potassium deficiency disease | success | 4 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Isoleucine, disease=unclassified intestinal pseudoobstruction | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Isoleucine, disease=unclassified intestinal pseudoobstruction | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Isoleucine, disease=unclassified intestinal pseudoobstruction | success | 0 |  |