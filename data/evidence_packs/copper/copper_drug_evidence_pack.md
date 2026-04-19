# Copper 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Copper | |
| DrugBank ID | DB09130 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | esotropia | 96.25% | L5 | 0 | 0 | S0 | Hold |
| 2 | dermatitis | 95.06% | L4 | 6 | 20 | S1 | Research Question |
| 3 | acrodermatitis chronica atrophicans | 93.82% | L5 | 0 | 0 | S0 | Hold |
| 4 | hydroa vacciniforme, familial | 93.78% | L5 | 0 | 0 | S0 | Hold |
| 5 | neonatal dermatomyositis | 93.55% | L5 | 0 | 0 | S0 | Hold |
| 6 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 93.34% | L5 | 0 | 0 | S0 | Hold |
| 7 | acne keloid | 93.33% | L5 | 0 | 1 | S0 | Hold |
| 8 | dry eye syndrome | 93.28% | L4 | 1 | 13 | S1 | Research Question |
| 9 | amyopathic dermatomyositis | 93.15% | L5 | 0 | 0 | S0 | Hold |
| 10 | bone Paget disease | 92.91% | L5 | 0 | 3 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Copper | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Copper | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Copper, disease=esotropia | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Copper, disease=esotropia | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Copper, disease=esotropia | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Copper, disease=dermatitis | success | 6 |  |
| 7 | ictrp | 2026-03-10 | drug=Copper, disease=dermatitis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Copper, disease=dermatitis | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Copper, disease=acrodermatitis chronica atrophicans | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Copper, disease=acrodermatitis chronica atrophicans | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Copper, disease=acrodermatitis chronica atrophicans | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Copper, disease=hydroa vacciniforme, familial | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Copper, disease=hydroa vacciniforme, familial | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Copper, disease=hydroa vacciniforme, familial | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Copper, disease=neonatal dermatomyositis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Copper, disease=neonatal dermatomyositis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Copper, disease=neonatal dermatomyositis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Copper, disease=secondary interstitial lung disease specific to childhood associated with a connective tissue disease | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Copper, disease=secondary interstitial lung disease specific to childhood associated with a connective tissue disease | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Copper, disease=secondary interstitial lung disease specific to childhood associated with a connective tissue disease | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Copper, disease=acne keloid | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Copper, disease=acne keloid | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Copper, disease=acne keloid | success | 1 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Copper, disease=dry eye syndrome | success | 1 |  |
| 25 | ictrp | 2026-03-10 | drug=Copper, disease=dry eye syndrome | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Copper, disease=dry eye syndrome | success | 13 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Copper, disease=amyopathic dermatomyositis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Copper, disease=amyopathic dermatomyositis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Copper, disease=amyopathic dermatomyositis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Copper, disease=bone Paget disease | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Copper, disease=bone Paget disease | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Copper, disease=bone Paget disease | success | 3 |  |