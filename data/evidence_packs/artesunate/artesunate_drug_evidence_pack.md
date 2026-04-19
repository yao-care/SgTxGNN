# Artesunate 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Artesunate | |
| DrugBank ID | DB09274 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | acne (disease) | 79.21% | L5 | 0 | 0 | S0 | Research Question |
| 2 | Smouldering systemic mastocytosis | 79.18% | L5 | 0 | 0 | S0 | Research Question |
| 3 | lymphoadenopathic mastocytosis with eosinophilia | 77.26% | L5 | 0 | 0 | S0 | Research Question |
| 4 | gastrin secretion abnormality | 76.71% | L5 | 0 | 0 | S0 | Hold |
| 5 | systemic mastocytosis | 71.44% | L5 | 0 | 0 | S0 | Research Question |
| 6 | leishmaniasis, diffuse cutaneous | 66.16% | L5 | 0 | 0 | S1 | Proceed with Guardrails |
| 7 | abnormality of glucagon secretion | 61.77% | L5 | 0 | 0 | S0 | Research Question |
| 8 | pyogenic arthritis-pyoderma gangrenosum-acne syndrome | 59.66% | L5 | 0 | 0 | S0 | Hold |
| 9 | Wiskott-Aldrich syndrome 2 | 59.41% | L5 | 0 | 0 | S0 | Hold |
| 10 | alacrima, achalasia, and intellectual disability syndrome | 59.33% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Artesunate | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Artesunate | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Artesunate, disease=acne (disease) | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Artesunate, disease=acne (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Artesunate, disease=acne (disease) | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Artesunate, disease=Smouldering systemic mastocytosis | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Artesunate, disease=Smouldering systemic mastocytosis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Artesunate, disease=Smouldering systemic mastocytosis | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Artesunate, disease=lymphoadenopathic mastocytosis with eosinophilia | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Artesunate, disease=lymphoadenopathic mastocytosis with eosinophilia | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Artesunate, disease=lymphoadenopathic mastocytosis with eosinophilia | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Artesunate, disease=gastrin secretion abnormality | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Artesunate, disease=gastrin secretion abnormality | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Artesunate, disease=gastrin secretion abnormality | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Artesunate, disease=systemic mastocytosis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Artesunate, disease=systemic mastocytosis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Artesunate, disease=systemic mastocytosis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Artesunate, disease=leishmaniasis, diffuse cutaneous | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Artesunate, disease=leishmaniasis, diffuse cutaneous | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Artesunate, disease=leishmaniasis, diffuse cutaneous | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Artesunate, disease=abnormality of glucagon secretion | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Artesunate, disease=abnormality of glucagon secretion | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Artesunate, disease=abnormality of glucagon secretion | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Artesunate, disease=pyogenic arthritis-pyoderma gangrenosum-acne syndrome | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Artesunate, disease=pyogenic arthritis-pyoderma gangrenosum-acne syndrome | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Artesunate, disease=pyogenic arthritis-pyoderma gangrenosum-acne syndrome | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Artesunate, disease=Wiskott-Aldrich syndrome 2 | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Artesunate, disease=Wiskott-Aldrich syndrome 2 | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Artesunate, disease=Wiskott-Aldrich syndrome 2 | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Artesunate, disease=alacrima, achalasia, and intellectual disability syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Artesunate, disease=alacrima, achalasia, and intellectual disability syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Artesunate, disease=alacrima, achalasia, and intellectual disability syndrome | success | 0 |  |