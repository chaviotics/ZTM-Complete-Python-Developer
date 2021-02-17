from translate import Translator

try:
    with open(r'13. File IO\exercise_translated.txt', 'r') as text:
        translator = Translator(to_lang="es")
        sentence = text.readline()
        translation = translator.translate(sentence)
        
        print(translation)
        # with open('.\exercise_translated.txt', 'w') as text2:
        #     text2.write(translation)

except FileNotFoundError as err:
    print("No file Sir!")
    raise err