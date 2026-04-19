# Guaifenesin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Guaifenesin | |
| DrugBank ID | DB00874 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | nasal cavity disease | 99.98% | L3 | 1 | 2 | S2 | Proceed with Guardrails |
| 2 | acute laryngopharyngitis | 99.98% | L5 | 0 | 0 | S0 | Hold |
| 3 | faucial diphtheria | 99.54% | L5 | 0 | 0 | S0 | Hold |
| 4 | cervical disc degenerative disorder | 99.50% | L5 | 0 | 0 | S0 | Hold |
| 5 | papillary conjunctivitis | 99.27% | L5 | 0 | 0 | S0 | Hold |
| 6 | tracheal disease | 98.83% | L3 | 3 | 5 | S1 | Research Question |
| 7 | trigeminal autonomic cephalalgia | 98.70% | L5 | 0 | 0 | S0 | Hold |
| 8 | anorectal stricture | 98.63% | L5 | 0 | 0 | S0 | Hold |
| 9 | anal polyp | 98.61% | L5 | 0 | 0 | S0 | Hold |
| 10 | punctate epithelial keratoconjunctivitis | 98.48% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Guaifenesin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Guaifenesin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Guaifenesin, disease=nasal cavity disease | success | 1 |  |
| 4 | ictrp | 2026-03-09 | drug=Guaifenesin, disease=nasal cavity disease | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Guaifenesin, disease=nasal cavity disease | success | 2 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Guaifenesin, disease=acute laryngopharyngitis | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Guaifenesin, disease=acute laryngopharyngitis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Guaifenesin, disease=acute laryngopharyngitis | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Guaifenesin, disease=faucial diphtheria | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Guaifenesin, disease=faucial diphtheria | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Guaifenesin, disease=faucial diphtheria | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Guaifenesin, disease=cervical disc degenerative disorder | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Guaifenesin, disease=cervical disc degenerative disorder | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Guaifenesin, disease=cervical disc degenerative disorder | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Guaifenesin, disease=papillary conjunctivitis | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Guaifenesin, disease=papillary conjunctivitis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Guaifenesin, disease=papillary conjunctivitis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Guaifenesin, disease=tracheal disease | success | 3 |  |
| 19 | ictrp | 2026-03-09 | drug=Guaifenesin, disease=tracheal disease | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Guaifenesin, disease=tracheal disease | success | 5 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Guaifenesin, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Guaifenesin, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Guaifenesin, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Guaifenesin, disease=anorectal stricture | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Guaifenesin, disease=anorectal stricture | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Guaifenesin, disease=anorectal stricture | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Guaifenesin, disease=anal polyp | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Guaifenesin, disease=anal polyp | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Guaifenesin, disease=anal polyp | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Guaifenesin, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Guaifenesin, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Guaifenesin, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |