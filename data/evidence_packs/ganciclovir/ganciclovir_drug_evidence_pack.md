# Ganciclovir 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Ganciclovir | |
| DrugBank ID | DB01004 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | cytomegalovirus pneumonia | 97.56% | L1 | 9 | 20 | S3 | Proceed with Guardrails |
| 2 | epidemic keratoconjunctivitis | 97.28% | L4 | 0 | 5 | S1 | Research Question |
| 3 | commissural lip fistula | 97.13% | L5 | 0 | 0 | S0 | Hold |
| 4 | idiopathic disseminated cytomegalovirus infection | 97.07% | L4 | 0 | 0 | S1 | Research Question |
| 5 | burning mouth syndrome | 97.06% | L5 | 0 | 0 | S0 | Hold |
| 6 | oral leukoedema | 97.06% | L5 | 0 | 0 | S0 | Hold |
| 7 | osteoradionecrosis of the mandible | 97.06% | L5 | 0 | 0 | S0 | Hold |
| 8 | punctate epithelial keratoconjunctivitis | 96.94% | L5 | 0 | 1 | S0 | Hold |
| 9 | oral candidiasis | 96.85% | L5 | 1 | 14 | S0 | Hold |
| 10 | pneumonia | 96.61% | L2 | 9 | 20 | S2 | Proceed with Guardrails |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Ganciclovir | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Ganciclovir | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Ganciclovir, disease=cytomegalovirus pneumonia | success | 9 |  |
| 4 | ictrp | 2026-03-10 | drug=Ganciclovir, disease=cytomegalovirus pneumonia | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Ganciclovir, disease=cytomegalovirus pneumonia | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Ganciclovir, disease=epidemic keratoconjunctivitis | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Ganciclovir, disease=epidemic keratoconjunctivitis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Ganciclovir, disease=epidemic keratoconjunctivitis | success | 5 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Ganciclovir, disease=commissural lip fistula | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Ganciclovir, disease=commissural lip fistula | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Ganciclovir, disease=commissural lip fistula | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Ganciclovir, disease=idiopathic disseminated cytomegalovirus infection | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Ganciclovir, disease=idiopathic disseminated cytomegalovirus infection | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Ganciclovir, disease=idiopathic disseminated cytomegalovirus infection | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Ganciclovir, disease=burning mouth syndrome | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Ganciclovir, disease=burning mouth syndrome | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Ganciclovir, disease=burning mouth syndrome | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Ganciclovir, disease=oral leukoedema | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Ganciclovir, disease=oral leukoedema | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Ganciclovir, disease=oral leukoedema | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Ganciclovir, disease=osteoradionecrosis of the mandible | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Ganciclovir, disease=osteoradionecrosis of the mandible | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Ganciclovir, disease=osteoradionecrosis of the mandible | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Ganciclovir, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Ganciclovir, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Ganciclovir, disease=punctate epithelial keratoconjunctivitis | success | 1 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Ganciclovir, disease=oral candidiasis | success | 1 |  |
| 28 | ictrp | 2026-03-10 | drug=Ganciclovir, disease=oral candidiasis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Ganciclovir, disease=oral candidiasis | success | 14 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Ganciclovir, disease=pneumonia | success | 9 |  |
| 31 | ictrp | 2026-03-10 | drug=Ganciclovir, disease=pneumonia | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Ganciclovir, disease=pneumonia | success | 20 |  |