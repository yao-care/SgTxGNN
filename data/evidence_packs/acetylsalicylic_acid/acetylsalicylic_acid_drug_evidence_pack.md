# Acetylsalicylic acid 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Acetylsalicylic acid | |
| DrugBank ID | DB00945 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | migraine with brainstem aura | 99.94% | L3 | 0 | 19 | S2 | Research Question |
| 2 | atrophoderma vermiculata | 99.59% | L5 | 0 | 0 | S0 | Hold |
| 3 | ulerythema ophryogenesis | 99.45% | L5 | 0 | 0 | S0 | Hold |
| 4 | heparin cofactor 2 deficiency | 99.41% | L4 | 0 | 3 | S0 | Hold |
| 5 | factor 5 excess with spontaneous thrombosis | 99.40% | L5 | 0 | 0 | S0 | Hold |
| 6 | antithrombin deficiency type 2 | 99.40% | L5 | 0 | 0 | S0 | Hold |
| 7 | trigeminal autonomic cephalalgia | 99.40% | L4 | 1 | 11 | S1 | Hold |
| 8 | thrombotic disease | 99.14% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 9 | thrombophilia | 99.04% | L2 | 25 | 20 | S3 | Proceed with Guardrails |
| 10 | Raynaud disease | 98.67% | L2 | 3 | 20 | S2 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Acetylsalicylic acid | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Acetylsalicylic acid | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Acetylsalicylic acid, disease=migraine with brainstem aura | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Acetylsalicylic acid, disease=migraine with brainstem aura | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Acetylsalicylic acid, disease=migraine with brainstem aura | success | 19 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Acetylsalicylic acid, disease=atrophoderma vermiculata | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Acetylsalicylic acid, disease=atrophoderma vermiculata | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Acetylsalicylic acid, disease=atrophoderma vermiculata | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Acetylsalicylic acid, disease=ulerythema ophryogenesis | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Acetylsalicylic acid, disease=ulerythema ophryogenesis | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Acetylsalicylic acid, disease=ulerythema ophryogenesis | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Acetylsalicylic acid, disease=heparin cofactor 2 deficiency | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Acetylsalicylic acid, disease=heparin cofactor 2 deficiency | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Acetylsalicylic acid, disease=heparin cofactor 2 deficiency | success | 3 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Acetylsalicylic acid, disease=factor 5 excess with spontaneous thrombosis | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Acetylsalicylic acid, disease=factor 5 excess with spontaneous thrombosis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Acetylsalicylic acid, disease=factor 5 excess with spontaneous thrombosis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Acetylsalicylic acid, disease=antithrombin deficiency type 2 | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Acetylsalicylic acid, disease=antithrombin deficiency type 2 | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Acetylsalicylic acid, disease=antithrombin deficiency type 2 | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Acetylsalicylic acid, disease=trigeminal autonomic cephalalgia | success | 1 |  |
| 22 | ictrp | 2026-03-09 | drug=Acetylsalicylic acid, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Acetylsalicylic acid, disease=trigeminal autonomic cephalalgia | success | 11 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Acetylsalicylic acid, disease=thrombotic disease | success | 50 |  |
| 25 | ictrp | 2026-03-09 | drug=Acetylsalicylic acid, disease=thrombotic disease | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Acetylsalicylic acid, disease=thrombotic disease | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Acetylsalicylic acid, disease=thrombophilia | success | 25 |  |
| 28 | ictrp | 2026-03-09 | drug=Acetylsalicylic acid, disease=thrombophilia | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Acetylsalicylic acid, disease=thrombophilia | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Acetylsalicylic acid, disease=Raynaud disease | success | 3 |  |
| 31 | ictrp | 2026-03-09 | drug=Acetylsalicylic acid, disease=Raynaud disease | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Acetylsalicylic acid, disease=Raynaud disease | success | 20 |  |