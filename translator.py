from deep_translator import MyMemoryTranslator
def englishToFrench(englishText):
    #write the code here
    language_translator.set_service_url('url')

    
    frenchText = language_translator.translate(
        text='Hello, how are you today?',
        model_id='en-fr').get_result()

    return frenchText
    print(frenchText)

# def frenchToEnglish(frenchText):
#     #write the code here
#     language_translator.set_service_url('url')

    
#     englishText = language_translator.translate(
#         text='Hello, how are you today?',
#         model_id='en-fr').get_result()
#     print(englishText)
#     return englishText
