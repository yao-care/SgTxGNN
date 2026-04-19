# Amantadine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Amantadine | |
| DrugBank ID | DB00915 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | Rasmussen subacute encephalitis | 99.48% | L5 | 0 | 0 | S0 | Hold |
| 2 | transaldolase deficiency | 99.27% | L5 | 0 | 0 | S0 | Hold |
| 3 | myelitis | 99.24% | L3 | 0 | 11 | S1 | Research Question |
| 4 | PLA2G6-associated neurodegeneration | 99.23% | L4 | 0 | 2 | S0 | Hold |
| 5 | fructose-1,6-bisphosphatase deficiency | 98.97% | L5 | 0 | 0 | S0 | Hold |
| 6 | paralysis agitans, juvenile, of Hunt | 97.86% | L4 | 0 | 0 | S0 | Hold |
| 7 | Lewy body dementia | 97.83% | L3 | 4 | 20 | S2 | Proceed with Guardrails |
| 8 | X-linked intellectual disability-ataxia-apraxia syndrome | 97.80% | L5 | 0 | 0 | S0 | Hold |
| 9 | progressive supranuclear palsy-corticobasal syndrome | 97.77% | L3 | 1 | 1 | S1 | Research Question |
| 10 | X-linked intellectual disability-cerebellar hypoplasia syndrome | 96.95% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Amantadine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Amantadine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Amantadine, disease=Rasmussen subacute encephalitis | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Amantadine, disease=Rasmussen subacute encephalitis | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Amantadine, disease=Rasmussen subacute encephalitis | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Amantadine, disease=transaldolase deficiency | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Amantadine, disease=transaldolase deficiency | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Amantadine, disease=transaldolase deficiency | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Amantadine, disease=myelitis | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Amantadine, disease=myelitis | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Amantadine, disease=myelitis | success | 11 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Amantadine, disease=PLA2G6-associated neurodegeneration | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Amantadine, disease=PLA2G6-associated neurodegeneration | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Amantadine, disease=PLA2G6-associated neurodegeneration | success | 2 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Amantadine, disease=fructose-1,6-bisphosphatase deficiency | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Amantadine, disease=fructose-1,6-bisphosphatase deficiency | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Amantadine, disease=fructose-1,6-bisphosphatase deficiency | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Amantadine, disease=paralysis agitans, juvenile, of Hunt | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Amantadine, disease=paralysis agitans, juvenile, of Hunt | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Amantadine, disease=paralysis agitans, juvenile, of Hunt | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Amantadine, disease=Lewy body dementia | success | 4 |  |
| 22 | ictrp | 2026-03-09 | drug=Amantadine, disease=Lewy body dementia | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Amantadine, disease=Lewy body dementia | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Amantadine, disease=X-linked intellectual disability-ataxia-apraxia syndrome | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Amantadine, disease=X-linked intellectual disability-ataxia-apraxia syndrome | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Amantadine, disease=X-linked intellectual disability-ataxia-apraxia syndrome | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Amantadine, disease=progressive supranuclear palsy-corticobasal syndrome | success | 1 |  |
| 28 | ictrp | 2026-03-09 | drug=Amantadine, disease=progressive supranuclear palsy-corticobasal syndrome | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Amantadine, disease=progressive supranuclear palsy-corticobasal syndrome | success | 1 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Amantadine, disease=X-linked intellectual disability-cerebellar hypoplasia syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Amantadine, disease=X-linked intellectual disability-cerebellar hypoplasia syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Amantadine, disease=X-linked intellectual disability-cerebellar hypoplasia syndrome | success | 0 |  |