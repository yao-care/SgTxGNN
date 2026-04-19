# Golimumab 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Golimumab | |
| DrugBank ID | DB06674 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | rheumatoid vasculitis | 99.73% | L3 | 3 | 6 | S1 | Research Question |
| 2 | hypermobility of coccyx | 99.67% | L5 | 0 | 0 | S0 | Hold |
| 3 | inflammatory spondylopathy | 99.66% | L1 | 50 | 18 | S3 | Proceed with Guardrails |
| 4 | Kummell disease | 99.61% | L5 | 0 | 0 | S0 | Hold |
| 5 | polyarticular juvenile rheumatoid arthritis | 99.59% | L1 | 2 | 17 | S3 | Proceed with Guardrails |
| 6 | vertebral disease | 98.76% | L2 | 3 | 20 | S2 | Research Question |
| 7 | congenital hypotrichosis with juvenile macular dystrophy | 96.16% | L5 | 0 | 0 | S0 | Hold |
| 8 | polyp of vocal cord | 95.83% | L5 | 0 | 0 | S0 | Hold |
| 9 | polyp of middle ear | 95.83% | L5 | 0 | 0 | S0 | Hold |
| 10 | mendelian susceptibility to mycobacterial diseases due to complete IL12B deficiency | 95.74% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Golimumab | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Golimumab | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Golimumab, disease=rheumatoid vasculitis | success | 3 |  |
| 4 | ictrp | 2026-03-09 | drug=Golimumab, disease=rheumatoid vasculitis | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Golimumab, disease=rheumatoid vasculitis | success | 6 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Golimumab, disease=hypermobility of coccyx | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Golimumab, disease=hypermobility of coccyx | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Golimumab, disease=hypermobility of coccyx | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Golimumab, disease=inflammatory spondylopathy | success | 50 |  |
| 10 | ictrp | 2026-03-09 | drug=Golimumab, disease=inflammatory spondylopathy | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Golimumab, disease=inflammatory spondylopathy | success | 18 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Golimumab, disease=Kummell disease | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Golimumab, disease=Kummell disease | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Golimumab, disease=Kummell disease | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Golimumab, disease=polyarticular juvenile rheumatoid arthritis | success | 2 |  |
| 16 | ictrp | 2026-03-09 | drug=Golimumab, disease=polyarticular juvenile rheumatoid arthritis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Golimumab, disease=polyarticular juvenile rheumatoid arthritis | success | 17 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Golimumab, disease=vertebral disease | success | 3 |  |
| 19 | ictrp | 2026-03-09 | drug=Golimumab, disease=vertebral disease | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Golimumab, disease=vertebral disease | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Golimumab, disease=congenital hypotrichosis with juvenile macular dystrophy | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Golimumab, disease=congenital hypotrichosis with juvenile macular dystrophy | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Golimumab, disease=congenital hypotrichosis with juvenile macular dystrophy | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Golimumab, disease=polyp of vocal cord | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Golimumab, disease=polyp of vocal cord | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Golimumab, disease=polyp of vocal cord | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Golimumab, disease=polyp of middle ear | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Golimumab, disease=polyp of middle ear | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Golimumab, disease=polyp of middle ear | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Golimumab, disease=mendelian susceptibility to mycobacterial diseases due to complete IL12B deficiency | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Golimumab, disease=mendelian susceptibility to mycobacterial diseases due to complete IL12B deficiency | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Golimumab, disease=mendelian susceptibility to mycobacterial diseases due to complete IL12B deficiency | success | 0 |  |