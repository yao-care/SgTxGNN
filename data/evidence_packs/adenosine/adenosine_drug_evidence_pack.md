# Adenosine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Adenosine | |
| DrugBank ID | DB00640 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | obsolete bundle branch block | 99.94% | L5 | 0 | 0 | S0 | Hold |
| 2 | catecholaminergic polymorphic ventricular tachycardia | 99.42% | L3 | 1 | 13 | S1 | Research Question |
| 3 | periodic paralysis with transient compartment-like syndrome | 98.98% | L5 | 0 | 0 | S0 | Hold |
| 4 | incessant infant ventricular tachycardia | 98.70% | L4 | 0 | 3 | S0 | Hold |
| 5 | arrhythmogenic right ventricular cardiomyopathy | 98.35% | L4 | 0 | 16 | S0 | Hold |
| 6 | primary hereditary glaucoma | 96.46% | L5 | 0 | 0 | S0 | Hold |
| 7 | attention deficit hyperactivity disorder, inattentive type | 95.73% | L5 | 0 | 0 | S0 | Hold |
| 8 | open-angle glaucoma | 95.12% | L2 | 5 | 20 | S2 | Proceed with Guardrails |
| 9 | specific developmental disorder | 94.54% | L5 | 41 | 19 | S0 | Hold |
| 10 | angle-closure glaucoma | 92.19% | L4 | 0 | 8 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Adenosine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Adenosine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Adenosine, disease=obsolete bundle branch block | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Adenosine, disease=obsolete bundle branch block | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Adenosine, disease=obsolete bundle branch block | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Adenosine, disease=catecholaminergic polymorphic ventricular tachycardia | success | 1 |  |
| 7 | ictrp | 2026-03-09 | drug=Adenosine, disease=catecholaminergic polymorphic ventricular tachycardia | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Adenosine, disease=catecholaminergic polymorphic ventricular tachycardia | success | 13 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Adenosine, disease=periodic paralysis with transient compartment-like syndrome | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Adenosine, disease=periodic paralysis with transient compartment-like syndrome | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Adenosine, disease=periodic paralysis with transient compartment-like syndrome | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Adenosine, disease=incessant infant ventricular tachycardia | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Adenosine, disease=incessant infant ventricular tachycardia | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Adenosine, disease=incessant infant ventricular tachycardia | success | 3 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Adenosine, disease=arrhythmogenic right ventricular cardiomyopathy | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Adenosine, disease=arrhythmogenic right ventricular cardiomyopathy | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Adenosine, disease=arrhythmogenic right ventricular cardiomyopathy | success | 16 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Adenosine, disease=primary hereditary glaucoma | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Adenosine, disease=primary hereditary glaucoma | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Adenosine, disease=primary hereditary glaucoma | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Adenosine, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Adenosine, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Adenosine, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Adenosine, disease=open-angle glaucoma | success | 5 |  |
| 25 | ictrp | 2026-03-09 | drug=Adenosine, disease=open-angle glaucoma | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Adenosine, disease=open-angle glaucoma | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Adenosine, disease=specific developmental disorder | success | 41 |  |
| 28 | ictrp | 2026-03-09 | drug=Adenosine, disease=specific developmental disorder | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Adenosine, disease=specific developmental disorder | success | 19 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Adenosine, disease=angle-closure glaucoma | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Adenosine, disease=angle-closure glaucoma | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Adenosine, disease=angle-closure glaucoma | success | 8 |  |