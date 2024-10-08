# Team 11

Table of Contents 
* Links to each section for easy navigation.
    * 2FA
    * ImageAI 
    * Flask  


Exfiltration and Dissemination of the DeathStar(Project Title)

## Project Description
- This project is a simulation of a stealth operation where a very high profile plans: Death Star plans, are transmitted from a raspberry pi to a rebel server secretly and then is made available to the galaxy(public at large). This high profile information must be transferred without the detection by the imperial guards.
-  The plans would be accessible to the galaxy the moment the plans have been uploaded to the rebel server. the webpage will analyze the plans looking for weakness(identifiable by the red circles). The webpage will in the display format of a scrollable table of image that are representing the contents of a red circle from the plans.
-  The project demonstrates secure data transmission, image processing, and dynamic UI display on mobile devices, all within the context of a stealth mission.
Description of each repository


## Design Objectives
- Detect Death Star images. 
- Compress and encrypt the Death Star images. 
- Transmit the Death Star images to the Rebel Army’s server. 
- The server detects any red circles in the Death Star plans. 
- The server hosts a public website where weaknesses are displayed and downloadable. 
- The entirety of Princess Leia’s video can only be viewed by Obi-Wan.


## Design Requirements 
- The system shall detect at least 60% of the Death Star images from a library of 1024x1024 pixel PNG images.
- The Death Star images shall be compressed by at least 5 percent of the original Death Star image.
- The Death Star images shall be encrypted following DES.
- The Death Star images shall be transferred wirelessly to the server by displaying 2D barcodes on a monitor in the lab and capturing the 2D barcodes using cameras connected to the server.
- Communication between the lab and the rebel server shall be bidirectional for a range of at least 5 meters using monitors and cameras.
- The server shall detect the Death Star weaknesses in the images.
- The server shall host a self-developed webpage through the use of webpage hosting software.
- The webpage shall be viewable to anyone with the web address to the webpage who is connected to Wright State University’s ‘WSU_EZ_CONNECT’ network.
- The webpage shall display at least 1 Death Star weakness.
- The webpage shall contain a scrollable table containing at least 1 image of the Death Star weakness.
- The webpage shall allow the Death Star weaknesses displayed to be downloaded.
- The webpage shall allow any user to view the non-confidential part of Princess Leia's video.
- The webpage shall only allow Obi-Wan to view the entire Princess Leia video.




## Design Requirements Definition
- System: The Raspberry Pi and other components inside of the lab.
- Death Star images: 1024 x 1024 pixel PNG files that depict a weaponized space station.
- Detect: Being able to distinguish between target images and miscellaneous images.
- Compressed: A way of reducing the size of the images, so they can be transferred more quickly.
- Encrypted: A way of changing data so it can not be easily understood.
- DES: A Data Encryption Standard that uses symmetric keys for data encryption.
- Wirelessly: Using visible light to transfer information.
- Server: The device that will collect transferred information.
- Communication: Data transfer between the Raspberry Pi in the lab and the server outside the lab using 2D barcodes.
- Bidirectional: The transmitter can send information to the receiver and vice versa.
- Death Star Weaknesses: Flaws in the Death Star images that are identified with red circles.
- Viewable: The ability to be seen.
- Connected: Using the specified network to access the internet.
- Downloaded: A way of retrieving data from the webpage.
- Princess Leia Video: A video created by Princess Leia that contains a personal message, with some information to only be viewed by Obi-Wan.

## DESIGN CONSTRAINTS
- The server and its components shall not be within 5 meters of the lab window.
- The equipment shall cost $300 or less.
- The images of Death Star weaknesses displayed shall be in a scrollable table.
- The images of Death Star weaknesses displayed shall be unique.
- The system shall operate within the temperature range of 58°F - 82°F.
- The system shall operate within a room with outlets with a voltage range between 110V - 130V and a current range between 100A - 200A.
- The system shall not exceed 50 pounds.
- The portion of the system that resides in the basement lab shall not exceed the dimensions of the basement lab in the Russ Engineering Center excluding the size of the items within the lab.
- The portion of the system that resides outside the lab shall not exceed the dimensions of 1 cubic meter excluding the required distance between this portion of the system and the lab.
- The project shall be completed before 2024-12-7.






##  FLASK(Repository)
- main.py: Runs server and renders the html pages.
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
otp.py: Checks user's name and password to see if it matches with the one stored in data/users.xlsx. Functions within this file are used in the flask instance (main.py)
* Requirements: data/users.xlsx with obiwans user name, password, and secret key.
* Output: If user is obiwan or not obi wan






