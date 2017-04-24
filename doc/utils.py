"""
Inspect source code to generate API Reference.

So far, only tested/used with inplace build

"""
import glob
import inspect
import importlib
import os
import re
import sys
import traceback

from colorama import Fore, init, Style
init(autoreset=True)


def fmt_func_src(raw_src, package, noindex=False):
    """
    return str suitable for autodoc
    src is func name(signature)
    """
    src = raw_src.replace('def ', '')
    src = re.sub('\s+', ' ', src)
    lb_ind = src.find('):')
    src = src[:lb_ind+1]
    if noindex:
        ad_str = f'.. autofunction:: {package}.{src.strip()}\n    :noindex:\n\n'
    else:
        ad_str = f'.. autofunction:: {package}.{src.strip()}\n\n'
    return ad_str


def fmt_class_src(obj, noindex=False):
    """
    return str for autodoc
    obj is actual object
    """
    s = str(obj)
    s = s.replace('<', '')
    s = s.replace('>', '')
    s = s.replace("'", '')
    s = s.replace('class ', '')
    ad_str = f'\n.. autoclass:: {s}\n'
    lines = [ad_str,
             '    :members:\n',
             '    :undoc-members:\n',
             '    :private-members:\n']
    if noindex:
        lines.append('    :noindex:\n\n')
    else:
        lines.append('\n')

    return lines


def inspect_module(Module, pkg_name):
    """
    get all attributes etc. of object
    mod_name somehow became package name ...
    """
    exclude_attrs = ('this_dir',
                     'basestring',
                     '_basestring',
                     'unicode',
                     '_unicode')
    classes = []
    functions = []
    data = []

    print(f'{Fore.GREEN}Module: {Module}')
    if not pkg_name:
        pkg_name = 'lxml'
    else:
        pkg_name = 'lxml.' + pkg_name
    basename = os.path.splitext(os.path.basename(str(Module)))[0]
    whole_name = f'{pkg_name}.{basename}'
    seen = []

    for attr_name in dir(Module):
        if attr_name.startswith('__'):
            continue

        obj = inspect.getattr_static(Module, attr_name)

        if attr_name in exclude_attrs:
            continue

        if inspect.isbuiltin(obj):
            continue

        # exclude items that aren't really from current module
        obj_mod = getattr(obj, '__module__', None)
        if obj_mod and obj_mod not in whole_name:
            print(f'{Fore.RED}SKIPPING: {attr_name} {obj} {whole_name}')
            continue

        noindex = False
        if attr_name:
            # keep track of things It's already seen
            obj_names = re.findall("'([a-zA-Z0-9./_-]+)'", str(obj))
            if obj_names:
                # noindex means item has been referenced somewhere else before
                # and thus should have :noindex: flag
                noindex = any([i for i in obj_names if i in seen])
                seen.extend(obj_names)

        if inspect.isfunction(obj):
            raw_src = inspect.getsource(obj)
            functions.append(fmt_func_src(raw_src, whole_name, noindex=noindex))
            continue

        if inspect.isclass(obj):
            classes.extend(fmt_class_src(obj, noindex=noindex))
            continue

        if not inspect.ismodule(obj):
            ad_str = f'.. autodata:: {whole_name}.{attr_name}\n'
            if noindex:
                ad_str += '    :noindex:\n\n'
            else:
                ad_str += '\n'
            data.append(ad_str)

    return classes, functions, data


RST_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'source', 'api_source')
if not os.path.exists(RST_ROOT):
    os.mkdir(RST_ROOT)


def write_rst(package, title, classes, functions, data):
    """
    write instructions for sphinx.autodoc to file
    keep nested paths
    """
    fn = title.split('.')[-1]+'.rst'
    pkg_path = os.path.join(RST_ROOT, package)
    if not os.path.exists(pkg_path):
        os.mkdir(pkg_path)
    outpath = os.path.join(pkg_path, fn)

    with open(outpath, 'w') as fd:
        title_str = f'{title}\n{"-"*(len(title))}\n\n'
        fd.write(title_str)
        fd.writelines(classes)
        fd.writelines(functions)
        fd.writelines(data)
        fd.write('\n\n')

    print(f'filename: {Fore.GREEN}{outpath}')


def inspect_source():
    """
    Try to automate creation of source docs

    Try to get all objects, including variables and stuff.

    """
    # Required so "it" can import lxml
    src_root = '/home/lemur/LibCode/lxml.git/src'
    base_dir = '/home/lemur/LibCode/lxml.git/src/lxml'
    sys.path.append(src_root)
    sys.path.append(base_dir)

    base_modules = glob.glob(os.path.join(base_dir, '*.py'))
    modules = glob.glob(os.path.join(base_dir, '**/*.py'))
    modules.extend(base_modules)
    # remove base path so It can get the module name and package name
    cmn_pth = os.path.commonpath(modules)

    for name in modules:
        if os.path.basename(name).startswith('__'):
            continue
        mod_name = os.path.splitext(os.path.basename(name))[0]
        mod_name = name.replace(cmn_pth, '')
        pkg, mod = os.path.split(mod_name)
        pkg = pkg.replace('/', '')
        mod = os.path.splitext(mod)[0]

        try:
            importlib.import_module('lxml')
            importlib.import_module('lxml.etree')
        except Exception as E:
            print(f'ImportError <{name}> {Fore.RED}{E}')

        try:
            if pkg:
                mod_name = f'lxml.{pkg}.{mod}'
            else:
                mod_name = mod
            print(f'{Fore.CYAN}{mod_name}')
            Module = importlib.import_module(mod_name, package=pkg)
            classes, functions, data = inspect_module(Module, pkg)
            write_rst(pkg, mod_name, classes, functions, data)

        except Exception as E:
            print(f'ImportError <{name}> {Fore.RED}{E}')
            # I guess... open the file and parse out the doc string
            print(f'{Fore.YELLOW}{name}')
            # traceback.print_tb(E.__traceback__)


if __name__ == '__main__':
    inspect_source()
