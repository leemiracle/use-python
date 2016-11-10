from jinja2 import Template, Environment, PackageLoader
template = Template('Hello {{ name }}!')
result = template.render(name='John Doe')
print(result)

# create a template environment with the default settings and a loader that looks up the templates in the templates folder inside
#  the yourapplication python package.
from jinja2 import Environment, PackageLoader
# env = Environment(loader=PackageLoader('yourapplication', 'templates'))

# To load a template from this environment you just have to call the get_template() method which then returns the loaded Template:
# template = env.get_template('mytemplate.html')

# To render it with some variables, just call the render() method:
# template.render(the='variables', go='here')
# Template or Environment.from_string()


# Unicode
m = Template(u"{% set a, b = 'foo', 'föö' %}").module
print(m.a)
print(m.b)

# High Level API
# class jinja2.Environment([options])
#     shared
#     sandboxed
#     filters
#     tests
#     globals
#     code_generator_class
#     context_class
#     overlay
#     undefined
#     add_extension
#     compile_expression
#     compile_templates
#     extend
#     from_string
#     get_or_select_template
#     get_template
#     join_path
#     list_templates
#     select_template


# class jinja2.Template
#     globals
#     name
#     filename
#     render
#     generate
#     stream
#     make_module
#     module

# class jinja2.environment.TemplateStream
#     disable_buffering
#     dump
#     enable_buffering




# Autoescaping




# Notes on Identifiers
# Valid identifiers have to match [a-zA-Z_][a-zA-Z0-9_]*.




# Undefined Types
# class jinja2.Undefined
#     _undefined_hint
#     _undefined_obj
#     _undefined_name
#     _undefined_exception
#     _fail_with_undefined_error
# class jinja2.DebugUndefined
# class jinja2.StrictUndefined
# jinja2.make_logging_undefined(logger=None, base=None)



# The Context
# class jinja2.runtime.Context
#     parent
#     vars
#     environment
#     exported_vars
#     name
#     blocks
#     eval_ctx
#     call
#     get_all
#     get_exported
#     resolve



# Loaders
# class jinja2.BaseLoader
#     get_source
#     load
# class jinja2.FileSystemLoader
# class jinja2.PackageLoader
# class jinja2.DictLoader
# class jinja2.FunctionLoader
# class jinja2.PrefixLoader
# class jinja2.ChoiceLoader
# class jinja2.ModuleLoader



# Bytecode Cache
# class jinja2.BytecodeCache
#     clear
#     dump_bytecode
#     load_bytecode
# class jinja2.bccache.Bucket
#     environment
#     key
#     code
#     bytecode_from_string
#     bytecode_to_string
#     load_bytecode
#     reset
#     write_bytecode
# class jinja2.FileSystemBytecodeCache
# class jinja2.MemcachedBytecodeCache
#     class MinimalClientInterface
#         set
#         get



# Utilities实用程序
# jinja2.environmentfilter(f)
# jinja2.contextfilter(f)
# jinja2.evalcontextfilter(f)
# jinja2.environmentfunction(f)
# jinja2.contextfunction(f)
# jinja2.evalcontextfunction(f)
# jinja2.escape(s)
# jinja2.clear_caches()
# jinja2.is_undefined(obj)
# class jinja2.Markup([string])
#     classmethod escape(s)
#     striptags()
#     unescape()




# Custom Filters自定义过滤器




# Evaluation Context评估上下文




# Custom Tests



# The Global Namespace： Environment.globals



# Low Level API
#     Environment.lex
#     Environment.parse
#     Environment.preprocess
#     Template.new_context
#     Template.root_render_func
#     Template.blocks
#     Template.is_up_to_date



# The Meta API
# jinja2.meta.find_undeclared_variables
# jinja2.meta.find_referenced_templates
