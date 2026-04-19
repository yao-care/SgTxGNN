# Clioquinol 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Clioquinol | |
| DrugBank ID | DB04815 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | cutaneous candidiasis | 99.84% | L3 | 0 | 6 | S1 | Research Question |
| 2 | Majocchi granuloma | 99.26% | L5 | 0 | 0 | S0 | Hold |
| 3 | ectothrix infectious disease | 99.26% | L5 | 0 | 0 | S0 | Hold |
| 4 | endothrix infectious disease | 99.19% | L5 | 0 | 0 | S0 | Hold |
| 5 | superficial mycosis | 99.18% | L4 | 0 | 2 | S1 | Research Question |
| 6 | dermatophytosis of scalp or beard | 99.17% | L5 | 0 | 20 | S0 | Hold |
| 7 | tinea profunda | 99.13% | L5 | 0 | 0 | S0 | Hold |
| 8 | pityriasis versicolor | 98.97% | L5 | 0 | 0 | S0 | Hold |
| 9 | granuloma annulare | 95.27% | L5 | 0 | 0 | S0 | Hold |
| 10 | tinea manuum | 94.12% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Clioquinol | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Clioquinol | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Clioquinol, disease=cutaneous candidiasis | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Clioquinol, disease=cutaneous candidiasis | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Clioquinol, disease=cutaneous candidiasis | success | 6 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Clioquinol, disease=Majocchi granuloma | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Clioquinol, disease=Majocchi granuloma | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Clioquinol, disease=Majocchi granuloma | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Clioquinol, disease=ectothrix infectious disease | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Clioquinol, disease=ectothrix infectious disease | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Clioquinol, disease=ectothrix infectious disease | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Clioquinol, disease=endothrix infectious disease | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Clioquinol, disease=endothrix infectious disease | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Clioquinol, disease=endothrix infectious disease | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Clioquinol, disease=superficial mycosis | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Clioquinol, disease=superficial mycosis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Clioquinol, disease=superficial mycosis | success | 2 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Clioquinol, disease=dermatophytosis of scalp or beard | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Clioquinol, disease=dermatophytosis of scalp or beard | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Clioquinol, disease=dermatophytosis of scalp or beard | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Clioquinol, disease=tinea profunda | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Clioquinol, disease=tinea profunda | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Clioquinol, disease=tinea profunda | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Clioquinol, disease=pityriasis versicolor | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Clioquinol, disease=pityriasis versicolor | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Clioquinol, disease=pityriasis versicolor | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Clioquinol, disease=granuloma annulare | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Clioquinol, disease=granuloma annulare | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Clioquinol, disease=granuloma annulare | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Clioquinol, disease=tinea manuum | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Clioquinol, disease=tinea manuum | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Clioquinol, disease=tinea manuum | success | 0 |  |