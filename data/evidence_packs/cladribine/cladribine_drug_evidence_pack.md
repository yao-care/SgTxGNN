# Cladribine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Cladribine | |
| DrugBank ID | DB00242 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | parameningeal embryonal rhabdomyosarcoma | 99.77% | L5 | 0 | 0 | S0 | Hold |
| 2 | botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.77% | L5 | 0 | 0 | S0 | Hold |
| 3 | embryonal extrahepatic bile duct rhabdomyosarcoma | 99.76% | L5 | 0 | 0 | S0 | Hold |
| 4 | prostate embryonal rhabdomyosarcoma | 99.75% | L5 | 0 | 0 | S0 | Hold |
| 5 | extrahepatic bile duct rhabdomyosarcoma | 99.75% | L5 | 0 | 0 | S0 | Hold |
| 6 | rhabdomyosarcoma (disease) | 99.74% | L5 | 0 | 0 | S0 | Hold |
| 7 | liver sarcoma | 99.70% | L5 | 0 | 1 | S0 | Hold |
| 8 | skeletal muscle neoplasm | 98.96% | L5 | 0 | 0 | S0 | Hold |
| 9 | gestational trophoblastic neoplasm | 98.37% | L5 | 0 | 0 | S0 | Hold |
| 10 | pleural adenomatoid tumor | 98.07% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Cladribine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Cladribine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Cladribine, disease=parameningeal embryonal rhabdomyosarcoma | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Cladribine, disease=parameningeal embryonal rhabdomyosarcoma | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Cladribine, disease=parameningeal embryonal rhabdomyosarcoma | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Cladribine, disease=botryoid-type embryonal rhabdomyosarcoma of the vagina | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Cladribine, disease=botryoid-type embryonal rhabdomyosarcoma of the vagina | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Cladribine, disease=botryoid-type embryonal rhabdomyosarcoma of the vagina | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Cladribine, disease=embryonal extrahepatic bile duct rhabdomyosarcoma | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Cladribine, disease=embryonal extrahepatic bile duct rhabdomyosarcoma | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Cladribine, disease=embryonal extrahepatic bile duct rhabdomyosarcoma | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Cladribine, disease=prostate embryonal rhabdomyosarcoma | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Cladribine, disease=prostate embryonal rhabdomyosarcoma | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Cladribine, disease=prostate embryonal rhabdomyosarcoma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Cladribine, disease=extrahepatic bile duct rhabdomyosarcoma | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Cladribine, disease=extrahepatic bile duct rhabdomyosarcoma | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Cladribine, disease=extrahepatic bile duct rhabdomyosarcoma | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Cladribine, disease=rhabdomyosarcoma (disease) | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Cladribine, disease=rhabdomyosarcoma (disease) | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Cladribine, disease=rhabdomyosarcoma (disease) | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Cladribine, disease=liver sarcoma | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Cladribine, disease=liver sarcoma | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Cladribine, disease=liver sarcoma | success | 1 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Cladribine, disease=skeletal muscle neoplasm | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Cladribine, disease=skeletal muscle neoplasm | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Cladribine, disease=skeletal muscle neoplasm | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Cladribine, disease=gestational trophoblastic neoplasm | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Cladribine, disease=gestational trophoblastic neoplasm | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Cladribine, disease=gestational trophoblastic neoplasm | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Cladribine, disease=pleural adenomatoid tumor | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Cladribine, disease=pleural adenomatoid tumor | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Cladribine, disease=pleural adenomatoid tumor | success | 0 |  |