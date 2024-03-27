def check_repeated():
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
                    repeated.append(f"{lines[index], index+1}")
                    continue    
            elif line in processed:
                repeated.append(f"{lines[index]} 第{index+1}行")
                continue
            else:
                processed.append(line)
                write.append(lines[index])

        with open('./import/import.txt', mode='w', encoding='utf-8') as f2:
            for line in write:
                f2.write(line)
                f2.write('\n')
            with open('./export/repeated.txt', 'w', encoding='utf-8') as f3:
                for line in repeated:
                    print("重複詞彙：")
                    print(line)
                    f3.write(line)
                    f3.write('\n')