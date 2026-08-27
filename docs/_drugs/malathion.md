---
layout: default
title: Malathion
parent: 僅模型預測 (L5)
nav_order: 627
evidence_level: L5
indication_count: 10
---

# Malathion
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Malathion：從頭蝨／疥瘡外用殺蟲劑到脂漏性角化病（Seborrheic Keratosis）預測

## 一句話摘要

Malathion 是一種有機磷酸酯類乙醯膽鹼酯酶抑制劑，目前已知的臨床用途為外用殺蟲劑，用於治療頭蝨（pediculosis capitis）及疥瘡（scabies）感染。TxGNN 模型預測其可能對**脂漏性角化病（Seborrheic Keratosis）**有效，但目前**沒有任何臨床試驗**、**沒有任何相關文獻**支持此方向，且證據包本身的機轉分析亦指出兩者間**無合理生物學連結**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 台灣藥政資料（`taiwan_regulatory.licenses`）無記錄、藥品未上市；依已知藥理用途，Malathion 為外用殺蟲劑，臨床上用於頭蝨與疥瘡之殺蟲/殺疥蟎治療 |
| 預測新適應症 | Seborrheic Keratosis（脂漏性角化病） |
| TxGNN 預測分數 | 96.45% |
| 證據等級 | L5（僅模型預測，無臨床試驗或文獻佐證） |
| 台灣市場狀態 | 未上市 |
| 登記證數量 | 0 |
| 建議決策 | Hold（暫緩） |

---

## 為什麼此預測合理？

目前尚無正式的作用機轉（MOA）資料可供查詢（`original_moa` 為資料缺口，優先級 High）。根據已知藥理資訊，Malathion 是一種有機磷酸酯類化合物，透過抑制乙醯膽鹼酯酶（AChE）達到殺蟲效果，臨床上作為外用製劑用於頭蝨與疥瘡感染的治療。

然而，就此次預測的目標適應症「脂漏性角化病」而言，證據包內附的機轉分析明確指出：脂漏性角化病是一種良性表皮增生性病變，其病理機轉主要與 FGFR3、PIK3CA 等基因突變及角質細胞增生相關，**與 AChE 抑制或殺蟲活性之間並無已知的生物學關聯**。

換言之，此預測目前**缺乏機轉上的合理性**，較可能是知識圖譜中因節點鄰近效應（例如與其他角化性皮膚病變節點相近）所產生的關聯假影（artifact），而非具有藥理學基礎的真實再利用信號。這點在證據包中對排名第 2（vulvar inverted follicular keratosis）等後續候選適應症的分析中也重複出現，進一步支持此判斷。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

（查詢紀錄顯示，針對 Malathion + Seborrheic Keratosis 已分別查詢 ClinicalTrials.gov 與 ICTRP，兩者結果數皆為 0。）

---

## 文獻證據

目前無相關文獻可查。

（PubMed 查詢 Malathion + Seborrheic Keratosis 之組合，結果數為 0。）

> 補充說明：證據包中排名第 3 的候選適應症「脂漏性皮膚炎（seborrheic dermatitis）」查得 1 篇相關文獻（PMID: [24126752](https://pubmed.ncbi.nlm.nih.gov/24126752/)），但該文獻主題是疥瘡頭皮感染與脂漏性皮膚炎的**臨床表徵鑑別診斷**混淆案例，並非「Malathion 對脂漏性皮膚炎具治療效果」的機轉證據，故不構成本報告主標的（seborrheic keratosis）之支持文獻。

---

## 台灣上市資訊

Malathion 目前**未於台灣上市**，登記證數量為 0，`taiwan_regulatory.licenses` 無任何授權紀錄可供列表。

---

## 安全性考量

安全性資訊請參閱藥品仿單。

（目前 `key_warnings`、`contraindications` 及藥物交互作用（DDI）查詢均無可用資料；DDI 查詢狀態為「未查獲」。）

---

## 結論與後續建議

**決策：Hold（暫緩）**

**理由：**
- 排名第一之預測適應症（脂漏性角化病）目前**零臨床試驗、零文獻支持**，且證據包內部機轉分析已明確指出兩者間無已知生物學連結，判斷此分數可能來自知識圖譜節點鄰近效應而非真實藥理訊號。
- 證據等級為 L5（僅模型預測），為五級中最低等級。
- 藥品目前未於台灣上市（登記證數 = 0），且**仿單警語/禁忌資料缺失（DG001，Blocking 等級）**——此為安全性初評（S1）的前置條件，目前無法通過。

**若要繼續推進，需要補充：**
- TFDA 仿單警語與禁忌資料（DG001，Blocking，需下載並解析官方仿單 PDF）
- Malathion 完整作用機轉（MOA）資料（DG002，需查詢 DrugBank API）
- 針對脂漏性角化病此適應症的獨立體外／體內機轉研究，以驗證或推翻目前「無合理機轉」的初步判斷
- 若機轉驗證通過，需重新評估台灣/新加坡在地法規上市路徑可行性

---

*本報告排名第 2–10 之候選適應症（vulvar inverted follicular keratosis、seborrheic dermatitis、mycotic corneal ulcer、inherited skin tumor、anogenital HPV infection、breast fibrocystic disease、benign mammary dysplasia、blunt duct adenosis of breast、apocrine adenosis of breast）皆同屬 L5 證據等級、建議 Hold，且證據包機轉分析均指出無合理生物學連結或屬知識圖譜關聯假影，暫不予以個別展開。*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

