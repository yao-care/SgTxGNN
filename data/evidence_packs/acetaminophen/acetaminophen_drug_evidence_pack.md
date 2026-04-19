# Acetaminophen 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Acetaminophen | |
| DrugBank ID | DB00316 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | migraine with brainstem aura | 99.15% | L3 | 0 | 20 | S2 | Research Question |
| 2 | trigeminal autonomic cephalalgia | 98.58% | L4 | 2 | 17 | S1 | Hold |
| 3 | atrophoderma vermiculata | 94.71% | L5 | 0 | 0 | S0 | Hold |
| 4 | tendinitis | 94.58% | L2 | 7 | 20 | S3 | Proceed with Guardrails |
| 5 | myositis fibrosa | 94.36% | L5 | 0 | 0 | S0 | Hold |
| 6 | idiopathic granulomatous myositis | 94.36% | L5 | 0 | 0 | S0 | Hold |
| 7 | ulerythema ophryogenesis | 92.44% | L5 | 0 | 0 | S0 | Hold |
| 8 | fibromyalgia | 90.84% | L2 | 38 | 16 | S2 | Research Question |
| 9 | inclusion body myositis | 89.17% | L5 | 0 | 0 | S0 | Hold |
| 10 | sciatic neuropathy | 86.63% | L2 | 10 | 20 | S3 | Proceed with Guardrails |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Acetaminophen | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Acetaminophen | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Acetaminophen, disease=migraine with brainstem aura | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Acetaminophen, disease=migraine with brainstem aura | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Acetaminophen, disease=migraine with brainstem aura | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Acetaminophen, disease=trigeminal autonomic cephalalgia | success | 2 |  |
| 7 | ictrp | 2026-03-10 | drug=Acetaminophen, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Acetaminophen, disease=trigeminal autonomic cephalalgia | success | 17 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Acetaminophen, disease=atrophoderma vermiculata | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Acetaminophen, disease=atrophoderma vermiculata | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Acetaminophen, disease=atrophoderma vermiculata | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Acetaminophen, disease=tendinitis | success | 7 |  |
| 13 | ictrp | 2026-03-10 | drug=Acetaminophen, disease=tendinitis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Acetaminophen, disease=tendinitis | success | 20 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Acetaminophen, disease=myositis fibrosa | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Acetaminophen, disease=myositis fibrosa | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Acetaminophen, disease=myositis fibrosa | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Acetaminophen, disease=idiopathic granulomatous myositis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Acetaminophen, disease=idiopathic granulomatous myositis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Acetaminophen, disease=idiopathic granulomatous myositis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Acetaminophen, disease=ulerythema ophryogenesis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Acetaminophen, disease=ulerythema ophryogenesis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Acetaminophen, disease=ulerythema ophryogenesis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Acetaminophen, disease=fibromyalgia | success | 38 |  |
| 25 | ictrp | 2026-03-10 | drug=Acetaminophen, disease=fibromyalgia | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Acetaminophen, disease=fibromyalgia | success | 16 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Acetaminophen, disease=inclusion body myositis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Acetaminophen, disease=inclusion body myositis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Acetaminophen, disease=inclusion body myositis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Acetaminophen, disease=sciatic neuropathy | success | 10 |  |
| 31 | ictrp | 2026-03-10 | drug=Acetaminophen, disease=sciatic neuropathy | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Acetaminophen, disease=sciatic neuropathy | success | 20 |  |