# Crisaborole 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Crisaborole | |
| DrugBank ID | DB05219 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | exanthem (disease) | 98.58% | L4 | 3 | 0 | S1 | Research Question |
| 2 | dermatitis | 96.64% | pending | 33 | 18 | pending | pending |
| 3 | acne keloid | 95.85% | L5 | 0 | 0 | S0 | Hold |
| 4 | neonatal dermatomyositis | 95.21% | L5 | 0 | 0 | S0 | Hold |
| 5 | acrodermatitis chronica atrophicans | 95.10% | L5 | 0 | 0 | S0 | Hold |
| 6 | bronchitis | 95.01% | L5 | 0 | 0 | S0 | Hold |
| 7 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 94.79% | L5 | 0 | 0 | S0 | Hold |
| 8 | hydroa vacciniforme, familial | 94.75% | L5 | 0 | 0 | S0 | Hold |
| 9 | amyopathic dermatomyositis | 94.49% | L5 | 0 | 0 | S0 | Research Question |
| 10 | pityriasis simplex | 87.80% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Crisaborole | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Crisaborole | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Crisaborole, disease=exanthem (disease) | success | 3 |  |
| 4 | ictrp | 2026-03-10 | drug=Crisaborole, disease=exanthem (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Crisaborole, disease=exanthem (disease) | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Crisaborole, disease=dermatitis | success | 33 |  |
| 7 | ictrp | 2026-03-10 | drug=Crisaborole, disease=dermatitis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Crisaborole, disease=dermatitis | success | 18 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Crisaborole, disease=acne keloid | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Crisaborole, disease=acne keloid | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Crisaborole, disease=acne keloid | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Crisaborole, disease=neonatal dermatomyositis | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Crisaborole, disease=neonatal dermatomyositis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Crisaborole, disease=neonatal dermatomyositis | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Crisaborole, disease=acrodermatitis chronica atrophicans | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Crisaborole, disease=acrodermatitis chronica atrophicans | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Crisaborole, disease=acrodermatitis chronica atrophicans | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Crisaborole, disease=bronchitis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Crisaborole, disease=bronchitis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Crisaborole, disease=bronchitis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Crisaborole, disease=secondary interstitial lung disease specific to childhood associated with a connective tissue disease | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Crisaborole, disease=secondary interstitial lung disease specific to childhood associated with a connective tissue disease | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Crisaborole, disease=secondary interstitial lung disease specific to childhood associated with a connective tissue disease | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Crisaborole, disease=hydroa vacciniforme, familial | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Crisaborole, disease=hydroa vacciniforme, familial | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Crisaborole, disease=hydroa vacciniforme, familial | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Crisaborole, disease=amyopathic dermatomyositis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Crisaborole, disease=amyopathic dermatomyositis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Crisaborole, disease=amyopathic dermatomyositis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Crisaborole, disease=pityriasis simplex | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Crisaborole, disease=pityriasis simplex | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Crisaborole, disease=pityriasis simplex | success | 0 |  |