[![CircleCI Status](https://circleci.com/gh/uijl/artifact-getter.svg?style=svg)](https://circleci.com/gh/uijl/artifact-getter)
[![Coverage Badge](https://artifact-getter.herokuapp.com/get_coverage_badge?circle_url=https://circleci.com/gh/uijl/artifact-getter&circle_token=4&output=str)](https://artifact-getter.herokuapp.com/get_coverage_report?circle_url=https://circleci.com/gh/uijl/artifact-getter&circle_token=4)

# artifact-getter

Basic Flask server to obtain CircleCI build artifacts. 🏗

Get build artifacts from CircleCI, for both closed and open repositories. A very basic Flask app is deployed to Heroku and you request will be forwarded to the correct page, displaying or returning the build artifact you are looking for.

## Example

Currently only the coverage badge and coverage report build artifacts are supported, but I am working on improving this. An example on how to show the coverage badge in your GitHub readme is shown below. Assuming your coverage badge is named `coverage.svg`, your coverage report is named `index.html`, and you store both in the main build artifact folder, you can build a request as shown below. 

``` markdown
[![Coverage Badge](https://artifact-getter.herokuapp.com/get_coverage_badge?circle_url=<URL_Of_Your_CircleCI_Repository>&circle_token=<Your_CircleCI_API_Token>)](https://artifact-getter.herokuapp.com/get_coverage_report?<URL_Of_Your_CircleCI_Repository>&circle_token=<Your_CircleCI_API_Token>)
```

You need to add the URL of your CircleCI repository, and if you have a closed repository you should get an API key. If you do not have an API key yet, yet can create one following the steps in their [documentation](https://circleci.com/docs/2.0/managing-api-tokens/).

## Installation

You can download the source code from this page by following the lines below.

``` bash
# Download the package
git clone https://github.com/uijl/artifact-getter

# Go to the correct folder
cd artifact-getter

# Install package so that you have the dependencies
pip install -e .

# Start up Flask server
export FLASK_APP = artifact-getter
export FLASK_ENV = artifact-getter
flask run

# Open your webbrowser and visit localhost
http://127.0.0.1:5000
```

## Starting up

The master branch of this repository is automatically deployed to Heroku if all tests pass. To test if your code is ready for deployement you can use the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli). If you have it installed you can run the code `heroku local` to see if it is working.
