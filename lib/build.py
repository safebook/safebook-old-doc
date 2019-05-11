# encoding=utf8
import os
from jinja2 import Template
import markdown

SRC_DIR = "src/"

with open("lib/template.j2") as template_file:
    template = Template(template_file.read())

srcs = os.listdir(SRC_DIR)
for src in srcs:
    with open(SRC_DIR + src) as src_file:
        md_content = src_file.read().decode('utf8')
        html = markdown.markdown(md_content)
        with open(os.path.splitext(src)[0]+'.html', 'w') as dst_file:
            dst_file.write(template.render(content=html).encode('utf8'))