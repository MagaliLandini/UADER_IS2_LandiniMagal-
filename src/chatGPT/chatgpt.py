#!/usr/bin/python 
import openai
import sys
#……. [ mas Código de inicialización aqui ] …………

consulta =input('ingrese un texto: ')

if len(consulta) == 0:
     print('debe ingresar un texto')
     sys.exit()
else:
    userText= "You: "+ consulta
        



openai.api_key = "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"
TOP_P=1 
FREQ_PENALTY=0 
PRES_PENALTY=0
STOP=None

MAX_TOKENS=1024 
TEMPERATURE=0.75 
NMAX=1
MODEL_ENGINE = "text-davinci-003"

#…..[otra lógica necesaria – el texto del prompt debe colocarse en userText]…..
# Set up the model and prompt

completion = openai.Completion.create(
    engine=MODEL_ENGINE, 
    prompt=userText,
    max_tokens=MAX_TOKENS, 
    n=NMAX,
    top_p=TOP_P, 
    frequency_penalty=FREQ_PENALTY, 
    presence_penalty=PRES_PENALTY, 
    temperature=TEMPERATURE, 
    stop=STOP)


respuesta=completion.choices[0].text
print('chatGPT: ' + respuesta)

