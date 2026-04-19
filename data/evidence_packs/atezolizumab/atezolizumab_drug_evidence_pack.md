# Atezolizumab 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Atezolizumab | |
| DrugBank ID | DB11595 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | prostatic urethra urothelial carcinoma | 99.98% | L2 | 2 | 0 | S2 | Proceed with Guardrails |
| 2 | kidney pelvis sarcomatoid transitional cell carcinoma | 99.98% | L4 | 0 | 0 | S0 | Hold |
| 3 | infiltrating bladder urothelial carcinoma sarcomatoid variant | 99.98% | L4 | 0 | 0 | S1 | Hold |
| 4 | renal pelvis papillary urothelial carcinoma | 99.98% | L3 | 1 | 0 | S1 | Research Question |
| 5 | uterine ligament adenocarcinoma | 99.93% | L5 | 0 | 0 | S0 | Hold |
| 6 | endocervical carcinoma | 99.92% | L2 | 2 | 1 | S2 | Research Question |
| 7 | adenoid cystic carcinoma of the cervix uteri | 99.92% | L5 | 0 | 0 | S0 | Hold |
| 8 | uterine ligament serous adenocarcinoma | 99.92% | L5 | 0 | 0 | S0 | Hold |
| 9 | signet ring cell variant cervical mucinous adenocarcinoma | 99.91% | L5 | 0 | 0 | S0 | Hold |
| 10 | intestinal variant cervical mucinous adenocarcinoma | 99.91% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Atezolizumab | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Atezolizumab | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Atezolizumab, disease=prostatic urethra urothelial carcinoma | success | 2 |  |
| 4 | ictrp | 2026-03-09 | drug=Atezolizumab, disease=prostatic urethra urothelial carcinoma | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Atezolizumab, disease=prostatic urethra urothelial carcinoma | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Atezolizumab, disease=kidney pelvis sarcomatoid transitional cell carcinoma | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Atezolizumab, disease=kidney pelvis sarcomatoid transitional cell carcinoma | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Atezolizumab, disease=kidney pelvis sarcomatoid transitional cell carcinoma | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Atezolizumab, disease=infiltrating bladder urothelial carcinoma sarcomatoid variant | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Atezolizumab, disease=infiltrating bladder urothelial carcinoma sarcomatoid variant | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Atezolizumab, disease=infiltrating bladder urothelial carcinoma sarcomatoid variant | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Atezolizumab, disease=renal pelvis papillary urothelial carcinoma | success | 1 |  |
| 13 | ictrp | 2026-03-09 | drug=Atezolizumab, disease=renal pelvis papillary urothelial carcinoma | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Atezolizumab, disease=renal pelvis papillary urothelial carcinoma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Atezolizumab, disease=uterine ligament adenocarcinoma | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Atezolizumab, disease=uterine ligament adenocarcinoma | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Atezolizumab, disease=uterine ligament adenocarcinoma | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Atezolizumab, disease=endocervical carcinoma | success | 2 |  |
| 19 | ictrp | 2026-03-09 | drug=Atezolizumab, disease=endocervical carcinoma | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Atezolizumab, disease=endocervical carcinoma | success | 1 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Atezolizumab, disease=adenoid cystic carcinoma of the cervix uteri | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Atezolizumab, disease=adenoid cystic carcinoma of the cervix uteri | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Atezolizumab, disease=adenoid cystic carcinoma of the cervix uteri | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Atezolizumab, disease=uterine ligament serous adenocarcinoma | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Atezolizumab, disease=uterine ligament serous adenocarcinoma | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Atezolizumab, disease=uterine ligament serous adenocarcinoma | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Atezolizumab, disease=signet ring cell variant cervical mucinous adenocarcinoma | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Atezolizumab, disease=signet ring cell variant cervical mucinous adenocarcinoma | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Atezolizumab, disease=signet ring cell variant cervical mucinous adenocarcinoma | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Atezolizumab, disease=intestinal variant cervical mucinous adenocarcinoma | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Atezolizumab, disease=intestinal variant cervical mucinous adenocarcinoma | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Atezolizumab, disease=intestinal variant cervical mucinous adenocarcinoma | success | 0 |  |