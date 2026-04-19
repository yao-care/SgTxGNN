# Amiodarone 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Amiodarone | |
| DrugBank ID | DB01118 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | catecholaminergic polymorphic ventricular tachycardia | 99.78% | L4 | 0 | 10 | S1 | Research Question |
| 2 | incessant infant ventricular tachycardia | 99.65% | L3 | 0 | 20 | S2 | Research Question |
| 3 | ventricular tachycardia | 99.64% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 4 | obsolete bundle branch block | 99.58% | L5 | 0 | 0 | S0 | Hold |
| 5 | rheumatoid arthritis | 99.40% | L5 | 0 | 18 | S0 | Hold |
| 6 | brachydactyly-syndactyly syndrome | 99.38% | L5 | 0 | 0 | S0 | Hold |
| 7 | heparin cofactor 2 deficiency | 99.36% | L5 | 0 | 0 | S0 | Hold |
| 8 | trichotillomania | 99.30% | L5 | 0 | 0 | S0 | Hold |
| 9 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.26% | L5 | 0 | 0 | S0 | Hold |
| 10 | gout | 99.19% | L5 | 0 | 9 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Amiodarone | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Amiodarone | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Amiodarone, disease=catecholaminergic polymorphic ventricular tachycardia | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Amiodarone, disease=catecholaminergic polymorphic ventricular tachycardia | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Amiodarone, disease=catecholaminergic polymorphic ventricular tachycardia | success | 10 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Amiodarone, disease=incessant infant ventricular tachycardia | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Amiodarone, disease=incessant infant ventricular tachycardia | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Amiodarone, disease=incessant infant ventricular tachycardia | success | 20 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Amiodarone, disease=ventricular tachycardia | success | 50 |  |
| 10 | ictrp | 2026-03-09 | drug=Amiodarone, disease=ventricular tachycardia | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Amiodarone, disease=ventricular tachycardia | success | 20 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Amiodarone, disease=obsolete bundle branch block | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Amiodarone, disease=obsolete bundle branch block | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Amiodarone, disease=obsolete bundle branch block | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Amiodarone, disease=rheumatoid arthritis | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Amiodarone, disease=rheumatoid arthritis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Amiodarone, disease=rheumatoid arthritis | success | 18 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Amiodarone, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Amiodarone, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Amiodarone, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Amiodarone, disease=heparin cofactor 2 deficiency | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Amiodarone, disease=heparin cofactor 2 deficiency | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Amiodarone, disease=heparin cofactor 2 deficiency | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Amiodarone, disease=trichotillomania | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Amiodarone, disease=trichotillomania | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Amiodarone, disease=trichotillomania | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Amiodarone, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Amiodarone, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Amiodarone, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Amiodarone, disease=gout | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Amiodarone, disease=gout | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Amiodarone, disease=gout | success | 9 |  |