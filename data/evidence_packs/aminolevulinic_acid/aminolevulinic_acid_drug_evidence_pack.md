# Aminolevulinic acid 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Aminolevulinic acid | |
| DrugBank ID | DB00855 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | pre-malignant neoplasm | 96.01% | L2 | 40 | 20 | S3 | Proceed with Guardrails |
| 2 | odontogenic cyst | 95.84% | L3 | 2 | 20 | S2 | Research Question |
| 3 | nasopharyngeal teratoma | 95.82% | L5 | 0 | 0 | S0 | Hold |
| 4 | cervical neuroblastoma | 95.76% | L5 | 0 | 0 | S0 | Hold |
| 5 | benign neoplasm of tongue | 95.73% | L3 | 0 | 18 | S2 | Research Question |
| 6 | benign neoplasm of buccal mucosa | 95.68% | L3 | 0 | 20 | S2 | Research Question |
| 7 | cystic neoplasm | 95.68% | L4 | 0 | 9 | S1 | Research Question |
| 8 | inner ear neoplasm | 95.67% | L5 | 0 | 0 | S0 | Hold |
| 9 | tumor of testis and paratestis | 95.64% | L5 | 0 | 0 | S0 | Hold |
| 10 | schwannoma of jugular foramen | 95.62% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Aminolevulinic acid | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Aminolevulinic acid | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Aminolevulinic acid, disease=pre-malignant neoplasm | success | 40 |  |
| 4 | ictrp | 2026-03-10 | drug=Aminolevulinic acid, disease=pre-malignant neoplasm | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Aminolevulinic acid, disease=pre-malignant neoplasm | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Aminolevulinic acid, disease=odontogenic cyst | success | 2 |  |
| 7 | ictrp | 2026-03-10 | drug=Aminolevulinic acid, disease=odontogenic cyst | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Aminolevulinic acid, disease=odontogenic cyst | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Aminolevulinic acid, disease=nasopharyngeal teratoma | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Aminolevulinic acid, disease=nasopharyngeal teratoma | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Aminolevulinic acid, disease=nasopharyngeal teratoma | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Aminolevulinic acid, disease=cervical neuroblastoma | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Aminolevulinic acid, disease=cervical neuroblastoma | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Aminolevulinic acid, disease=cervical neuroblastoma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Aminolevulinic acid, disease=benign neoplasm of tongue | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Aminolevulinic acid, disease=benign neoplasm of tongue | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Aminolevulinic acid, disease=benign neoplasm of tongue | success | 18 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Aminolevulinic acid, disease=benign neoplasm of buccal mucosa | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Aminolevulinic acid, disease=benign neoplasm of buccal mucosa | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Aminolevulinic acid, disease=benign neoplasm of buccal mucosa | success | 20 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Aminolevulinic acid, disease=cystic neoplasm | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Aminolevulinic acid, disease=cystic neoplasm | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Aminolevulinic acid, disease=cystic neoplasm | success | 9 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Aminolevulinic acid, disease=inner ear neoplasm | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Aminolevulinic acid, disease=inner ear neoplasm | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Aminolevulinic acid, disease=inner ear neoplasm | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Aminolevulinic acid, disease=tumor of testis and paratestis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Aminolevulinic acid, disease=tumor of testis and paratestis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Aminolevulinic acid, disease=tumor of testis and paratestis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Aminolevulinic acid, disease=schwannoma of jugular foramen | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Aminolevulinic acid, disease=schwannoma of jugular foramen | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Aminolevulinic acid, disease=schwannoma of jugular foramen | success | 0 |  |