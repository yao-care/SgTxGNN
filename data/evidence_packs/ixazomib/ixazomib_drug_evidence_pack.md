# Ixazomib 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Ixazomib | |
| DrugBank ID | DB09570 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | indolent plasma cell myeloma | 96.17% | L2 | 0 | 2 | S2 | Proceed with Guardrails |
| 2 | CMM7 | 81.96% | L5 | 0 | 0 | S0 | Hold |
| 3 | pediatric leptomeningeal melanoma | 80.85% | L5 | 0 | 0 | S0 | Hold |
| 4 | vulvar melanoma (disease) | 80.35% | L5 | 0 | 0 | S0 | Hold |
| 5 | epithelioid cell uveal melanoma | 79.61% | L5 | 0 | 0 | S0 | Hold |
| 6 | ganglioneuroblastoma (disease) | 73.87% | L5 | 0 | 0 | S0 | Hold |
| 7 | melanoma | 72.89% | L4 | 0 | 2 | S1 | Research Question |
| 8 | retroperitoneal neoplasm | 70.99% | L5 | 0 | 0 | S0 | Hold |
| 9 | vertebral anomalies and variable endocrine and T-cell dysfunction | 68.59% | L5 | 0 | 0 | S0 | Hold |
| 10 | intellectual disability, autosomal dominant 55, with seizures | 61.99% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Ixazomib | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Ixazomib | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Ixazomib, disease=indolent plasma cell myeloma | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Ixazomib, disease=indolent plasma cell myeloma | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Ixazomib, disease=indolent plasma cell myeloma | success | 2 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Ixazomib, disease=CMM7 | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Ixazomib, disease=CMM7 | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Ixazomib, disease=CMM7 | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Ixazomib, disease=pediatric leptomeningeal melanoma | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Ixazomib, disease=pediatric leptomeningeal melanoma | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Ixazomib, disease=pediatric leptomeningeal melanoma | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Ixazomib, disease=vulvar melanoma (disease) | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Ixazomib, disease=vulvar melanoma (disease) | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Ixazomib, disease=vulvar melanoma (disease) | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Ixazomib, disease=epithelioid cell uveal melanoma | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Ixazomib, disease=epithelioid cell uveal melanoma | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Ixazomib, disease=epithelioid cell uveal melanoma | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Ixazomib, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Ixazomib, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Ixazomib, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Ixazomib, disease=melanoma | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Ixazomib, disease=melanoma | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Ixazomib, disease=melanoma | success | 2 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Ixazomib, disease=retroperitoneal neoplasm | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Ixazomib, disease=retroperitoneal neoplasm | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Ixazomib, disease=retroperitoneal neoplasm | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Ixazomib, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Ixazomib, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Ixazomib, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Ixazomib, disease=intellectual disability, autosomal dominant 55, with seizures | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Ixazomib, disease=intellectual disability, autosomal dominant 55, with seizures | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Ixazomib, disease=intellectual disability, autosomal dominant 55, with seizures | success | 0 |  |