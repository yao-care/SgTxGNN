# Ketoprofen 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Ketoprofen | |
| DrugBank ID | DB01009 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | acromesomelic dysplasia, Hunter-Thompson type | 99.98% | L5 | 0 | 0 | S0 | Hold |
| 2 | brachyolmia-amelogenesis imperfecta syndrome | 99.98% | L5 | 0 | 0 | S0 | Hold |
| 3 | myosclerosis | 99.98% | L5 | 0 | 0 | S0 | Hold |
| 4 | brachyolmia | 99.98% | L5 | 0 | 0 | S0 | Hold |
| 5 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.98% | L5 | 0 | 0 | S0 | Hold |
| 6 | brachydactyly-syndactyly syndrome | 99.97% | L5 | 0 | 0 | S0 | Hold |
| 7 | pseudoachondroplasia | 99.95% | L5 | 0 | 0 | S0 | Hold |
| 8 | spondyloarthropathy, susceptibility to | 99.86% | L4 | 0 | 1 | S1 | Research Question |
| 9 | WHIM syndrome | 99.86% | L5 | 0 | 0 | S0 | Hold |
| 10 | juvenile arthritis due to defect in LACC1 | 99.74% | L4 | 0 | 0 | S0 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Ketoprofen | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Ketoprofen | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Ketoprofen, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Ketoprofen, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Ketoprofen, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Ketoprofen, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Ketoprofen, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Ketoprofen, disease=brachyolmia-amelogenesis imperfecta syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Ketoprofen, disease=myosclerosis | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Ketoprofen, disease=myosclerosis | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Ketoprofen, disease=myosclerosis | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Ketoprofen, disease=brachyolmia | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Ketoprofen, disease=brachyolmia | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Ketoprofen, disease=brachyolmia | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Ketoprofen, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Ketoprofen, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Ketoprofen, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Ketoprofen, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Ketoprofen, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Ketoprofen, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Ketoprofen, disease=pseudoachondroplasia | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Ketoprofen, disease=pseudoachondroplasia | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Ketoprofen, disease=pseudoachondroplasia | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Ketoprofen, disease=spondyloarthropathy, susceptibility to | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Ketoprofen, disease=spondyloarthropathy, susceptibility to | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Ketoprofen, disease=spondyloarthropathy, susceptibility to | success | 1 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Ketoprofen, disease=WHIM syndrome | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Ketoprofen, disease=WHIM syndrome | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Ketoprofen, disease=WHIM syndrome | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Ketoprofen, disease=juvenile arthritis due to defect in LACC1 | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Ketoprofen, disease=juvenile arthritis due to defect in LACC1 | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Ketoprofen, disease=juvenile arthritis due to defect in LACC1 | success | 0 |  |