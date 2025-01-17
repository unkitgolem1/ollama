from ohllama import ia
while True:
  pregunta = str(input('TU:'))
  promt = f'''
    Habla como Marco Aurelio, el filósofo estoico. Emplea un tono reflexivo, sereno y lleno de sabiduría. Ofrece consejos prácticos y filosóficos, enfatizando la importancia de la virtud, la razón y la aceptación de la naturaleza de la vida.
    {pregunta}'''
  print(ia(promt))
