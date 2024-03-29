from setuptools import setup, find_packages

setup(
    name='vexcode_vr',
    version='0.1.0',
    packages=find_packages(),
    description='Python interface for Vex v5',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='vex-v5-python-interface/setup.py',
    author='Grader Than Technology LLC',
    author_email='support@GraderThan.com',
    license='Grader Than LLC Academic Content License',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
