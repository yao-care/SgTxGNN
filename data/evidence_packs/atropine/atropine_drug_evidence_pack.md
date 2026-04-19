# Atropine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Atropine | |
| DrugBank ID | DB00572 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | migraine disorder | 99.56% | L4 | 0 | 13 | S1 | Research Question |
| 2 | migraine with brainstem aura | 99.42% | L4 | 0 | 1 | S1 | Hold |
| 3 | migraine with or without aura, susceptibility to | 98.15% | L5 | 0 | 20 | S0 | Hold |
| 4 | atrophoderma vermiculata | 98.15% | L5 | 0 | 0 | S0 | Hold |
| 5 | open-angle glaucoma | 98.03% | L4 | 0 | 20 | S1 | Hold |
| 6 | primary hereditary glaucoma | 97.78% | L5 | 0 | 0 | S0 | Hold |
| 7 | ulerythema ophryogenesis | 97.76% | L5 | 0 | 0 | S0 | Hold |
| 8 | headache disorder | 97.24% | L2 | 16 | 19 | S2 | Proceed with Guardrails |
| 9 | trigeminal autonomic cephalalgia | 96.46% | L4 | 0 | 3 | S1 | Research Question |
| 10 | nephrogenic syndrome of inappropriate antidiuresis | 96.34% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Atropine | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Atropine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Atropine, disease=migraine disorder | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Atropine, disease=migraine disorder | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Atropine, disease=migraine disorder | success | 13 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Atropine, disease=migraine with brainstem aura | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Atropine, disease=migraine with brainstem aura | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Atropine, disease=migraine with brainstem aura | success | 1 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Atropine, disease=migraine with or without aura, susceptibility to | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Atropine, disease=migraine with or without aura, susceptibility to | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Atropine, disease=migraine with or without aura, susceptibility to | success | 20 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Atropine, disease=atrophoderma vermiculata | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Atropine, disease=atrophoderma vermiculata | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Atropine, disease=atrophoderma vermiculata | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Atropine, disease=open-angle glaucoma | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Atropine, disease=open-angle glaucoma | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Atropine, disease=open-angle glaucoma | success | 20 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Atropine, disease=primary hereditary glaucoma | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Atropine, disease=primary hereditary glaucoma | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Atropine, disease=primary hereditary glaucoma | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Atropine, disease=ulerythema ophryogenesis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Atropine, disease=ulerythema ophryogenesis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Atropine, disease=ulerythema ophryogenesis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Atropine, disease=headache disorder | success | 16 |  |
| 25 | ictrp | 2026-03-10 | drug=Atropine, disease=headache disorder | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Atropine, disease=headache disorder | success | 19 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Atropine, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Atropine, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Atropine, disease=trigeminal autonomic cephalalgia | success | 3 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Atropine, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Atropine, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Atropine, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |