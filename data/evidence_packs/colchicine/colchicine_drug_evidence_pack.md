# Colchicine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Colchicine | |
| DrugBank ID | DB01394 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | Plasmodium falciparum malaria | 99.60% | L4 | 0 | 6 | S1 | Research Question |
| 2 | familial Mediterranean fever, autosomal dominant | 99.38% | L1 | 1 | 20 | S3 | Proceed with Guardrails |
| 3 | dermatofibrosarcoma protuberans | 99.37% | L5 | 0 | 0 | S0 | Hold |
| 4 | primary immunodeficiency due to a genetic defect in innate immunity | 98.67% | L5 | 0 | 0 | S0 | Hold |
| 5 | sitosterolemia | 98.59% | L5 | 0 | 0 | S0 | Hold |
| 6 | Smouldering systemic mastocytosis | 98.24% | L5 | 0 | 0 | S0 | Hold |
| 7 | systemic mastocytosis | 98.20% | L5 | 0 | 1 | S0 | Hold |
| 8 | lymphoadenopathic mastocytosis with eosinophilia | 98.08% | L5 | 0 | 0 | S0 | Hold |
| 9 | hemoglobin H disease | 98.06% | L5 | 1 | 0 | S0 | Hold |
| 10 | blepharo-cheilo-odontic syndrome | 96.71% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Colchicine | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Colchicine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Colchicine, disease=Plasmodium falciparum malaria | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Colchicine, disease=Plasmodium falciparum malaria | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Colchicine, disease=Plasmodium falciparum malaria | success | 6 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Colchicine, disease=familial Mediterranean fever, autosomal dominant | success | 1 |  |
| 7 | ictrp | 2026-03-10 | drug=Colchicine, disease=familial Mediterranean fever, autosomal dominant | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Colchicine, disease=familial Mediterranean fever, autosomal dominant | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Colchicine, disease=dermatofibrosarcoma protuberans | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Colchicine, disease=dermatofibrosarcoma protuberans | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Colchicine, disease=dermatofibrosarcoma protuberans | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Colchicine, disease=primary immunodeficiency due to a genetic defect in innate immunity | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Colchicine, disease=primary immunodeficiency due to a genetic defect in innate immunity | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Colchicine, disease=primary immunodeficiency due to a genetic defect in innate immunity | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Colchicine, disease=sitosterolemia | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Colchicine, disease=sitosterolemia | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Colchicine, disease=sitosterolemia | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Colchicine, disease=Smouldering systemic mastocytosis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Colchicine, disease=Smouldering systemic mastocytosis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Colchicine, disease=Smouldering systemic mastocytosis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Colchicine, disease=systemic mastocytosis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Colchicine, disease=systemic mastocytosis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Colchicine, disease=systemic mastocytosis | success | 1 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Colchicine, disease=lymphoadenopathic mastocytosis with eosinophilia | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Colchicine, disease=lymphoadenopathic mastocytosis with eosinophilia | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Colchicine, disease=lymphoadenopathic mastocytosis with eosinophilia | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Colchicine, disease=hemoglobin H disease | success | 1 |  |
| 28 | ictrp | 2026-03-10 | drug=Colchicine, disease=hemoglobin H disease | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Colchicine, disease=hemoglobin H disease | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Colchicine, disease=blepharo-cheilo-odontic syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Colchicine, disease=blepharo-cheilo-odontic syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Colchicine, disease=blepharo-cheilo-odontic syndrome | success | 0 |  |