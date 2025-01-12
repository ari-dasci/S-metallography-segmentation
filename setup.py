from setuptools import setup, find_packages

setup(
    name='metallograph_segmentation',
    version='0.1.0',
    author='TBD',
    author_email='tbd@ugr.es',
    packages=[*find_packages(".")],
    scripts=['metallograph_segmentation/models/usss/train.py',
    'metallograph_segmentation/models/sm/train.py',
    'metallograph_segmentation/models/sm/inference.py',
    'metallograph_segmentation/models/sm/train_single_model.py',
    'metallograph_segmentation/models/multiview/train.py',
    'metallograph_segmentation/models/multiview/trainK3.py',
    'metallograph_segmentation/models/stacking/train.py',
    'metallograph_segmentation/models/stacking/trainK3.py'],
    url='https://github.com/ari-dasci/S-metallograph-segmentation',
    license='LICENSE',
    description='Code for semantic segmentation models and techniques applied to metal microstructures, in collaboration with ArcelorMittal',
    long_description=open('README.md').read(),
    install_requires=[
        "torch >= 1.7.0",
        "torchvision >= 0.8.0",
        "opencv-python",
        "tensorflow >= 2.0.0",
        "scikit-learn",
        "scikit-image",
        "matplotlib",
        "pandas",
        "segmentation-models-pytorch",
        "pytest",
        "pkginfo >= 1.10"
    ],
)