# Amitriptyline 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Amitriptyline | |
| DrugBank ID | DB00321 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | benign paroxysmal torticollis of infancy | 97.72% | L5 | 0 | 0 | S0 | Hold |
| 2 | endogenous depression | 97.71% | L2 | 0 | 20 | S2 | Proceed with Guardrails |
| 3 | agoraphobia | 97.27% | L4 | 0 | 6 | S1 | Research Question |
| 4 | major depressive disorder | 96.85% | L1 | 19 | 20 | S3 | Proceed with Guardrails |
| 5 | Ohdo syndrome and variants | 95.95% | L5 | 0 | 0 | S0 | Hold |
| 6 | melancholia | 95.52% | L2 | 0 | 20 | S2 | Proceed with Guardrails |
| 7 | neurotic depression | 95.48% | L2 | 0 | 20 | S2 | Proceed with Guardrails |
| 8 | phobic disorder | 94.68% | L4 | 0 | 20 | S1 | Research Question |
| 9 | unipolar depression | 94.61% | L1 | 8 | 20 | S3 | Proceed with Guardrails |
| 10 | blepharophimosis - intellectual disability syndrome, Ohdo type | 94.47% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Amitriptyline | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Amitriptyline | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Amitriptyline, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Amitriptyline, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Amitriptyline, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Amitriptyline, disease=endogenous depression | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Amitriptyline, disease=endogenous depression | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Amitriptyline, disease=endogenous depression | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Amitriptyline, disease=agoraphobia | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Amitriptyline, disease=agoraphobia | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Amitriptyline, disease=agoraphobia | success | 6 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Amitriptyline, disease=major depressive disorder | success | 19 |  |
| 13 | ictrp | 2026-03-10 | drug=Amitriptyline, disease=major depressive disorder | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Amitriptyline, disease=major depressive disorder | success | 20 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Amitriptyline, disease=Ohdo syndrome and variants | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Amitriptyline, disease=Ohdo syndrome and variants | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Amitriptyline, disease=Ohdo syndrome and variants | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Amitriptyline, disease=melancholia | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Amitriptyline, disease=melancholia | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Amitriptyline, disease=melancholia | success | 20 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Amitriptyline, disease=neurotic depression | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Amitriptyline, disease=neurotic depression | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Amitriptyline, disease=neurotic depression | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Amitriptyline, disease=phobic disorder | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Amitriptyline, disease=phobic disorder | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Amitriptyline, disease=phobic disorder | success | 20 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Amitriptyline, disease=unipolar depression | success | 8 |  |
| 28 | ictrp | 2026-03-10 | drug=Amitriptyline, disease=unipolar depression | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Amitriptyline, disease=unipolar depression | success | 20 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Amitriptyline, disease=blepharophimosis - intellectual disability syndrome, Ohdo type | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Amitriptyline, disease=blepharophimosis - intellectual disability syndrome, Ohdo type | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Amitriptyline, disease=blepharophimosis - intellectual disability syndrome, Ohdo type | success | 0 |  |