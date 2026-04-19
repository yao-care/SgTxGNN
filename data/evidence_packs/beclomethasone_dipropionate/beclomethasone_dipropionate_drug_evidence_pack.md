# Beclomethasone dipropionate 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Beclomethasone dipropionate | |
| DrugBank ID | DB00394 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | atopic eczema | 99.41% | L2 | 0 | 18 | S2 | Proceed with Guardrails |
| 2 | bronchitis | 98.68% | L1 | 6 | 20 | S3 | Proceed with Guardrails |
| 3 | 2-hydroxyethyl methacrylate sensitization | 97.05% | L5 | 0 | 0 | S0 | Hold |
| 4 | polyp of vocal cord | 92.37% | L5 | 0 | 0 | S0 | Hold |
| 5 | polyp of middle ear | 92.29% | L5 | 0 | 1 | S0 | Hold |
| 6 | fibroepithelial polyp | 92.10% | L5 | 0 | 0 | S0 | Hold |
| 7 | uterine polyp | 92.03% | L5 | 0 | 0 | S0 | Hold |
| 8 | polyp of frontal sinus | 92.01% | L4 | 0 | 1 | S1 | Research Question |
| 9 | seborrheic dermatitis | 92.00% | L4 | 0 | 2 | S1 | Research Question |
| 10 | polyp of ureter | 91.97% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Beclomethasone dipropionate | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Beclomethasone dipropionate | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Beclomethasone dipropionate, disease=atopic eczema | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Beclomethasone dipropionate, disease=atopic eczema | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Beclomethasone dipropionate, disease=atopic eczema | success | 18 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Beclomethasone dipropionate, disease=bronchitis | success | 6 |  |
| 7 | ictrp | 2026-03-10 | drug=Beclomethasone dipropionate, disease=bronchitis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Beclomethasone dipropionate, disease=bronchitis | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Beclomethasone dipropionate, disease=2-hydroxyethyl methacrylate sensitization | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Beclomethasone dipropionate, disease=2-hydroxyethyl methacrylate sensitization | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Beclomethasone dipropionate, disease=2-hydroxyethyl methacrylate sensitization | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Beclomethasone dipropionate, disease=polyp of vocal cord | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Beclomethasone dipropionate, disease=polyp of vocal cord | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Beclomethasone dipropionate, disease=polyp of vocal cord | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Beclomethasone dipropionate, disease=polyp of middle ear | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Beclomethasone dipropionate, disease=polyp of middle ear | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Beclomethasone dipropionate, disease=polyp of middle ear | success | 1 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Beclomethasone dipropionate, disease=fibroepithelial polyp | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Beclomethasone dipropionate, disease=fibroepithelial polyp | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Beclomethasone dipropionate, disease=fibroepithelial polyp | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Beclomethasone dipropionate, disease=uterine polyp | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Beclomethasone dipropionate, disease=uterine polyp | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Beclomethasone dipropionate, disease=uterine polyp | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Beclomethasone dipropionate, disease=polyp of frontal sinus | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Beclomethasone dipropionate, disease=polyp of frontal sinus | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Beclomethasone dipropionate, disease=polyp of frontal sinus | success | 1 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Beclomethasone dipropionate, disease=seborrheic dermatitis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Beclomethasone dipropionate, disease=seborrheic dermatitis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Beclomethasone dipropionate, disease=seborrheic dermatitis | success | 2 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Beclomethasone dipropionate, disease=polyp of ureter | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Beclomethasone dipropionate, disease=polyp of ureter | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Beclomethasone dipropionate, disease=polyp of ureter | success | 0 |  |