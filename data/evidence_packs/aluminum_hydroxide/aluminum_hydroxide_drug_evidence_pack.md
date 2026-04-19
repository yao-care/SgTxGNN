# Aluminum hydroxide 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Aluminum hydroxide | |
| DrugBank ID | DB06723 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | active peptic ulcer disease | 99.64% | L2 | 0 | 20 | S3 | Proceed with Guardrails |
| 2 | gastroduodenitis | 99.59% | L3 | 0 | 20 | S2 | Proceed with Guardrails |
| 3 | peptic ulcer perforation | 99.54% | L5 | 1 | 0 | S0 | Hold |
| 4 | gastrojejunal ulcer | 99.54% | L2 | 0 | 20 | S2 | Proceed with Guardrails |
| 5 | hiatus hernia (disease) | 98.78% | L4 | 0 | 4 | S1 | Research Question |
| 6 | achlorhydria | 98.71% | L5 | 0 | 1 | S0 | Hold |
| 7 | pylorospasm | 98.59% | L5 | 0 | 0 | S0 | Hold |
| 8 | gastric dilatation | 98.59% | L5 | 1 | 0 | S0 | Hold |
| 9 | Dieulafoy lesion | 98.59% | L5 | 0 | 0 | S0 | Hold |
| 10 | cascade stomach | 98.59% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Aluminum hydroxide | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Aluminum hydroxide | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Aluminum hydroxide, disease=active peptic ulcer disease | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Aluminum hydroxide, disease=active peptic ulcer disease | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Aluminum hydroxide, disease=active peptic ulcer disease | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Aluminum hydroxide, disease=gastroduodenitis | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Aluminum hydroxide, disease=gastroduodenitis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Aluminum hydroxide, disease=gastroduodenitis | success | 20 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Aluminum hydroxide, disease=peptic ulcer perforation | success | 1 |  |
| 10 | ictrp | 2026-03-09 | drug=Aluminum hydroxide, disease=peptic ulcer perforation | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Aluminum hydroxide, disease=peptic ulcer perforation | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Aluminum hydroxide, disease=gastrojejunal ulcer | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Aluminum hydroxide, disease=gastrojejunal ulcer | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Aluminum hydroxide, disease=gastrojejunal ulcer | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Aluminum hydroxide, disease=hiatus hernia (disease) | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Aluminum hydroxide, disease=hiatus hernia (disease) | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Aluminum hydroxide, disease=hiatus hernia (disease) | success | 4 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Aluminum hydroxide, disease=achlorhydria | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Aluminum hydroxide, disease=achlorhydria | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Aluminum hydroxide, disease=achlorhydria | success | 1 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Aluminum hydroxide, disease=pylorospasm | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Aluminum hydroxide, disease=pylorospasm | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Aluminum hydroxide, disease=pylorospasm | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Aluminum hydroxide, disease=gastric dilatation | success | 1 |  |
| 25 | ictrp | 2026-03-09 | drug=Aluminum hydroxide, disease=gastric dilatation | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Aluminum hydroxide, disease=gastric dilatation | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Aluminum hydroxide, disease=Dieulafoy lesion | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Aluminum hydroxide, disease=Dieulafoy lesion | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Aluminum hydroxide, disease=Dieulafoy lesion | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Aluminum hydroxide, disease=cascade stomach | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Aluminum hydroxide, disease=cascade stomach | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Aluminum hydroxide, disease=cascade stomach | success | 0 |  |