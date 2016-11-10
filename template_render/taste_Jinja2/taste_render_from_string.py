from jinja2.sandbox import SandboxedEnvironment


jinja_template_env = SandboxedEnvironment(
    variable_start_string='{$',
    variable_end_string='$}',
)


def jinja_render_string(string, variables):
    template = jinja_template_env.from_string(string)
    result = template.render(variables)
    return result

if __name__=='__main__':
    string = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Title</title></head>' \
             '<body>hello {$ name $}!<div></div>{% for i in items %}{% if i %}<div>{$ i $}</div>{% endif %}{% endfor %}</body></html>'
    variables = {"name": "jaja", "items": [i for i in range(0,9)]}
    result = jinja_render_string(string,variables)
    print(result)