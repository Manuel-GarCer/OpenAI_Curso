import openai

openai.api_key = "TU_API_KEY creada en https://platform.openai.com"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # es el grado de aleatoriedad de los resultados del modelo
    )
    return response.choices[0].message["content"]





# text = f"""
# You should express what you want a model to do by \ 
# providing instructions that are as clear and \ 
# specific as you can possibly make them. \ 
# This will guide the model towards the desired output, \ 
# and reduce the chances of receiving irrelevant \ 
# or incorrect responses. Don't confuse writing a \ 
# clear prompt with writing a short prompt. \ 
# In many cases, longer prompts provide more clarity \ 
# and context for the model, which can lead to \ 
# more detailed and relevant outputs.
# """
# prompt = f"""
# Summarize the text delimited by triple backticks \ 
# into a single sentence.
# ```{text}```
# """
# response = get_completion(prompt)
# print(response)

###################################################################################

# prompt = f"""
# Generate a list of three made-up book titles along \ 
# with their authors and genres. 
# Provide them in JSON format with the following keys: 
# book_id, title, author, genre.
# """
# response = get_completion(prompt)
# print(response)

###################################################################################


# text_1 = f"""
# Preparar una taza de té es muy fácil. En primer lugar, usted necesita para obtener algunos \ 
# agua hirviendo. Mientras eso sucede, \ 
# coge una taza y pon una bolsita de té en ella. Cuando el agua esté 
# lo suficientemente caliente, viértela sobre la bolsita de té. \ 
# Déjalo reposar un rato para que el té se infusione. Después de 
# minutos, saca la bolsita. Si quieres 
# Si quieres, puedes añadir un poco de azúcar o leche al gusto. \ 
# Y ¡listo! Ya tienes una deliciosa 
# taza de té para disfrutar.
# """
# prompt = f"""
# Se le proporcionará un texto delimitado por comillas triples. 
# Si contiene una secuencia de instrucciones, \ 
# reescriba esas instrucciones en el siguiente formato:

# Paso 1 - ...
# Paso 2 - ...
# ...
# Paso N - ...

# Si el texto no contiene una secuencia de instrucciones, \ 
# entonces simplemente escriba \ "No se proporcionan pasos.\"

# \"\"\"{text_1}"\"\"\"
# """
# response = get_completion(prompt)
# print("Finalización del texto 1:")
# print(response)

###################################################################################

# text_2 = f"""
# El sol brilla intensamente hoy, y los pájaros están \
# cantando. Es un hermoso día para ir a dar un \ 
# pasear por el parque. Las flores están floreciendo, y los árboles... 
# árboles se mecen suavemente con la brisa. La gente 
# está fuera, disfrutando del buen tiempo. \ 
# Algunos hacen picnic, otros juegan o simplemente se relajan en la hierba. 
# juegos o simplemente se relajan en la hierba. Es un día 
# día perfecto para pasar tiempo al aire libre y apreciar la \ 
# la belleza de la naturaleza.
# """
# prompt = f"""
# Se le proporcionará un texto delimitado por comillas triples. 
# Si contiene una secuencia de instrucciones, \ 
# reescriba esas instrucciones en el siguiente formato:

# Paso 1 - ...
# Paso 2 - ...
# ...
# Paso N - ...

# Si el texto no contiene una secuencia de instrucciones, \ 
# entonces simplemente escriba \ "No se proporcionan pasos.\"

# \"\"\"{text_2}"\"\"\"
# """
# response = get_completion(prompt)
# print("Finalización del texto 2:")
# print(response)

###################################################################################

# prompt = f"""
# Tu tarea es responder con un estilo coherente.

# <niño>: Enséñame sobre la paciencia.

# <abuelo>: El río que esculpe el más profundo \ 
# valle más profundo fluye de un modesto manantial. 
# más grandiosa sinfonía se origina en una sola nota; \ 
# el tapiz más intrincado comienza con un hilo solitario.

# <child>: Enséñame sobre la resiliencia.
# """
# response = get_completion(prompt)
# print(response)

###################################################################################

# Principio 2: Dar tiempo al modelo para "pensar"
# Táctica 1: Especificar los pasos necesarios para completar una tarea

