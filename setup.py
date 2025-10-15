from setuptools import setup, find_packages

def get_requrirements(file_path:str)->list:
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="XRay Image Clasification",
    version="0.1.0",
    author ="Narne",
    packages=find_packages(),
    install_requires=get_requrirements("C:\\Users\\bhara\\DeepLearningProject\\requirements_dev.txt")
)