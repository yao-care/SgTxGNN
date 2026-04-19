# Imiquimod 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Imiquimod | |
| DrugBank ID | DB00724 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | pre-malignant neoplasm | 99.92% | L2 | 19 | 9 | S3 | Proceed with Guardrails |
| 2 | benign neoplasm of buccal mucosa | 99.91% | L4 | 0 | 8 | S1 | Research Question |
| 3 | cervical neuroblastoma | 99.91% | L5 | 0 | 0 | S0 | Hold |
| 4 | odontogenic cyst | 99.91% | L4 | 0 | 20 | S1 | Research Question |
| 5 | benign neoplasm of tongue | 99.91% | L5 | 0 | 1 | S0 | Hold |
| 6 | nasopharyngeal teratoma | 99.91% | L5 | 0 | 0 | S0 | Hold |
| 7 | cystic neoplasm | 99.91% | L5 | 0 | 0 | S0 | Hold |
| 8 | inner ear neoplasm | 99.91% | L5 | 0 | 0 | S0 | Hold |
| 9 | neoplasm of major salivary gland | 99.91% | L5 | 0 | 0 | S0 | Hold |
| 10 | schwannoma of jugular foramen | 99.91% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Imiquimod | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Imiquimod | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Imiquimod, disease=pre-malignant neoplasm | success | 19 |  |
| 4 | ictrp | 2026-03-09 | drug=Imiquimod, disease=pre-malignant neoplasm | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Imiquimod, disease=pre-malignant neoplasm | success | 9 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Imiquimod, disease=benign neoplasm of buccal mucosa | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Imiquimod, disease=benign neoplasm of buccal mucosa | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Imiquimod, disease=benign neoplasm of buccal mucosa | success | 8 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Imiquimod, disease=cervical neuroblastoma | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Imiquimod, disease=cervical neuroblastoma | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Imiquimod, disease=cervical neuroblastoma | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Imiquimod, disease=odontogenic cyst | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Imiquimod, disease=odontogenic cyst | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Imiquimod, disease=odontogenic cyst | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Imiquimod, disease=benign neoplasm of tongue | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Imiquimod, disease=benign neoplasm of tongue | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Imiquimod, disease=benign neoplasm of tongue | success | 1 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Imiquimod, disease=nasopharyngeal teratoma | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Imiquimod, disease=nasopharyngeal teratoma | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Imiquimod, disease=nasopharyngeal teratoma | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Imiquimod, disease=cystic neoplasm | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Imiquimod, disease=cystic neoplasm | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Imiquimod, disease=cystic neoplasm | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Imiquimod, disease=inner ear neoplasm | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Imiquimod, disease=inner ear neoplasm | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Imiquimod, disease=inner ear neoplasm | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Imiquimod, disease=neoplasm of major salivary gland | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Imiquimod, disease=neoplasm of major salivary gland | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Imiquimod, disease=neoplasm of major salivary gland | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Imiquimod, disease=schwannoma of jugular foramen | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Imiquimod, disease=schwannoma of jugular foramen | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Imiquimod, disease=schwannoma of jugular foramen | success | 0 |  |