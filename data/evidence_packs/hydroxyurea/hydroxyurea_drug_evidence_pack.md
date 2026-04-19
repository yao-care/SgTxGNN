# Hydroxyurea 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Hydroxyurea | |
| DrugBank ID | DB01005 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | female breast carcinoma | 99.97% | L3 | 0 | 20 | S1 | Research Question |
| 2 | sickle cell-hemoglobin E disease syndrome | 99.67% | L3 | 4 | 1 | S2 | Proceed with Guardrails |
| 3 | hereditary persistence of fetal hemoglobin-sickle cell disease syndrome | 99.67% | L4 | 0 | 1 | S0 | Hold |
| 4 | sickle cell-hemoglobin c disease syndrome | 99.67% | L2 | 11 | 19 | S3 | Proceed with Guardrails |
| 5 | sickle cell-hemoglobin d disease syndrome | 99.67% | L3 | 4 | 2 | S1 | Research Question |
| 6 | sickle cell-beta-thalassemia disease syndrome | 99.67% | L3 | 4 | 2 | S2 | Proceed with Guardrails |
| 7 | cervical adenosarcoma | 99.40% | L5 | 0 | 0 | S0 | Hold |
| 8 | colon mucinous adenocarcinoma | 99.32% | L5 | 0 | 0 | S0 | Hold |
| 9 | rectum mucinous adenocarcinoma | 99.31% | L5 | 0 | 0 | S0 | Hold |
| 10 | gallbladder mucinous adenocarcinoma | 99.28% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Hydroxyurea | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Hydroxyurea | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Hydroxyurea, disease=female breast carcinoma | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Hydroxyurea, disease=female breast carcinoma | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Hydroxyurea, disease=female breast carcinoma | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Hydroxyurea, disease=sickle cell-hemoglobin E disease syndrome | success | 4 |  |
| 7 | ictrp | 2026-03-09 | drug=Hydroxyurea, disease=sickle cell-hemoglobin E disease syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Hydroxyurea, disease=sickle cell-hemoglobin E disease syndrome | success | 1 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Hydroxyurea, disease=hereditary persistence of fetal hemoglobin-sickle cell disease syndrome | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Hydroxyurea, disease=hereditary persistence of fetal hemoglobin-sickle cell disease syndrome | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Hydroxyurea, disease=hereditary persistence of fetal hemoglobin-sickle cell disease syndrome | success | 1 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Hydroxyurea, disease=sickle cell-hemoglobin c disease syndrome | success | 11 |  |
| 13 | ictrp | 2026-03-09 | drug=Hydroxyurea, disease=sickle cell-hemoglobin c disease syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Hydroxyurea, disease=sickle cell-hemoglobin c disease syndrome | success | 19 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Hydroxyurea, disease=sickle cell-hemoglobin d disease syndrome | success | 4 |  |
| 16 | ictrp | 2026-03-09 | drug=Hydroxyurea, disease=sickle cell-hemoglobin d disease syndrome | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Hydroxyurea, disease=sickle cell-hemoglobin d disease syndrome | success | 2 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Hydroxyurea, disease=sickle cell-beta-thalassemia disease syndrome | success | 4 |  |
| 19 | ictrp | 2026-03-09 | drug=Hydroxyurea, disease=sickle cell-beta-thalassemia disease syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Hydroxyurea, disease=sickle cell-beta-thalassemia disease syndrome | success | 2 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Hydroxyurea, disease=cervical adenosarcoma | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Hydroxyurea, disease=cervical adenosarcoma | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Hydroxyurea, disease=cervical adenosarcoma | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Hydroxyurea, disease=colon mucinous adenocarcinoma | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Hydroxyurea, disease=colon mucinous adenocarcinoma | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Hydroxyurea, disease=colon mucinous adenocarcinoma | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Hydroxyurea, disease=rectum mucinous adenocarcinoma | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Hydroxyurea, disease=rectum mucinous adenocarcinoma | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Hydroxyurea, disease=rectum mucinous adenocarcinoma | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Hydroxyurea, disease=gallbladder mucinous adenocarcinoma | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Hydroxyurea, disease=gallbladder mucinous adenocarcinoma | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Hydroxyurea, disease=gallbladder mucinous adenocarcinoma | success | 0 |  |