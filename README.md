# `mc-precip-iso`: Open monthly stable isotope data of precipitation over the Maritime Continent 


[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub watchers](https://img.shields.io/github/watchers/Naereen/StrapDown.js.svg?style=social&label=Watch&maxAge=2592000)](https://github.com/sandyherho/mc-precip-iso/watchers)
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

![DOI](https://zenodo.org/badge/671343723.svg)](https://zenodo.org/badge/latestdoi/671343723)

[![python](https://img.shields.io/badge/python-★★★-lightgrey?labelColor=3776AB&logo=Python&style=for-the-badge&logoColor=white)](https://www.python.org/)
![Overleaf](https://img.shields.io/badge/-Overleaf-47A141?logo=Overleaf&style=for-the-badge&logoColor=white)


This GitHub repository contains observational data on the traditional monthly isotopic compositions of the precipitation ($\delta^{2}$ H and $\delta^{18}$ O) over the Maritime Continent, collected from [62 stations](https://github.com/sandyherho/mc-precip-iso/blob/main/output_data/sta_list.csv) throughout Indonesia, along with the Python code used to process them. The data collection process was performed from September 2010 to September 2017.

 We used the Picarro L2120-i water isotope analyzer with calibration using three water isotope standards, Aqua Standard<sup>&reg;</sup>. DOW, SLW2, and ICE2 at [the Hydrology Laboratory of Kumamoto University, Japan](https://www.fast.kumamoto-u.ac.jp/gsst-en/department/masters_c/science/earth_and_environmental_sciences/). The cleaning process and simple data analysis were conducted at [the Weather and Climate Prediction Laboratory (WCPL) of Bandung Institute of Technology (ITB), Indonesia](https://www.meteo.itb.ac.id/en/lab-of-meteorological-analysis/). The following are the individuals involved in this project: [R. Suwarman](https://scholar.google.com/citations?user=NfMfR8LMVz8C&hl=en), [S. H. S. Herho](https://scholar.google.com/citations?user=uYQgjxMAAAAJ&hl=id), [H. A. Belgaman](https://scholar.google.co.id/citations?user=BnuFrE8AAAAJ&hl=en), [D. E. Irawan](https://scholar.google.com/citations?user=Myvc78MAAAAJ&hl=en), [K. Ichiyanagi](https://researchmap.jp/kimpei/research_experience/16460562?lang=en), and [M. Tanoue](https://scholar.google.co.id/citations?user=0IdG2G4AAAAJ&hl=en).

### License
These data and code were released under the [GPL-3.0 License](https://github.com/sandyherho/mc-precip-iso/blob/main/LICENSE.txt).

### Citation
If you find these data useful, please  consider citing our paper:


`
@article{SuwarmanEtAl23,
         author={Suwarman, R. and  Herho, S. H. S. and Belgaman, H. A. and Irawan, D. E. and Ichiyanagi, K. and Tanoue M.},
         title={},
         journal={xxxxx},
         year={2023},
         volume={x},
         number={x},
         pages={x - x},
         doi={xx}
}
`

### Requirements

We produced the data under the [Python 3](https://www.python.org/) computing environment by using the following libraries:

- [matplotlib](https://matplotlib.org/)
- [numpy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [pygmt](https://www.pygmt.org/)
- [pymc3](https://www.pymc.io/projects/docs/en/v3/index.html)
- [scikit-learn](https://scikit-learn.org/)
- [seaborn](https://seaborn.pydata.org/)

### Acknowledgements
We are grateful to Michael N. Evans (UMD) for discussing fractionation on precipitation isotopes in the tropics, which was useful in producing these data. This study was supported by ITB Research, Community Service and Innovation Program (P3MI-ITB), Japan Society for the Promotion of Science (JSPS) KAKENHI (#24510256 and #16H05619), and the National Science Foundation (NSF) (#AGS1903626).
