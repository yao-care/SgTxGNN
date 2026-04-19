# Cimetidine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Cimetidine | |
| DrugBank ID | DB00501 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | Smouldering systemic mastocytosis | 99.80% | L5 | 0 | 0 | S0 | Research Question |
| 2 | active peptic ulcer disease | 99.79% | L1 | 1 | 18 | S3 | Proceed with Guardrails |
| 3 | peptic ulcer perforation | 99.77% | L4 | 0 | 20 | S1 | Hold |
| 4 | gastrojejunal ulcer | 99.77% | L3 | 0 | 20 | S1 | Research Question |
| 5 | lymphoadenopathic mastocytosis with eosinophilia | 99.76% | L5 | 0 | 0 | S0 | Research Question |
| 6 | duodenogastric reflux | 99.49% | L3 | 0 | 8 | S1 | Research Question |
| 7 | duodenal obstruction | 99.44% | L4 | 0 | 11 | S1 | Hold |
| 8 | acne (disease) | 99.33% | L4 | 0 | 3 | S1 | Research Question |
| 9 | abnormality of glucagon secretion | 99.14% | L5 | 0 | 1 | S0 | Hold |
| 10 | gastroduodenitis | 98.89% | L2 | 0 | 20 | S2 | Proceed with Guardrails |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Cimetidine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Cimetidine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Cimetidine, disease=Smouldering systemic mastocytosis | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Cimetidine, disease=Smouldering systemic mastocytosis | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Cimetidine, disease=Smouldering systemic mastocytosis | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Cimetidine, disease=active peptic ulcer disease | success | 1 |  |
| 7 | ictrp | 2026-03-09 | drug=Cimetidine, disease=active peptic ulcer disease | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Cimetidine, disease=active peptic ulcer disease | success | 18 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Cimetidine, disease=peptic ulcer perforation | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Cimetidine, disease=peptic ulcer perforation | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Cimetidine, disease=peptic ulcer perforation | success | 20 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Cimetidine, disease=gastrojejunal ulcer | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Cimetidine, disease=gastrojejunal ulcer | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Cimetidine, disease=gastrojejunal ulcer | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Cimetidine, disease=lymphoadenopathic mastocytosis with eosinophilia | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Cimetidine, disease=lymphoadenopathic mastocytosis with eosinophilia | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Cimetidine, disease=lymphoadenopathic mastocytosis with eosinophilia | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Cimetidine, disease=duodenogastric reflux | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Cimetidine, disease=duodenogastric reflux | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Cimetidine, disease=duodenogastric reflux | success | 8 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Cimetidine, disease=duodenal obstruction | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Cimetidine, disease=duodenal obstruction | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Cimetidine, disease=duodenal obstruction | success | 11 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Cimetidine, disease=acne (disease) | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Cimetidine, disease=acne (disease) | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Cimetidine, disease=acne (disease) | success | 3 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Cimetidine, disease=abnormality of glucagon secretion | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Cimetidine, disease=abnormality of glucagon secretion | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Cimetidine, disease=abnormality of glucagon secretion | success | 1 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Cimetidine, disease=gastroduodenitis | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Cimetidine, disease=gastroduodenitis | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Cimetidine, disease=gastroduodenitis | success | 20 |  |