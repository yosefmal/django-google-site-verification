from setuptools import setup, find_packages

setup(
    name='django-google-site-verification',
    version='0.0.1',
    url='https://github.com/lotrekagency/cattp',
    install_requires=[],
    description="django-google-site-verification",
    long_description=open('README.rst', 'r').read(),
    license="MIT",
    author="Lotrek",
    author_email="dimmitutto@lotrek.it",
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)