# 利用清單儲存分類
Words = {
    "n.": [],
    "v.": [],
    "adj.": [],
    "adv.": []
    }
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
    "Others": Others
}

# 將資料讀取
with open("import.txt", "r") as f:
    content = f.read()

for line in content.split("\n"):
    # 如果含有以下詞性，將他視為單詞
    if "(n.)" in line or "(v.)" in line or "(adj.)" in line or "(adv.)" in line:
        # 如果含有空格，將他視為句子
        if " " in line.split('(')[0]:
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
    # 如果不含以下詞性，將他視為句子
    elif "=" in line or "A" in line or "B" in line or "sb." in line or "sth." in line or not line.endswith("."):
        Phrases.append(line)

    elif line.endswith('.'):
        Sentences.append(line)
    else:
      Others.append(line)

# 將資料寫入檔案並詢問是否排序
with open("export.txt", "w") as f:
    if input("要按字母順序嗎y/n ").lower() == 'y':
      for i in Words:
         Words[i].sort()
      Phrases.sort()
      Sentences.sort()
    # 將索引中的每個清單寫入檔案並加上換行
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
    