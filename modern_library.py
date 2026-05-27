import os
import json

# 取得目前程式碼所在的資料夾絕對路徑，確保 books.json 永遠與程式碼在同一層
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "books.json")

class Library:
    def __init__(self, filename=FILE_NAME):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        """讀取 JSON 格式的書籍資料，並確保安全關閉檔案"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"讀取檔案失敗: {e}")
                return []
        return []

    def save_books(self):
        """將書籍資料儲存為 JSON 格式，並確保安全關閉檔案"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.books, f, ensure_ascii=False, indent=2)

    def is_isbn_duplicate(self, isbn):
        """檢查 ISBN 是否已存在"""
        for book in self.books:
            if book['isbn'] == isbn:
                return True
        return False

    def add_book(self, title, isbn, status):
        if not self.is_isbn_duplicate(isbn):
            self.books.append({"title": title, "isbn": isbn, "status": status})
            self.save_books()  # 新增成功後自動存檔
            print("Success")
        else:
            print("ISBN Exist")

    def show_books(self):
        if not self.books:
            print("目前系統中沒有書籍。")
            return
        for book in self.books:
            print(f"書名: {book['title']}, ISBN: {book['isbn']}, 狀態: {book['status']}")

    def borrow_book(self, isbn):
        """借書功能：檢查書籍是否存在且尚未被借出"""
        for book in self.books:
            if book['isbn'] == isbn:
                if book['status'] == "borrowed":
                    print("Book is already borrowed")
                else:
                    book['status'] = "borrowed"
                    self.save_books()  # 借閱成功後自動存檔
                    print("Updated")
                return
        print("Book not found")

    def return_book(self, isbn):
        """還書功能：修補原先缺乏還書機制的邏輯漏洞"""
        for book in self.books:
            if book['isbn'] == isbn:
                if book['status'] != "borrowed":
                    print("Book is not borrowed")
                else:
                    book['status'] = "available"
                    self.save_books()  # 還書成功後自動存檔
                    print("Updated")
                return
        print("Book not found")


def main():
    library = Library()
    print("=== 圖書管理系統 v1.0 (Modern) ===")
    
    while True:
        op = input("> ").strip()
        
        if op == "exit":
            library.save_books()
            print("系統關閉")
            break
            
        elif op.startswith("add "):
            raw = op[4:].split("/")
            if len(raw) == 3:
                library.add_book(raw[0], raw[1], raw[2])
            else:
                print("Format Error")
                
        elif op == "show":
            library.show_books()
            
        elif op.startswith("borrow "):
            target_isbn = op[7:].strip()
            library.borrow_book(target_isbn)
            
        elif op.startswith("return "):
            target_isbn = op[7:].strip()
            library.return_book(target_isbn)
            
        else:
            print("Unknown Command")

if __name__ == "__main__":
    main()