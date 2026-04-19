# Dacarbazine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Dacarbazine | |
| DrugBank ID | DB00851 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | upper aerodigestive tract neoplasm | 99.26% | L4 | 1 | 20 | S1 | Research Question |
| 2 | small cell lung carcinoma | 98.81% | L3 | 42 | 20 | S2 | Research Question |
| 3 | primary pulmonary lymphoma | 98.64% | L2 | 12 | 20 | S2 | Proceed with Guardrails |
| 4 | well-differentiated fetal adenocarcinoma of the lung | 98.56% | L5 | 0 | 0 | S0 | Hold |
| 5 | pulmonary blastoma | 98.44% | L5 | 0 | 0 | S0 | Hold |
| 6 | breast papillomatosis | 98.38% | L5 | 0 | 0 | S0 | Hold |
| 7 | head and neck cancer | 98.36% | L3 | 11 | 20 | S2 | Proceed with Guardrails |
| 8 | salivary gland type cancer of the breast | 98.34% | L5 | 0 | 0 | S0 | Hold |
| 9 | adult astrocytic tumour | 98.28% | L4 | 2 | 20 | S1 | Research Question |
| 10 | breast lipoma | 98.26% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Dacarbazine | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Dacarbazine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Dacarbazine, disease=upper aerodigestive tract neoplasm | success | 1 |  |
| 4 | ictrp | 2026-03-10 | drug=Dacarbazine, disease=upper aerodigestive tract neoplasm | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Dacarbazine, disease=upper aerodigestive tract neoplasm | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Dacarbazine, disease=small cell lung carcinoma | success | 42 |  |
| 7 | ictrp | 2026-03-10 | drug=Dacarbazine, disease=small cell lung carcinoma | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Dacarbazine, disease=small cell lung carcinoma | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Dacarbazine, disease=primary pulmonary lymphoma | success | 12 |  |
| 10 | ictrp | 2026-03-10 | drug=Dacarbazine, disease=primary pulmonary lymphoma | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Dacarbazine, disease=primary pulmonary lymphoma | success | 20 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Dacarbazine, disease=well-differentiated fetal adenocarcinoma of the lung | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Dacarbazine, disease=well-differentiated fetal adenocarcinoma of the lung | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Dacarbazine, disease=well-differentiated fetal adenocarcinoma of the lung | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Dacarbazine, disease=pulmonary blastoma | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Dacarbazine, disease=pulmonary blastoma | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Dacarbazine, disease=pulmonary blastoma | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Dacarbazine, disease=breast papillomatosis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Dacarbazine, disease=breast papillomatosis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Dacarbazine, disease=breast papillomatosis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Dacarbazine, disease=head and neck cancer | success | 11 |  |
| 22 | ictrp | 2026-03-10 | drug=Dacarbazine, disease=head and neck cancer | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Dacarbazine, disease=head and neck cancer | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Dacarbazine, disease=salivary gland type cancer of the breast | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Dacarbazine, disease=salivary gland type cancer of the breast | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Dacarbazine, disease=salivary gland type cancer of the breast | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Dacarbazine, disease=adult astrocytic tumour | success | 2 |  |
| 28 | ictrp | 2026-03-10 | drug=Dacarbazine, disease=adult astrocytic tumour | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Dacarbazine, disease=adult astrocytic tumour | success | 20 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Dacarbazine, disease=breast lipoma | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Dacarbazine, disease=breast lipoma | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Dacarbazine, disease=breast lipoma | success | 0 |  |