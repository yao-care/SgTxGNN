# Ifosfamide 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Ifosfamide | |
| DrugBank ID | DB01181 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | female breast carcinoma | 99.91% | L2 | 8 | 20 | S2 | Proceed with Guardrails |
| 2 | unclassified myelodysplastic syndrome | 99.71% | L5 | 0 | 0 | S0 | Hold |
| 3 | partial deletion of the long arm of chromosome 5 | 99.70% | L5 | 0 | 0 | S0 | Hold |
| 4 | refractory cytopenia of childhood | 99.70% | L4 | 1 | 1 | S1 | Research Question |
| 5 | severe congenital hypochromic anemia with ringed sideroblasts | 99.68% | L5 | 0 | 0 | S0 | Hold |
| 6 | aregenerative anemia | 99.68% | L4 | 0 | 20 | S0 | Hold |
| 7 | rhabdomyosarcoma (disease) | 99.67% | L1 | 34 | 20 | S3 | Proceed with Guardrails |
| 8 | myelodysplastic syndrome | 99.66% | L4 | 4 | 20 | S0 | Hold |
| 9 | monocytic leukemia | 99.64% | L4 | 0 | 3 | S0 | Hold |
| 10 | botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.57% | L4 | 0 | 1 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Ifosfamide | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Ifosfamide | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Ifosfamide, disease=female breast carcinoma | success | 8 |  |
| 4 | ictrp | 2026-03-09 | drug=Ifosfamide, disease=female breast carcinoma | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Ifosfamide, disease=female breast carcinoma | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Ifosfamide, disease=unclassified myelodysplastic syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Ifosfamide, disease=unclassified myelodysplastic syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Ifosfamide, disease=unclassified myelodysplastic syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Ifosfamide, disease=partial deletion of the long arm of chromosome 5 | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Ifosfamide, disease=partial deletion of the long arm of chromosome 5 | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Ifosfamide, disease=partial deletion of the long arm of chromosome 5 | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Ifosfamide, disease=refractory cytopenia of childhood | success | 1 |  |
| 13 | ictrp | 2026-03-09 | drug=Ifosfamide, disease=refractory cytopenia of childhood | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Ifosfamide, disease=refractory cytopenia of childhood | success | 1 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Ifosfamide, disease=severe congenital hypochromic anemia with ringed sideroblasts | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Ifosfamide, disease=severe congenital hypochromic anemia with ringed sideroblasts | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Ifosfamide, disease=severe congenital hypochromic anemia with ringed sideroblasts | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Ifosfamide, disease=aregenerative anemia | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Ifosfamide, disease=aregenerative anemia | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Ifosfamide, disease=aregenerative anemia | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Ifosfamide, disease=rhabdomyosarcoma (disease) | success | 34 |  |
| 22 | ictrp | 2026-03-09 | drug=Ifosfamide, disease=rhabdomyosarcoma (disease) | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Ifosfamide, disease=rhabdomyosarcoma (disease) | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Ifosfamide, disease=myelodysplastic syndrome | success | 4 |  |
| 25 | ictrp | 2026-03-09 | drug=Ifosfamide, disease=myelodysplastic syndrome | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Ifosfamide, disease=myelodysplastic syndrome | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Ifosfamide, disease=monocytic leukemia | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Ifosfamide, disease=monocytic leukemia | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Ifosfamide, disease=monocytic leukemia | success | 3 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Ifosfamide, disease=botryoid-type embryonal rhabdomyosarcoma of the vagina | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Ifosfamide, disease=botryoid-type embryonal rhabdomyosarcoma of the vagina | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Ifosfamide, disease=botryoid-type embryonal rhabdomyosarcoma of the vagina | success | 1 |  |