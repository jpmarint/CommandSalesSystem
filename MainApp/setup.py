from setuptools import setup


setup(
    name='jp',
    version='0.1',
    py_modules=['jp'],
    install_requires=[
        'click',
        'tabulate',
        'uuid'
    ],
    entry_points='''
        [console_scripts]
        jp=sales:cli
    ''',
)