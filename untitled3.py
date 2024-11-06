# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lS1yaVxn1cgtDf5rWFeaFWEzZCBvtaGa
"""

import pandas as pd
baza={

    "FISH": [
        "Aliyev Alisher",
        "Karimova Nilufar",
        "Nazarov Bekzod",
        "Saidova Kamola",
        "Ismailov Ibrohim",
        "Jabborova Laylo",
        "Rasulov Sanjar",
        "G'aniyeva Mohira",
        "Yusupov Temur",
        "Yoqubova Madina"
    ],
    "YOSHI": [15, 16, 14, 17, 15, 16, 14, 15, 16, 17],
    "MAKTABI": [
        "1-maktab",
        "2-maktab",
        "3-maktab",
        "4-maktab",
        "5-maktab",
        "6-maktab",
        "7-maktab",
        "8-maktab",
        "9-maktab",
        "10-maktab"
    ],
    "JINSI": ["Erkak", "Ayol", "Erkak", "Ayol", "Erkak", "Ayol", "Erkak", "Ayol", "Erkak", "Ayol"],
    "MANZILI": [
        "Toshkent, Chilonzor tumani",
        "Toshkent, Yunusobod tumani",
        "Toshkent, Sergeli tumani",
        "Toshkent, Yakkasaroy tumani",
        "Toshkent, Mirobod tumani",
        "Toshkent, Mirzo Ulug'bek tumani",
        "Toshkent, Shayxontohur tumani",
        "Toshkent, Uchtepa tumani",
        "Toshkent, Olmazor tumani",
        "Toshkent, Bektemir tumani"
    ]


}
df=pd.DataFrame (baza)
print(df)

filtr=df[df['JINSI']=="Ayol"]
print(filtr)

filtr=df[df['JINSI']=="Erkak"]
print(filtr)