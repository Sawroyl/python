def add_daily_temp(dict,temp,day):
    if day not in dict:
        dict[day]=temp
    return dict
dict={'Sun':29.6,'Tue':28,'Thu':27}
dict=add_daily_temp(dict,25,'Mon')
dict=add_daily_temp(dict,27.6,'Wed')
dict=add_daily_temp(dict,26,'Mon')
print(dict)