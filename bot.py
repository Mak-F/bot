import json

# SE INICIALIZA EL JSON COMO LA VARIABLE DATA
with open("data.json", encoding='utf-8') as jsonFile:
    data = json.load(jsonFile)

intro_data  = data['question_list'][0] # BIENVENIDA / RETRY_TEXT
prod_data   = data['question_list'][1] # PRODUCTOS
suc_data    = data['question_list'][2] # SUCURSALES
hor_data    = data['question_list'][3] # HORARIOS

while True:
    print(intro_data['text'][0])

    for option in intro_data['response_options']:
        print(option)

    response = input("Escribí tu consulta: ")

    # SE CREA UN BUCLE PARA VERIFICAR QUE EL DATO INGRESADO CORRESPONDE A UNA DE LAS OPCIONES EXISTENTES
    _retry = True
    while _retry:
        for options in intro_data['response_options']:
            if response in options:
                _retry = False

        if _retry:
            response = input(intro_data['retry_text'][0])

    if response in intro_data['response_options'][0]:
        #PRODUCTOS
        print(prod_data['text'][0])

    if response in intro_data['response_options'][1]:
        #SUCURSAL
        print(suc_data['text'][0])

    if response in intro_data['response_options'][2]:
        #HORARIOS
        print(hor_data['text'][0])

    _close = input('Lo podemos ayudar en algo más? Elija entre S/N: ')

    while _close not in ['s', 'n', 'S', 'N']:
        _close = input('Disculpa, no entendí el mensaje, podrías ingresarlo otra vez? Elija entre S/N: ')

    if _close in ['n', 'N']:
        print("Gracias por comunicarte con nosotros :)")
        break