from os.path import exists, dirname, join
from textx.metamodel import metamodel_from_file
import jinja2

def clearSpace(chain):
	return str(chain).replace(' ','')

def gologOperator(operator):
	return {
		'mayor o igual que':'>=',
		'menor o igual que':'<=',
		'mayor que':'>',
		'menor que':'<',
		'igual que':'==',
		'diferente que':'!=',
		'y':',',
		'o':';'
	}.get(operator, operator)


this_folder = dirname(__file__)

categoria_mm = metamodel_from_file('gramatica.tx')
modelo_categoria = categoria_mm.model_from_file('entidad.ent')

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(this_folder), trim_blocks=True, lstrip_blocks=True)

factTemplate = jinja_env.get_template('golog.template')

print(factTemplate.render(dominio=modelo_categoria,clearSpace=clearSpace,gologOperator=gologOperator))

print("ok")