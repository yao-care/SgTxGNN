# Indomethacin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Indomethacin | |
| DrugBank ID | DB00328 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | brachydactyly-syndactyly syndrome | 99.97% | L5 | 0 | 0 | S0 | Hold |
| 2 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.97% | L5 | 0 | 0 | S0 | Hold |
| 3 | acromesomelic dysplasia, Hunter-Thompson type | 99.89% | L5 | 0 | 0 | S0 | Hold |
| 4 | WHIM syndrome | 99.88% | L5 | 0 | 0 | S0 | Hold |
| 5 | brachyolmia-amelogenesis imperfecta syndrome | 99.87% | L5 | 0 | 0 | S0 | Hold |
| 6 | brachyolmia | 99.87% | L5 | 0 | 0 | S0 | Hold |
| 7 | myosclerosis | 99.86% | L5 | 0 | 0 | S0 | Hold |
| 8 | juvenile idiopathic arthritis | 99.84% | L2 | 0 | 20 | S2 | Proceed with Guardrails |
| 9 | rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | 99.84% | L4 | 0 | 0 | S1 | Research Question |
| 10 | rheumatoid nodulosis | 99.83% | L4 | 0 | 3 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Indomethacin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Indomethacin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Indomethacin, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Indomethacin, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Indomethacin, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Indomethacin, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Indomethacin, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Indomethacin, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Indomethacin, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Indomethacin, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Indomethacin, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Indomethacin, disease=WHIM syndrome | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Indomethacin, disease=WHIM syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Indomethacin, disease=WHIM syndrome | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Indomethacin, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Indomethacin, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Indomethacin, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Indomethacin, disease=brachyolmia | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Indomethacin, disease=brachyolmia | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Indomethacin, disease=brachyolmia | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Indomethacin, disease=myosclerosis | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Indomethacin, disease=myosclerosis | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Indomethacin, disease=myosclerosis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Indomethacin, disease=juvenile idiopathic arthritis | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Indomethacin, disease=juvenile idiopathic arthritis | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Indomethacin, disease=juvenile idiopathic arthritis | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Indomethacin, disease=rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Indomethacin, disease=rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Indomethacin, disease=rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Indomethacin, disease=rheumatoid nodulosis | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Indomethacin, disease=rheumatoid nodulosis | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Indomethacin, disease=rheumatoid nodulosis | success | 3 |  |