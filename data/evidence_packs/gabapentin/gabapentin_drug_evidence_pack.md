# Gabapentin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Gabapentin | |
| DrugBank ID | DB00996 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | acne (disease) | 98.46% | L5 | 0 | 1 | S0 | Hold |
| 2 | adolescent/adult onset autosomal dominant epilepsy with auditory features | 95.94% | L5 | 0 | 0 | S0 | Hold |
| 3 | epilepsy with generalized tonic-clonic seizures | 94.56% | L2 | 2 | 19 | S2 | Proceed with Guardrails |
| 4 | myofascial pain syndrome | 92.97% | L2 | 18 | 11 | S2 | Proceed with Guardrails |
| 5 | visual epilepsy | 85.28% | L3 | 6 | 19 | S1 | Hold |
| 6 | active cochlear Meniere disease | 83.40% | L5 | 0 | 0 | S0 | Hold |
| 7 | active vestibular Meniere disease | 83.40% | L5 | 0 | 0 | S0 | Hold |
| 8 | active cochleovestibular Meniere disease | 83.40% | L5 | 0 | 0 | S0 | Hold |
| 9 | trigeminal nerve neoplasm | 82.92% | L4 | 0 | 5 | S1 | Research Question |
| 10 | osteoarthritis susceptibility | 82.91% | L5 | 0 | 1 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Gabapentin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Gabapentin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Gabapentin, disease=acne (disease) | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Gabapentin, disease=acne (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Gabapentin, disease=acne (disease) | success | 1 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Gabapentin, disease=adolescent/adult onset autosomal dominant epilepsy with auditory features | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Gabapentin, disease=adolescent/adult onset autosomal dominant epilepsy with auditory features | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Gabapentin, disease=adolescent/adult onset autosomal dominant epilepsy with auditory features | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Gabapentin, disease=epilepsy with generalized tonic-clonic seizures | success | 2 |  |
| 10 | ictrp | 2026-03-09 | drug=Gabapentin, disease=epilepsy with generalized tonic-clonic seizures | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Gabapentin, disease=epilepsy with generalized tonic-clonic seizures | success | 19 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Gabapentin, disease=myofascial pain syndrome | success | 18 |  |
| 13 | ictrp | 2026-03-09 | drug=Gabapentin, disease=myofascial pain syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Gabapentin, disease=myofascial pain syndrome | success | 11 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Gabapentin, disease=visual epilepsy | success | 6 |  |
| 16 | ictrp | 2026-03-09 | drug=Gabapentin, disease=visual epilepsy | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Gabapentin, disease=visual epilepsy | success | 19 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Gabapentin, disease=active cochlear Meniere disease | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Gabapentin, disease=active cochlear Meniere disease | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Gabapentin, disease=active cochlear Meniere disease | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Gabapentin, disease=active vestibular Meniere disease | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Gabapentin, disease=active vestibular Meniere disease | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Gabapentin, disease=active vestibular Meniere disease | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Gabapentin, disease=active cochleovestibular Meniere disease | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Gabapentin, disease=active cochleovestibular Meniere disease | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Gabapentin, disease=active cochleovestibular Meniere disease | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Gabapentin, disease=trigeminal nerve neoplasm | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Gabapentin, disease=trigeminal nerve neoplasm | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Gabapentin, disease=trigeminal nerve neoplasm | success | 5 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Gabapentin, disease=osteoarthritis susceptibility | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Gabapentin, disease=osteoarthritis susceptibility | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Gabapentin, disease=osteoarthritis susceptibility | success | 1 |  |