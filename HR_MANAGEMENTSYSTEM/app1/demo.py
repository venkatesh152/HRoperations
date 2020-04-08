year = int(input("enter the year"))
if year % 400 == 0:
    lf_yr = True
elif year % 4 == 0:
    lf_yr = False
elif year%100 == 0:
    lf_yr = False
else:
    lf_yr = False
month = int(input("enter month"))
if month in (1, 3, 5, 7, 8, 10, 12):
    m_len = 31
elif month == 2:
    if lf_yr:
        m_len = 29
    else:
        m_len = 28
else:
    m_len = 30
day = int(input("enter day"))
if day > m_len:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print("dd-mm-yy", (day, month, year))
