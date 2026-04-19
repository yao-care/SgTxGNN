# Darunavir 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Darunavir | |
| DrugBank ID | DB01264 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | simian immunodeficiency virus infection | 99.97% | L4 | 0 | 4 | S1 | Research Question |
| 2 | feline acquired immunodeficiency syndrome | 99.97% | L5 | 1 | 0 | S0 | Hold |
| 3 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.97% | L5 | 0 | 0 | S0 | Hold |
| 4 | obsolete familial combined hyperlipidemia | 99.19% | L5 | 0 | 0 | S0 | Hold |
| 5 | AIDS related complex | 98.97% | L2 | 2 | 8 | S3 | Proceed with Guardrails |
| 6 | congenital human immunodeficiency virus | 98.97% | L1 | 23 | 9 | S3 | Proceed with Guardrails |
| 7 | fibroma of prostate | 97.74% | L5 | 0 | 0 | S0 | Hold |
| 8 | Brenner tumor | 97.53% | L5 | 0 | 0 | S0 | Hold |
| 9 | benign reproductive system neoplasm | 97.52% | L5 | 0 | 0 | S0 | Hold |
| 10 | benign prostate phyllodes tumor | 97.35% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Darunavir | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Darunavir | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Darunavir, disease=simian immunodeficiency virus infection | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Darunavir, disease=simian immunodeficiency virus infection | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Darunavir, disease=simian immunodeficiency virus infection | success | 4 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Darunavir, disease=feline acquired immunodeficiency syndrome | success | 1 |  |
| 7 | ictrp | 2026-03-09 | drug=Darunavir, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Darunavir, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Darunavir, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Darunavir, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Darunavir, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Darunavir, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Darunavir, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Darunavir, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Darunavir, disease=AIDS related complex | success | 2 |  |
| 16 | ictrp | 2026-03-09 | drug=Darunavir, disease=AIDS related complex | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Darunavir, disease=AIDS related complex | success | 8 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Darunavir, disease=congenital human immunodeficiency virus | success | 23 |  |
| 19 | ictrp | 2026-03-09 | drug=Darunavir, disease=congenital human immunodeficiency virus | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Darunavir, disease=congenital human immunodeficiency virus | success | 9 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Darunavir, disease=fibroma of prostate | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Darunavir, disease=fibroma of prostate | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Darunavir, disease=fibroma of prostate | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Darunavir, disease=Brenner tumor | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Darunavir, disease=Brenner tumor | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Darunavir, disease=Brenner tumor | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Darunavir, disease=benign reproductive system neoplasm | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Darunavir, disease=benign reproductive system neoplasm | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Darunavir, disease=benign reproductive system neoplasm | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Darunavir, disease=benign prostate phyllodes tumor | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Darunavir, disease=benign prostate phyllodes tumor | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Darunavir, disease=benign prostate phyllodes tumor | success | 0 |  |