# Group 4 測試總結報告

此文件彙整 Group 4 所完成的 pytest 測試情況，涵蓋各 lecture 主題內容與測試重點。

---

## ✅ Lec3：字串處理與完美立方

- 覆蓋函式：`is_perfect_cube`, `cube_root`, `approx_cube_root`
- 測試重點：
  - 整數立方、負數立方根
  - 近似值誤差範圍控制
- 測試組數：9

---

## ✅ Lec4：函式設計與共通因數

- 覆蓋函式：`is_even_with_return`, `get_divisors`, `find_common_factors`, `get_multiplication_table`
- 測試組數：10+
- 涵蓋質數、倍數、最大公因數邊界等案例

---

## ✅ Lec5：tuple 資料結構與萃取分析

- 覆蓋函式：`quotient_and_remainder`, `get_data`
- 測試組數：10+
- 強調資料萃取與文字資料統計意義

---

## ✅ Lec6（V2）：遞迴與 dictionary 高品質測試

分兩個檔案進行，包含：

### Part 1：fib, is_palindrome
- 含多種遞迴測試、回文空字串與標點處理
- 使用高品質測試命名與 assert 分類

### Part 2：lyrics_to_frequencies, towers
- 歌詞字詞頻率計數，空詞與重複處理
- 河內塔 1~3 碟移動步驟驗證，遞迴紀錄正確性

---

## ✅ Lec7 ~ Lec12

皆已依照標準格式完成 pytest 測試，請見各 PR 詳述。

---

### 🎓 總結

- 使用 `pytest` 撰寫所有單元測試
- 所有測試通過，assert 覆蓋完整邊界情境
- 每份測試保持模組化、命名一致，方便後續維護與測試自動化擴充