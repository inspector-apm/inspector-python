from setuptools import setup, find_packages

setup(
    name='inspector-python',
    version='0.1.4',
    description='Connect your Python applications with Inspector.',
    long_description='Inspector is a Code Execution Monitoring tool to help developers find out technical problems in their software automatically, before customers do.',
    author='Antonio Bruno',
    author_email='antoniobruno82@gmail.com',
    url='https://inspector.dev/',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    license='MIT'
)
