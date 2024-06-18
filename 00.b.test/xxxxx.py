def print_person_info(name, age, country):
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    print(f"国家: {country}")

person = {"name": "小明", "age": 20, "country": "中国"}

print_person_info(**person)
