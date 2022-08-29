import speech_recognition as sr
from spanlp.palabrota import Palabrota
from spanlp.domain.countries import Country
import csv

def validar_vulgaridades(data):
    if data is None:
        raise Exception("Datos vacios")
    
    contador_palabrotas = 0
    validador = Palabrota(countries=[Country.COLOMBIA, Country.VENEZUELA, Country.MEXICO, Country.ARGENTINA])
    
    if isinstance(data, str):
      es_palabrota = validador.contains_palabrota(data)
      if es_palabrota:
         contador_palabrotas += 1
    return (contador_palabrotas>0,contador_palabrotas)


r = sr.Recognizer()


with sr.AudioFile('assets/triste1.wav') as source:
    
    audio_text = r.listen(source)
    
    try:
        text = r.recognize_google(audio_text, language="es-PE")
        print(text)
     
    except:
         print('Sorry.. run again...')


         
contiene, cantidad = validar_vulgaridades(text)
print(f"Los datos contienen {cantidad} vulgaridades." if contiene else "Los datos no contienen vulgaridades.")
