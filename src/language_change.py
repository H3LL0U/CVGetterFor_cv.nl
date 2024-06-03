change_language = {
    "Dutch": {
        0:"Typ de view link van jouw CV",
        1:"Selecteer het pad waar u de CV wilt opslaan",
        2:"Indienen",
        3:"Schrijf de naam van het bestand"
    },
    "English": {
        0:"Type the view link of your CV",
        1:"Select the path where you want the image to be stored",
        2:"Submit",
        3:"Enter the file name(s)"
    },
    "Russian": {
        0:"Напишите ссылку на ваше резюме здесь",
        1:"Напишите путь где вы хотите сохранить свое резюме",
        2:"Отправить",
        3:"Напишите имя для файла(ов)"
    }

}

def getStringByID(id, selected_language = "English"):
    return change_language[selected_language][id]
