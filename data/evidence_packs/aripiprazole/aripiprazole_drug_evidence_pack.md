# Aripiprazole 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Aripiprazole | |
| DrugBank ID | DB01238 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | major affective disorder | 99.62% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 2 | gaze palsy, familial horizontal, with progressive scoliosis | 99.60% | L5 | 0 | 0 | S0 | Hold |
| 3 | asperger syndrome, susceptibility to | 99.52% | L5 | 0 | 0 | S0 | Hold |
| 4 | Phelan-McDermid syndrome | 99.44% | L5 | 0 | 0 | S0 | Hold |
| 5 | amelocerebrohypohidrotic syndrome | 99.34% | L5 | 0 | 0 | S0 | Hold |
| 6 | distal 17p13.3 microdeletion syndrome | 99.34% | L5 | 0 | 0 | S0 | Hold |
| 7 | trichotillomania | 99.26% | L3 | 2 | 14 | S2 | Research Question |
| 8 | Malan overgrowth syndrome | 99.26% | L5 | 0 | 0 | S0 | Hold |
| 9 | retinal dystrophy with or without extraocular anomalies | 99.25% | L5 | 0 | 15 | S0 | Hold |
| 10 | hydranencephaly (disease) | 99.21% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Aripiprazole | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Aripiprazole | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Aripiprazole, disease=major affective disorder | success | 50 |  |
| 4 | ictrp | 2026-03-09 | drug=Aripiprazole, disease=major affective disorder | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Aripiprazole, disease=major affective disorder | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Aripiprazole, disease=gaze palsy, familial horizontal, with progressive scoliosis | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Aripiprazole, disease=gaze palsy, familial horizontal, with progressive scoliosis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Aripiprazole, disease=gaze palsy, familial horizontal, with progressive scoliosis | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Aripiprazole, disease=asperger syndrome, susceptibility to | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Aripiprazole, disease=asperger syndrome, susceptibility to | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Aripiprazole, disease=asperger syndrome, susceptibility to | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Aripiprazole, disease=Phelan-McDermid syndrome | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Aripiprazole, disease=Phelan-McDermid syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Aripiprazole, disease=Phelan-McDermid syndrome | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Aripiprazole, disease=amelocerebrohypohidrotic syndrome | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Aripiprazole, disease=amelocerebrohypohidrotic syndrome | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Aripiprazole, disease=amelocerebrohypohidrotic syndrome | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Aripiprazole, disease=distal 17p13.3 microdeletion syndrome | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Aripiprazole, disease=distal 17p13.3 microdeletion syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Aripiprazole, disease=distal 17p13.3 microdeletion syndrome | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Aripiprazole, disease=trichotillomania | success | 2 |  |
| 22 | ictrp | 2026-03-09 | drug=Aripiprazole, disease=trichotillomania | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Aripiprazole, disease=trichotillomania | success | 14 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Aripiprazole, disease=Malan overgrowth syndrome | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Aripiprazole, disease=Malan overgrowth syndrome | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Aripiprazole, disease=Malan overgrowth syndrome | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Aripiprazole, disease=retinal dystrophy with or without extraocular anomalies | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Aripiprazole, disease=retinal dystrophy with or without extraocular anomalies | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Aripiprazole, disease=retinal dystrophy with or without extraocular anomalies | success | 15 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Aripiprazole, disease=hydranencephaly (disease) | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Aripiprazole, disease=hydranencephaly (disease) | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Aripiprazole, disease=hydranencephaly (disease) | success | 0 |  |