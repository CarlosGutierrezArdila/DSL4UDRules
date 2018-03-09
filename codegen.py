from os.path import exists, dirname, join
from textx.metamodel import metamodel_from_file
import jinja2

this_folder = dirname(__file__)

categoria_mm = metamodel_from_file('gramatica.tx')
modelo_categoria = categoria_mm.model_from_file('entidad.ent')

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(this_folder), trim_blocks=True, lstrip_blocks=True)

factTemplate = jinja_env.get_template('fact.template')

print(factTemplate.render(dominio=modelo_categoria))

print("ok")