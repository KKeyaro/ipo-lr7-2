import json
kvalif = str(input("Введите номер квалификации: "))
found = False
with open("dump.json", encoding= "utf-8") as file:
    soderjim = file.read()
    text = json.loads(soderjim)
    for skill in text:
        if skill["model"] == "data.skill" and skill["fields"]["code"] == kvalif:
            skill_code = skill["fields"]["code"]
            skill_title = skill["fields"]["title"]
            found = True
            for spec in text:
                if spec["model"] == "data.specialty":
                    if spec["fields"]["code"] == kvalif:
                        spec_code = spec["fields"]["code"]
                        spec_title = spec["fields"]["title"]
                        spec_type = spec["fields"]["c_type"]
            break
if found:
    print("=============== Найдено ===============")
    print(f"{spec_code} >> Специальность '{spec_title}', {spec_type}")
    print(f"{skill_code} >> Квалификация '{skill_title}'")
else:
    print("=============== Не найдено ===============")