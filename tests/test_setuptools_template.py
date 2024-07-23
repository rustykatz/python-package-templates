from setuptools_package.module import module_fxn
from setuptools_package.nested_package.nested_module import nested_module_fxn

def test_import_module():
    res = module_fxn()
    assert str(res), "Failed to import module"

def test_import_nested_module():
    res = nested_module_fxn()
    assert str(res), "Failed to import nested module"
