def thesaurus(*names):
    set_names = {name.title() for name in names}
    first_letter = [name[0].upper() for name in set_names]
    result_dict = {k: list() for k in first_letter}

    for name in set_names:
        result_dict[name[0]].append(name)

    return result_dict

print(thesaurus("Иван", "Мария", 'Петр', 'Илья'))