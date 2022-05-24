# **Domain Checker 🌐**

![demo_video](static/dga_demo.gif)

## ✔️ **Description** 📑
___
The aim of this project is to build a machine leraning classifier web app  which can help us detect a potential machines infected by the DGA (Domain Generation Algorithm) malware.
Typically machines that are infected tend to generate a bunch of random domain names which will contain one active C&C server.
<br><br>
This application guides users on 
detecting potential DGA (Domain Generation Algorithm) generated malware domains
to avoid maleware attack also other numerous purposes including educational purposes.

<!--  -->

## **✔️ Libraries and tools 🛠️**
___
<a href="https://www.python.org" target="_blank"> <img src="https://img.icons8.com/color/48/000000/python.png"/> </a>
<a href="https://git-scm.com/" target="_blank"> <img src="https://img.icons8.com/color/48/000000/git.png" height="50"> </a>
<a href="https://code.visualstudio.com/" target="_blank"> <img src="https://img.icons8.com/color/48/000000/visual-studio-code-2019.png"/>
    <img height="45" src="https://img.icons8.com/dusk/64/000000/anaconda.png"/>
    <img height="30" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1280px-Scikit_learn_logo_small.svg.png">
    <img height="30" src="https://raw.githubusercontent.com/numpy/numpy/7e7f4adab814b223f7f917369a72757cd28b10cb/branding/icons/numpylogo.svg">
    <img height="30" src="https://raw.githubusercontent.com/pandas-dev/pandas/761bceb77d44aa63b71dda43ca46e8fd4b9d7422/web/pandas/static/img/pandas.svg">
    <img height="30" src="https://matplotlib.org/_static/logo2.svg">
    <img height="30" src="https://jehyunlee.github.io/2020/09/09/Python-DS-31-seaborn_upgrade/31-seaborn_upgrade_1.png">
    <img height="50" src="https://cdn3.iconfinder.com/data/icons/social-media-2169/24/social_media_social_media_logo_docker-512.png">
    <img height="50" src="https://p7.hiclipart.com/preview/508/316/14/flask-by-example-python-web-framework-bottle-bottle.jpg">
    <a href="https://aws.amazon.com/" target="_blank"> <img src="https://img.icons8.com/color/48/000000/amazon-web-services.png"/> </a>
    



##  **✔️ Tech stack**
___
    * Python 
    * flask
    * Numpy
    * Matplotlib
    * Seaborn
    * Pandas 
    * Scikit-learn
    * nltk
    * Joblib
    * Docker 
    * AWS

## **✔️ Deployment 🚀**
___
This app was containerized with the docker contrainer and the app image was pushed to docker hub and deployed on [AWS](https://aws.amazon.com/)

**Link to Domain Checker web app : [Domain checker app](#)**

**Link to Domain Checker docker image : [Domain checker app image](https://hub.docker.com/repository/docker/bestnyah/domain-checker)**


## **✔️ Project Organization 📌**
___
    DOMAIN CHECKER
    .
    ├── app.py
    ├── config.py
    ├── dataset
    │   └── dga_data.csv
    ├── model_build_binary_class.ipynb
    ├── models
    │   ├── trained_rf_dga_classifier.sav
    │   └── Xtrain.pkl
    ├── __pycache__
    │   ├── config.cpython-310.pyc
    │   └── utils.cpython-310.pyc
    ├── README.md
    ├── static
    │   ├── css
    │   │   └── main.css
    │   └── hero_img.svg
    ├── sub_class_model.ipynb
    ├── templates
    │   ├── index.html
    │   └── predict.html
    └── utils.py
