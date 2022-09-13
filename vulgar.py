from spanlp.palabrota import Palabrota
from spanlp.domain.countries import Country

def find_depression_words(data):
    if data is None:
        raise Exception("Datos vacios")
    
    words = data.split()
    new_text = ""
    word_count = 0
    for word in words:
        new_text += word + " "
        word_count += 1
        if word_count == 10:
            new_text += ","
            word_count = 0

    words_splitted = new_text.split(',')
    count_depression_words = 0
    validator = Palabrota(countries=[Country.COLOMBIA, Country.VENEZUELA, Country.MEXICO, Country.ARGENTINA])

    for texto in words_splitted:
        print('texto ', texto)
        if isinstance(texto, str):
            es_palabrota = validator.contains_palabrota(texto)
            if es_palabrota:
                count_depression_words += 1
    
    return (count_depression_words>0,count_depression_words)


print(find_depression_words('Estoy tristeza ya no puedo mas'))