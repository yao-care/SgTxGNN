# Dabrafenib 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Dabrafenib | |
| DrugBank ID | DB08912 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | choroideremia | 98.63% | L5 | 0 | 0 | S0 | Hold |
| 2 | non-cutaneous melanoma | 98.48% | L2 | 50 | 0 | S2 | Proceed with Guardrails |
| 3 | epithelioid cell melanoma | 98.44% | L4 | 0 | 2 | S1 | Research Question |
| 4 | eyelid melanoma | 98.41% | L4 | 0 | 3 | S1 | Research Question |
| 5 | scrotum melanoma | 98.28% | L4 | 0 | 1 | S1 | Research Question |
| 6 | choroidal dystrophy, central areolar | 98.27% | L5 | 0 | 0 | S0 | Hold |
| 7 | amyotrophic lateral sclerosis | 98.26% | L5 | 0 | 0 | S0 | Hold |
| 8 | bilateral parasagittal parieto-occipital polymicrogyria | 98.21% | L5 | 0 | 0 | S0 | Hold |
| 9 | lentigo maligna melanoma | 98.09% | L4 | 0 | 1 | S1 | Research Question |
| 10 | amelanotic skin melanoma | 98.09% | L4 | 0 | 2 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Dabrafenib | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Dabrafenib | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Dabrafenib, disease=choroideremia | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Dabrafenib, disease=choroideremia | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Dabrafenib, disease=choroideremia | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Dabrafenib, disease=non-cutaneous melanoma | success | 50 |  |
| 7 | ictrp | 2026-03-10 | drug=Dabrafenib, disease=non-cutaneous melanoma | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Dabrafenib, disease=non-cutaneous melanoma | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Dabrafenib, disease=epithelioid cell melanoma | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Dabrafenib, disease=epithelioid cell melanoma | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Dabrafenib, disease=epithelioid cell melanoma | success | 2 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Dabrafenib, disease=eyelid melanoma | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Dabrafenib, disease=eyelid melanoma | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Dabrafenib, disease=eyelid melanoma | success | 3 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Dabrafenib, disease=scrotum melanoma | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Dabrafenib, disease=scrotum melanoma | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Dabrafenib, disease=scrotum melanoma | success | 1 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Dabrafenib, disease=choroidal dystrophy, central areolar | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Dabrafenib, disease=choroidal dystrophy, central areolar | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Dabrafenib, disease=choroidal dystrophy, central areolar | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Dabrafenib, disease=amyotrophic lateral sclerosis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Dabrafenib, disease=amyotrophic lateral sclerosis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Dabrafenib, disease=amyotrophic lateral sclerosis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Dabrafenib, disease=bilateral parasagittal parieto-occipital polymicrogyria | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Dabrafenib, disease=bilateral parasagittal parieto-occipital polymicrogyria | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Dabrafenib, disease=bilateral parasagittal parieto-occipital polymicrogyria | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Dabrafenib, disease=lentigo maligna melanoma | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Dabrafenib, disease=lentigo maligna melanoma | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Dabrafenib, disease=lentigo maligna melanoma | success | 1 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Dabrafenib, disease=amelanotic skin melanoma | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Dabrafenib, disease=amelanotic skin melanoma | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Dabrafenib, disease=amelanotic skin melanoma | success | 2 |  |