# Ipilimumab 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Ipilimumab | |
| DrugBank ID | DB06186 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | choroideremia | 99.06% | L5 | 0 | 0 | S0 | Hold |
| 2 | non-cutaneous melanoma | 99.02% | L2 | 50 | 5 | S2 | Proceed with Guardrails |
| 3 | epithelioid cell melanoma | 98.96% | L3 | 1 | 7 | S2 | Research Question |
| 4 | eyelid melanoma | 98.95% | L4 | 0 | 9 | S1 | Research Question |
| 5 | scrotum melanoma | 98.84% | L3 | 1 | 0 | S1 | Research Question |
| 6 | amelanotic skin melanoma | 98.64% | L4 | 0 | 6 | S1 | Research Question |
| 7 | superficial spreading melanoma | 98.64% | L3 | 0 | 6 | S2 | Research Question |
| 8 | lentigo maligna melanoma | 98.64% | L4 | 0 | 5 | S1 | Research Question |
| 9 | CDK4 linked melanoma | 98.64% | L5 | 0 | 0 | S0 | Hold |
| 10 | acral lentiginous melanoma (disease) | 98.64% | L2 | 6 | 5 | S2 | Proceed with Guardrails |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Ipilimumab | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Ipilimumab | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Ipilimumab, disease=choroideremia | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Ipilimumab, disease=choroideremia | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Ipilimumab, disease=choroideremia | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Ipilimumab, disease=non-cutaneous melanoma | success | 50 |  |
| 7 | ictrp | 2026-03-10 | drug=Ipilimumab, disease=non-cutaneous melanoma | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Ipilimumab, disease=non-cutaneous melanoma | success | 5 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Ipilimumab, disease=epithelioid cell melanoma | success | 1 |  |
| 10 | ictrp | 2026-03-10 | drug=Ipilimumab, disease=epithelioid cell melanoma | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Ipilimumab, disease=epithelioid cell melanoma | success | 7 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Ipilimumab, disease=eyelid melanoma | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Ipilimumab, disease=eyelid melanoma | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Ipilimumab, disease=eyelid melanoma | success | 9 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Ipilimumab, disease=scrotum melanoma | success | 1 |  |
| 16 | ictrp | 2026-03-10 | drug=Ipilimumab, disease=scrotum melanoma | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Ipilimumab, disease=scrotum melanoma | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Ipilimumab, disease=amelanotic skin melanoma | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Ipilimumab, disease=amelanotic skin melanoma | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Ipilimumab, disease=amelanotic skin melanoma | success | 6 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Ipilimumab, disease=superficial spreading melanoma | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Ipilimumab, disease=superficial spreading melanoma | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Ipilimumab, disease=superficial spreading melanoma | success | 6 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Ipilimumab, disease=lentigo maligna melanoma | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Ipilimumab, disease=lentigo maligna melanoma | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Ipilimumab, disease=lentigo maligna melanoma | success | 5 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Ipilimumab, disease=CDK4 linked melanoma | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Ipilimumab, disease=CDK4 linked melanoma | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Ipilimumab, disease=CDK4 linked melanoma | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Ipilimumab, disease=acral lentiginous melanoma (disease) | success | 6 |  |
| 31 | ictrp | 2026-03-10 | drug=Ipilimumab, disease=acral lentiginous melanoma (disease) | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Ipilimumab, disease=acral lentiginous melanoma (disease) | success | 5 |  |