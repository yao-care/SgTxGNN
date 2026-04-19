# Adalimumab 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Adalimumab | |
| DrugBank ID | DB00051 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | rheumatoid vasculitis | 99.80% | L4 | 5 | 20 | S1 | Research Question |
| 2 | hypermobility of coccyx | 99.77% | L5 | 0 | 0 | S0 | Hold |
| 3 | inflammatory spondylopathy | 99.77% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 4 | Kummell disease | 99.74% | L5 | 0 | 0 | S0 | Hold |
| 5 | polyarticular juvenile rheumatoid arthritis | 99.72% | L1 | 11 | 20 | S3 | Proceed with Guardrails |
| 6 | vertebral disease | 99.18% | L1 | 8 | 20 | S3 | Proceed with Guardrails |
| 7 | polyp of middle ear | 97.94% | L5 | 0 | 0 | S0 | Hold |
| 8 | polyp of vocal cord | 97.93% | L5 | 0 | 0 | S0 | Hold |
| 9 | polyp of ureter | 97.86% | L5 | 0 | 0 | S0 | Hold |
| 10 | polyp of frontal sinus | 97.85% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Adalimumab | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Adalimumab | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Adalimumab, disease=rheumatoid vasculitis | success | 5 |  |
| 4 | ictrp | 2026-03-09 | drug=Adalimumab, disease=rheumatoid vasculitis | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Adalimumab, disease=rheumatoid vasculitis | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Adalimumab, disease=hypermobility of coccyx | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Adalimumab, disease=hypermobility of coccyx | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Adalimumab, disease=hypermobility of coccyx | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Adalimumab, disease=inflammatory spondylopathy | success | 50 |  |
| 10 | ictrp | 2026-03-09 | drug=Adalimumab, disease=inflammatory spondylopathy | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Adalimumab, disease=inflammatory spondylopathy | success | 20 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Adalimumab, disease=Kummell disease | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Adalimumab, disease=Kummell disease | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Adalimumab, disease=Kummell disease | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Adalimumab, disease=polyarticular juvenile rheumatoid arthritis | success | 11 |  |
| 16 | ictrp | 2026-03-09 | drug=Adalimumab, disease=polyarticular juvenile rheumatoid arthritis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Adalimumab, disease=polyarticular juvenile rheumatoid arthritis | success | 20 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Adalimumab, disease=vertebral disease | success | 8 |  |
| 19 | ictrp | 2026-03-09 | drug=Adalimumab, disease=vertebral disease | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Adalimumab, disease=vertebral disease | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Adalimumab, disease=polyp of middle ear | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Adalimumab, disease=polyp of middle ear | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Adalimumab, disease=polyp of middle ear | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Adalimumab, disease=polyp of vocal cord | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Adalimumab, disease=polyp of vocal cord | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Adalimumab, disease=polyp of vocal cord | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Adalimumab, disease=polyp of ureter | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Adalimumab, disease=polyp of ureter | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Adalimumab, disease=polyp of ureter | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Adalimumab, disease=polyp of frontal sinus | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Adalimumab, disease=polyp of frontal sinus | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Adalimumab, disease=polyp of frontal sinus | success | 0 |  |