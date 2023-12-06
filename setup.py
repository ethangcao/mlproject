from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path):
    '''
    :param file_path: file path for requirements.txt
    :return: list of required packages
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    f.close()
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Ethan Cao',
    author_email = 'guoyi.ethan.cao@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)