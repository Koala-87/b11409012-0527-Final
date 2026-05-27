# 台科大資管 Python 考試作答區

---

## 基本資料

**學號：** B11409012  
**系級：** 資管系大一  
**姓名：** 吳偉彬  

---

## 一、 原始碼分析報告 (Static Analysis) (共8小題，每小題3分，總共24分)

### 1.1 變數與邏輯對照表

| 原始變數名稱 | 代表意義 (Business Logic) | 建議修正名稱 |
|---|---|---|
| Q1 l1 (in load_proc) | 從檔案讀取的內容（未處理的原始書籍資料行陣列） | `lines` 或 `raw_lines` |
| Q2 d2 (in main) | 系統中存放所有書籍資料的記憶體清單（串列） | `books` 或 `book_list` |
| Q3 c_res (in check) | 檢查特定的 ISBN 是否已經存在於系統中 | `check_isbn_exists` 或 `is_isbn_duplicate` |

### 1.2 壞味道 (Code Smells) 診斷

請列出原程式碼中至少 5 個嚴重的設計問題，並說明為什麼不好：

- **Q1：** 變數命名缺乏語意 (Magic Names)，當變數名稱（如 `d2`, `c_res`, `l1`）無法反映其業務邏輯時，會大幅增加後續維護與閱讀程式碼的困難度。
- **Q2：** 檔案處理未確保安全關閉 (Resource Leak)，當發生例外錯誤時（例如讀取或寫入時出錯），`f.close()` 不會被執行，導致檔案資源被鎖死。應改用 `with open(...)` 語法。
- **Q3：** 脆弱的自訂資料儲存格式 (Brittle Data Format)，當書名或狀態中剛好包含分隔符號 `@@` 或 `##` 時，會導致下次啟動程式分割字串失敗並崩潰。應改用 JSON 格式。
- **Q4：** 業務邏輯漏洞 (Logical Flaws)，當使用者執行 `borrow` 借書時，程式未檢查該書是否「已經借出」，導致同本書可以被重複借閱；且系統缺乏對應的還書功能。
- **Q5：** 過度依賴全域變數 (Global State)，當多個函式（如 `load_proc`, `c_res`, `main`）都直接存取並修改全域變數 `d2` 時，會造成模組間高度耦合，難以進行單元測試與功能擴展。

---

## 二、 Vibe-Coding 協作紀錄 (共6小題，每小題3分，總共18分)

請記錄你如何引導 GitHub Copilot 進行重構。
重構的要求，請根據題目卷以及你發現的 Code Smells 來進行。

### 2.1 關鍵 Prompt 紀錄

請貼出你對 AI 下達過最有效的 3 個 Prompt：

```log
Prompt A：幫我詳細分析程式碼功能及如何測試

Prompt B：幫我依照剛剛找到的5大壞味道修改並且重購整份程式碼

Prompt C：請幫我修正最後程式碼不會將記錄存入book.json的問題
```

### 2.2 AI 錯誤處理

1. AI 在撰寫過程中是否有出錯？（例如：漏寫了某個功能、語法錯誤）你是如何發現並請它修正的？
有的，AI並沒有成功建立json檔案來存取紀錄。
重複測試時發現紀錄並無被保存。

2. 發現的問題： (範例：AI 漏掉了 exit 時要印出分類統計的功能)
AI忽略要建立json的部分

3. 修正的對話： (範例：我告訴它「請在結束前迴圈遍歷 JSON 資料並計算分類總額」)
我問:請問jason檔案存在哪裡了，重開程式碼紀錄都沒有保存?
---

## 三、 成果驗證與測試  (共2小題，每小題10分，總共20分)

確保你的 `modern_library.py` 功能正確。

### 3.1 測試結果驗證 (Terminal)

請貼上執行程式並輸入 show 後，顯示資料清單。(請從呼叫執行程式到結束程式完整的把操作對話複製到下框)

```log
> python modern_library.py
=== 圖書管理系統 v1.0 (Modern) ===
> add 寫給邊緣人的Python/978986502/available
Success
> show
書名: 寫給邊緣人的Python, ISBN: 978986502, 狀態: available
> borrow 978986502
Updated
> exit
系統關閉

```

### 3.2 產出的資料檔案格式

請貼上重構後生成的 `books.json` 前幾行內容：

```json
[
  {
    "title": "寫給邊緣人的Python",
    "isbn": "978986502",
    "status": "borrowed"
  },
  {
    "title": "早安老師",
    "isbn": "12345679",
    "status": "available"
  },
  {
    "title": "午安老師",
    "isbn": "123654",
    "status": "borrowed"
  }
]
```

---

## 四、 Git 提交紀錄 (Commit History)  (共2小題，總共13分)

### 4.1. 請執行 `git log --oneline` 並將 Commit 紀錄貼在此處，以證明你的開發流程(此小題6分)


```log
# 請在此處貼上 git log 內容
bcb77d9 (HEAD -> main, origin/main) AnswerUpdate
6fa86de Quiz_programTest
61f619a Quiz V1.0
```

### 4.2. GitHub Repository 連結(此小題7分)

將專案推送到 GitHub (Public) 若提交到 Private 連結不給分。 請設定 Repository 名稱為 `學號-0527-Final` Ex: B11526748-0527-Final **請用 - 不是 _**

```log
https://github.com/Koala-87/b11409012-0527-Final.git
```

希望這兩份 Markdown 格式能幫你省下不少排版時間！祝你的考試順利舉行！

最後請保留整份專案資料夾歐！