# text = f"""
# En un encantador pueblo, los hermanos Jack y Jill emprenden \ 
# a buscar agua de un pozo en lo alto de una colina.
# Mientras subían, cantando alegremente, la desgracia los golpeó. 
# Jack tropezó con una piedra y cayó colina abajo. 
# y Jill le siguió. \ 
# Aunque algo maltrecha, la pareja regresó a casa... 
# abrazos reconfortantes. A pesar del percance. 
# sus espíritus aventureros permanecieron intactos, y continuaron 
# siguieron explorando con deleite.
# """
# # ejemplo 1
# prompt_1 = f"""
# Realice las siguientes acciones: 
# 1 - Resumir el siguiente texto delimitado por triple \
# con 1 frase.
# 2 - Traduzca el resumen al francés.
# 3 - Listar cada nombre en el resumen francés.
# 4 - Generar un objeto json que contenga lo siguiente
# claves: french_summary, num_names.

# Separe sus respuestas con saltos de línea.

# Texto:
# ```{text}```
# """
# response = get_completion(prompt_1)
# print("Respuesta a la pregunta 1:")
# print(response)

# prompt_2 = f"""
# Su tarea consiste en realizar las siguientes acciones 
# 1 - Resumir el siguiente texto delimitado por 
#   <> con 1 frase.
# 2 - Traduzca el resumen al francés.
# 3 - Listar cada nombre en el resumen francés.
# 4 - Dar salida a un objeto json que contenga las 
#   siguientes claves: french_summary, num_names.

# Utilice el siguiente formato:
# Texto: <texto a resumir>
# Resumen: <resumen>
# Traducción: <traducción del resumen>
# Nombres: <lista de nombres en italiano resumen>
# JSON de salida: <json con resumen y número_nombres>

# Texto: <{text}>
# """
# response = get_completion(prompt_2)
# print("respuesta para pregunta 2:")
# print(response)

###########################################################################################

# Táctica 2: Pedir al modelo que elabore su propia solución antes de llegar a una conclusión precipitada.

# prompt = f"""
# Determine si la solución del alumno es correcta o no.

# Pregunta:
# Estoy construyendo una instalación de energía solar y necesito
#  ayuda para calcular los costes. 
# - El terreno cuesta 100 $ / pie cuadrado
# - Puedo comprar paneles solares por 250 $ / pie cuadrado
# - He negociado un contrato de mantenimiento que me costará 
# 100 mil dólares al año, y 10 dólares adicionales por pie cuadrado.
# pie cuadrado
# ¿Cuál es el coste total para el primer año de operaciones 
# en función del número de pies cuadrados.

# Solución del alumno:
# Sea x el tamaño de la instalación en pies cuadrados.
# Costes:
# 1. Coste del terreno: 100x
# 2. Coste del panel solar: 250x
# 3. Coste de mantenimiento: 100.000 + 100x
# Coste total: 100x + 250x + 100.000 + 100x = 450x + 100.000
# """
# response = get_completion(prompt)
# print(response)

# Nótese que la solución del estudiante no es correcta. #
# Podemos arreglar esto instruyendo al modelo para que elabore su propia solución primero.

prompt = f"""
Su tarea es determinar si la solución del estudiante \
es correcta o no.
Para resolver el problema haz lo siguiente:
- Primero, elabora tu propia solución al problema. 
- Después compara tu solución con la del alumno \ 
y valora si la solución del alumno es correcta o no. 
No decidas si la solución del alumno es correcta hasta que 
que hayas resuelto el problema tú mismo.

Utiliza el siguiente formato:
Pregunta:
```
pregunta aquí
```
Solución del alumno:
```
solución del estudiante aquí
```
Solución real:
```
pasos para elaborar la solución y su solución aquí
```
¿Es la solución del alumno la misma que la solución real \
que acaba de calcular:
```
sí o no
```
Calificación del alumno:
```
correcta o incorrecta
```

Pregunta:
```
Estoy construyendo una instalación de energía solar y necesito ayuda para
a calcular los costes. 
- El terreno cuesta 100 $ / pie cuadrado
- Puedo comprar paneles solares por $ 250 / pie cuadrado
- He negociado un contrato de mantenimiento que me costará
100 mil dólares al año, y un adicional de 10 dólares por pie cuadrado.
pie cuadrado
¿Cuál es el coste total para el primer año de operaciones /
en función del número de pies cuadrados.
``` 
Solución del alumno:
```
Sea x el tamaño de la instalación en pies cuadrados.
Costes:
1. Coste del terreno: 100x
2. Coste del panel solar: 250x
3. Coste de mantenimiento: 100.000 + 100x
Coste total: 100x + 250x + 100.000 + 100x = 450x + 400.000
```
Solución real:
"""
response = get_completion(prompt)
print(response)