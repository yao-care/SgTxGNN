# Baclofen 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Baclofen | |
| DrugBank ID | DB00181 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | attention deficit-hyperactivity disorder | 99.32% | L4 | 0 | 10 | S0 | Hold |
| 2 | nicotine dependence | 99.19% | L3 | 3 | 20 | S2 | Proceed with Guardrails |
| 3 | attention deficit hyperactivity disorder, inattentive type | 98.89% | L5 | 0 | 0 | S0 | Hold |
| 4 | myofascial pain syndrome | 98.87% | L3 | 2 | 4 | S1 | Research Question |
| 5 | faciodigitogenital syndrome | 98.78% | L5 | 0 | 0 | S0 | Hold |
| 6 | trigeminal nerve neoplasm | 98.70% | L4 | 0 | 2 | S0 | Hold |
| 7 | methemoglobinemia | 98.33% | L5 | 0 | 1 | S0 | Hold |
| 8 | chondromyxoid fibroma | 98.15% | L5 | 0 | 0 | S0 | Hold |
| 9 | methemoglobinemia, alpha type | 97.97% | L5 | 0 | 0 | S0 | Hold |
| 10 | specific developmental disorder | 97.95% | L4 | 2 | 2 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Baclofen | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Baclofen | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Baclofen, disease=attention deficit-hyperactivity disorder | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Baclofen, disease=attention deficit-hyperactivity disorder | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Baclofen, disease=attention deficit-hyperactivity disorder | success | 10 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Baclofen, disease=nicotine dependence | success | 3 |  |
| 7 | ictrp | 2026-03-10 | drug=Baclofen, disease=nicotine dependence | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Baclofen, disease=nicotine dependence | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Baclofen, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Baclofen, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Baclofen, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Baclofen, disease=myofascial pain syndrome | success | 2 |  |
| 13 | ictrp | 2026-03-10 | drug=Baclofen, disease=myofascial pain syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Baclofen, disease=myofascial pain syndrome | success | 4 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Baclofen, disease=faciodigitogenital syndrome | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Baclofen, disease=faciodigitogenital syndrome | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Baclofen, disease=faciodigitogenital syndrome | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Baclofen, disease=trigeminal nerve neoplasm | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Baclofen, disease=trigeminal nerve neoplasm | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Baclofen, disease=trigeminal nerve neoplasm | success | 2 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Baclofen, disease=methemoglobinemia | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Baclofen, disease=methemoglobinemia | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Baclofen, disease=methemoglobinemia | success | 1 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Baclofen, disease=chondromyxoid fibroma | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Baclofen, disease=chondromyxoid fibroma | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Baclofen, disease=chondromyxoid fibroma | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Baclofen, disease=methemoglobinemia, alpha type | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Baclofen, disease=methemoglobinemia, alpha type | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Baclofen, disease=methemoglobinemia, alpha type | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Baclofen, disease=specific developmental disorder | success | 2 |  |
| 31 | ictrp | 2026-03-10 | drug=Baclofen, disease=specific developmental disorder | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Baclofen, disease=specific developmental disorder | success | 2 |  |