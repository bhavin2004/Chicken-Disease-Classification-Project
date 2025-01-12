from setuptools import find_packages,setup

HYPEN_E_DOT='-e .'

def get_requirements(filepath:str):
    with open(filepath,'r') as f:
        requirements= f.readlines()
        requirements = [i.replace('\n','') for i in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements
        

setup(
    author="Bhavin Karangia",
    author_email="karangiabhavin2004@gmail.com",
    name="Chicken-Disease-Classification-Project",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)