# Diazepam 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Diazepam | |
| DrugBank ID | DB00829 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | insomnia (disease) | 100.00% | L2 | 24 | 18 | S2 | Proceed with Guardrails |
| 2 | cauda equina syndrome | 99.99% | L5 | 0 | 1 | S0 | Hold |
| 3 | sleep disorder, initiating and maintaining sleep | 99.97% | L3 | 0 | 20 | S1 | Research Question |
| 4 | attention deficit hyperactivity disorder, inattentive type | 99.97% | L5 | 0 | 0 | S0 | Hold |
| 5 | barbiturate abuse | 99.95% | L5 | 0 | 0 | S0 | Hold |
| 6 | hallucinogen abuse | 99.95% | L4 | 0 | 20 | S1 | Research Question |
| 7 | antidepressant type abuse | 99.95% | L4 | 0 | 5 | S0 | Hold |
| 8 | specific developmental disorder | 99.95% | L5 | 1 | 5 | S0 | Hold |
| 9 | attention deficit-hyperactivity disorder | 99.93% | L5 | 1 | 18 | S0 | Hold |
| 10 | obsolete neurogenic bladder (disease) | 99.91% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Diazepam | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Diazepam | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Diazepam, disease=insomnia (disease) | success | 24 |  |
| 4 | ictrp | 2026-03-09 | drug=Diazepam, disease=insomnia (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Diazepam, disease=insomnia (disease) | success | 18 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Diazepam, disease=cauda equina syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Diazepam, disease=cauda equina syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Diazepam, disease=cauda equina syndrome | success | 1 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Diazepam, disease=sleep disorder, initiating and maintaining sleep | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Diazepam, disease=sleep disorder, initiating and maintaining sleep | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Diazepam, disease=sleep disorder, initiating and maintaining sleep | success | 20 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Diazepam, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Diazepam, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Diazepam, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Diazepam, disease=barbiturate abuse | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Diazepam, disease=barbiturate abuse | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Diazepam, disease=barbiturate abuse | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Diazepam, disease=hallucinogen abuse | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Diazepam, disease=hallucinogen abuse | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Diazepam, disease=hallucinogen abuse | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Diazepam, disease=antidepressant type abuse | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Diazepam, disease=antidepressant type abuse | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Diazepam, disease=antidepressant type abuse | success | 5 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Diazepam, disease=specific developmental disorder | success | 1 |  |
| 25 | ictrp | 2026-03-09 | drug=Diazepam, disease=specific developmental disorder | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Diazepam, disease=specific developmental disorder | success | 5 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Diazepam, disease=attention deficit-hyperactivity disorder | success | 1 |  |
| 28 | ictrp | 2026-03-09 | drug=Diazepam, disease=attention deficit-hyperactivity disorder | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Diazepam, disease=attention deficit-hyperactivity disorder | success | 18 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Diazepam, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Diazepam, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Diazepam, disease=obsolete neurogenic bladder (disease) | success | 0 |  |