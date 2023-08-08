import pandas as pd

data = [
    {'ชื่อ': 'สมชาย', 'ส่วนสูง': 185, 'เงินเดือน': 16000},
    {'ชื่อ': 'วีระชัย', 'ส่วนสูง': 175, 'เงินเดือน': 17500},
    {'ชื่อ': 'พรชัย', 'ส่วนสูง': 182, 'เงินเดือน': 20000},
    {'ชื่อ': 'วีระ', 'ส่วนสูง': 183, 'เงินเดือน': 19900}
]

df = pd.DataFrame(data)
print('--------------------------')
print(df)

person = ["สมศรี", "พิมพ์พร", "สุดใจ", "สมหญิง"]
height = [160, 166, 163, 168]
age = [25, 23, 27, 19]

data2 = {
    'ชื่อ': person,
    'ส่วนสูง': height,
    'อายุ': age
}

df2 = pd.DataFrame(data2)
print('-------------------------')
print(type(data2))
print(df2)