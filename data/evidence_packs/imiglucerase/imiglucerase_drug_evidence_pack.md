# Imiglucerase 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Imiglucerase | |
| DrugBank ID | DB00053 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | Hurler syndrome | 99.52% | L4 | 0 | 2 | S0 | Hold |
| 2 | Scheie syndrome | 99.29% | L4 | 0 | 1 | S0 | Hold |
| 3 | benign neoplasm of adrenal gland | 99.28% | L5 | 0 | 0 | S0 | Hold |
| 4 | autosomal ichthyosis syndrome with fatal disease course | 99.24% | L5 | 0 | 0 | S0 | Hold |
| 5 | cholesteryl ester storage disease | 99.12% | L5 | 0 | 0 | S0 | Hold |
| 6 | lysosomal storage disease with skeletal involvement | 98.94% | L1 | 2 | 20 | S3 | Proceed with Guardrails |
| 7 | Wolman disease with hypolipoproteinemia and acanthocytosis | 98.93% | L5 | 0 | 0 | S0 | Hold |
| 8 | Wolman disease | 98.78% | L5 | 0 | 0 | S0 | Hold |
| 9 | proximal myopathy with extrapyramidal signs | 98.54% | L5 | 0 | 0 | S0 | Hold |
| 10 | growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant | 98.49% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Imiglucerase | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Imiglucerase | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Imiglucerase, disease=Hurler syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Imiglucerase, disease=Hurler syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Imiglucerase, disease=Hurler syndrome | success | 2 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Imiglucerase, disease=Scheie syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Imiglucerase, disease=Scheie syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Imiglucerase, disease=Scheie syndrome | success | 1 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Imiglucerase, disease=benign neoplasm of adrenal gland | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Imiglucerase, disease=benign neoplasm of adrenal gland | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Imiglucerase, disease=benign neoplasm of adrenal gland | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Imiglucerase, disease=autosomal ichthyosis syndrome with fatal disease course | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Imiglucerase, disease=autosomal ichthyosis syndrome with fatal disease course | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Imiglucerase, disease=autosomal ichthyosis syndrome with fatal disease course | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Imiglucerase, disease=cholesteryl ester storage disease | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Imiglucerase, disease=cholesteryl ester storage disease | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Imiglucerase, disease=cholesteryl ester storage disease | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Imiglucerase, disease=lysosomal storage disease with skeletal involvement | success | 2 |  |
| 19 | ictrp | 2026-03-10 | drug=Imiglucerase, disease=lysosomal storage disease with skeletal involvement | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Imiglucerase, disease=lysosomal storage disease with skeletal involvement | success | 20 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Imiglucerase, disease=Wolman disease with hypolipoproteinemia and acanthocytosis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Imiglucerase, disease=Wolman disease with hypolipoproteinemia and acanthocytosis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Imiglucerase, disease=Wolman disease with hypolipoproteinemia and acanthocytosis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Imiglucerase, disease=Wolman disease | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Imiglucerase, disease=Wolman disease | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Imiglucerase, disease=Wolman disease | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Imiglucerase, disease=proximal myopathy with extrapyramidal signs | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Imiglucerase, disease=proximal myopathy with extrapyramidal signs | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Imiglucerase, disease=proximal myopathy with extrapyramidal signs | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Imiglucerase, disease=growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Imiglucerase, disease=growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Imiglucerase, disease=growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant | success | 0 |  |