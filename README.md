INSTALLATION:

1. .env file yarating va .env_example file dan nusxalang

2. kompyuteringizda dockerni ishga tushiring

3. docker-compose up --build   kommandas orqali proektni ihsga tushiring

4. docker-compose run --rm web python manage.py migrate  orqali modellarni databazada yarating

5. docker-compose run --rm web python manage.py createsuperuser orqali admin user yarating

NOTES:

yuborilgan exel filening ichidagi faqat 1-sheet ni o'qiydi 

sheet dagi column nomlari {"hisobot_code", "soato", "year", "indicator_code", "value"}  ko'rinishida to'g'ri yozilishi kerk

MISOL:
[
    {"hisobot_code":1,"soato":1700,"year":2023,"indicator_code":"101_1","value":0},
    {"hisobot_code":1,"soato":1735,"year":2023,"indicator_code":"101_1","value":0},
    {"hisobot_code":1,"soato":1735401,"year":2023,"indicator_code":"101_1","value":0},
    {"hisobot_code":1,"soato":1735204,"year":2023,"indicator_code":"101_1","value":0},
    {"hisobot_code":1,"soato":1735207,"year":2023,"indicator_code":"101_1","value":0},
    {"hisobot_code":1,"soato":1735209,"year":2023,"indicator_code":"101_1","value":0},
    {"hisobot_code":1,"soato":1735211,"year":2023,"indicator_code":"101_1","value":0},
    {"hisobot_code":1,"soato":1735212,"year":2023,"indicator_code":"101_1","value":0},
    {"hisobot_code":1,"soato":1735215,"year":2023,"indicator_code":"101_1","value":0},
    {"hisobot_code":1,"soato":1735218,"year":2023,"indicator_code":"101_1","value":0},
    {"hisobot_code":1,"soato":1735222,"year":2023,"indicator_code":"101_1","value":0},
    {"hisobot_code":1,"soato":1735225,"year":2023,"indicator_code":"101_1","value":0},
    {"hisobot_code":1,"soato":1735228,"year":2023,"indicator_code":"101_1","value":0}
]

