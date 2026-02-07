from setuptools import setup, find_packages

setup(
    name="QRCode-Scanner",
    version="1.0",
    author="saaketh",
    author_email="saakethsoma@gmail.com",
    description="QR code scanning app using Python",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "numpy",
        "pyzbar"
    ],
)
