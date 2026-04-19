# Dacomitinib 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Dacomitinib | |
| DrugBank ID | DB11963 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | rheumatoid arthritis | 97.79% | L5 | 0 | 0 | S0 | Hold |
| 2 | homozygous familial hypercholesterolemia | 96.92% | L5 | 0 | 0 | S0 | Hold |
| 3 | brachydactyly-syndactyly syndrome | 96.78% | L5 | 0 | 0 | S0 | Hold |
| 4 | pulmonary hypertension | 96.51% | L3 | 1 | 1 | S1 | Research Question |
| 5 | nephrogenic syndrome of inappropriate antidiuresis | 96.44% | L5 | 0 | 0 | S0 | Hold |
| 6 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 96.44% | L5 | 0 | 0 | S0 | Hold |
| 7 | kyphoscoliotic heart disease | 96.18% | L5 | 0 | 0 | S0 | Hold |
| 8 | multiple endocrine neoplasia | 96.18% | L4 | 1 | 0 | S0 | Hold |
| 9 | amyotrophic lateral sclerosis | 95.12% | L5 | 0 | 0 | S0 | Hold |
| 10 | leprosy | 94.95% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Dacomitinib | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Dacomitinib | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Dacomitinib, disease=rheumatoid arthritis | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Dacomitinib, disease=rheumatoid arthritis | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Dacomitinib, disease=rheumatoid arthritis | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Dacomitinib, disease=homozygous familial hypercholesterolemia | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Dacomitinib, disease=homozygous familial hypercholesterolemia | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Dacomitinib, disease=homozygous familial hypercholesterolemia | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Dacomitinib, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Dacomitinib, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Dacomitinib, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Dacomitinib, disease=pulmonary hypertension | success | 1 |  |
| 13 | ictrp | 2026-03-10 | drug=Dacomitinib, disease=pulmonary hypertension | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Dacomitinib, disease=pulmonary hypertension | success | 1 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Dacomitinib, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Dacomitinib, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Dacomitinib, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Dacomitinib, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Dacomitinib, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Dacomitinib, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Dacomitinib, disease=kyphoscoliotic heart disease | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Dacomitinib, disease=kyphoscoliotic heart disease | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Dacomitinib, disease=kyphoscoliotic heart disease | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Dacomitinib, disease=multiple endocrine neoplasia | success | 1 |  |
| 25 | ictrp | 2026-03-10 | drug=Dacomitinib, disease=multiple endocrine neoplasia | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Dacomitinib, disease=multiple endocrine neoplasia | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Dacomitinib, disease=amyotrophic lateral sclerosis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Dacomitinib, disease=amyotrophic lateral sclerosis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Dacomitinib, disease=amyotrophic lateral sclerosis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Dacomitinib, disease=leprosy | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Dacomitinib, disease=leprosy | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Dacomitinib, disease=leprosy | success | 0 |  |