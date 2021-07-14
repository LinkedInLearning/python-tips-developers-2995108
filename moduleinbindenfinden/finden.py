import pathlib
from modulefinder import ModuleFinder

finder = ModuleFinder()
finder.run_script(str(pathlib.Path(__file__).parent.absolute()) + '\mod1.py')

print('Information über geladene Module:')
for name, mod in finder.modules.items():
    print('%s: ' % name, end='')
    print(', '.join(list(mod.globalnames.keys())[:3]))
finder = ModuleFinder()
finder.run_script(str(pathlib.Path(__file__).parent.absolute()) + '/uv/mod2.py')

print('Information über geladene Module:')
for name, mod in finder.modules.items():
    print('%s: ' % name, end='')
    print(', '.join(list(mod.globalnames.keys())[:3]))
