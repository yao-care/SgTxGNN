# Cinnarizine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Cinnarizine | |
| DrugBank ID | DB00568 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | migraine disorder | 97.69% | L2 | 0 | 20 | S3 | Proceed with Guardrails |
| 2 | migraine with brainstem aura | 97.27% | L3 | 0 | 4 | S2 | Research Question |
| 3 | nephrogenic syndrome of inappropriate antidiuresis | 96.87% | L5 | 0 | 0 | S0 | Hold |
| 4 | headache disorder | 95.99% | L2 | 0 | 20 | S2 | Research Question |
| 5 | trigeminal autonomic cephalalgia | 95.48% | L5 | 0 | 0 | S0 | Hold |
| 6 | migraine with or without aura, susceptibility to | 94.07% | L3 | 0 | 20 | S1 | Research Question |
| 7 | common cold | 93.39% | L5 | 0 | 1 | S0 | Hold |
| 8 | atrophoderma vermiculata | 93.29% | L5 | 0 | 0 | S0 | Hold |
| 9 | pulmonary hypertension | 92.16% | L4 | 0 | 3 | S0 | Hold |
| 10 | ulerythema ophryogenesis | 92.11% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Cinnarizine | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Cinnarizine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Cinnarizine, disease=migraine disorder | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Cinnarizine, disease=migraine disorder | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Cinnarizine, disease=migraine disorder | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Cinnarizine, disease=migraine with brainstem aura | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Cinnarizine, disease=migraine with brainstem aura | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Cinnarizine, disease=migraine with brainstem aura | success | 4 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Cinnarizine, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Cinnarizine, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Cinnarizine, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Cinnarizine, disease=headache disorder | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Cinnarizine, disease=headache disorder | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Cinnarizine, disease=headache disorder | success | 20 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Cinnarizine, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Cinnarizine, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Cinnarizine, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Cinnarizine, disease=migraine with or without aura, susceptibility to | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Cinnarizine, disease=migraine with or without aura, susceptibility to | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Cinnarizine, disease=migraine with or without aura, susceptibility to | success | 20 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Cinnarizine, disease=common cold | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Cinnarizine, disease=common cold | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Cinnarizine, disease=common cold | success | 1 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Cinnarizine, disease=atrophoderma vermiculata | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Cinnarizine, disease=atrophoderma vermiculata | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Cinnarizine, disease=atrophoderma vermiculata | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Cinnarizine, disease=pulmonary hypertension | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Cinnarizine, disease=pulmonary hypertension | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Cinnarizine, disease=pulmonary hypertension | success | 3 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Cinnarizine, disease=ulerythema ophryogenesis | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Cinnarizine, disease=ulerythema ophryogenesis | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Cinnarizine, disease=ulerythema ophryogenesis | success | 0 |  |