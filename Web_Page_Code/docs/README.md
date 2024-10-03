# Webpage Code

## Dependencies
* blinker==1.8.2
* click==8.1.7
* contourpy==1.3.0
* cycler==0.12.1
* et-xmlfile==1.1.0
* Flask==3.0.3
* fonttools==4.53.1
* itsdangerous==2.2.0
* Jinja2==3.1.4
* kiwisolver==1.4.7
* MarkupSafe==2.1.5
* matplotlib==3.9.2
* numpy==2.1.1
* openpyxl==3.1.5
* packaging==24.1
* pandas==2.2.2
* pillow==10.4.0
* pip==22.0.2
* pyotp==2.9.0
* pyparsing==3.1.4
* pypng==0.20220715.0
* python-dateutil==2.9.0.post0
* pytz==2024.2
* qrcode==7.4.2
* setuptools==59.6.0
* six==1.16.0
* typing_extensions==4.12.2
* tzdata==2024.1
* Werkzeug==3.0.4

## Scripts
* main.py: Runs server and renders the html pages.
    * Requirements: Install Dependencies. To ensure images are outputted to the scrollable table, store the images in static/img/death_star_images.
    * Directories:
        * static: holds images and css files
            * css: holds css files
            * img: holds images and background image
                * death_star_images: holds specifically death star images
        * data: holds Obi-Wan password and secret key
        * docs: holds documents (README)
        * templates: holds html files
    * Input: User information.
    * Output: Html pages and allows navigation between the pages.
* otp.py: Checks user's name and password to see if it matches with the one stored in data/users.xlsx. Functions within this file are used in the flask instance (main.py)
    * Requirements: data/users.xlsx with obiwans user name, password, and secret key.
    * Output: If user is obiwan or not obi wan,