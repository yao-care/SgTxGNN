# Alprostadil 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Alprostadil | |
| DrugBank ID | DB00770 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | aortic malformation | 99.98% | L3 | 2 | 20 | S2 | Proceed with Guardrails |
| 2 | congenital tricuspid stenosis | 99.94% | L3 | 0 | 4 | S1 | Research Question |
| 3 | congenital valvular dysplasia | 99.93% | L5 | 0 | 0 | S0 | Hold |
| 4 | straddling or overriding tricuspid valve | 99.93% | L5 | 0 | 20 | S0 | Hold |
| 5 | tricuspid valve agenesis | 99.93% | L4 | 0 | 3 | S1 | Research Question |
| 6 | tricuspid valve prolapse (disease) | 99.92% | L5 | 0 | 0 | S0 | Hold |
| 7 | anomaly of the tricuspid subvalvular apparatus | 99.92% | L5 | 0 | 0 | S0 | Hold |
| 8 | double outlet right ventricle with atrioventricular septal defect, pulmonary stenosis, heterotaxy | 99.91% | L5 | 0 | 0 | S0 | Hold |
| 9 | heart septal defect | 99.39% | L3 | 0 | 20 | S2 | Proceed with Guardrails |
| 10 | endemic goiter | 99.34% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Alprostadil | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Alprostadil | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Alprostadil, disease=aortic malformation | success | 2 |  |
| 4 | ictrp | 2026-03-09 | drug=Alprostadil, disease=aortic malformation | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Alprostadil, disease=aortic malformation | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Alprostadil, disease=congenital tricuspid stenosis | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Alprostadil, disease=congenital tricuspid stenosis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Alprostadil, disease=congenital tricuspid stenosis | success | 4 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Alprostadil, disease=congenital valvular dysplasia | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Alprostadil, disease=congenital valvular dysplasia | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Alprostadil, disease=congenital valvular dysplasia | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Alprostadil, disease=straddling or overriding tricuspid valve | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Alprostadil, disease=straddling or overriding tricuspid valve | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Alprostadil, disease=straddling or overriding tricuspid valve | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Alprostadil, disease=tricuspid valve agenesis | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Alprostadil, disease=tricuspid valve agenesis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Alprostadil, disease=tricuspid valve agenesis | success | 3 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Alprostadil, disease=tricuspid valve prolapse (disease) | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Alprostadil, disease=tricuspid valve prolapse (disease) | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Alprostadil, disease=tricuspid valve prolapse (disease) | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Alprostadil, disease=anomaly of the tricuspid subvalvular apparatus | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Alprostadil, disease=anomaly of the tricuspid subvalvular apparatus | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Alprostadil, disease=anomaly of the tricuspid subvalvular apparatus | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Alprostadil, disease=double outlet right ventricle with atrioventricular septal defect, pulmonary stenosis, heterotaxy | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Alprostadil, disease=double outlet right ventricle with atrioventricular septal defect, pulmonary stenosis, heterotaxy | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Alprostadil, disease=double outlet right ventricle with atrioventricular septal defect, pulmonary stenosis, heterotaxy | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Alprostadil, disease=heart septal defect | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Alprostadil, disease=heart septal defect | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Alprostadil, disease=heart septal defect | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Alprostadil, disease=endemic goiter | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Alprostadil, disease=endemic goiter | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Alprostadil, disease=endemic goiter | success | 0 |  |