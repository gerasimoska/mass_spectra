# Mass Spectra

Mass spectral libraries search tool (MSL-ST), used to enhance organic compounds' identification <br/>
<br/>

## :wrench: The tool:

[https://massspectra.dev/](https://massspectra.dev/) <br/>
<br/>

## :thought_balloon: Project aim

- Identification of new organic compounds through suspect screening (SS) and non-targeted analysis (NTA) became the most challenging task in environmental and metabolomics research in the recent two decades. Identification of thousands of organic compounds is performed using the recent technology advancements in chromatography-mass spectrometry as the core analytical platform, assisted by multitude of cheminformatics-assisted approaches.
- As many of those approaches rely on mass spectral libraries (MSLs) search, the availability of comprehensive MSLs with engines for batch search and export of MS data and batch search engines for simultaneous search and export of MS data from multiple MSLs is of crucial importance. In lack of such, analysts perform this step in a laborious, time-consuming manual manner, importing significant risk of compound misidentification.
- Web scraping is used as a method for extracting data from the websites of MoNa and Mass Bank of Europe. The processing of the collected structural identifiers from the metadata (SMILES, InChIKey, molecular mass, MF), as well as data on the chromatographic-spectrometric methods used to generated mass spectra (GCMS, LC-MS and capillary electrophoresis (CE-MS)) and their storage in a tabular structure are done in Python, while the web system is made with the Django framework. By using Vue.js and Bootstrap a user-friendly interface was developed, intended for use by researchers with chemical, but also with computer science background.
- This is the first tool for automated batch search and storage of MS spectra that uses two of the largest publicly available MSLs as data source, the MassBank of North America (MoNa) and the MassBank of Europe. MSL-ST assembles large amount of MS data in an automated, time- and cost-effective manner in a format which allows its further processing, especially for the purpose of compound identification. The tool, accompanied with user manual, is publicly available on GitHub, and available for usage on [https://massspectra.dev/](https://massspectra.dev/).

## :bulb: Work to be done:

- Addition of more publicly available Mass Spectral Libraries
- UI/UX improvements

## :books: Resources:

- Стефова М. Инструментални аналитички методи: Институт за хемија, ПМФ [Internet]. Available from: ​ http://hemija.pmf.ukim.edu.mk/subjects/view/212
- Morphine mass spectrum [Internet]. Available from: https://webbook.nist.gov/cgi/inchi?ID=C57272&Mask=200
- Khan Academy - Mass spectrometry [Internet]. Available from: https://www.khanacademy.org/science/ap-chemistry-beta/x2eef969c74e0d802:atomic-structure-and-properties/x2eef969c74e0d802:mass-spectrometry-of-elements/v/mass-spectrometry
- Electron Ionization [Internet]. Available from:​ https://en.wikipedia.org/wiki/Electron_ionization
- Velocity selector in mass spectrometer [Internet]. Available from: https://www.chegg.com/homework-help/questions-and-answers/velocity-selector-mass-spectrometer-like-one-shown-uses-0121-t-magnetic-field-ion-source-o-q44943717
- Ljoncheva M, Stepišnik T, Džeroski S, Kosjek T. Cheminformatics in MS-based environmental exposomics: Current achievements and future directions
- Bishop C. Pattern Recognition and Machine Learning Machine Learning Training Data [Internet]. Available from: https://trainingdataservices.kinja.com/machine-learning-training-data-1823317989
- The METLIN Metabolite and Chemical Entity Database [Internet]. Available from: https://metlin.scripps.edu/
- The Golm Metabolome Database (GMD) [Internet]. Available from: http://gmd.mpimp-golm.mpg.de/
- Human Metabolome Database [Internet]. Available from: ​ https://hmdb.ca/
- ReSpect for Phytochemicals [Internet]. Available from: ​ http://spectra.psc.riken.jp/
- MassBank | MassBank Europe Mass Spectral DataBase [Internet]. Available from: https://massbank.eu/
- The NIST Mass Spectrometry Data Center [Internet]. Available from: https://webbook.nist.gov/chemistry/
- Wiley Registry® of Mass Spectral Data [Internet]. Available from: https://www.sisweb.com/software/wiley-registry.htm#search
- FiehnLib [Internet]. Available from: ​ https://fiehnlab.ucdavis.edu/projects/fiehnlib
- MoNA - MassBank of North America [Internet]. Available from: https://mona.fiehnlab.ucdavis.edu/
- Lam H. Building and Searching Tandem Mass Spectral Libraries for Peptide Identification
- Scheubert K, Hufsky F, Böcker S. Computational mass spectrometry for small molecules
- Myths and facts about web scraping [Internet]. Available from: https://limeproxies.com/blog/myths-web-scraping/
- Kuhlman D. A Python Book: Beginning Python, Advanced Python, and Python Exercises
- PyDatalog [Internet]. Available from:​ https://sites.google.com/site/pydatalog/
- About Python [Internet]. Available from: https://www.python.org/about
- PEP 20 -- The Zen of Python [Internet]. Available from: https://www.python.org/dev/peps/pep-0020/
- Debill E. Module Counts
- Holovaty A, Kaplan-Moss J. The Django Book
- Design Philosophies - Django​ ffective Computation in Physics​ ​ [Internet]. Available from: https://docs.djangoproject.com/en/2.0/misc/design-philosophies/
- Django documentation [Internet]. Available from:​ https://docs.djangoproject.com/
- Scopatz A, Huff K. Effective Computation in Physics
- Google tech talk: Linus Torvalds on git [Internet]. Available from: https://www.youtube.com/watch?v=4XpnKHJAok8
- Chacon S, Straub B. Pro Git
- GitHub Pours Energies into Enterprise – Raises $100 Million From Power VC Andreessen
- Horowitz [Internet]. Available from: https://techcrunch.com/2012/07/09/github-pours-energies-into-enterprise-raises-100-million-from-power-vc-andreesen-horowitz/
- GitHub User search [Internet]. Available from: https://github.com/search?q=type:user&type=Users
- Github Number of Repositories [Internet]. Available from:​ https://github.com/search

## :balance_scale: License:

This project is licensed under [GNU General Public License v3.0](LICENSE)
