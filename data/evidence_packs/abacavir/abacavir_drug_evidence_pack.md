# Abacavir 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Abacavir | |
| DrugBank ID | DB01048 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | simian immunodeficiency virus infection | 99.79% | L4 | 0 | 1 | S1 | Hold |
| 2 | feline acquired immunodeficiency syndrome | 99.79% | L4 | 4 | 1 | S1 | Hold |
| 3 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.78% | L5 | 0 | 0 | S0 | Hold |
| 4 | obsolete familial combined hyperlipidemia | 98.69% | L5 | 0 | 0 | S0 | Hold |
| 5 | congenital human immunodeficiency virus | 92.76% | L1 | 24 | 7 | S3 | Proceed with Guardrails |
| 6 | AIDS related complex | 92.76% | L2 | 2 | 14 | S2 | Research Question |
| 7 | chronic hepatitis C virus infection | 92.67% | L3 | 3 | 20 | S2 | Research Question |
| 8 | paratenonitis | 88.15% | L5 | 0 | 0 | S0 | Hold |
| 9 | calcific tendinitis | 87.89% | L5 | 0 | 0 | S0 | Hold |
| 10 | fibroma of prostate | 87.03% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Abacavir | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Abacavir | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Abacavir, disease=simian immunodeficiency virus infection | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Abacavir, disease=simian immunodeficiency virus infection | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Abacavir, disease=simian immunodeficiency virus infection | success | 1 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Abacavir, disease=feline acquired immunodeficiency syndrome | success | 4 |  |
| 7 | ictrp | 2026-03-09 | drug=Abacavir, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Abacavir, disease=feline acquired immunodeficiency syndrome | success | 1 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Abacavir, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Abacavir, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Abacavir, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Abacavir, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Abacavir, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Abacavir, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Abacavir, disease=congenital human immunodeficiency virus | success | 24 |  |
| 16 | ictrp | 2026-03-09 | drug=Abacavir, disease=congenital human immunodeficiency virus | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Abacavir, disease=congenital human immunodeficiency virus | success | 7 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Abacavir, disease=AIDS related complex | success | 2 |  |
| 19 | ictrp | 2026-03-09 | drug=Abacavir, disease=AIDS related complex | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Abacavir, disease=AIDS related complex | success | 14 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Abacavir, disease=chronic hepatitis C virus infection | success | 3 |  |
| 22 | ictrp | 2026-03-09 | drug=Abacavir, disease=chronic hepatitis C virus infection | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Abacavir, disease=chronic hepatitis C virus infection | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Abacavir, disease=paratenonitis | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Abacavir, disease=paratenonitis | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Abacavir, disease=paratenonitis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Abacavir, disease=calcific tendinitis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Abacavir, disease=calcific tendinitis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Abacavir, disease=calcific tendinitis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Abacavir, disease=fibroma of prostate | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Abacavir, disease=fibroma of prostate | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Abacavir, disease=fibroma of prostate | success | 0 |  |