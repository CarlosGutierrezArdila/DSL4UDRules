from os.path import exists, dirname, join
from textx.metamodel import metamodel_from_file
import jinja2


this_folder = dirname(__file__)

dsl_mm = metamodel_from_file('gramatica.tx')
dsl_model = dsl_mm.model_from_file('entidad.ent')	

def clearSpace(chain):
	return str(chain).replace(' ','')

def gologOperator(operator):
	return {
		'mayor o igual a':'@>=',
		'menor o igual a':'@=<',
		'mayor a':'@>',
		'menor a':'@<',
		'igual a':'==',
		'diferente a':'\==',
		'y':',',
		'o':';'
	}.get(operator, operator)

def is_rule(n):
        """
        Test if the line is a rule
        """
        if n.rule is not None: 
            return True
        else:
            return False

def is_predicate(n):
        """
        Test if the line is a predicate
         if n.type in dsl_model.ruleLines.predicate:
        """
        if n.predicate is not None:
            return True
        else:
            return False

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(this_folder), trim_blocks=True, lstrip_blocks=True)

##filters
jinja_env.filters['gologOperator'] = gologOperator
jinja_env.filters['clearSpace'] = clearSpace
jinja_env.filters['is_predicate'] = is_predicate
jinja_env.filters['is_rule'] = is_rule

factTemplate = jinja_env.get_template('golog.template')

print(factTemplate.render(dominio=dsl_model,clearSpace=clearSpace))

print("ok")