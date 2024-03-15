from jinja2 import Environment, FileSystemLoader, select_autoescape
from build_pages import build_index, build_write_up
from shutil import rmtree, copytree
from os.path import exists, dirname, basename
from os import makedirs
from json import load

def clean(dir: str) -> None:
    if exists(dir): rmtree(dir)
    makedirs(dir, exist_ok=True)
    print(f'[+] Folder "{dir}" cleaned')

def build(env: Environment, dir: str) -> None:
    data: dict = load(open('write_up_data.json', 'r'))
    index_data: dict = {}
    for ctf, write_ups in data.items():
        build_write_up(env, write_ups, dir)
        index_data[ctf] = {}
        for w in write_ups:
            category: str = dirname(w['path'][9 + len(ctf) + 2:])
            if not index_data[ctf].get(category): index_data[ctf][category] = []
            index_data[ctf][category].append(basename(w['path'][:-3]))
    build_index(env, index_data, dir)
    print(f'[+] Write-ups successfully created')

def setup_static_files(static_dir: str, build_dir: str):
    copytree(static_dir, build_dir, dirs_exist_ok=True)
    print(f'[+] Copied {static_dir} to {build_dir}')

def main() -> None:
    build_dir: str = 'dist/'
    static_dir: str = 'static/'
    env: Environment = Environment(
        loader = FileSystemLoader('templates'),
        autoescape = select_autoescape()
        )
    clean(build_dir)
    setup_static_files(static_dir, build_dir)
    build(env, build_dir)

if __name__ == '__main__':
    main()

