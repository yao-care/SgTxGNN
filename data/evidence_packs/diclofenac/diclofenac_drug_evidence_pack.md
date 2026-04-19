# Diclofenac 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Diclofenac | |
| DrugBank ID | DB00586 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | hypotrichosis simplex of the scalp | 99.69% | L5 | 0 | 0 | S0 | Hold |
| 2 | acromesomelic dysplasia, Hunter-Thompson type | 99.67% | L5 | 0 | 0 | S0 | Hold |
| 3 | pseudoachondroplasia | 99.66% | L5 | 0 | 0 | S0 | Hold |
| 4 | brachyolmia | 99.65% | L5 | 0 | 0 | S0 | Hold |
| 5 | brachyolmia-amelogenesis imperfecta syndrome | 99.63% | L5 | 0 | 0 | S0 | Hold |
| 6 | congenital hypotrichosis milia | 99.60% | L5 | 0 | 0 | S0 | Hold |
| 7 | myosclerosis | 99.60% | L5 | 0 | 0 | S0 | Hold |
| 8 | diffuse alopecia areata | 99.57% | L5 | 0 | 0 | S0 | Hold |
| 9 | juvenile idiopathic arthritis | 99.25% | L3 | 2 | 18 | S2 | Proceed with Guardrails |
| 10 | WHIM syndrome | 99.16% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Diclofenac | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Diclofenac | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Diclofenac, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Diclofenac, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Diclofenac, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Diclofenac, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Diclofenac, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Diclofenac, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Diclofenac, disease=pseudoachondroplasia | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Diclofenac, disease=pseudoachondroplasia | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Diclofenac, disease=pseudoachondroplasia | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Diclofenac, disease=brachyolmia | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Diclofenac, disease=brachyolmia | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Diclofenac, disease=brachyolmia | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Diclofenac, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Diclofenac, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Diclofenac, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Diclofenac, disease=congenital hypotrichosis milia | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Diclofenac, disease=congenital hypotrichosis milia | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Diclofenac, disease=congenital hypotrichosis milia | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Diclofenac, disease=myosclerosis | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Diclofenac, disease=myosclerosis | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Diclofenac, disease=myosclerosis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Diclofenac, disease=diffuse alopecia areata | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Diclofenac, disease=diffuse alopecia areata | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Diclofenac, disease=diffuse alopecia areata | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Diclofenac, disease=juvenile idiopathic arthritis | success | 2 |  |
| 28 | ictrp | 2026-03-09 | drug=Diclofenac, disease=juvenile idiopathic arthritis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Diclofenac, disease=juvenile idiopathic arthritis | success | 18 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Diclofenac, disease=WHIM syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Diclofenac, disease=WHIM syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Diclofenac, disease=WHIM syndrome | success | 0 |  |