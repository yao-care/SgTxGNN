# Dexlansoprazole 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Dexlansoprazole | |
| DrugBank ID | DB05351 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | active peptic ulcer disease | 100.00% | L1 | 18 | 3 | S3 | Proceed with Guardrails |
| 2 | gastrojejunal ulcer | 100.00% | L3 | 1 | 18 | S2 | Research Question |
| 3 | peptic ulcer perforation | 100.00% | L4 | 2 | 0 | S1 | Hold |
| 4 | gastric ulcer (disease) | 99.99% | L1 | 50 | 4 | S3 | Proceed with Guardrails |
| 5 | gastroduodenitis | 99.98% | L5 | 0 | 0 | S0 | Hold |
| 6 | duodenal obstruction | 99.85% | L5 | 4 | 0 | S0 | Hold |
| 7 | duodenogastric reflux | 99.81% | L5 | 0 | 0 | S0 | Hold |
| 8 | duodenal ulcer (disease) | 99.79% | L1 | 50 | 2 | S3 | Proceed with Guardrails |
| 9 | achlorhydria | 99.47% | L5 | 0 | 0 | S0 | Hold |
| 10 | leather-bottle stomach | 99.36% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Dexlansoprazole | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Dexlansoprazole | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Dexlansoprazole, disease=active peptic ulcer disease | success | 18 |  |
| 4 | ictrp | 2026-03-09 | drug=Dexlansoprazole, disease=active peptic ulcer disease | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Dexlansoprazole, disease=active peptic ulcer disease | success | 3 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Dexlansoprazole, disease=gastrojejunal ulcer | success | 1 |  |
| 7 | ictrp | 2026-03-09 | drug=Dexlansoprazole, disease=gastrojejunal ulcer | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Dexlansoprazole, disease=gastrojejunal ulcer | success | 18 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Dexlansoprazole, disease=peptic ulcer perforation | success | 2 |  |
| 10 | ictrp | 2026-03-09 | drug=Dexlansoprazole, disease=peptic ulcer perforation | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Dexlansoprazole, disease=peptic ulcer perforation | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Dexlansoprazole, disease=gastric ulcer (disease) | success | 50 |  |
| 13 | ictrp | 2026-03-09 | drug=Dexlansoprazole, disease=gastric ulcer (disease) | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Dexlansoprazole, disease=gastric ulcer (disease) | success | 4 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Dexlansoprazole, disease=gastroduodenitis | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Dexlansoprazole, disease=gastroduodenitis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Dexlansoprazole, disease=gastroduodenitis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Dexlansoprazole, disease=duodenal obstruction | success | 4 |  |
| 19 | ictrp | 2026-03-09 | drug=Dexlansoprazole, disease=duodenal obstruction | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Dexlansoprazole, disease=duodenal obstruction | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Dexlansoprazole, disease=duodenogastric reflux | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Dexlansoprazole, disease=duodenogastric reflux | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Dexlansoprazole, disease=duodenogastric reflux | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Dexlansoprazole, disease=duodenal ulcer (disease) | success | 50 |  |
| 25 | ictrp | 2026-03-09 | drug=Dexlansoprazole, disease=duodenal ulcer (disease) | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Dexlansoprazole, disease=duodenal ulcer (disease) | success | 2 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Dexlansoprazole, disease=achlorhydria | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Dexlansoprazole, disease=achlorhydria | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Dexlansoprazole, disease=achlorhydria | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Dexlansoprazole, disease=leather-bottle stomach | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Dexlansoprazole, disease=leather-bottle stomach | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Dexlansoprazole, disease=leather-bottle stomach | success | 0 |  |