def month_to_season(month):
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]

    if month in winter:
        return "Зима"
    elif month in spring:
        return "Весна"
    elif month in summer:
        return "Лето"
    elif month in autumn:
        return "Осень"
    else:
        return "Некорректный номер месяца"
    
print(month_to_season(2))
