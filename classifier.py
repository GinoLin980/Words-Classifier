import csv, openpyxl
import pandas as pd

max_len = 0

# 利用清單儲存分類
Words = {"n.": [], "v.": [], "adj.": [], "adv.": []}
Idioms = []
Phrases = []
Sentences = []
Others = []

# 將各個清單組成索引以利後面的輸出
index = {
    "Words": Words,
    "Idioms": Idioms,
    "Phrases": Phrases,
    "Sentences": Sentences,
    "Others": Others,
}

def check_repeated():
    global max_len
    with open('./unprocessed/unprocessed.txt', mode='r', encoding='utf-8') as f:
        processed = []
        write = []
        repeated = []

        lines = f.readlines()
        lines = [x.replace('\n', '') for x in lines]
        for index, line in enumerate(lines):
            if '(' in line:
                line = line.split('(')[0]
                if line not in processed:
                    processed.append(line)
                    write.append(lines[index])
                else:
                    repeated.append(f"第{index+1}行 {lines[index]}")
                    continue    
            elif line in processed:
                repeated.append(f"第{index+1}行 {lines[index]}")
                continue
            else:
                processed.append(line)
                write.append(lines[index])

        with open('./import/import.txt', mode='w', encoding='utf-8') as f2:
            for line in write:
                f2.write(line)
                # 如果不是最後一行，則換行。
                if line is not write[-1]:
                    f2.write('\n')
            with open('./export/repeated.txt', 'w', encoding='utf-8') as f3:
                f3.write("在'unprocessed.txt' 重複出現的字詞：\n\n")
                for line in repeated:
                    f3.write(line)
                    f3.write('\n')
        max_len = len(max(write, key=len)) + 20 if len(max(write, key=len)) > 30 else 15

def classifier():
    global Words, Idioms, Phrases, Sentences, Others
    
    # 將資料讀取
    with open("./import/import.txt", "r", encoding='utf-8') as f:
        content = f.read()
        # 將資料分類，並將資料儲存至各個清單中。
        for line in content.split("\n"):
            # 如果含有以下詞性，將他視為單詞或成語
            if "(n.)" in line or "(v.)" in line or "(adj.)" in line or "(adv.)" in line:
                # 如果含有空格，將他視為成語
                if " " in line.split("(")[0]:
                    Idioms.append(line)
                    continue
                # 將詞性儲存至清單中，並將詞性後面的詞儲存至對應清單中。
                if "(n.)" in line:
                    Words["n."].append(line)
                elif "(v.)" in line:
                    Words["v."].append(line)
                elif "(adj.)" in line:
                    Words["adj."].append(line)
                elif "(adv.)" in line:
                    Words["adv."].append(line)
            # 如果包含以下詞性，將他視為短語
            elif (
                "=" in line
                or "A" in line
                or "B" in line
                or "sb." in line
                or "sth." in line
                or not line.endswith(".")
            ):
                Phrases.append(line)
            # 如果是以句點為結尾，將他視為句子。
            elif line.endswith("."):
                Sentences.append(line)
                
            else:
                Others.append(line)

def if_sort_and_export():
    # 將資料寫入檔案並詢問是否排序
    with open("./export/export.txt", "w", encoding='utf-8') as f:
        if input("要按字母順序嗎(y/n) ").lower() == "y":
            for i in Words:
                Words[i].sort()
            Idioms.sort()
            Phrases.sort()
            Sentences.sort()
            Others.sort()
            
        # 將索引中的每個清單寫入純文本並加上換行
        for name, value in index.items():
            f.write(f"{name}:\n")
            if name == "Words":
                f.write("\n")
                for part, value in value.items():
                    f.write(f"{part}:\n")
                    f.write("\n".join(value))
                    f.write("\n\n")
            else:
                f.write("\n".join(value))
                f.write("\n\n")
            
def write_CSV():
    headers = ["Words", "Idioms", "Phrases", "Sentences", "Others"]
    vocabulary = ["n.", "v.", "adj.", "adv."]
    # 針對CSV的資料處理
    data = []
    for i in range(
        max(len(Words["n."]),
            len(Words["v."]),
            len(Words["adj."]),
            len(Words["adv."]),
            len(Idioms),
            len(Phrases),
            len(Sentences),
            len(Others))
    ):
        row = []
        for category in headers:
            if category == "Words":
                for part in vocabulary:
                    row.append(Words[part][i] if i < len(Words[part]) else "")
            else:
                row.append(index[category][i] if i < len(index[category]) else "")
        data.append(row)

    # 寫入CSV
    headers = ["Words", " ", "  ", "   ", "Idioms", "Phrases", "Sentences", "Others"]
    with open("./export/export.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerow(vocabulary)
        writer.writerows(data)
        
def xlsx_convert():
    # 利用Pandas來轉換資料格式
    data = pd.read_csv("./export/export.csv").to_excel("./export/export.xlsx", index=False)

    # 載入Excel檔案
    wb = openpyxl.load_workbook('./export/export.xlsx')
    ws = wb.active

    # 設定寬度
    for col in ['A', 'B', 'C','D', 'E', 'F', 'G', 'H']:
        ws.column_dimensions[col].width = max_len
    # 設定字體大小
    for row in ws.iter_rows():
        for cell in row:
            cell.font = openpyxl.styles.Font(size=16)
    # 保存
    wb.save('./export/export.xlsx')

def main():
    print('檢查是否重複...')
    check_repeated()
    print('分類...')
    classifier()
    if_sort_and_export()
    print('輸出...')
    write_CSV()
    xlsx_convert()
    
main()