# Azathioprine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Azathioprine | |
| DrugBank ID | DB00993 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 100.00% | L5 | 0 | 0 | S0 | Hold |
| 2 | brachydactyly-syndactyly syndrome | 100.00% | L5 | 0 | 0 | S0 | Hold |
| 3 | osteoarthritis susceptibility | 99.70% | L5 | 0 | 0 | S0 | Hold |
| 4 | WHIM syndrome | 99.68% | L5 | 0 | 0 | S0 | Hold |
| 5 | inflammatory bowel disease | 99.52% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 6 | granulomatous disease, chronic, autosomal recessive, 5 | 99.41% | L5 | 0 | 0 | S0 | Hold |
| 7 | osteoarthritis | 99.40% | L4 | 4 | 12 | S1 | Hold |
| 8 | granulomatous disease with defect in neutrophil chemotaxis | 99.37% | L5 | 0 | 0 | S0 | Hold |
| 9 | ulcerative colitis (disease) | 99.33% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 10 | acromesomelic dysplasia, Hunter-Thompson type | 99.27% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Azathioprine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Azathioprine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Azathioprine, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Azathioprine, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Azathioprine, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Azathioprine, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Azathioprine, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Azathioprine, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Azathioprine, disease=osteoarthritis susceptibility | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Azathioprine, disease=osteoarthritis susceptibility | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Azathioprine, disease=osteoarthritis susceptibility | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Azathioprine, disease=WHIM syndrome | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Azathioprine, disease=WHIM syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Azathioprine, disease=WHIM syndrome | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Azathioprine, disease=inflammatory bowel disease | success | 50 |  |
| 16 | ictrp | 2026-03-09 | drug=Azathioprine, disease=inflammatory bowel disease | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Azathioprine, disease=inflammatory bowel disease | success | 20 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Azathioprine, disease=granulomatous disease, chronic, autosomal recessive, 5 | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Azathioprine, disease=granulomatous disease, chronic, autosomal recessive, 5 | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Azathioprine, disease=granulomatous disease, chronic, autosomal recessive, 5 | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Azathioprine, disease=osteoarthritis | success | 4 |  |
| 22 | ictrp | 2026-03-09 | drug=Azathioprine, disease=osteoarthritis | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Azathioprine, disease=osteoarthritis | success | 12 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Azathioprine, disease=granulomatous disease with defect in neutrophil chemotaxis | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Azathioprine, disease=granulomatous disease with defect in neutrophil chemotaxis | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Azathioprine, disease=granulomatous disease with defect in neutrophil chemotaxis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Azathioprine, disease=ulcerative colitis (disease) | success | 50 |  |
| 28 | ictrp | 2026-03-09 | drug=Azathioprine, disease=ulcerative colitis (disease) | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Azathioprine, disease=ulcerative colitis (disease) | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Azathioprine, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Azathioprine, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Azathioprine, disease=acromesomelic dysplasia, Hunter-Thompson type | success | 0 |  |