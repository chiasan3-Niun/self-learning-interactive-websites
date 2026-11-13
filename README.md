# 自學互動式網站

這是一個可安裝到 Codex 或 Claude Code 的 skill。它把教材文本與使用者提供的媒體素材，轉成獨立的互動式學習網站。

## GitHub 安裝

將此資料夾放入 GitHub 後，使用者可以下載：

```bash
git clone https://github.com/<你的帳號>/<你的儲存庫>.git
```

### Codex

把 skill 資料夾複製到 Codex 可讀取的 skills 目錄，例如：

```powershell
Copy-Item -Recurse .\自學互動式網站 "$env:CODEX_HOME\skills\self-learning-interactive-websites"
```

若環境沒有設定 `CODEX_HOME`，請依 Codex 的 skills 目錄設定放置；skill 目錄名稱使用 `self-learning-interactive-websites`。

### Claude Code

把資料夾複製到 Claude Code 的個人 skills 目錄：

```bash
cp -R 自學互動式網站 ~/.claude/skills/self-learning-interactive-websites
```

也可以放在支援的 `~/.agents/skills/` 共用目錄。

## 使用方式

安裝後，在對話中提供：

- 教材文本或文件
- 一組圖片或圖片資料夾
- 語音來源網站或語音需求
- 想要的學習活動，例如閃卡、聽音選圖、配對、拼圖或闖關

範例：

```text
請使用 self-learning-interactive-websites skill，將我提供的文本和圖片製作成獨立的互動式學習網站。請先讀取資料，再整理內容、處理圖片與音檔、製作網站、測試，最後在我確認後部署。
```

## 參考案例

巒群布農語動物閃卡：

- https://luanqun-bunun-animal-flashcards.netlify.app/index.html
- https://luanqun-bunun-animal-flashcards.netlify.app/quiz

案例包含單字閃卡、族語單字與例句播放、自動播放、角色選擇、冒險地圖與五個測驗關卡。它只是教學案例，不是新專案的同步目標。

## 權限提醒

Agent 可以先在本機整理與測試，但上傳教材到第三方服務、登入帳號、公開部署或傳送私人資料前，必須確認具體目的與目的地。
