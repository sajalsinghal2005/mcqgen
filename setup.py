from setuptools import find_packages,setup

setup(
    name = 'mcqgenerator',
    version = '0.0.1',
    author = 'Sajal Singhal',
    author_email = 'sajalsinghal62650@gmail.com',
    install_requires = ["openai","longchain","streamlit","python-dotenv","PyPDF2"],
    packages = find_packages()
)