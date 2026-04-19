# Imatinib 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Imatinib | |
| DrugBank ID | DB00619 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | heart fibrosarcoma | 99.94% | L4 | 0 | 1 | S0 | Hold |
| 2 | fibroblastic neoplasm | 99.94% | L2 | 0 | 20 | S3 | Proceed with Guardrails |
| 3 | conventional fibrosarcoma | 99.93% | L3 | 1 | 9 | S2 | Research Question |
| 4 | kidney fibrosarcoma | 99.93% | L3 | 1 | 1 | S1 | Research Question |
| 5 | low grade fibromyxoid sarcoma | 99.93% | L5 | 0 | 1 | S0 | Hold |
| 6 | liposarcoma | 99.88% | L3 | 5 | 20 | S1 | Research Question |
| 7 | liver fibrosarcoma | 99.86% | L4 | 0 | 2 | S0 | Hold |
| 8 | autosomal recessive familial Mediterranean fever | 99.86% | L5 | 0 | 0 | S0 | Hold |
| 9 | ovarian myxoid liposarcoma | 99.85% | L5 | 0 | 0 | S0 | Hold |
| 10 | familial rhabdoid tumor | 99.83% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Imatinib | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Imatinib | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Imatinib, disease=heart fibrosarcoma | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Imatinib, disease=heart fibrosarcoma | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Imatinib, disease=heart fibrosarcoma | success | 1 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Imatinib, disease=fibroblastic neoplasm | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Imatinib, disease=fibroblastic neoplasm | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Imatinib, disease=fibroblastic neoplasm | success | 20 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Imatinib, disease=conventional fibrosarcoma | success | 1 |  |
| 10 | ictrp | 2026-03-09 | drug=Imatinib, disease=conventional fibrosarcoma | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Imatinib, disease=conventional fibrosarcoma | success | 9 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Imatinib, disease=kidney fibrosarcoma | success | 1 |  |
| 13 | ictrp | 2026-03-09 | drug=Imatinib, disease=kidney fibrosarcoma | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Imatinib, disease=kidney fibrosarcoma | success | 1 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Imatinib, disease=low grade fibromyxoid sarcoma | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Imatinib, disease=low grade fibromyxoid sarcoma | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Imatinib, disease=low grade fibromyxoid sarcoma | success | 1 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Imatinib, disease=liposarcoma | success | 5 |  |
| 19 | ictrp | 2026-03-09 | drug=Imatinib, disease=liposarcoma | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Imatinib, disease=liposarcoma | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Imatinib, disease=liver fibrosarcoma | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Imatinib, disease=liver fibrosarcoma | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Imatinib, disease=liver fibrosarcoma | success | 2 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Imatinib, disease=autosomal recessive familial Mediterranean fever | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Imatinib, disease=autosomal recessive familial Mediterranean fever | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Imatinib, disease=autosomal recessive familial Mediterranean fever | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Imatinib, disease=ovarian myxoid liposarcoma | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Imatinib, disease=ovarian myxoid liposarcoma | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Imatinib, disease=ovarian myxoid liposarcoma | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Imatinib, disease=familial rhabdoid tumor | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Imatinib, disease=familial rhabdoid tumor | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Imatinib, disease=familial rhabdoid tumor | success | 0 |  |