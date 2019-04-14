import operator

alp = {}
ver = {}
coding = {}

lit = []
freq = []

count = 0

#поиск кода для буквы
def search_tree(code, full_code, start_pos, end_pos, fl):

    #если это не первое выхождение, работаем дальше. Иначе очистить историю
    if not fl:
        tmp_code = full_code + code
        fl = False
    else:
        tmp_code = ''

    #если прошлись по всему списку, то выход
    if start_pos == end_pos:
        print('{} = {}'.format(lit[start_pos], tmp_code))
        coding[lit[start_pos]] = coding.get(lit[start_pos], '') + tmp_code
        return 0

    #подсчет средней частоты встречи символов
    ds = 0
    for i in range(start_pos, end_pos):
        ds += freq[i]
    ds /= 2

    summ = 0
    i = start_pos
    m = i
    while summ + freq[i] < ds and i < end_pos:
        summ += freq[i]
        i += 1
        m += 1
    #рекурсия для левой ветки
    search_tree('0', tmp_code, start_pos, m, False)
    # рекурсия для правой ветки
    search_tree('1', tmp_code, m+1, end_pos, False)

#определение алфавита и вероятности
with open('text.txt', 'r', encoding='utf-8') as f:
    while True:
        st = f.readline()
        if not st:
            break
        for i in st.lower():
            if i.isalnum():
                alp[i] = alp.get(i, 0) + 1
                count += 1

#подсчет вероятности
for key in alp:
    ver[key] = alp[key]/count

#сортировка вероятности по убыванию
sorted_ver = sorted(ver.items(), key=operator.itemgetter(1), reverse=True)

#создание списков для упрощенной работы
for key, value in sorted_ver:
    lit.append(key)
    freq.append(value)
    print("{}: {}".format(key, value))

print(lit, freq)

search_tree(' ', ' ', 0, len(lit)-1, True) #len - 1 т.к. нужно передать позицию, а не длину

print(coding)