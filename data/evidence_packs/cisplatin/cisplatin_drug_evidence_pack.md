# Cisplatin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Cisplatin | |
| DrugBank ID | DB00515 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | female breast carcinoma | 97.39% | L1 | 46 | 20 | S3 | Proceed with Guardrails |
| 2 | choriocarcinoma of ovary | 95.68% | L2 | 2 | 20 | S2 | Research Question |
| 3 | gonadal germ cell tumor | 95.65% | L1 | 50 | 19 | S3 | Proceed with Guardrails |
| 4 | adult germ cell tumor | 95.49% | L1 | 48 | 20 | S3 | Proceed with Guardrails |
| 5 | ovarian primitive germ cell tumor | 95.46% | L3 | 4 | 6 | S2 | Research Question |
| 6 | enteric pattern testicular yolk sac tumor | 95.02% | L4 | 0 | 0 | S0 | Hold |
| 7 | testicular yolk sac tumor, papillary pattern | 95.02% | L4 | 0 | 0 | S0 | Hold |
| 8 | reticular pattern testicular yolk sac tumor | 95.02% | L4 | 0 | 0 | S0 | Hold |
| 9 | testicular yolk sac tumor, solid pattern | 95.02% | L3 | 1 | 0 | S1 | Hold |
| 10 | testicular yolk sac tumor, macrocystic pattern | 95.02% | L4 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Cisplatin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Cisplatin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Cisplatin, disease=female breast carcinoma | success | 46 |  |
| 4 | ictrp | 2026-03-10 | drug=Cisplatin, disease=female breast carcinoma | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Cisplatin, disease=female breast carcinoma | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Cisplatin, disease=choriocarcinoma of ovary | success | 2 |  |
| 7 | ictrp | 2026-03-10 | drug=Cisplatin, disease=choriocarcinoma of ovary | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Cisplatin, disease=choriocarcinoma of ovary | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Cisplatin, disease=gonadal germ cell tumor | success | 50 |  |
| 10 | ictrp | 2026-03-10 | drug=Cisplatin, disease=gonadal germ cell tumor | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Cisplatin, disease=gonadal germ cell tumor | success | 19 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Cisplatin, disease=adult germ cell tumor | success | 48 |  |
| 13 | ictrp | 2026-03-10 | drug=Cisplatin, disease=adult germ cell tumor | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Cisplatin, disease=adult germ cell tumor | success | 20 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Cisplatin, disease=ovarian primitive germ cell tumor | success | 4 |  |
| 16 | ictrp | 2026-03-10 | drug=Cisplatin, disease=ovarian primitive germ cell tumor | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Cisplatin, disease=ovarian primitive germ cell tumor | success | 6 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Cisplatin, disease=enteric pattern testicular yolk sac tumor | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Cisplatin, disease=enteric pattern testicular yolk sac tumor | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Cisplatin, disease=enteric pattern testicular yolk sac tumor | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Cisplatin, disease=testicular yolk sac tumor, papillary pattern | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Cisplatin, disease=testicular yolk sac tumor, papillary pattern | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Cisplatin, disease=testicular yolk sac tumor, papillary pattern | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Cisplatin, disease=reticular pattern testicular yolk sac tumor | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Cisplatin, disease=reticular pattern testicular yolk sac tumor | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Cisplatin, disease=reticular pattern testicular yolk sac tumor | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Cisplatin, disease=testicular yolk sac tumor, solid pattern | success | 1 |  |
| 28 | ictrp | 2026-03-10 | drug=Cisplatin, disease=testicular yolk sac tumor, solid pattern | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Cisplatin, disease=testicular yolk sac tumor, solid pattern | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Cisplatin, disease=testicular yolk sac tumor, macrocystic pattern | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Cisplatin, disease=testicular yolk sac tumor, macrocystic pattern | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Cisplatin, disease=testicular yolk sac tumor, macrocystic pattern | success | 0 |  |