change_language = {
    "Dutch": {
        0:"Typ de view link van jouw CV",
        1:"Selecteer het pad waar u de CV wilt opslaan",
        2:"Indienen",
        3:"Schrijf de naam van het bestand",
        4:"Er is iets mis gegaan",
        5:"Succesvol!",
        6:"Jouw CV was opgelsagen in ",
        7:"Een onverwachtte fout is ontstaan tijdens het opslaan van jouw CV",
        8:"Jouw CV wordt opgeslagen... Een moment geduld"
    },
    "English": {
        0:"Type the view link of your CV",
        1:"Select the path where you want the image to be stored",
        2:"Submit",
        3:"Enter the file name(s)",
        4:"An error acured",
        5:"Success!",
        6:"Your CV has been saved to ",
        7:"An error acured when trying to save your CV",
        8:"CV is being saved... Please wait",

    },
    "Russian": {
        0:"Напишите ссылку на ваше резюме здесь",
        1:"Напишите путь где вы хотите сохранить свое резюме",
        2:"Отправить",
        3:"Напишите имя для файла(ов)",
        4:"Произошла ошибка",
        5:"Готово!",
        6:"Ваше резюме было сохраненно в ",
        7:"Произошла ощибка во время сохранения вашего резюме",
        8:"Ваше резюме сохраняется... Пожалуйста подождите"
    }

}

def getStringByID(id, selected_language = "English"):
    return change_language[selected_language][id]
