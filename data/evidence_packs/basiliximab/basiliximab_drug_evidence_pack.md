# Basiliximab 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Basiliximab | |
| DrugBank ID | DB00074 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | plasma cell myeloma | 95.61% | L3 | 3 | 3 | S1 | Research Question |
| 2 | bronchitis | 95.54% | L3 | 1 | 7 | S1 | Research Question |
| 3 | indolent plasma cell myeloma | 95.29% | L5 | 0 | 0 | S0 | Hold |
| 4 | hemoglobinopathy | 94.28% | L2 | 2 | 1 | S2 | Proceed with Guardrails |
| 5 | gastric carcinoma | 93.89% | L5 | 0 | 0 | S0 | Hold |
| 6 | diffuse gastric adenocarcinoma | 93.75% | L5 | 0 | 0 | S0 | Hold |
| 7 | partial deletion of the short arm of chromosome 16 | 93.52% | L5 | 0 | 0 | S0 | Hold |
| 8 | beta-thalassemia with other manifestations | 93.29% | L4 | 0 | 0 | S0 | Research Question |
| 9 | hemolytic anemia due to glucophosphate isomerase deficiency | 92.93% | L5 | 0 | 0 | S0 | Hold |
| 10 | Jeune syndrome situs inversus | 92.86% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Basiliximab | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Basiliximab | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Basiliximab, disease=plasma cell myeloma | success | 3 |  |
| 4 | ictrp | 2026-03-10 | drug=Basiliximab, disease=plasma cell myeloma | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Basiliximab, disease=plasma cell myeloma | success | 3 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Basiliximab, disease=bronchitis | success | 1 |  |
| 7 | ictrp | 2026-03-10 | drug=Basiliximab, disease=bronchitis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Basiliximab, disease=bronchitis | success | 7 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Basiliximab, disease=indolent plasma cell myeloma | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Basiliximab, disease=indolent plasma cell myeloma | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Basiliximab, disease=indolent plasma cell myeloma | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Basiliximab, disease=hemoglobinopathy | success | 2 |  |
| 13 | ictrp | 2026-03-10 | drug=Basiliximab, disease=hemoglobinopathy | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Basiliximab, disease=hemoglobinopathy | success | 1 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Basiliximab, disease=gastric carcinoma | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Basiliximab, disease=gastric carcinoma | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Basiliximab, disease=gastric carcinoma | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Basiliximab, disease=diffuse gastric adenocarcinoma | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Basiliximab, disease=diffuse gastric adenocarcinoma | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Basiliximab, disease=diffuse gastric adenocarcinoma | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Basiliximab, disease=partial deletion of the short arm of chromosome 16 | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Basiliximab, disease=partial deletion of the short arm of chromosome 16 | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Basiliximab, disease=partial deletion of the short arm of chromosome 16 | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Basiliximab, disease=beta-thalassemia with other manifestations | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Basiliximab, disease=beta-thalassemia with other manifestations | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Basiliximab, disease=beta-thalassemia with other manifestations | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Basiliximab, disease=hemolytic anemia due to glucophosphate isomerase deficiency | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Basiliximab, disease=hemolytic anemia due to glucophosphate isomerase deficiency | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Basiliximab, disease=hemolytic anemia due to glucophosphate isomerase deficiency | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Basiliximab, disease=Jeune syndrome situs inversus | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Basiliximab, disease=Jeune syndrome situs inversus | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Basiliximab, disease=Jeune syndrome situs inversus | success | 0 |  |