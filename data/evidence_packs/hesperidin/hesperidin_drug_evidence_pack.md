# Hesperidin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Hesperidin | |
| DrugBank ID | DB04703 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | myeloproliferative neoplasm | 99.47% | L4 | 0 | 2 | S1 | Research Question |
| 2 | monocytic leukemia | 99.40% | L4 | 0 | 1 | S0 | Hold |
| 3 | spermatocytic seminoma | 99.34% | L5 | 0 | 0 | S0 | Hold |
| 4 | tubular variant testicular seminoma | 99.31% | L5 | 0 | 0 | S0 | Hold |
| 5 | gestational trophoblastic neoplasm | 99.03% | L5 | 0 | 0 | S0 | Hold |
| 6 | primary peritoneal carcinoma (disease) | 98.79% | L5 | 0 | 0 | S0 | Hold |
| 7 | acute lymphoblastic leukemia (disease) | 98.74% | L5 | 0 | 0 | S0 | Hold |
| 8 | myeloid leukemia | 98.73% | L4 | 0 | 16 | S1 | Research Question |
| 9 | Seckel syndrome | 98.71% | L5 | 0 | 0 | S0 | Hold |
| 10 | myeloproliferative neoplasm, unclassifiable | 98.68% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Hesperidin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Hesperidin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Hesperidin, disease=myeloproliferative neoplasm | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Hesperidin, disease=myeloproliferative neoplasm | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Hesperidin, disease=myeloproliferative neoplasm | success | 2 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Hesperidin, disease=monocytic leukemia | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Hesperidin, disease=monocytic leukemia | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Hesperidin, disease=monocytic leukemia | success | 1 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Hesperidin, disease=spermatocytic seminoma | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Hesperidin, disease=spermatocytic seminoma | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Hesperidin, disease=spermatocytic seminoma | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Hesperidin, disease=tubular variant testicular seminoma | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Hesperidin, disease=tubular variant testicular seminoma | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Hesperidin, disease=tubular variant testicular seminoma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Hesperidin, disease=gestational trophoblastic neoplasm | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Hesperidin, disease=gestational trophoblastic neoplasm | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Hesperidin, disease=gestational trophoblastic neoplasm | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Hesperidin, disease=primary peritoneal carcinoma (disease) | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Hesperidin, disease=primary peritoneal carcinoma (disease) | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Hesperidin, disease=primary peritoneal carcinoma (disease) | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Hesperidin, disease=acute lymphoblastic leukemia (disease) | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Hesperidin, disease=acute lymphoblastic leukemia (disease) | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Hesperidin, disease=acute lymphoblastic leukemia (disease) | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Hesperidin, disease=myeloid leukemia | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Hesperidin, disease=myeloid leukemia | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Hesperidin, disease=myeloid leukemia | success | 16 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Hesperidin, disease=Seckel syndrome | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Hesperidin, disease=Seckel syndrome | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Hesperidin, disease=Seckel syndrome | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Hesperidin, disease=myeloproliferative neoplasm, unclassifiable | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Hesperidin, disease=myeloproliferative neoplasm, unclassifiable | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Hesperidin, disease=myeloproliferative neoplasm, unclassifiable | success | 0 |  |