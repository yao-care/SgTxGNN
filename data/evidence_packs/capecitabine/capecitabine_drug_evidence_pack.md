# Capecitabine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Capecitabine | |
| DrugBank ID | DB01101 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | gastric adenocarcinoma and proximal polyposis of the stomach | 99.94% | L5 | 0 | 0 | S0 | Hold |
| 2 | gastric tubular adenocarcinoma | 99.94% | L1 | 0 | 20 | S3 | Proceed with Guardrails |
| 3 | microinvasive gastric cancer | 99.94% | L5 | 0 | 0 | S0 | Hold |
| 4 | signet ring cell gastric adenocarcinoma | 99.94% | L2 | 2 | 20 | S2 | Research Question |
| 5 | gastric cardia adenocarcinoma | 99.91% | L1 | 6 | 8 | S3 | Proceed with Guardrails |
| 6 | gastric pylorus carcinoma | 99.91% | L4 | 0 | 2 | S1 | Hold |
| 7 | carcinoma of stomach, salivary gland type | 99.91% | L3 | 2 | 0 | S1 | Research Question |
| 8 | gastric body carcinoma | 99.90% | L2 | 14 | 18 | S2 | Proceed with Guardrails |
| 9 | Epstein-Barr virus-associated gastric carcinoma | 99.90% | L5 | 0 | 0 | S0 | Hold |
| 10 | malignant gastric granular cell tumor | 99.89% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Capecitabine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Capecitabine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Capecitabine, disease=gastric adenocarcinoma and proximal polyposis of the stomach | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Capecitabine, disease=gastric adenocarcinoma and proximal polyposis of the stomach | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Capecitabine, disease=gastric adenocarcinoma and proximal polyposis of the stomach | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Capecitabine, disease=gastric tubular adenocarcinoma | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Capecitabine, disease=gastric tubular adenocarcinoma | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Capecitabine, disease=gastric tubular adenocarcinoma | success | 20 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Capecitabine, disease=microinvasive gastric cancer | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Capecitabine, disease=microinvasive gastric cancer | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Capecitabine, disease=microinvasive gastric cancer | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Capecitabine, disease=signet ring cell gastric adenocarcinoma | success | 2 |  |
| 13 | ictrp | 2026-03-09 | drug=Capecitabine, disease=signet ring cell gastric adenocarcinoma | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Capecitabine, disease=signet ring cell gastric adenocarcinoma | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Capecitabine, disease=gastric cardia adenocarcinoma | success | 6 |  |
| 16 | ictrp | 2026-03-09 | drug=Capecitabine, disease=gastric cardia adenocarcinoma | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Capecitabine, disease=gastric cardia adenocarcinoma | success | 8 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Capecitabine, disease=gastric pylorus carcinoma | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Capecitabine, disease=gastric pylorus carcinoma | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Capecitabine, disease=gastric pylorus carcinoma | success | 2 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Capecitabine, disease=carcinoma of stomach, salivary gland type | success | 2 |  |
| 22 | ictrp | 2026-03-09 | drug=Capecitabine, disease=carcinoma of stomach, salivary gland type | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Capecitabine, disease=carcinoma of stomach, salivary gland type | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Capecitabine, disease=gastric body carcinoma | success | 14 |  |
| 25 | ictrp | 2026-03-09 | drug=Capecitabine, disease=gastric body carcinoma | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Capecitabine, disease=gastric body carcinoma | success | 18 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Capecitabine, disease=Epstein-Barr virus-associated gastric carcinoma | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Capecitabine, disease=Epstein-Barr virus-associated gastric carcinoma | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Capecitabine, disease=Epstein-Barr virus-associated gastric carcinoma | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Capecitabine, disease=malignant gastric granular cell tumor | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Capecitabine, disease=malignant gastric granular cell tumor | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Capecitabine, disease=malignant gastric granular cell tumor | success | 0 |  |