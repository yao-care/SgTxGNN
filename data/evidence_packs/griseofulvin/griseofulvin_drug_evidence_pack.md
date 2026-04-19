# Griseofulvin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Griseofulvin | |
| DrugBank ID | DB00400 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | myiasis | 99.41% | L5 | 0 | 1 | S0 | Hold |
| 2 | creeping myiasis | 99.34% | L5 | 0 | 0 | S0 | Hold |
| 3 | wound myiasis | 99.34% | L5 | 0 | 0 | S0 | Hold |
| 4 | furuncular myiasis | 99.34% | L5 | 0 | 0 | S0 | Hold |
| 5 | echinococcus granulosus infectious disease | 99.32% | L5 | 0 | 0 | S0 | Hold |
| 6 | cutaneous candidiasis | 98.71% | L4 | 0 | 20 | S0 | Hold |
| 7 | toxoplasmosis | 98.69% | L5 | 0 | 0 | S0 | Hold |
| 8 | alveolar echinococcosis | 98.36% | L5 | 0 | 0 | S0 | Hold |
| 9 | blastomycosis | 97.08% | L4 | 0 | 6 | S0 | Hold |
| 10 | Bacteroidaceae infectious disease | 95.57% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Griseofulvin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Griseofulvin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Griseofulvin, disease=myiasis | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Griseofulvin, disease=myiasis | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Griseofulvin, disease=myiasis | success | 1 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Griseofulvin, disease=creeping myiasis | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Griseofulvin, disease=creeping myiasis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Griseofulvin, disease=creeping myiasis | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Griseofulvin, disease=wound myiasis | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Griseofulvin, disease=wound myiasis | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Griseofulvin, disease=wound myiasis | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Griseofulvin, disease=furuncular myiasis | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Griseofulvin, disease=furuncular myiasis | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Griseofulvin, disease=furuncular myiasis | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Griseofulvin, disease=echinococcus granulosus infectious disease | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Griseofulvin, disease=echinococcus granulosus infectious disease | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Griseofulvin, disease=echinococcus granulosus infectious disease | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Griseofulvin, disease=cutaneous candidiasis | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Griseofulvin, disease=cutaneous candidiasis | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Griseofulvin, disease=cutaneous candidiasis | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Griseofulvin, disease=toxoplasmosis | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Griseofulvin, disease=toxoplasmosis | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Griseofulvin, disease=toxoplasmosis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Griseofulvin, disease=alveolar echinococcosis | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Griseofulvin, disease=alveolar echinococcosis | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Griseofulvin, disease=alveolar echinococcosis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Griseofulvin, disease=blastomycosis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Griseofulvin, disease=blastomycosis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Griseofulvin, disease=blastomycosis | success | 6 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Griseofulvin, disease=Bacteroidaceae infectious disease | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Griseofulvin, disease=Bacteroidaceae infectious disease | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Griseofulvin, disease=Bacteroidaceae infectious disease | success | 0 |  |