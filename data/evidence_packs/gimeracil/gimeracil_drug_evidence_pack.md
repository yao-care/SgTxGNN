# Gimeracil 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Gimeracil | |
| DrugBank ID | DB09257 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | colonic neoplasm | 99.88% | pending | 8 | 14 | pending | pending |
| 2 | cecum villous adenoma | 99.82% | pending | 0 | 0 | pending | pending |
| 3 | malignant gastric granular cell tumor | 99.82% | pending | 0 | 0 | pending | pending |
| 4 | lipoma of colon | 99.82% | pending | 0 | 0 | pending | pending |
| 5 | cecum neuroendocrine tumor G1 | 99.82% | pending | 0 | 0 | pending | pending |
| 6 | rectosigmoid junction neoplasm | 99.82% | pending | 0 | 0 | pending | pending |
| 7 | cardia cancer | 99.81% | pending | 0 | 1 | pending | pending |
| 8 | colonic lymphangioma | 99.81% | pending | 0 | 0 | pending | pending |
| 9 | colon leiomyoma | 99.81% | pending | 0 | 1 | pending | pending |
| 10 | gastric lymphoma | 99.81% | pending | 0 | 0 | pending | pending |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Gimeracil | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Gimeracil | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Gimeracil, disease=colonic neoplasm | success | 8 |  |
| 4 | ictrp | 2026-03-09 | drug=Gimeracil, disease=colonic neoplasm | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Gimeracil, disease=colonic neoplasm | success | 14 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Gimeracil, disease=cecum villous adenoma | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Gimeracil, disease=cecum villous adenoma | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Gimeracil, disease=cecum villous adenoma | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Gimeracil, disease=malignant gastric granular cell tumor | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Gimeracil, disease=malignant gastric granular cell tumor | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Gimeracil, disease=malignant gastric granular cell tumor | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Gimeracil, disease=lipoma of colon | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Gimeracil, disease=lipoma of colon | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Gimeracil, disease=lipoma of colon | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Gimeracil, disease=cecum neuroendocrine tumor G1 | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Gimeracil, disease=cecum neuroendocrine tumor G1 | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Gimeracil, disease=cecum neuroendocrine tumor G1 | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Gimeracil, disease=rectosigmoid junction neoplasm | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Gimeracil, disease=rectosigmoid junction neoplasm | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Gimeracil, disease=rectosigmoid junction neoplasm | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Gimeracil, disease=cardia cancer | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Gimeracil, disease=cardia cancer | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Gimeracil, disease=cardia cancer | success | 1 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Gimeracil, disease=colonic lymphangioma | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Gimeracil, disease=colonic lymphangioma | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Gimeracil, disease=colonic lymphangioma | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Gimeracil, disease=colon leiomyoma | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Gimeracil, disease=colon leiomyoma | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Gimeracil, disease=colon leiomyoma | success | 1 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Gimeracil, disease=gastric lymphoma | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Gimeracil, disease=gastric lymphoma | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Gimeracil, disease=gastric lymphoma | success | 0 |  |