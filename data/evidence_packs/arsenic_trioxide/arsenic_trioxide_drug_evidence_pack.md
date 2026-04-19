# Arsenic trioxide 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Arsenic trioxide | |
| DrugBank ID | DB01169 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | unclassified myelodysplastic syndrome | 99.93% | L4 | 0 | 0 | S1 | Research Question |
| 2 | refractory cytopenia of childhood | 99.93% | L3 | 1 | 0 | S1 | Research Question |
| 3 | severe congenital hypochromic anemia with ringed sideroblasts | 99.93% | L5 | 0 | 0 | S0 | Hold |
| 4 | aregenerative anemia | 99.92% | L3 | 6 | 12 | S2 | Proceed with Guardrails |
| 5 | partial deletion of the long arm of chromosome 5 | 99.92% | L4 | 0 | 0 | S1 | Research Question |
| 6 | myelodysplastic syndrome | 99.91% | L2 | 24 | 20 | S3 | Proceed with Guardrails |
| 7 | Ewing sarcoma | 99.89% | L3 | 1 | 10 | S1 | Research Question |
| 8 | dermatofibrosarcoma protuberans | 99.77% | L5 | 0 | 0 | S0 | Hold |
| 9 | liposarcoma | 99.75% | L5 | 0 | 0 | S0 | Hold |
| 10 | ovarian myxoid liposarcoma | 99.70% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Arsenic trioxide | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Arsenic trioxide | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Arsenic trioxide, disease=unclassified myelodysplastic syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Arsenic trioxide, disease=unclassified myelodysplastic syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Arsenic trioxide, disease=unclassified myelodysplastic syndrome | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Arsenic trioxide, disease=refractory cytopenia of childhood | success | 1 |  |
| 7 | ictrp | 2026-03-09 | drug=Arsenic trioxide, disease=refractory cytopenia of childhood | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Arsenic trioxide, disease=refractory cytopenia of childhood | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Arsenic trioxide, disease=severe congenital hypochromic anemia with ringed sideroblasts | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Arsenic trioxide, disease=severe congenital hypochromic anemia with ringed sideroblasts | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Arsenic trioxide, disease=severe congenital hypochromic anemia with ringed sideroblasts | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Arsenic trioxide, disease=aregenerative anemia | success | 6 |  |
| 13 | ictrp | 2026-03-09 | drug=Arsenic trioxide, disease=aregenerative anemia | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Arsenic trioxide, disease=aregenerative anemia | success | 12 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Arsenic trioxide, disease=partial deletion of the long arm of chromosome 5 | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Arsenic trioxide, disease=partial deletion of the long arm of chromosome 5 | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Arsenic trioxide, disease=partial deletion of the long arm of chromosome 5 | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Arsenic trioxide, disease=myelodysplastic syndrome | success | 24 |  |
| 19 | ictrp | 2026-03-09 | drug=Arsenic trioxide, disease=myelodysplastic syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Arsenic trioxide, disease=myelodysplastic syndrome | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Arsenic trioxide, disease=Ewing sarcoma | success | 1 |  |
| 22 | ictrp | 2026-03-09 | drug=Arsenic trioxide, disease=Ewing sarcoma | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Arsenic trioxide, disease=Ewing sarcoma | success | 10 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Arsenic trioxide, disease=dermatofibrosarcoma protuberans | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Arsenic trioxide, disease=dermatofibrosarcoma protuberans | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Arsenic trioxide, disease=dermatofibrosarcoma protuberans | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Arsenic trioxide, disease=liposarcoma | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Arsenic trioxide, disease=liposarcoma | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Arsenic trioxide, disease=liposarcoma | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Arsenic trioxide, disease=ovarian myxoid liposarcoma | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Arsenic trioxide, disease=ovarian myxoid liposarcoma | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Arsenic trioxide, disease=ovarian myxoid liposarcoma | success | 0 |  |