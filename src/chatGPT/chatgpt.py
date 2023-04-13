#importamos la librerias de openai y de sys que se va a utilizar en el programa
import sys
import openai
# ……. [ mas Código de inicialización aqui ] …………
#openai nos proporciona una clave key unica la cual no puede ser expuesta
#--[ingrese la clave key que obtuvo en openai]...
openai.api_key = "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"
TOP_P = 1
FREQ_PENALTY = 0
PRES_PENALTY = 0
STOP = None
MAX_TOKENS = 1024
TEMPERATURE = 0.75
NMAX = 1
MODEL_ENGINE = "text-davinci-003"
try:
    # …..[otra lógica necesaria – el texto del prompt debe colocarse en userText]…..
    # Set up the model and prompt
    #....[funcion que obtiene la respuesta de chatGPT]....
    def obtener_respuesta(prompt):
        completion = openai.Completion.create(
            engine=MODEL_ENGINE,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            n=NMAX,
            top_p=TOP_P,
            frequency_penalty=FREQ_PENALTY,
            presence_penalty=PRES_PENALTY,
            temperature=TEMPERATURE,
            stop=["You:","chatGPT:"])
        return completion.choices[0].text
    #...[funcion se encarga de guardar el historial de consultas y de mostrar la respuesta de chatGPT]...
    def handle_input(
        input_str : str,
        conversation_history : str,
        usuario: str,
        chatgpt : str,
        buffer=[],
        ):
        buffer.append('You: '+input_str)
        # actualiza el historial de conversacion
        conversation_history += f"{usuario}: {buffer}\n"
        # genera una respuesta utilizando la funcion obtener_respuesta
        message = obtener_respuesta(conversation_history)
        # actualiza el historial de conversacion
        conversation_history += f"{chatgpt}: {message}\n"
        buffer.append('ChatGPT: '+ message)
        # imprime la respuesta
        print(f'{chatgpt}: {message}')
        return conversation_history
#--[exepcion en caso de que la api falle]...
except TypeError:
    print('ChaptGPT no pudo dar una respuesta.')
# inicializamos la conversacion
INITIAL_PROMPT = ''
conversacion_inicial = INITIAL_PROMPT
username = "You"
ai_name = "chatGPT"
#si no se ingresa argumento no se inicia el modo conversacion
if len(sys.argv) == 1:
    #hacemos un bucle infinito para que siempre pegunte chatpgpt
    while True:
        user_input = input(f"{username}: ")
        respuesta=obtener_respuesta(user_input)
        print(f'{ai_name}: {respuesta}')
else:
    #verificamos que se ingrese como argumento --convers
    conver=str(sys.argv[1])
    if(conver == "--convers"):
        try:
            while True:
                # obtenemos la consulta
                user_input = input(f"{username}: ")
                #si la consulta es vacia salta una excepcion
                if not user_input:
                    raise ValueError
                #si la consulta es numerica salta una excepcion
                elif not all(x.isalpha() or x.isspace() for x in user_input):
                    raise TypeError
                else:
                    # ejecuta las funcion handle_input
                    res3ultado = handle_input(user_input,conversacion_inicial, username, ai_name)
    #exepciones que se ejecuta en caso de que la cosnulta tenga algun error
        except ValueError:
            print('No te entiendo,asegurate de escribir la consulta.')
    #excepcion de tipo error al ingresar un numero
        except TypeError:
            print('no te entiendo, asegurate de estar escribiendo un texto ')
