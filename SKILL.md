---
name: self-learning-interactive-websites
description: Use when a learner wants an agent to turn source text and supplied media into an independent interactive learning website, including flashcards, audio, image-based exercises, game levels, asset processing, testing, and deployment.
---

# 自學互動式網站

把教材文本與媒體素材轉成獨立的互動式學習網站。使用者只需指定專案位置，資料夾與檔案由 agent 建立。

## 專案資料夾建立規則

使用者指定專案位置後，先在該專案根目錄自行建立名為「自學互動式網站」的資料夾。不要要求使用者預先建立資料夾，也不要要求使用者提供 skill 內部檔案名稱。網站原始碼、DESIGN.md、教材整理、圖片、音檔、授權紀錄、測試與部署設定都放進這個資料夾；原始教材可放在 source/，衍生素材放在 assets/。

## 必要前置步驟

建立資料夾後，必須在其中建立並讀取 DESIGN.md。依照 https://github.com/VoltAgent/awesome-design-md 的格式，定義色彩、字體、元件、間距、版面、陰影、響應式規則與互動狀態。沒有 DESIGN.md 不得直接用預設 CSS 製作網站。

開始前也讀取 skill 內的 references/workflow.md、references/prompt-template.md 與 references/example-luanqun-animal-flashcards.md；這些參考檔不需要複製到使用者專案。

## 核心規則

1. 先掃描文件、圖片、音檔與既有專案，列出資料與不確定事項。
2. 保留原始語言拼寫、方言與翻譯來源，不猜測不確定內容。
3. 原始圖片不可覆寫，衍生圖片輸出到獨立目錄。
4. 圖片優先使用 ChatGPT Image、Gemini、Canva 或其他免費生圖工具。使用者沒有付費方案時，不把付費服務列為必要條件；沒有生圖功能時，改用授權清楚的免費素材。
5. 每張圖片記錄生成工具或來源網址、日期、授權條款、署名要求與限制。授權不明、需要付費授權、含未授權人物／商標或直接抓取的圖片，不放入公開網站。
6. 族語語音使用 https://ai-labs.ilrdf.org.tw/hnang-kari-ai-asi-sluhay/。製作前先確認語言別與方言別，向使用者回報；不得自行猜測方言。
7. 每個有語音的項目都要有回報音檔錯誤與修改文字／備註入口。保留原音檔和錯誤紀錄，確認修改與方言後重新生成；新音檔播放及對應檢查通過後才設為目前版本。
8. 上傳素材、登入服務、公開部署或傳送私人資料前，先取得特定目的的確認；不繞過登入、驗證或下載限制。
9. 完成前執行資產、功能與手機／電腦版面檢查。

## 可攜式腳本

python scripts/scan_assets.py <素材目錄> --output <asset-inventory.json>
python scripts/build_manifest.py <內容資料.json> --output <manifest.json>
python scripts/validate_assets.py --manifest <manifest.json> --root <專案目錄>
python scripts/run_site_checks.py <網站目錄>

## 完成回報

說明專案資料夾位置、教材、DESIGN.md、圖片來源與授權、頁面功能、語言別／方言別、音檔版本、測試結果、未確認事項與部署狀態。
