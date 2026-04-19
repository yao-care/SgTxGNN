# Alirocumab 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Alirocumab | |
| DrugBank ID | DB09302 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | ichthyosis, X-linked, without steroid sulfatase deficiency | 99.43% | L5 | 0 | 0 | S0 | Hold |
| 2 | disorder of other vitamins and cofactors metabolism and transport | 99.41% | L5 | 0 | 0 | S0 | Hold |
| 3 | xanthomatosis (disease) | 99.37% | L4 | 0 | 2 | S1 | Research Question |
| 4 | 46,XY disorder of sexual development due to dihydrotestosterone backdoor pathway biosynthesis defect | 99.37% | L5 | 0 | 0 | S0 | Hold |
| 5 | cholesterol catabolic process disease | 99.36% | L2 | 1 | 19 | S3 | Proceed with Guardrails |
| 6 | 46,XY disorder of sex development due to a cholesterol synthesis defect | 99.35% | L5 | 0 | 0 | S0 | Hold |
| 7 | dappled diaphyseal dysplasia | 99.30% | L5 | 0 | 0 | S0 | Hold |
| 8 | neutral lipid storage disease | 99.29% | L5 | 0 | 0 | S0 | Hold |
| 9 | 3-hydroxyacyl-CoA dehydrogenase deficiency | 99.29% | L5 | 0 | 0 | S0 | Hold |
| 10 | spastic paraplegia-optic atrophy-neuropathy and spastic paraplegia-optic atrophy-neuropathy-related disorder | 99.26% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Alirocumab | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Alirocumab | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Alirocumab, disease=ichthyosis, X-linked, without steroid sulfatase deficiency | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Alirocumab, disease=ichthyosis, X-linked, without steroid sulfatase deficiency | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Alirocumab, disease=ichthyosis, X-linked, without steroid sulfatase deficiency | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Alirocumab, disease=disorder of other vitamins and cofactors metabolism and transport | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Alirocumab, disease=disorder of other vitamins and cofactors metabolism and transport | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Alirocumab, disease=disorder of other vitamins and cofactors metabolism and transport | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Alirocumab, disease=xanthomatosis (disease) | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Alirocumab, disease=xanthomatosis (disease) | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Alirocumab, disease=xanthomatosis (disease) | success | 2 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Alirocumab, disease=46,XY disorder of sexual development due to dihydrotestosterone backdoor pathway biosynthesis defect | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Alirocumab, disease=46,XY disorder of sexual development due to dihydrotestosterone backdoor pathway biosynthesis defect | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Alirocumab, disease=46,XY disorder of sexual development due to dihydrotestosterone backdoor pathway biosynthesis defect | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Alirocumab, disease=cholesterol catabolic process disease | success | 1 |  |
| 16 | ictrp | 2026-03-10 | drug=Alirocumab, disease=cholesterol catabolic process disease | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Alirocumab, disease=cholesterol catabolic process disease | success | 19 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Alirocumab, disease=46,XY disorder of sex development due to a cholesterol synthesis defect | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Alirocumab, disease=46,XY disorder of sex development due to a cholesterol synthesis defect | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Alirocumab, disease=46,XY disorder of sex development due to a cholesterol synthesis defect | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Alirocumab, disease=dappled diaphyseal dysplasia | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Alirocumab, disease=dappled diaphyseal dysplasia | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Alirocumab, disease=dappled diaphyseal dysplasia | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Alirocumab, disease=neutral lipid storage disease | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Alirocumab, disease=neutral lipid storage disease | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Alirocumab, disease=neutral lipid storage disease | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Alirocumab, disease=3-hydroxyacyl-CoA dehydrogenase deficiency | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Alirocumab, disease=3-hydroxyacyl-CoA dehydrogenase deficiency | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Alirocumab, disease=3-hydroxyacyl-CoA dehydrogenase deficiency | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Alirocumab, disease=spastic paraplegia-optic atrophy-neuropathy and spastic paraplegia-optic atrophy-neuropathy-related disorder | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Alirocumab, disease=spastic paraplegia-optic atrophy-neuropathy and spastic paraplegia-optic atrophy-neuropathy-related disorder | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Alirocumab, disease=spastic paraplegia-optic atrophy-neuropathy and spastic paraplegia-optic atrophy-neuropathy-related disorder | success | 0 |  |