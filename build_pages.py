from jinja2 import Environment, Template
from markdown2 import markdown
from os.path import dirname
from os import makedirs
import re

def save_rendered(file: str, content: str) -> None:
    makedirs(dirname(file), exist_ok=True)
    print(f'\t[+] Saving {file}')
    open(file, 'w').write(content)

def build_index(env: Environment, data: dict, dir: str) -> None:
    site: dict = {
        'title': 'CTF Write ups',
        'description': 'Write ups I made',
        'url': 'htsuyoshiy.online',
        'ctfs': data
    }

    html_content: str = markdown('hihi')
    template: Template = env.get_template('index.html')
    save_rendered(
            dir + 'index.html',
            template.render(
                site=site,
                content=html_content
                )
            )

def build_write_up(env: Environment, write_ups: dict, dir: str) -> None:
    template: Template = env.get_template('write_up.html')
    for w in write_ups:
        w['content'] = markdown(open(w['path']).read(),
                                extras = [
                                    'code-friendly',
                                    'fenced-code-blocks',
                                    'footnotes'
                                    ])
        page: str = template.render(write_up = w)
        save_rendered(
                dir + re.sub(r'\.md$', '.html', w['path']),
                page
                )
