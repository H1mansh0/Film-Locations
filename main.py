def file_reader(filename: str) -> list:
    res = []
    with open(filename, 'r') as file:
        data = file.readlines()[14:-1]
        for line in data:
            res += [(line[:-2].split(' (')[0] ,line[:-2].split(' (')[1][:4],
                                [ele for ele in line.replace('\n', '').split('\t')[1:] if ele][0])]
    return res
