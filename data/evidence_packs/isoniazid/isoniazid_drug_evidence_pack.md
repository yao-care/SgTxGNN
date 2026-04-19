# Isoniazid 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Isoniazid | |
| DrugBank ID | DB00951 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | conjunctivitis | 99.36% | L4 | 1 | 20 | S1 | Hold |
| 2 | rheumatoid arthritis | 98.71% | L3 | 0 | 20 | S1 | Research Question |
| 3 | shigellosis | 98.49% | L5 | 0 | 0 | S0 | Hold |
| 4 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 97.87% | L5 | 0 | 0 | S0 | Hold |
| 5 | leprosy | 97.85% | L3 | 4 | 20 | S2 | Research Question |
| 6 | brachydactyly-syndactyly syndrome | 97.82% | L5 | 0 | 0 | S0 | Hold |
| 7 | vestibular neuronitis | 97.80% | L5 | 0 | 0 | S0 | Hold |
| 8 | motor nerve neuritis | 97.76% | L4 | 0 | 2 | S0 | Hold |
| 9 | infectious otitis media | 97.73% | L4 | 0 | 1 | S0 | Hold |
| 10 | brachial plexus neuritis | 97.72% | L4 | 0 | 2 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Isoniazid | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Isoniazid | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Isoniazid, disease=conjunctivitis | success | 1 |  |
| 4 | ictrp | 2026-03-10 | drug=Isoniazid, disease=conjunctivitis | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Isoniazid, disease=conjunctivitis | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Isoniazid, disease=rheumatoid arthritis | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Isoniazid, disease=rheumatoid arthritis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Isoniazid, disease=rheumatoid arthritis | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Isoniazid, disease=shigellosis | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Isoniazid, disease=shigellosis | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Isoniazid, disease=shigellosis | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Isoniazid, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Isoniazid, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Isoniazid, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Isoniazid, disease=leprosy | success | 4 |  |
| 16 | ictrp | 2026-03-10 | drug=Isoniazid, disease=leprosy | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Isoniazid, disease=leprosy | success | 20 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Isoniazid, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Isoniazid, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Isoniazid, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Isoniazid, disease=vestibular neuronitis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Isoniazid, disease=vestibular neuronitis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Isoniazid, disease=vestibular neuronitis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Isoniazid, disease=motor nerve neuritis | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Isoniazid, disease=motor nerve neuritis | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Isoniazid, disease=motor nerve neuritis | success | 2 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Isoniazid, disease=infectious otitis media | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Isoniazid, disease=infectious otitis media | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Isoniazid, disease=infectious otitis media | success | 1 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Isoniazid, disease=brachial plexus neuritis | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Isoniazid, disease=brachial plexus neuritis | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Isoniazid, disease=brachial plexus neuritis | success | 2 |  |