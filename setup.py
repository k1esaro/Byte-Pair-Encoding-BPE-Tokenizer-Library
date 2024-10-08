from setuptools import setup, find_packages

setup(
    name="my_tokenizer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Укажите зависимости, если они есть, например:
        # 'torch>=1.7.1',
    ],
    description="Byte Pair Encoding (BPE) Tokenizer Library",
    author="Kiesaro",
    author_email="freestylerspb@gmail.com",
    url="https://github.com/k1esaro/Byte-Pair-Encoding-BPE-Tokenizer-Library.gitgit commit -m",  # Ссылка на проект (если есть)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
