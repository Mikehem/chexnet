from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Reproduction of the CheXNet paper that predicted 14 common diagnoses using convolutional neural networks in over 100,000 NIH chest x-rays.',
    author='michael',
    license='MIT',
)
