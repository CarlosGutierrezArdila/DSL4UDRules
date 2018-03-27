from os.path import exists, dirname, join
from textx.metamodel import metamodel_from_file
from os import mkdir
import sys
import jinja2

def main(entity):
    
    this_folder = dirname(__file__)

    print("Loading metamodel file")
    dsl_mm = metamodel_from_file('gramatica.tx')

    print("Loading model from input file")
    dsl_model = dsl_mm.model_from_file(entity)	

    def clearSpace(chain):
        """
        replace spaces
        """
        return str(chain).replace(' ','')

    def gologOperator(operator):
        #golog operators  
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

    print("Creating template environment")
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(this_folder), trim_blocks=True, lstrip_blocks=True)

    ##filters
    jinja_env.filters['gologOperator'] = gologOperator
    jinja_env.filters['clearSpace'] = clearSpace
    jinja_env.filters['is_predicate'] = is_predicate
    jinja_env.filters['is_rule'] = is_rule

    ruleTemplate = jinja_env.get_template('golog.template')

    #print render output
    #print(ruleTemplate.render(dominio=dsl_model))

    print("Generating output")
    # Create output folder
    rules_folder = join(this_folder, 'rules')
    if not exists(rules_folder):
        mkdir(rules_folder)

    #Write output in txt 
    with open(join(rules_folder, "%s.txt" % dsl_model.domain), 'w') as rule_file:
        rule_file.write(ruleTemplate.render(dominio=dsl_model))

    print("Output generated")


if __name__ == "__main__":
    entity = None
    if len(sys.argv) > 1:
        print("Rule Generator...")
        entity = sys.argv[1]
        main(entity)
    else:
        print("Entity file not found in arguments")
        exit(1)