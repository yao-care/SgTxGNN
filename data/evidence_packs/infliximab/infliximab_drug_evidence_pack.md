# Infliximab 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Infliximab | |
| DrugBank ID | DB00065 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 90.22% | L5 | 0 | 0 | S0 | Hold |
| 2 | brachydactyly-syndactyly syndrome | 89.88% | L5 | 0 | 0 | S0 | Hold |
| 3 | rheumatoid vasculitis | 85.32% | L4 | 4 | 20 | S1 | Hold |
| 4 | hypermobility of coccyx | 82.49% | L5 | 0 | 0 | S0 | Hold |
| 5 | anus disease | 81.21% | L1 | 16 | 20 | S3 | Proceed with Guardrails |
| 6 | Kummell disease | 81.15% | L5 | 0 | 0 | S0 | Hold |
| 7 | inflammatory spondylopathy | 80.92% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 8 | polyarticular juvenile rheumatoid arthritis | 80.14% | L1 | 3 | 19 | S3 | Proceed with Guardrails |
| 9 | bronchitis | 77.87% | L4 | 4 | 20 | S1 | Research Question |
| 10 | Crohn disease of the esophagus | 77.58% | L3 | 0 | 8 | S2 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Infliximab | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Infliximab | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Infliximab, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Infliximab, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Infliximab, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Infliximab, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Infliximab, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Infliximab, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Infliximab, disease=rheumatoid vasculitis | success | 4 |  |
| 10 | ictrp | 2026-03-10 | drug=Infliximab, disease=rheumatoid vasculitis | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Infliximab, disease=rheumatoid vasculitis | success | 20 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Infliximab, disease=hypermobility of coccyx | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Infliximab, disease=hypermobility of coccyx | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Infliximab, disease=hypermobility of coccyx | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Infliximab, disease=anus disease | success | 16 |  |
| 16 | ictrp | 2026-03-10 | drug=Infliximab, disease=anus disease | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Infliximab, disease=anus disease | success | 20 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Infliximab, disease=Kummell disease | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Infliximab, disease=Kummell disease | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Infliximab, disease=Kummell disease | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Infliximab, disease=inflammatory spondylopathy | success | 50 |  |
| 22 | ictrp | 2026-03-10 | drug=Infliximab, disease=inflammatory spondylopathy | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Infliximab, disease=inflammatory spondylopathy | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Infliximab, disease=polyarticular juvenile rheumatoid arthritis | success | 3 |  |
| 25 | ictrp | 2026-03-10 | drug=Infliximab, disease=polyarticular juvenile rheumatoid arthritis | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Infliximab, disease=polyarticular juvenile rheumatoid arthritis | success | 19 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Infliximab, disease=bronchitis | success | 4 |  |
| 28 | ictrp | 2026-03-10 | drug=Infliximab, disease=bronchitis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Infliximab, disease=bronchitis | success | 20 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Infliximab, disease=Crohn disease of the esophagus | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Infliximab, disease=Crohn disease of the esophagus | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Infliximab, disease=Crohn disease of the esophagus | success | 8 |  |