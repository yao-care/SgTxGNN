# Activated charcoal 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Activated charcoal | |
| DrugBank ID | DB09278 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | Jeune syndrome situs inversus | 89.94% | L5 | 0 | 0 | S0 | Hold |
| 2 | orofacial clefting syndrome | 89.57% | L5 | 0 | 0 | S0 | Hold |
| 3 | disorder of fucoglycosan synthesis | 89.53% | L5 | 0 | 20 | S0 | Hold |
| 4 | Pierre Robin syndrome associated with a chromosomal anomaly | 89.49% | L5 | 0 | 0 | S0 | Hold |
| 5 | partial deletion of the long arm of chromosome 22 | 89.39% | L5 | 0 | 0 | S0 | Hold |
| 6 | partial deletion of the long arm of chromosome 7 | 89.29% | L5 | 0 | 0 | S0 | Hold |
| 7 | pulmonary valve disease | 89.19% | L5 | 0 | 2 | S0 | Hold |
| 8 | heart disease | 89.16% | L4 | 16 | 20 | S1 | Research Question |
| 9 | genetic syndromic Pierre Robin syndrome | 89.16% | L5 | 0 | 0 | S0 | Hold |
| 10 | Laubry-Pezzi syndrome | 89.06% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Activated charcoal | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Activated charcoal | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Activated charcoal, disease=Jeune syndrome situs inversus | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Activated charcoal, disease=Jeune syndrome situs inversus | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Activated charcoal, disease=Jeune syndrome situs inversus | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Activated charcoal, disease=orofacial clefting syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Activated charcoal, disease=orofacial clefting syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Activated charcoal, disease=orofacial clefting syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Activated charcoal, disease=disorder of fucoglycosan synthesis | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Activated charcoal, disease=disorder of fucoglycosan synthesis | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Activated charcoal, disease=disorder of fucoglycosan synthesis | success | 20 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Activated charcoal, disease=Pierre Robin syndrome associated with a chromosomal anomaly | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Activated charcoal, disease=Pierre Robin syndrome associated with a chromosomal anomaly | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Activated charcoal, disease=Pierre Robin syndrome associated with a chromosomal anomaly | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Activated charcoal, disease=partial deletion of the long arm of chromosome 22 | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Activated charcoal, disease=partial deletion of the long arm of chromosome 22 | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Activated charcoal, disease=partial deletion of the long arm of chromosome 22 | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Activated charcoal, disease=partial deletion of the long arm of chromosome 7 | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Activated charcoal, disease=partial deletion of the long arm of chromosome 7 | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Activated charcoal, disease=partial deletion of the long arm of chromosome 7 | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Activated charcoal, disease=pulmonary valve disease | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Activated charcoal, disease=pulmonary valve disease | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Activated charcoal, disease=pulmonary valve disease | success | 2 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Activated charcoal, disease=heart disease | success | 16 |  |
| 25 | ictrp | 2026-03-10 | drug=Activated charcoal, disease=heart disease | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Activated charcoal, disease=heart disease | success | 20 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Activated charcoal, disease=genetic syndromic Pierre Robin syndrome | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Activated charcoal, disease=genetic syndromic Pierre Robin syndrome | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Activated charcoal, disease=genetic syndromic Pierre Robin syndrome | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Activated charcoal, disease=Laubry-Pezzi syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Activated charcoal, disease=Laubry-Pezzi syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Activated charcoal, disease=Laubry-Pezzi syndrome | success | 0 |  |