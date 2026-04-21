from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = [
        line.strip()
        for line in f.read().splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]

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
