# Gemcitabine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Gemcitabine | |
| DrugBank ID | DB00441 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | female breast carcinoma | 99.98% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 2 | rectum mucinous adenocarcinoma | 99.77% | L4 | 1 | 0 | S1 | Hold |
| 3 | colon mucinous adenocarcinoma | 99.76% | L4 | 2 | 3 | S1 | Hold |
| 4 | villoglandular endometrial endometrioid adenocarcinoma | 99.76% | L5 | 0 | 0 | S0 | Hold |
| 5 | endometrial mixed adenocarcinoma | 99.76% | L3 | 0 | 2 | S1 | Research Question |
| 6 | endometrial mucinous adenocarcinoma | 99.75% | L3 | 1 | 7 | S2 | Research Question |
| 7 | cervical mucinous adenocarcinoma | 99.75% | L4 | 2 | 4 | S1 | Hold |
| 8 | gallbladder mucinous adenocarcinoma | 99.75% | L4 | 2 | 3 | S1 | Research Question |
| 9 | rete ovarii adenocarcinoma | 99.73% | L5 | 0 | 0 | S0 | Hold |
| 10 | mucin-rich endometrial endometrioid adenocarcinoma | 99.73% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Gemcitabine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Gemcitabine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Gemcitabine, disease=female breast carcinoma | success | 50 |  |
| 4 | ictrp | 2026-03-09 | drug=Gemcitabine, disease=female breast carcinoma | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Gemcitabine, disease=female breast carcinoma | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Gemcitabine, disease=rectum mucinous adenocarcinoma | success | 1 |  |
| 7 | ictrp | 2026-03-09 | drug=Gemcitabine, disease=rectum mucinous adenocarcinoma | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Gemcitabine, disease=rectum mucinous adenocarcinoma | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Gemcitabine, disease=colon mucinous adenocarcinoma | success | 2 |  |
| 10 | ictrp | 2026-03-09 | drug=Gemcitabine, disease=colon mucinous adenocarcinoma | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Gemcitabine, disease=colon mucinous adenocarcinoma | success | 3 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Gemcitabine, disease=villoglandular endometrial endometrioid adenocarcinoma | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Gemcitabine, disease=villoglandular endometrial endometrioid adenocarcinoma | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Gemcitabine, disease=villoglandular endometrial endometrioid adenocarcinoma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Gemcitabine, disease=endometrial mixed adenocarcinoma | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Gemcitabine, disease=endometrial mixed adenocarcinoma | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Gemcitabine, disease=endometrial mixed adenocarcinoma | success | 2 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Gemcitabine, disease=endometrial mucinous adenocarcinoma | success | 1 |  |
| 19 | ictrp | 2026-03-09 | drug=Gemcitabine, disease=endometrial mucinous adenocarcinoma | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Gemcitabine, disease=endometrial mucinous adenocarcinoma | success | 7 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Gemcitabine, disease=cervical mucinous adenocarcinoma | success | 2 |  |
| 22 | ictrp | 2026-03-09 | drug=Gemcitabine, disease=cervical mucinous adenocarcinoma | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Gemcitabine, disease=cervical mucinous adenocarcinoma | success | 4 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Gemcitabine, disease=gallbladder mucinous adenocarcinoma | success | 2 |  |
| 25 | ictrp | 2026-03-09 | drug=Gemcitabine, disease=gallbladder mucinous adenocarcinoma | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Gemcitabine, disease=gallbladder mucinous adenocarcinoma | success | 3 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Gemcitabine, disease=rete ovarii adenocarcinoma | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Gemcitabine, disease=rete ovarii adenocarcinoma | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Gemcitabine, disease=rete ovarii adenocarcinoma | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Gemcitabine, disease=mucin-rich endometrial endometrioid adenocarcinoma | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Gemcitabine, disease=mucin-rich endometrial endometrioid adenocarcinoma | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Gemcitabine, disease=mucin-rich endometrial endometrioid adenocarcinoma | success | 0 |  |