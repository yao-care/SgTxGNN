# Dactinomycin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Dactinomycin | |
| DrugBank ID | DB00970 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | relapsing-remitting multiple sclerosis | 99.58% | L5 | 0 | 0 | S0 | Hold |
| 2 | botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.54% | L3 | 0 | 0 | S2 | Research Question |
| 3 | extrahepatic bile duct rhabdomyosarcoma | 99.49% | L4 | 0 | 1 | S1 | Research Question |
| 4 | embryonal extrahepatic bile duct rhabdomyosarcoma | 99.48% | L4 | 0 | 0 | S1 | Research Question |
| 5 | parameningeal embryonal rhabdomyosarcoma | 99.48% | L1 | 0 | 3 | S3 | Proceed with Guardrails |
| 6 | prostate embryonal rhabdomyosarcoma | 99.46% | L3 | 0 | 15 | S2 | Research Question |
| 7 | liver sarcoma | 99.42% | L2 | 1 | 20 | S2 | Research Question |
| 8 | upper aerodigestive tract neoplasm | 99.16% | L3 | 0 | 20 | S2 | Research Question |
| 9 | head and neck cancer | 99.16% | L3 | 1 | 20 | S1 | Research Question |
| 10 | T-cell leukemia | 98.88% | L5 | 1 | 20 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Dactinomycin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Dactinomycin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Dactinomycin, disease=relapsing-remitting multiple sclerosis | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Dactinomycin, disease=relapsing-remitting multiple sclerosis | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Dactinomycin, disease=relapsing-remitting multiple sclerosis | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Dactinomycin, disease=botryoid-type embryonal rhabdomyosarcoma of the vagina | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Dactinomycin, disease=botryoid-type embryonal rhabdomyosarcoma of the vagina | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Dactinomycin, disease=botryoid-type embryonal rhabdomyosarcoma of the vagina | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Dactinomycin, disease=extrahepatic bile duct rhabdomyosarcoma | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Dactinomycin, disease=extrahepatic bile duct rhabdomyosarcoma | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Dactinomycin, disease=extrahepatic bile duct rhabdomyosarcoma | success | 1 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Dactinomycin, disease=embryonal extrahepatic bile duct rhabdomyosarcoma | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Dactinomycin, disease=embryonal extrahepatic bile duct rhabdomyosarcoma | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Dactinomycin, disease=embryonal extrahepatic bile duct rhabdomyosarcoma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Dactinomycin, disease=parameningeal embryonal rhabdomyosarcoma | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Dactinomycin, disease=parameningeal embryonal rhabdomyosarcoma | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Dactinomycin, disease=parameningeal embryonal rhabdomyosarcoma | success | 3 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Dactinomycin, disease=prostate embryonal rhabdomyosarcoma | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Dactinomycin, disease=prostate embryonal rhabdomyosarcoma | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Dactinomycin, disease=prostate embryonal rhabdomyosarcoma | success | 15 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Dactinomycin, disease=liver sarcoma | success | 1 |  |
| 22 | ictrp | 2026-03-10 | drug=Dactinomycin, disease=liver sarcoma | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Dactinomycin, disease=liver sarcoma | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Dactinomycin, disease=upper aerodigestive tract neoplasm | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Dactinomycin, disease=upper aerodigestive tract neoplasm | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Dactinomycin, disease=upper aerodigestive tract neoplasm | success | 20 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Dactinomycin, disease=head and neck cancer | success | 1 |  |
| 28 | ictrp | 2026-03-10 | drug=Dactinomycin, disease=head and neck cancer | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Dactinomycin, disease=head and neck cancer | success | 20 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Dactinomycin, disease=T-cell leukemia | success | 1 |  |
| 31 | ictrp | 2026-03-10 | drug=Dactinomycin, disease=T-cell leukemia | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Dactinomycin, disease=T-cell leukemia | success | 20 |  |