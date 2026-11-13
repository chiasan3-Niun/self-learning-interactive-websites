
## 族語語音合成前置確認

需要族語語音時，先進入[族語 AI 語音合成系統](https://ai-labs.i---
name: self-learning-interactive-websites
description: Use when a learner wants an agent to turn source text and supplied media into an independent interactive learning website, including flashcards, audio, image-based exercises, game levels, asset processing, testing, and deployment.
---

# 自學互動式網站

把教材原始資料轉成可自學的互動式網站。使用者提供文本、圖片、語音來源與教學目標；agent 負責資料整理、資產處理、網站製作、測試與部署準備。

## 先讀取

開始前讀取：

- [workflow.md](references/workflow.md)：完整工作流程與輸出格式。
- [prompt-template.md](references/prompt-template.md)：使用者可直接複製的提示詞。
- [example-luanqun-animal-flashcards.md](references/example-luanqun-animal-flashcards.md)：巒群布農語動物閃卡案例。

## 核心規則

1. 先掃描文件、圖片、音檔與既有專案，再提出資料清單與不確定事項。
2. 保留原始語言拼寫、方言與翻譯來源；不自行猜測或改寫不確定內容。
3. 原始圖片不可覆寫。需要測驗用圖片時，輸出到獨立的衍生素材目錄。
4. 不要求使用者預先命名音檔、建立資料夾或生成第二套圖片；這些由 agent 處理。
5. 若語音網站沒有可用 API，依網站允許的方式取得音檔；不能假裝音檔已產生，也不能繞過登入、驗證或下載限制。
6. 閃卡、測驗、遊戲關卡與部署設定要依使用者需求建立成獨立專案，不要自動併入其他既有網站。
7. 上傳素材、登入服務、公開部署或傳送私人資料前，先取得使用者對該特定目的的確認。
8. 完成前執行資產檢查、功能測試與手機／電腦版面檢查；測試失敗時先修正再回報。

## 可攜式腳本

從 skill 根目錄執行：

```text
python scripts/scan_assets.py <素材目錄> --output <asset-inventory.json>
python scripts/build_manifest.py <內容資料.json> --output <manifest.json>
python scripts/crop_images.py --input <圖片目錄> --output <衍生圖片目錄> --crop-map <crop-map.json>
python scripts/validate_assets.py --manifest <manifest.json> --root <專案目錄>
python scripts/run_site_checks.py <網站目錄>
```

腳本是輔助工具，不取代 agent 對族語內容、圖片對應、互動設計與部署權限的判斷。

## 完成回報

回報必須分開說明：

- 已讀取與已確認的教材資料。
- 已建立的頁面、功能與資產。
- 測試命令與結果。
- 尚未確認的族語、圖片或音檔問題。
- 是否已部署；若已部署，提供已驗證的網址；若未部署，說明需要的授權或使用者動作。
