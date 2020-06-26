from django import template
register = template.Library()

def contador(request):
	if request.session.get('contador', False):
		contador = GetContador()
		return str(contador)
	request.session['contador'] = True
	contador = GetContador()
	contador = contador + 1
	SetContador(str(contador))
	return str(contador)
	
def GetContador():
	f_contador = open('media/contador/visitas_archivos_residencia.txt', 'r') 
	contador = f_contador.read()
	return int(contador)

def SetContador(contador):
	'''Funcion que guarda la posición actual del visitante'''
	f_contador = open('media/contador/visitas_archivos_residencia.txt', 'w')
	f_contador.write(contador)
	f_contador.close()

register.simple_tag(contador)