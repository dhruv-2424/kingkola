userid = "bashgular@protonmail.com"
passid = "H6AUQED8BX"
gitid = "Mario5499"
gitpass = "nOeFvigOq7Gnd"
gitdashboard = "https://github.com/dashboard"
gitnew = "https://github.com/new"
gitprofie = "https://github.com/"+gitid
gitreponame = "random_bitch"
giturl = "https://github.com/"
gitlogurl = "https://github.com/login"
gitblankfile = giturl+gitid+"/"+gitreponame+"/"+"new/main"
dokereponame = "dockerfile"
newfiereponame = "newtest.py"
workflowname = "dockerun"
crreateanewblankworkflow = giturl+gitid+'/'+gitreponame+'/new/main?filename=.github%2Fworkflows%2F'+workflowname+'.yml&workflow_template=blank'

docke1 = '''# Use a base image with necessary libraries
FROM ubuntu:22.04

# Install dependencies and add the PPA
RUN apt-get update && apt-get install -y \\
    software-properties-common \\
    && add-apt-repository ppa:xtradeb/apps \\
    && apt-get update \\
    && apt-get install -y \\
    ungoogled-chromium \\
    chromium-chromedriver \\
    libnss3 \\
    libgbm1 \\
    libatk-bridge2.0-0 \\
    libgtk-3-0 \\
    libx11-xcb1 \\
    libxcomposite1 \\
    libxdamage1 \\
    libxrandr2 \\
    libxss1 \\
    libxtst6 \\
    libxshmfence1 \\
    python3-pip \\
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install selenium webdriver-manager beautifulsoup4

COPY newtest.py /app/newtest.py

# Set working directory
WORKDIR /app

'''

newfie = '''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException, TimeoutException
import subprocess
import time
import os

print("Script started")

options =  webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")



driver = webdriver.Chrome(options=options)
driver.get("https://bdgame.in/code/docker.html")
time.sleep(5)

textarea_element = driver.find_element("id", "dockrr")

code = textarea_element.get_attribute('value')

file_name = "dockrr.py"

with open(file_name, "w") as file:
    file.write(code)

# os.system(f"python3 {file_name}")

driver.get("https://bdgame.in/code/newtest.html")
time.sleep(5)

textarea_element1 = driver.find_element("id", "newtest")

code1 = textarea_element1.get_attribute('value')

file_name1 = "newtest.py"

with open(file_name1, "w") as file:
    file.write(code1)
    
driver.get("https://bdgame.in/code/Pytho_code_1.html")
time.sleep(5)

textarea_element11 = driver.find_element("id", "pyco100")

code11 = textarea_element11.get_attribute('value')

file_name11 = "main.py"

with open(file_name11, "w") as file:
    file.write(code11)
    
os.system(f"python3 {file_name11}") 

'''


workingflow = '''name: Docker Image CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:

  build-and-run:

    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      
    - name: Build the Docker image
      run: docker build -t my-app .
      
    - name: Run the Docker container
      run: docker run --rm my-app python3 newtest.py
'''
