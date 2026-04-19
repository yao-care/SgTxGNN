# Clobazam 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Clobazam | |
| DrugBank ID | DB00349 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | febrile infection-related epilepsy syndrome | 99.82% | L4 | 0 | 2 | S1 | Research Question |
| 2 | perioral myoclonia with absences | 99.79% | L5 | 0 | 0 | S0 | Hold |
| 3 | cryptogenic late-onset epileptic spasms | 99.77% | L5 | 0 | 0 | S0 | Hold |
| 4 | atypical childhood epilepsy with centrotemporal spikes | 99.77% | L3 | 0 | 3 | S1 | Research Question |
| 5 | photosensitive occipital lobe epilepsy | 99.77% | L4 | 0 | 1 | S0 | Hold |
| 6 | childhood onset epileptic encephalopathy | 99.59% | L1 | 0 | 20 | S3 | Proceed with Guardrails |
| 7 | benign occipital epilepsy | 99.58% | L2 | 0 | 20 | S2 | Proceed with Guardrails |
| 8 | early-onset epileptic encephalopathy and intellectual disability due to GRIN2A mutation | 99.40% | L5 | 0 | 0 | S0 | Hold |
| 9 | restless legs syndrome | 99.30% | L5 | 0 | 0 | S0 | Hold |
| 10 | polymicrogyria with optic nerve hypoplasia | 99.09% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Clobazam | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Clobazam | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Clobazam, disease=febrile infection-related epilepsy syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Clobazam, disease=febrile infection-related epilepsy syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Clobazam, disease=febrile infection-related epilepsy syndrome | success | 2 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Clobazam, disease=perioral myoclonia with absences | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Clobazam, disease=perioral myoclonia with absences | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Clobazam, disease=perioral myoclonia with absences | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Clobazam, disease=cryptogenic late-onset epileptic spasms | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Clobazam, disease=cryptogenic late-onset epileptic spasms | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Clobazam, disease=cryptogenic late-onset epileptic spasms | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Clobazam, disease=atypical childhood epilepsy with centrotemporal spikes | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Clobazam, disease=atypical childhood epilepsy with centrotemporal spikes | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Clobazam, disease=atypical childhood epilepsy with centrotemporal spikes | success | 3 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Clobazam, disease=photosensitive occipital lobe epilepsy | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Clobazam, disease=photosensitive occipital lobe epilepsy | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Clobazam, disease=photosensitive occipital lobe epilepsy | success | 1 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Clobazam, disease=childhood onset epileptic encephalopathy | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Clobazam, disease=childhood onset epileptic encephalopathy | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Clobazam, disease=childhood onset epileptic encephalopathy | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Clobazam, disease=benign occipital epilepsy | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Clobazam, disease=benign occipital epilepsy | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Clobazam, disease=benign occipital epilepsy | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Clobazam, disease=early-onset epileptic encephalopathy and intellectual disability due to GRIN2A mutation | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Clobazam, disease=early-onset epileptic encephalopathy and intellectual disability due to GRIN2A mutation | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Clobazam, disease=early-onset epileptic encephalopathy and intellectual disability due to GRIN2A mutation | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Clobazam, disease=restless legs syndrome | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Clobazam, disease=restless legs syndrome | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Clobazam, disease=restless legs syndrome | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Clobazam, disease=polymicrogyria with optic nerve hypoplasia | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Clobazam, disease=polymicrogyria with optic nerve hypoplasia | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Clobazam, disease=polymicrogyria with optic nerve hypoplasia | success | 0 |  |