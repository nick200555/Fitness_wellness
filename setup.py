from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="fitness_wellness",
    version="1.0.0",
    description="Fitness and Wellness Management System for ERPNext v15+",
    author="Your Organization",
    author_email="admin@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
