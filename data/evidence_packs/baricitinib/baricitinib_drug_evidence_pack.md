# Baricitinib 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Baricitinib | |
| DrugBank ID | DB11817 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.94% | L5 | 0 | 0 | S0 | Hold |
| 2 | brachydactyly-syndactyly syndrome | 99.94% | L5 | 0 | 0 | S0 | Hold |
| 3 | indolent plasma cell myeloma | 93.31% | L5 | 0 | 0 | S0 | Hold |
| 4 | WHIM syndrome | 93.12% | L5 | 0 | 0 | S0 | Hold |
| 5 | plasma cell myeloma | 91.83% | L4 | 0 | 1 | S1 | Hold |
| 6 | myeloid leukemia | 91.01% | L2 | 1 | 4 | S2 | Research Question |
| 7 | Meester-Loeys syndrome | 88.21% | L5 | 0 | 0 | S0 | Hold |
| 8 | ganglioneuroblastoma (disease) | 87.59% | L5 | 0 | 0 | S0 | Hold |
| 9 | heparin cofactor 2 deficiency | 86.31% | L5 | 0 | 0 | S0 | Hold |
| 10 | vertebral anomalies and variable endocrine and T-cell dysfunction | 84.68% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Baricitinib | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Baricitinib | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Baricitinib, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Baricitinib, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Baricitinib, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Baricitinib, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Baricitinib, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Baricitinib, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Baricitinib, disease=indolent plasma cell myeloma | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Baricitinib, disease=indolent plasma cell myeloma | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Baricitinib, disease=indolent plasma cell myeloma | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Baricitinib, disease=WHIM syndrome | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Baricitinib, disease=WHIM syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Baricitinib, disease=WHIM syndrome | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Baricitinib, disease=plasma cell myeloma | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Baricitinib, disease=plasma cell myeloma | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Baricitinib, disease=plasma cell myeloma | success | 1 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Baricitinib, disease=myeloid leukemia | success | 1 |  |
| 19 | ictrp | 2026-03-09 | drug=Baricitinib, disease=myeloid leukemia | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Baricitinib, disease=myeloid leukemia | success | 4 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Baricitinib, disease=Meester-Loeys syndrome | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Baricitinib, disease=Meester-Loeys syndrome | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Baricitinib, disease=Meester-Loeys syndrome | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Baricitinib, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Baricitinib, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Baricitinib, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Baricitinib, disease=heparin cofactor 2 deficiency | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Baricitinib, disease=heparin cofactor 2 deficiency | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Baricitinib, disease=heparin cofactor 2 deficiency | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Baricitinib, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Baricitinib, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Baricitinib, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |