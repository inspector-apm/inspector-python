from setuptools import setup, find_packages

setup(
    name='inspector-python',
    description='Connect your Python applications with Inspector.',
    long_description='Inspector is a Code Execution Monitoring tool to help developers find out technical problem in their software before customers do.',
    version='0.1.4',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://inspector.dev/',
    license='MIT',
    author='Antonio Bruno',
    author_email='antoniobruno82@gmail.com'
)
