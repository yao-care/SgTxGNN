# Ketoconazole 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Ketoconazole | |
| DrugBank ID | DB01026 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | acne (disease) | 99.80% | L3 | 1 | 15 | S2 | Research Question |
| 2 | zinc, elevated plasma | 95.38% | L5 | 0 | 0 | S0 | Hold |
| 3 | leprosy | 93.11% | L5 | 0 | 20 | S0 | Hold |
| 4 | vulvovaginal candidiasis | 92.95% | L1 | 2 | 20 | S3 | Proceed with Guardrails |
| 5 | urticaria, aquagenic | 92.69% | L5 | 0 | 0 | S0 | Hold |
| 6 | punctate epithelial keratoconjunctivitis | 91.43% | L5 | 0 | 0 | S0 | Hold |
| 7 | tinea profunda | 90.76% | L3 | 0 | 6 | S2 | Research Question |
| 8 | nail infection | 90.71% | pending | 1 | 20 | pending | pending |
| 9 | candida glabrata | 90.39% | L4 | 0 | 20 | S1 | Research Question |
| 10 | neonatal candidiasis | 90.39% | L4 | 0 | 20 | S1 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Ketoconazole | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Ketoconazole | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Ketoconazole, disease=acne (disease) | success | 1 |  |
| 4 | ictrp | 2026-03-09 | drug=Ketoconazole, disease=acne (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Ketoconazole, disease=acne (disease) | success | 15 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Ketoconazole, disease=zinc, elevated plasma | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Ketoconazole, disease=zinc, elevated plasma | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Ketoconazole, disease=zinc, elevated plasma | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Ketoconazole, disease=leprosy | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Ketoconazole, disease=leprosy | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Ketoconazole, disease=leprosy | success | 20 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Ketoconazole, disease=vulvovaginal candidiasis | success | 2 |  |
| 13 | ictrp | 2026-03-09 | drug=Ketoconazole, disease=vulvovaginal candidiasis | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Ketoconazole, disease=vulvovaginal candidiasis | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Ketoconazole, disease=urticaria, aquagenic | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Ketoconazole, disease=urticaria, aquagenic | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Ketoconazole, disease=urticaria, aquagenic | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Ketoconazole, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Ketoconazole, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Ketoconazole, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Ketoconazole, disease=tinea profunda | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Ketoconazole, disease=tinea profunda | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Ketoconazole, disease=tinea profunda | success | 6 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Ketoconazole, disease=nail infection | success | 1 |  |
| 25 | ictrp | 2026-03-09 | drug=Ketoconazole, disease=nail infection | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Ketoconazole, disease=nail infection | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Ketoconazole, disease=candida glabrata | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Ketoconazole, disease=candida glabrata | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Ketoconazole, disease=candida glabrata | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Ketoconazole, disease=neonatal candidiasis | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Ketoconazole, disease=neonatal candidiasis | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Ketoconazole, disease=neonatal candidiasis | success | 20 |  |