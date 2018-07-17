#!/usr/bin/env python3

# Core libraries
import os
import os.path

# 3rd party libs
from jinja2 import Template
import yaml


base_dir = os.path.dirname(os.path.abspath(__file__))

notebook_dir = base_dir
langauge_dir = os.path.join(base_dir, 'languages')
output_dir = os.path.join(base_dir, 'notebooks')


languages = []
for language in os.listdir(langauge_dir):
    if os.path.isdir(os.path.join(langauge_dir, language)):
        print("Detected language %s" % language)
        languages.append(language)


if not os.path.exists(output_dir):
    os.mkdir(output_dir)

for notebook in os.listdir(notebook_dir):
    if notebook.endswith('.ipynb.j2'):
        notebook_basename = notebook[:-9]
        templ = Template(open(os.path.join(notebook_dir, notebook)).read())
        print("Processing notebook %s..." % notebook, end='')
        os.mkdir(os.path.join(output_dir, notebook_basename))
        for language in languages:
            print(language, end=' ')
            with open(os.path.join(output_dir, notebook_basename, language + '.ipynb'), 'w') as out_f:
                y = yaml.load(open(os.path.join(base_dir, langauge_dir, language, notebook_basename + '.yml')).read())
                out_f.write(templ.render(**y))
        print()
        # with open(os.path.join(langauge_dir, language, 'Sources.yml')) as f:
        #     y = yaml.load(f.read())
        #     print(y)




