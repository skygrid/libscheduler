from setuptools import setup

setup(
    name='skygrid-libscheduler',
    version='0.5.8',
    url='https://github.com/skygrid/libscheduler',
    author='Alexander Baranov',
    author_email='sashab1@yandex-team.ru',
    description='Metascheduler API client library',
    packages=['libscheduler'],
    install_requires=[
        "requests>=2.7.0",
    ],
    tests_require=[
        "nose==1.3.4",
        "nose-testconfig==0.9",
    ],
)
