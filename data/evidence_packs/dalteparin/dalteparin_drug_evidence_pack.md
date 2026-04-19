# Dalteparin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Dalteparin | |
| DrugBank ID | DB06779 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | thrombophilia due to protein C deficiency, autosomal recessive | 99.88% | L4 | 0 | 0 | S1 | Research Question |
| 2 | primary release disorder of platelets | 99.67% | L5 | 14 | 0 | S0 | Hold |
| 3 | pseudo-von Willebrand disease | 99.52% | L5 | 0 | 0 | S0 | Hold |
| 4 | atypical hemolytic-uremic syndrome with thrombomodulin anomaly | 99.34% | L5 | 0 | 0 | S0 | Research Question |
| 5 | neuropathy, painful | 99.19% | L3 | 3 | 0 | S1 | Research Question |
| 6 | thrombotic thrombocytopenic purpura | 98.09% | L5 | 0 | 0 | S0 | Hold |
| 7 | retinal telangiectasia | 95.54% | L4 | 0 | 1 | S0 | Research Question |
| 8 | retinal microaneurysm | 95.19% | L5 | 0 | 0 | S0 | Hold |
| 9 | arteriosclerotic retinopathy | 95.19% | L5 | 0 | 0 | S0 | Hold |
| 10 | vertebral artery occlusion | 94.96% | L4 | 0 | 1 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Dalteparin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Dalteparin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Dalteparin, disease=thrombophilia due to protein C deficiency, autosomal recessive | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Dalteparin, disease=thrombophilia due to protein C deficiency, autosomal recessive | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Dalteparin, disease=thrombophilia due to protein C deficiency, autosomal recessive | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Dalteparin, disease=primary release disorder of platelets | success | 14 |  |
| 7 | ictrp | 2026-03-09 | drug=Dalteparin, disease=primary release disorder of platelets | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Dalteparin, disease=primary release disorder of platelets | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Dalteparin, disease=pseudo-von Willebrand disease | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Dalteparin, disease=pseudo-von Willebrand disease | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Dalteparin, disease=pseudo-von Willebrand disease | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Dalteparin, disease=atypical hemolytic-uremic syndrome with thrombomodulin anomaly | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Dalteparin, disease=atypical hemolytic-uremic syndrome with thrombomodulin anomaly | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Dalteparin, disease=atypical hemolytic-uremic syndrome with thrombomodulin anomaly | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Dalteparin, disease=neuropathy, painful | success | 3 |  |
| 16 | ictrp | 2026-03-09 | drug=Dalteparin, disease=neuropathy, painful | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Dalteparin, disease=neuropathy, painful | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Dalteparin, disease=thrombotic thrombocytopenic purpura | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Dalteparin, disease=thrombotic thrombocytopenic purpura | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Dalteparin, disease=thrombotic thrombocytopenic purpura | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Dalteparin, disease=retinal telangiectasia | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Dalteparin, disease=retinal telangiectasia | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Dalteparin, disease=retinal telangiectasia | success | 1 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Dalteparin, disease=retinal microaneurysm | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Dalteparin, disease=retinal microaneurysm | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Dalteparin, disease=retinal microaneurysm | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Dalteparin, disease=arteriosclerotic retinopathy | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Dalteparin, disease=arteriosclerotic retinopathy | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Dalteparin, disease=arteriosclerotic retinopathy | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Dalteparin, disease=vertebral artery occlusion | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Dalteparin, disease=vertebral artery occlusion | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Dalteparin, disease=vertebral artery occlusion | success | 1 |  |