# Clonazepam 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Clonazepam | |
| DrugBank ID | DB01068 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | restless legs syndrome | 99.65% | L3 | 0 | 20 | S2 | Proceed with Guardrails |
| 2 | insomnia (disease) | 99.32% | L3 | 12 | 18 | S2 | Proceed with Guardrails |
| 3 | trigeminal nerve neoplasm | 99.30% | L5 | 0 | 2 | S0 | Hold |
| 4 | sleep disorder, initiating and maintaining sleep | 98.75% | L3 | 0 | 20 | S2 | Proceed with Guardrails |
| 5 | acute encephalopathy with biphasic seizures and late reduced diffusion | 98.60% | L4 | 0 | 1 | S0 | Hold |
| 6 | trigeminal neuralgia | 97.66% | L3 | 0 | 20 | S2 | Research Question |
| 7 | status epilepticus | 96.97% | L1 | 6 | 18 | S3 | Proceed with Guardrails |
| 8 | adolescent/adult onset autosomal dominant epilepsy with auditory features | 96.82% | L5 | 0 | 0 | S0 | Hold |
| 9 | reading seizures | 96.57% | L4 | 0 | 20 | S1 | Research Question |
| 10 | epilepsy with generalized tonic-clonic seizures | 96.53% | L2 | 2 | 18 | S2 | Proceed with Guardrails |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Clonazepam | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Clonazepam | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Clonazepam, disease=restless legs syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Clonazepam, disease=restless legs syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Clonazepam, disease=restless legs syndrome | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Clonazepam, disease=insomnia (disease) | success | 12 |  |
| 7 | ictrp | 2026-03-10 | drug=Clonazepam, disease=insomnia (disease) | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Clonazepam, disease=insomnia (disease) | success | 18 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Clonazepam, disease=trigeminal nerve neoplasm | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Clonazepam, disease=trigeminal nerve neoplasm | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Clonazepam, disease=trigeminal nerve neoplasm | success | 2 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Clonazepam, disease=sleep disorder, initiating and maintaining sleep | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Clonazepam, disease=sleep disorder, initiating and maintaining sleep | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Clonazepam, disease=sleep disorder, initiating and maintaining sleep | success | 20 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Clonazepam, disease=acute encephalopathy with biphasic seizures and late reduced diffusion | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Clonazepam, disease=acute encephalopathy with biphasic seizures and late reduced diffusion | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Clonazepam, disease=acute encephalopathy with biphasic seizures and late reduced diffusion | success | 1 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Clonazepam, disease=trigeminal neuralgia | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Clonazepam, disease=trigeminal neuralgia | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Clonazepam, disease=trigeminal neuralgia | success | 20 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Clonazepam, disease=status epilepticus | success | 6 |  |
| 22 | ictrp | 2026-03-10 | drug=Clonazepam, disease=status epilepticus | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Clonazepam, disease=status epilepticus | success | 18 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Clonazepam, disease=adolescent/adult onset autosomal dominant epilepsy with auditory features | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Clonazepam, disease=adolescent/adult onset autosomal dominant epilepsy with auditory features | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Clonazepam, disease=adolescent/adult onset autosomal dominant epilepsy with auditory features | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Clonazepam, disease=reading seizures | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Clonazepam, disease=reading seizures | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Clonazepam, disease=reading seizures | success | 20 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Clonazepam, disease=epilepsy with generalized tonic-clonic seizures | success | 2 |  |
| 31 | ictrp | 2026-03-10 | drug=Clonazepam, disease=epilepsy with generalized tonic-clonic seizures | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Clonazepam, disease=epilepsy with generalized tonic-clonic seizures | success | 18 |  |