# Chromium 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Chromium | |
| DrugBank ID | DB11136 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | osteoarthritis | 98.68% | L3 | 48 | 20 | S1 | Hold |
| 2 | osteoarthritis susceptibility | 98.54% | L5 | 0 | 5 | S0 | Hold |
| 3 | rheumatoid arthritis | 98.54% | L2 | 9 | 20 | S3 | Proceed with Guardrails |
| 4 | gout | 97.98% | L5 | 0 | 7 | S0 | Hold |
| 5 | pseudoachondroplasia | 97.95% | L5 | 0 | 0 | S0 | Hold |
| 6 | hepatic porphyria | 97.87% | L5 | 0 | 4 | S0 | Hold |
| 7 | brachyolmia | 97.80% | L5 | 0 | 0 | S0 | Hold |
| 8 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 97.69% | L5 | 0 | 0 | S0 | Hold |
| 9 | acromesomelic dysplasia, Hunter-Thompson type | 97.67% | L5 | 0 | 0 | S0 | Hold |
| 10 | brachyolmia-amelogenesis imperfecta syndrome | 97.58% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Chromium | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Chromium | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Chromium, disease=osteoarthritis | success | 48 |  |
| 4 | ictrp | 2026-03-10 | drug=Chromium, disease=osteoarthritis | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Chromium, disease=osteoarthritis | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Chromium, disease=osteoarthritis susceptibility | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Chromium, disease=osteoarthritis susceptibility | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Chromium, disease=osteoarthritis susceptibility | success | 5 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Chromium, disease=rheumatoid arthritis | success | 9 |  |
| 10 | ictrp | 2026-03-10 | drug=Chromium, disease=rheumatoid arthritis | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Chromium, disease=rheumatoid arthritis | success | 20 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Chromium, disease=gout | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Chromium, disease=gout | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Chromium, disease=gout | success | 7 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Chromium, disease=pseudoachondroplasia | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Chromium, disease=pseudoachondroplasia | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Chromium, disease=pseudoachondroplasia | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Chromium, disease=hepatic porphyria | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Chromium, disease=hepatic porphyria | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Chromium, disease=hepatic porphyria | success | 4 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Chromium, disease=brachyolmia | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Chromium, disease=brachyolmia | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Chromium, disease=brachyolmia | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Chromium, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Chromium, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Chromium, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Chromium, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Chromium, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Chromium, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Chromium, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Chromium, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Chromium, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |