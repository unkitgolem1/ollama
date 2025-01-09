from ollama import generate
class ia:
	def ia (self, pregunta = ''):		
		response= generate('llama2-uncensored',pregunta)
		return response['response']

#Para usar esa madre tenemos que tener ollama installado en local
