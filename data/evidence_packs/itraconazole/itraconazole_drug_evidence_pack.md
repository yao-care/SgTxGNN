# Itraconazole 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Itraconazole | |
| DrugBank ID | DB01167 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | pneumocystosis | 99.34% | L4 | 0 | 20 | S1 | Hold |
| 2 | Cryptococcal meningitis | 93.74% | L2 | 3 | 19 | S2 | Proceed with Guardrails |
| 3 | trichosporonosis | 89.01% | L3 | 0 | 20 | S1 | Research Question |
| 4 | hyalohyphomycosis | 89.01% | L3 | 0 | 20 | S1 | Research Question |
| 5 | penicilliosis | 89.01% | L2 | 3 | 20 | S2 | Proceed with Guardrails |
| 6 | geotrichosis | 89.01% | L3 | 0 | 9 | S1 | Research Question |
| 7 | maple bark strippers' lung | 88.83% | L5 | 0 | 0 | S0 | Hold |
| 8 | leprosy | 87.50% | L5 | 0 | 20 | S0 | Hold |
| 9 | congenital candidiasis | 85.04% | L4 | 0 | 2 | S1 | Hold |
| 10 | candida glabrata | 85.04% | L3 | 0 | 20 | S1 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Itraconazole | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Itraconazole | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Itraconazole, disease=pneumocystosis | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Itraconazole, disease=pneumocystosis | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Itraconazole, disease=pneumocystosis | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Itraconazole, disease=Cryptococcal meningitis | success | 3 |  |
| 7 | ictrp | 2026-03-10 | drug=Itraconazole, disease=Cryptococcal meningitis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Itraconazole, disease=Cryptococcal meningitis | success | 19 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Itraconazole, disease=trichosporonosis | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Itraconazole, disease=trichosporonosis | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Itraconazole, disease=trichosporonosis | success | 20 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Itraconazole, disease=hyalohyphomycosis | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Itraconazole, disease=hyalohyphomycosis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Itraconazole, disease=hyalohyphomycosis | success | 20 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Itraconazole, disease=penicilliosis | success | 3 |  |
| 16 | ictrp | 2026-03-10 | drug=Itraconazole, disease=penicilliosis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Itraconazole, disease=penicilliosis | success | 20 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Itraconazole, disease=geotrichosis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Itraconazole, disease=geotrichosis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Itraconazole, disease=geotrichosis | success | 9 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Itraconazole, disease=maple bark strippers' lung | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Itraconazole, disease=maple bark strippers' lung | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Itraconazole, disease=maple bark strippers' lung | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Itraconazole, disease=leprosy | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Itraconazole, disease=leprosy | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Itraconazole, disease=leprosy | success | 20 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Itraconazole, disease=congenital candidiasis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Itraconazole, disease=congenital candidiasis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Itraconazole, disease=congenital candidiasis | success | 2 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Itraconazole, disease=candida glabrata | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Itraconazole, disease=candida glabrata | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Itraconazole, disease=candida glabrata | success | 20 |  |