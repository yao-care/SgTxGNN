# Gemfibrozil 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Gemfibrozil | |
| DrugBank ID | DB01241 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | rheumatoid arthritis | 99.90% | L4 | 0 | 4 | S1 | Research Question |
| 2 | multiple endocrine neoplasia | 99.83% | L5 | 0 | 0 | S0 | Hold |
| 3 | HIV infectious disease | 99.80% | L2 | 3 | 20 | S2 | Proceed with Guardrails |
| 4 | hypoalphalipoproteinemia | 99.77% | L2 | 0 | 13 | S2 | Proceed with Guardrails |
| 5 | brachydactyly-syndactyly syndrome | 99.77% | L5 | 0 | 0 | S0 | Hold |
| 6 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.77% | L5 | 0 | 0 | S0 | Hold |
| 7 | methemoglobinemia, alpha type | 99.76% | L5 | 0 | 0 | S0 | Hold |
| 8 | obsolete familial combined hyperlipidemia | 99.71% | L3 | 0 | 0 | S1 | Research Question |
| 9 | sclerosing cholangitis | 99.70% | L4 | 0 | 2 | S1 | Research Question |
| 10 | methemoglobin reductase deficiency | 99.70% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Gemfibrozil | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Gemfibrozil | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Gemfibrozil, disease=rheumatoid arthritis | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Gemfibrozil, disease=rheumatoid arthritis | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Gemfibrozil, disease=rheumatoid arthritis | success | 4 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Gemfibrozil, disease=multiple endocrine neoplasia | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Gemfibrozil, disease=multiple endocrine neoplasia | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Gemfibrozil, disease=multiple endocrine neoplasia | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Gemfibrozil, disease=HIV infectious disease | success | 3 |  |
| 10 | ictrp | 2026-03-09 | drug=Gemfibrozil, disease=HIV infectious disease | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Gemfibrozil, disease=HIV infectious disease | success | 20 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Gemfibrozil, disease=hypoalphalipoproteinemia | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Gemfibrozil, disease=hypoalphalipoproteinemia | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Gemfibrozil, disease=hypoalphalipoproteinemia | success | 13 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Gemfibrozil, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Gemfibrozil, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Gemfibrozil, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Gemfibrozil, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Gemfibrozil, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Gemfibrozil, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Gemfibrozil, disease=methemoglobinemia, alpha type | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Gemfibrozil, disease=methemoglobinemia, alpha type | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Gemfibrozil, disease=methemoglobinemia, alpha type | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Gemfibrozil, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Gemfibrozil, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Gemfibrozil, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Gemfibrozil, disease=sclerosing cholangitis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Gemfibrozil, disease=sclerosing cholangitis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Gemfibrozil, disease=sclerosing cholangitis | success | 2 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Gemfibrozil, disease=methemoglobin reductase deficiency | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Gemfibrozil, disease=methemoglobin reductase deficiency | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Gemfibrozil, disease=methemoglobin reductase deficiency | success | 0 |  |