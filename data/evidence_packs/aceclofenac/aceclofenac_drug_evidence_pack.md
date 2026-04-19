# Aceclofenac 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Aceclofenac | |
| DrugBank ID | DB06736 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | brachyolmia-amelogenesis imperfecta syndrome | 99.89% | L5 | 0 | 0 | S0 | Hold |
| 2 | acromesomelic dysplasia, Hunter-Thompson type | 99.89% | L5 | 0 | 0 | S0 | Hold |
| 3 | myosclerosis | 99.88% | L5 | 0 | 0 | S0 | Hold |
| 4 | brachyolmia | 99.87% | L5 | 0 | 0 | S0 | Hold |
| 5 | pseudoachondroplasia | 99.85% | L5 | 0 | 0 | S0 | Hold |
| 6 | hypermobility of coccyx | 99.69% | L5 | 0 | 0 | S0 | Hold |
| 7 | rheumatoid vasculitis | 99.64% | L5 | 0 | 0 | S0 | Hold |
| 8 | inflammatory spondylopathy | 99.63% | L2 | 3 | 17 | S2 | Proceed with Guardrails |
| 9 | polyarticular juvenile rheumatoid arthritis | 99.63% | L5 | 0 | 0 | S0 | Hold |
| 10 | Kummell disease | 99.62% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Aceclofenac | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Aceclofenac | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Aceclofenac, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Aceclofenac, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Aceclofenac, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Aceclofenac, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Aceclofenac, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Aceclofenac, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Aceclofenac, disease=myosclerosis | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Aceclofenac, disease=myosclerosis | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Aceclofenac, disease=myosclerosis | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Aceclofenac, disease=brachyolmia | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Aceclofenac, disease=brachyolmia | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Aceclofenac, disease=brachyolmia | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Aceclofenac, disease=pseudoachondroplasia | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Aceclofenac, disease=pseudoachondroplasia | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Aceclofenac, disease=pseudoachondroplasia | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Aceclofenac, disease=hypermobility of coccyx | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Aceclofenac, disease=hypermobility of coccyx | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Aceclofenac, disease=hypermobility of coccyx | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Aceclofenac, disease=rheumatoid vasculitis | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Aceclofenac, disease=rheumatoid vasculitis | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Aceclofenac, disease=rheumatoid vasculitis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Aceclofenac, disease=inflammatory spondylopathy | success | 3 |  |
| 25 | ictrp | 2026-03-09 | drug=Aceclofenac, disease=inflammatory spondylopathy | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Aceclofenac, disease=inflammatory spondylopathy | success | 17 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Aceclofenac, disease=polyarticular juvenile rheumatoid arthritis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Aceclofenac, disease=polyarticular juvenile rheumatoid arthritis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Aceclofenac, disease=polyarticular juvenile rheumatoid arthritis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Aceclofenac, disease=Kummell disease | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Aceclofenac, disease=Kummell disease | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Aceclofenac, disease=Kummell disease | success | 0 |  |