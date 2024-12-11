import pkgutil

available_modules = [module.name for module in pkgutil.iter_modules()]

print("Доступные модули:")
for module in sorted(available_modules):
    print(module)
