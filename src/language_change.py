change_language = {
    "Dutch": (
        "Typ de view link van jouw CV",
        "Selecteer het pad waar u de CV wilt opslaan"
    ),
    "English": (
        "Type the view link of your CV",
        "Select the path where you want the image to be stored"
    ),
    "Russian": (
        "Напишите ссылку на ваше резюме здесь",
        "Напишите путь где вы хотите сохранить свое резюме"
    )

}

def getStringByID(id, selected_language = "English"):
    return change_language[selected_language][id]
