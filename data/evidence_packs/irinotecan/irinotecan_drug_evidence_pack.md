# Irinotecan 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Irinotecan | |
| DrugBank ID | DB00762 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | female breast carcinoma | 99.08% | L2 | 22 | 20 | S2 | Proceed with Guardrails |
| 2 | pancreatic carcinoma with mixed differentiation | 98.61% | L3 | 1 | 1 | S2 | Research Question |
| 3 | osteoclastic giant cell tumor of pancreas | 98.60% | L5 | 0 | 0 | S0 | Hold |
| 4 | solid pseudopapillary carcinoma of pancreas | 98.60% | L4 | 0 | 3 | S1 | Hold |
| 5 | pancreatic intraductal papillary-mucinous carcinoma | 98.56% | L4 | 0 | 2 | S1 | Hold |
| 6 | pancreatic intraductal papillary-mucinous neoplasm | 98.48% | L4 | 0 | 4 | S1 | Research Question |
| 7 | pancreatic signet ring cell adenocarcinoma | 98.48% | L3 | 1 | 3 | S2 | Research Question |
| 8 | mixed ductal-endocrine carcinoma of pancreas | 98.46% | L5 | 0 | 0 | S0 | Hold |
| 9 | malignant exocrine pancreas neoplasm | 98.45% | L3 | 0 | 5 | S2 | Research Question |
| 10 | undifferentiated pancreatic carcinoma | 98.42% | L4 | 1 | 2 | S1 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Irinotecan | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Irinotecan | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Irinotecan, disease=female breast carcinoma | success | 22 |  |
| 4 | ictrp | 2026-03-10 | drug=Irinotecan, disease=female breast carcinoma | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Irinotecan, disease=female breast carcinoma | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Irinotecan, disease=pancreatic carcinoma with mixed differentiation | success | 1 |  |
| 7 | ictrp | 2026-03-10 | drug=Irinotecan, disease=pancreatic carcinoma with mixed differentiation | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Irinotecan, disease=pancreatic carcinoma with mixed differentiation | success | 1 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Irinotecan, disease=osteoclastic giant cell tumor of pancreas | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Irinotecan, disease=osteoclastic giant cell tumor of pancreas | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Irinotecan, disease=osteoclastic giant cell tumor of pancreas | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Irinotecan, disease=solid pseudopapillary carcinoma of pancreas | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Irinotecan, disease=solid pseudopapillary carcinoma of pancreas | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Irinotecan, disease=solid pseudopapillary carcinoma of pancreas | success | 3 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Irinotecan, disease=pancreatic intraductal papillary-mucinous carcinoma | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Irinotecan, disease=pancreatic intraductal papillary-mucinous carcinoma | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Irinotecan, disease=pancreatic intraductal papillary-mucinous carcinoma | success | 2 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Irinotecan, disease=pancreatic intraductal papillary-mucinous neoplasm | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Irinotecan, disease=pancreatic intraductal papillary-mucinous neoplasm | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Irinotecan, disease=pancreatic intraductal papillary-mucinous neoplasm | success | 4 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Irinotecan, disease=pancreatic signet ring cell adenocarcinoma | success | 1 |  |
| 22 | ictrp | 2026-03-10 | drug=Irinotecan, disease=pancreatic signet ring cell adenocarcinoma | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Irinotecan, disease=pancreatic signet ring cell adenocarcinoma | success | 3 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Irinotecan, disease=mixed ductal-endocrine carcinoma of pancreas | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Irinotecan, disease=mixed ductal-endocrine carcinoma of pancreas | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Irinotecan, disease=mixed ductal-endocrine carcinoma of pancreas | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Irinotecan, disease=malignant exocrine pancreas neoplasm | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Irinotecan, disease=malignant exocrine pancreas neoplasm | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Irinotecan, disease=malignant exocrine pancreas neoplasm | success | 5 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Irinotecan, disease=undifferentiated pancreatic carcinoma | success | 1 |  |
| 31 | ictrp | 2026-03-10 | drug=Irinotecan, disease=undifferentiated pancreatic carcinoma | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Irinotecan, disease=undifferentiated pancreatic carcinoma | success | 2 |  |