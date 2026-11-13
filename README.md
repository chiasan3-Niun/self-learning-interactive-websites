# 自學互動式網站

這是一個可安裝到 Codex 或 Claude Code 的 skill。它會把教材文本與媒體素材轉成獨立的互動式學習網站。

## 重要區分

安裝 skill 與建立網站專案是兩件事：

- 安裝 skill：把本 repository 的 skill 放入 agent 可讀取的 skills 目錄。
- 建立網站：使用者只要指定專案位置，agent 會自行在該專案內建立「自學互動式網站」資料夾，不要求使用者先建立。

## Codex 安裝

若使用 Codex skill installer，直接從 GitHub 安裝：

https://github.com/chiasan3-Niun/self-learning-interactive-websites

若手動安裝，才需要把 repository 放到 Codex 的 skills 目錄；CODEX_HOME 未設定不代表不能建立網站專案。

## Claude Code 安裝

將 repository 的 skill 目錄放到 ~/.claude/skills/self-learning-interactive-websites，或支援的 ~/.agents/skills/ 共用目錄。

## 使用方式

提供專案位置，例如：

請在 C:\我的專案 製作網站。請自動建立「自學互動式網站」資料夾，把網站、DESIGN.md、素材、授權紀錄與測試都放進去；不要要求我先建立資料夾。

Agent 會自行建立並使用：

- 自學互動式網站/DESIGN.md
- 自學互動式網站/source/
- 自學互動式網站/assets/
- 自學互動式網站/ 內的網站程式與測試

## 參考案例

- https://luanqun-bunun-animal-flashcards.netlify.app/index.html
- https://luanqun-bunun-animal-flashcards.netlify.app/quiz

此案例僅供設計與互動參考，不會同步到新專案。
