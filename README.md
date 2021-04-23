<div align="center">
  <img src="static/assets/images/readme/uR-Responsive.png">
  <h1>Tabletop-READY</h1>
<hr>

**A miniature painting commission e-commerce app with full user and admin functionality**

This app was built using [GitHub](https://pages.github.com/) and deployed to [Heroku](https://www.heroku.com/).

Visit the live site [here](https://tabletop-ready.herokuapp.com/)

</div>

---

## <u>Table of contents</u>

**<details><summary> User Experience (UX)</summary>**
  - [Scope](#scope)
  - [Design](#design)
  - [User stories](#user-stories)
  - [Wireframes](#wireframes)
</details>

**<details><summary> Features</summary>**
  - [Features](#features)
  - [Version and future](#version-and-future)
  - [Status](#status)
</details>

**<details><summary> Technologies</summary>**
  - [Languages](#languages)
  - [Frameworks, Libraries & Programs](#frameworks-libraries-programs)
</details>

**<details><summary> Deployment</summary>**
  - [Deploy to Heroku](#deploy-to-heroku)
  - [Accessing code](#accessing-code)
</details>

**<details><summary> Testing</summary>**
  - [Testing Documentation](https://github.com/NikolasKotsikos/uReview/blob/master/testing.md)
</details>

**<details><summary> Credits</summary>**
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)
</details>

**<details><summary> Contact</summary>**
  - [Contact details](#contact-details) 
</details>

# &rarr; **User Experience (UX)**

### **<u>Scope</u>**

The scope of this app is to create a Python and Django based e-commerce site for an imaginary miniature painting commissions service. Tabletop ready offers the advantage of a combined price for receiving a miniature
ready to use in your tabletop games. It aims to provide all relevant and expected functionality commonly found in e-shops to visitors, as well as an easy to use toolset for the site owner, customised to the specific product's demands. The app supports payments via Stripe and uses an 
AWS S3 bucket for media and static file storage.

### **<u>Wireframes</u>**

As part of the design process, before starting my project I made initial wireframes using [Lucidchart](https://lucidchart.com). Creating these mock-ups helped me plan the basic structure and arrangement of the features for my site.

The final design has been influenced by my mentor and the need to redesign and simplify some features. In this senses the wireframes map the journey from idea to functioning app.

- [Homepage](static/assets/images/readme/pdfs/home.pdf)
- [Create account page](static/assets/images/readme/pdfs/create-account.pdf)
- [Log in page](static/assets/images/readme/pdfs/log-in.pdf)
- [Reviews page](static/assets/images/readme/pdfs/reviews-visitor.pdf)
- [Add/Edit review page](static/assets/images/readme/pdfs/add-edit-review.pdf)
- [Read review page visitor view](static/assets/images/readme/pdfs/read-review-visitor.pdf)
- [Read review page user view](static/assets/images/readme/pdfs/read-review-user.pdf)
- [Mobile view](static/assets/images/readme/pdfs/mobile.pdf)
- [Tablet view](static/assets/images/readme/pdfs/tablet.pdf)


### **<u>Design</u>**

**Structure**

- A simple design structure with a fixed navbar, a dropdown side navigation menu accessible from every page and a fixed footer. A brand logo is displayed in the top left of the screen to allow easy navigation back to the homepage.

- As a mobile first site I contained the logo, login button and nav menu icon centered by two spaces creating a core towards the center of the page. This helps keep the design consistent as it moves from smaller to larger viewports.

- As well as including a title tag on my base.html, I have also added the meta description tag to help optimize my click-through rate from search engine result pages.

**Colour palette**

- The #333333 shade of grey has been used for the main background throughout the site with all the forms using a #fafafa shade of white creating a slight contrast.

- Default Bootstrap white (#fff) was used as a background for the navbar as well as the colour of various UI buttons throughout the site. 

- The #fafafa shade of white has been used as a background for cards and forms throughout the app.

- The ##7ab648 shade of green has been used as the accent colour for title text throughout the website, as well as the color of more prominent callouts and buttons.

- I decided on this neutral colour scheme as the colours allow the images in the site to stand out more, with images being central to app's function and presentation. 

<img src="static/assets/images/readme/palette.png">

**Typography**

- The main font used throughout the site is 'Lato' which belongs to the sans-serif typeface family. The font is clean and elegant, making it a good choice for web design.

- I have used the 'Julius Sans One' font to create the 'Tabletop-READY' logo as it pairs well with my overall branding. Moreover it has been used as the font for titles and fonts around the site.


**Logo Design**

- A minimal design so as not to visually challenge the images, using typography and css to make it high-res and responsive. The color #333333 is used as it is a shade of grey commonly used in miniatures and green represents both ready and painted as the only touch of color.

- Following website conventions, my website logo is a link to the homepage. Over time many people have learned that clicking on a site’s logo leads them back to the homepage so adopting this standard reduces confusion by matching the UI to users’ expectations. The logo is also left-aligned which is the most familiar placement, and is where users look to find it.


### <u>**User stories**</u>

| User Story  #              | As a/an              | I want to be able to...                             | So that I can...                                |
| -------------------------- | -------------------- | --------------------------------------------------- | ----------------------------------------------- |
|                            |                      | Viewing and Site Navigation                         |                                                 |
| 1                          | Visitor              | View a gallery of painted models.                   | Decide if I like the painting style.            |
| 2                          | Visitor              | Easily navigate the shop.                           | See if there's something I want to buy.         |
| 3                          | Visitor              | Easily view the total of my commission anytime.     | Avoid spending too much.                        |
|                            |                      | Registration and User Accounts                      |                                                 |
| 4                          | Site User            | Easily register for an account.                     | Have a personal account and be able to view     |
|                            |                      |                                                     | my profile.                                     |
| 5                          | Site User            | Easily login or logout.                             | Access my personal account info.                |
| 6                          | Site User            | Receive an email confirmation after registering.    | Verify that my account reg. was successfull.    |
| 7                          | Site User            | Have a personalized user profile.                   | View my personal order history and save my      |
|                            |                      |                                                     | shipping and payment info.                      |
|                            |                      | Sorting and Searching                               |                                                 |
| 8                          | Visitor              | Sort the list of available miniatures by keyword.   | Easily find the miniature I am looking for.     |
| 9                          | Visitor              | Sort miniatures by the game system (i.e. WH40K)     | Find available miniatures from a system         |
|                            |                      | I am interested in.                                 |                                                 |
| 10                         | Visitor              | Sort miniatures by faction and subfaction.          | Find a specific miniature I want to commission. |
| 11                         | Visitor              | Easily see what I've searched for and the           | Quickly decide whether the miniature            |
|                            |                      | number of results.                                  | I want is available.                            |
|                            |                      | Commision Set-Up and Checkout                       |                                                 |
| 12                         | Visitor              | Easily select the finishing level for my miniature. | Ensure I am not paying over my set budget.      |
| 13                         | Visitor              | View items in my commission to be purchased.        | Identify the total cost of my purchase and all  |
|                            |                      |                                                     | miniatures I will receive.                      |
| 14                         | Visitor              | Easily enter my payment information.                | Check out quickly and with no hassles.          |
| 15                         | Visitor              | Feel my personal and payment info is secure.        | Confidently provide the needed info to order a  |
|                            |                      |                                                     | commission.                                     |
| 16                         | Visitor              | Receive an email confirmation after checking out.   | Keep the confirmation of what I've purchased.   |
|                            |                      | Admin and Store Management                          |                                                 |
| 17                         | Owner                | Add a miniature, army or game system.               | Extend the range of miniatures provided.        |
| 18                         | Owner                | Edit/update a miniature, army or game system.       | Change miniature info, images etc.              |
| 19                         | Owner                | Delete a miniature, army or game system             | Delete an existing miniature or army .          |

 > **Note**: The user stories are tested in [testing.md](https://github.com/NikolasKotsikos/uReview/blob/master/testing.md).

## &rarr; **Database Architecture**

- ** <u>Data Schema</u> **

  <img src="static/assets/images/readme/db-schema.png">

    The `Miniature` model within the miniature's app, is used to store information about individual miniatures.
    The `Army` model within the miniature's app, is used to group miniatures into specific armies.
    The `Game Systems` model within the miniature's app, is used to group miniatures into specific game systems.

    The `UserProfile` model within the profiles app is used to store user's profile information and is connected to the checkout `Order` model - to store the user's checkout information, as well as order history.   

    The `Order` model within the checkout app, is used to store orders.
    The `OrderLineItem` model within the checkout app, is used to store information about individual miniatures on the order.
    
    The `Gallery` model within the gallery app, is used to store gallery items created by the admin user.

## &rarr; **Features**

- **Responsive on all device sizes**
  - Mobile-first design, responsive on all devices through using the Materialize grid system and CSS media queries.

- **A user-friendly interface with easy navigation throughout the site**
  - Attractive, minimalistic design with visuals and information presented clearly and concisely.

  - Easily readable fonts and simple navigation throughout the site.
    - Fixed navigation bar visible on every page including a menu dropdown and brand logo to link back to the homepage.

  - Aesthetically pleasing 404 & 500 error pages if the user is directed to a non-existent page or encounters an internal server error.

- **Buttons**
    - Clear interactive buttons used for a effortless user journey.

- **Forms**
  - Forms used for login and register pages, and adding/editing reviews and genres & platforms.

  - Materialize form elements used include input fields, text area fields, select dropdowns and submit buttons.

- **Card Previews**
  - Used to display reviews & genre and platform armies.

  - Images included contributing to the visual look.

- **Modals**
  - Used for delete confirmation and admin edit genres and platforms tools.

- **Carousel**
  - Used for sorting reviews by genre and platform displayed on the homepage.

- **Search bar**
  - Allows the user to search reviews by keywords using text index searching. Review names, genre and platform names, developer names and release years can be used as keywords for the query.

- **Flash Messages**
  - Used for login and register form error responses.

### **Version and Future**

#### Status

> App Version: <u>1.0</u>

I will continue to update my website as I grow my platform of users. Most things I wanted to add are there but the ones I didn't are listed bellow.

**Future Development plans**
- Add bookmarks button on reviews.

- Allow for user created review collections.

- Add text formating tools to add/edit review forms.

---

## &rarr; **Technologies**

#### <ins>Languages</ins>

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)

#### <ins>Frameworks, Libraries & Programs</ins>

- [**Django**](https://www.djangoproject.com/)
  - Python Web framework used to build the site.

- [**Git**](https://git-scm.com/)
  - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.

- [**GitHub**](https://github.com/)
  - GitHub is used to store the project code after being pushed from Git.

- [**Heroku**](https://www.heroku.com/)
  - Heroku is the app platform I deployed my project to.

- [**Heroku Postgres**](https://www.heroku.com/postgres)
  - Heroku’s reliable and powerful database used to store the data for my deployed Heroku App.

- [**jQuery:**](https://jquery.com/)
  - A javascript library used to simplify DOM manipulation.

- [**Bootstrap 4.5.3**](https://getbootstrap.com/)
  - Bootstrap was used to assist with the responsiveness and styling of the website using design templates.

- [**Boto3**](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    - Python SDK for AWS, used to directly create, update, and delete AWS resources from my Python scripts.

- [**gunicorn**](https://gunicorn.org/)
   - WSGI server used to take care of everything happening between the web server and web application.

- [**pillow**](https://pypi.org/project/Pillow/2.2.1/)
    - Python Imaging Library (PIL), used to add support for opening, manipulating, and saving images.

- [**psycopg2**](https://pypi.org/project/psycopg2/)
    - PostgreSQL database adapter

- [**AWS**](https://aws.amazon.com/)
  - A cloud-based storage service used to store static and, media files.

- [**Stripe**](https://stripe.com/gb)
  - Stripe was used to deal with payments.

- [**Temp Mail**](https://temp-mail.org/en/)
  - Temp Mail was used to provide temporary, secure, anonymous, free, disposable email addresses for testing purposes.

- [**Google fonts**](https://fonts.google.com/)
  - Google fonts were used to import the fonts into the CSS file which is used on all pages throughout the project.

- [**Font Awesome 4.7.0**](https://fontawesome.com/)
  - Font Awesome was used to add icons for aesthetic and UX purposes.

- [**Flaticon**](https://www.flaticon.com/)
  - Provided icons throughout site.

- [**Lucidchart**](https://lucidchart.com/)
  - Balsamiq was used to create the wireframes during the design process.

- [**Grammarly**](https://www.grammarly.com/)
  - Grammarly was used to ensure any grammar errors are eliminated.

- [**HTML Formatter**](https://www.freeformatter.com/html-formatter.html) and [**CSS Formatter**](https://www.freeformatter.com/css-beautifier.html)
  - Used to format my HTML and CSS files with the desired indentation level for optimal readability.

- [**W3 Validator**](https://validator.w3.org/#validate_by_input) and [**W3C CSS Validator**](https://jigsaw.w3.org/css-validator/#validate_by_input)
  - Used to validate my HTML and CSS files

- [**JShint**](https://jshint.com)
    - Used to validate JS code

- [**PEP8 online**](http://pep8online.com)
    - Used to check code for PEP8 requirements.

- [**Tables Generator**](https://www.tablesgenerator.com/markdown_tables)
  - Used to create tables in my readme file.

- [**Favicon**](https://favicon.io/)
    - Used to create a favicon, displaying my logo on a web browser next to the web address bar, the browser tab, and the bookmarks bar.

- [**Techsini**](http://techsini.com/multi-mockup/index.php)
    - Multi Device Website Mockup Generator Tool

- [**Resize Pixal**](https://www.resizepixel.com/download) 
    - To help compress image sizes

## [&#8679;](#table-of-contents)
---

## &rarr; **Deployment**

#### <ins>Deploy to Heroku</ins>

The project was deployed to Heroku with all static and media files stored on Amazon S3. I also set up automatic deployment to ensure my Heroku app was always up to date with my GitPod repository.

> **Note:** As all static and media files were stored in an AWS bucket and content was created in admin, these are not available through the GitHub repository. Please contact the site owner if you wish to use any of the images or content included.

<details>
<summary>Deploying to Heroku</summary>
<p>

> **Note:** Before following the below steps ensure you have already created your new repo in Github.

1. Log in (or Register) to [Heroku](https://www.heroku.com/) and from your dashboard click 'new' > 'create new app'.

   ![New app btn](readme/media/new-app.png)

2. Enter your 'App name' and choose the appropriate region, then click 'Create app'.
   > **Note:** 
 The app name must be unique, all lowercase, and '-' to be used instead of spaces.
The region chosen should be the one closest to you.

   ![Create new app](readme/media/create-new-app.png)

3. Then on the 'Resources' tab, search and add on the Heroku Postgres database.

4. To use Postgres, install dj_database_url, and psycopg2 in the project terminal using the following commands;

    `$ pip3 install dj_database_url`

    `$ pip3 install psycopg2`

5. Freeze the requirements to ensure Heroku installs all the apps requirements when deployed using the following command;

    `$ pip3 freeze > requirements.txt`

6. To migrate to the Postgres, go to settings.py and add the following import;

    `import dj_database_url`

   Then down in the databases setting comment out the default configuration and replace the default database with a call to dj_database_url.parse and give it the database URL from Heroku.

   ![Config Vars](readme/media/database_url.png)

    > **Note:** You can either get the database URL from your config variables in your app settings tab or from the command line by typing Heroku config.

7. Apply all migrations using the following command;

    `$ python3 manage.py migrate`

    After migrations have been applied amend your database configurations to;

    ![Config Vars](readme/media/database_url2.png)

     > **Note:** This will ensure that your Postgres database is used in deployment and your sqlite3 in development.
    
    Your database should now be all set up.

8. Create a superuser to log in with using the following command;

    `$ python3 manage.py createsuperuser`


9. Go to the Settings tab on Heroku, scroll to the 'Config Vars' section, and click 'Reveal Config Vars'. 

   Enter the variables (key and value) contained in your environment settings or stored in an env.py. The keys are listed below and values are inputted by the user.

| Key               | Value               |
|-------------------|---------------------|
| AWS_ACCESS_KEY_ID | To be added by user |
| AWS_SECRET_KEY_ID | To be added by user |
| USE_AWS           |        TRUE         |
| DATABASE_URL      | To be added by user |
| EMAIL_HOST_PASS   | To be added by user |
| EMAIL_HOST_USER   | To be added by user |
| SECRET_KEY        | To be added by user |
| STRIPE_PUBLIC_KEY | To be added by user |
| STRIPE_SECRET_KEY | To be added by user |
| STRIPE_WH_SECRET  | To be added by user |

10. Install gunicorn using the following command;

    `$ pip3 install gunicorn`

    Then freeze into your requirements file.

11. Create a Procfile and add the following line;

    `web: gunicorn tabletop_ready.wsgi:application`

    This tells Heroku to create a web dyno which will run gunicorn and serve the Django app.

    > **Note:** The **P**rocfile must be assigned a capital P.

12. Last, you need to temporarily disable collectstatic to ensure that Heroku won't try to collect static files when we deploy. This is done by adding the below variable;

    | DISABLE_COLLECTSTATIC  | 1 |

13. Add the hostname of your Heroku app to allowed hosts in settings.py

14. Now you can commit all the changes and push to GitHub;

    `$ git add .`
    `$ git commit -m <'your commit message'>`
    `$ git push`

    If you created your app on the website you will need to initialize your Heroku git remote using the following command;

    `$ heroku git:remote -a tabletop-ready`

    Then use the following command to push to Heroku;

    `$ git push heroku master`

</p>
</details>

<details>
<summary>Deploying AWS Static and Media files</summary>
<p>

The project used Amazon Web Services s3, which is a cloud-based storage service, to store static and media files.

1. Create an account by navigating to [aws.amazon.com](https://aws.amazon.com/) and clicking create an AWS account. Fill in your email and password, and a username for your account, and select continue.

2. Now on the account type page, select personal and fill out the required information, click create an account and continue.

3. Next you will be asked to enter a credit card number which will be used for billing if we go above the free usage limits. Beyond this, you'll be asked a couple more verification questions then once all required information is confirmed your account will be created.

   > **Note**: For this project, I didn't go anywhere near the usage limits but keep in mind that AWS is not free if you go above the free usage limits.

4. Now you can navigate back to [aws.amazon.com](https://aws.amazon.com/) and sign-in to your account.

5. Navigate to AWS management console under my account and using the 'find services' search bar, find s3.

6. Now open s3 and create a new bucket to store all your files.

- Enter a name for your bucket
    > **Note**: I'd recommend naming your bucket to match your Heroku app name.

- Select a region
    > **Note**: Select the region closest to you like you did when creating your Heroku app.

- Uncheck block all public access and acknowledge that the bucket will be public.
    > **Note**: Allows public access to our static files.

- Click create bucket and your bucket should be created.

7. Now click into your new bucket and set some settings;

- On the properties tab and turn on static website hosting.

    > **Note**: For the index and error document, just fill in some default values.

- On the permissions tab 

  - Paste in a **CORS Configuration** to set up the required access between your Heroku app and this s3 bucket. Copy the code below supplied by CodeInstitute;

        [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
        ]

  - In the **Bucket Policy** tab, select policy generator
    - Policy type is 's3 bucket policy'
    - Allow all principles using a *
    - Actions is 'GetObject'
    - Add in your ARN (found on previous page)
    - Click 'Add statement' then 'Generate policy'
    - Copy the policy code and paste it into the bucket policy editor

       > **Note:** To allow access to all resources in this bucket add a slash star onto the end of the resource key.
    
    - Click save

  - In the **Access Control List** tab, under the Public Access section, set the list objects permission to everyone.

8. Create a user to access the bucket created.

- Search for a new service 'IAM'
- Now open IAM, navigate to 'groups' and click 'Create new group'

  > **Note:** You can call your group whatever you want but try to give it a name that makes sense to you for what it is.

- Create a policy by navigating to 'policies' and click 'Create policy'
- Go JSON tab and click 'import managed policy'
  - Search for s3 and then import the s3 full access policy.
    - Replace resource value '*' with your bucket ARN from the bucket policy page;

    "Resource": [
        "arn:aws:s3:::tabletop-ready",
        "arn:aws:s3:::tabletop-ready/*"
    ]

  - Click 'Review policy', give it a name and a description and click 'Create policy'

9. Attach the policy to the group you created.
- Navigate to 'groups', select the group you created and on permissions tab select 'Attach policy'.
- Search for the policy you created, select it and click 'Attach policy'.

- Now to create the user, navigate to 'users' and click 'Add user'
  - Add username, select programmatic access and click 'Next'
  - Add user to a group by selecting the group you created and click 'Next' then click through to the end and click 'Create user'
  - Now download the CSV file which will contain this users access key and secret access key

    > **Note:** It's very important you download and save this CSV because once you've gone through this process we can't download them again.

10. To connect to Django, head to your project and install two new packages then freeze them into your requirements.txt;
  - $ pip3 install boto3
  - $ pip3 install django-storages
  - $ pip3 freeze > requirements.txt

11. In settings, add 'storages' to installed apps.

12. To connect Jdango to s3 add the below settings in settings.py which will tell it which bucket it should be communicating with;

        if 'USE_AWS' in os.environ:
            AWS_STORAGE_BUCKET_NAME = 'tabletop-ready'
            AWS_S3_REGION_NAME = 'eu-west-2'
            AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
            AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
            AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'


13. Create a file called custom_storages.py and add the content below;

        from django.conf import settings
        from storages.backends.s3boto3 import S3Boto3Storage


        class StaticStorage(S3Boto3Storage):
            location = settings.STATICFILES_LOCATION


        class MediaStorage(S3Boto3Storage):
            location = settings.MEDIAFILES_LOCATION

    Then in settings.py add the below:

        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
</p>
</details>

<details>
<summary>Setting up Automatic Deployment to Heroku</summary>
<p>

1. From the Heroku deploy tab, select the Deployment method 'GitHub'.
   
2. On the 'Connect to GitHub' section make sure your GitHub profile is displayed then add your repository name and click 'Search'.

    > **Note:** This is the name of your repo in GitHub. It is good practice to use an identical name for your Heroku app.

   3. Your repo should now be displayed below, click 'Connect' to connect to this app.

4. Go to the Deploy tab on Heroku and under the Automatic deployment section, click 'Enable Automatic Deploys'. Then under Manual deploy click 'Deploy Branch'.

   - Heroku will now receive the code from GitHub and start building the app using the required packages.
   - Once built you will receive the message 'Your app was successfully deployed' and you can click 'View' to launch your new app.

        > **Note:** 
        In Manual deploy dropdown 'master' is selected'

</details>

`Sensitive data` for your project can either be stored in your environment settings or be added to an env.py file in your workspace.

<details>
<summary>More details on creating an env.py file</summary> 
<p>

1. Add a env.py file to store environment variables:

    `os.environ.setdefault("Key", "Value")`


| Key               | Value               |
|-------------------|---------------------|
| AWS_ACCESS_KEY_ID | To be added by user |
| AWS_SECRET_KEY_ID | To be added by user |
| DATABASE_URL      | To be added by user |
| EMAIL_HOST_PASS   | To be added by user |
| EMAIL_HOST_USER   | To be added by user |
| SECRET_KEY        | To be added by user |
| STRIPE_PUBLIC_KEY | To be added by user |
| STRIPE_SECRET_KEY | To be added by user |
| STRIPE_WH_SECRET  | To be added by user |

 2. Add env.py to your .gitignore file to ensure this file is never pushed to GitHub.
    > **Note:** The env.py mustn't be tracked as any GitHub user can access your confidential data.

</p>
</details>

#### <ins>Accessing code</ins>

Forking allows you to create a copy of the original repository and propose changes to the repository owner via a pull request.

<details>
<summary>Forking the GitHub Repository</summary>
<p>

1. Log in to GitHub and locate the GitHub Repository.
    
    The Tabletop-Ready repository can be found [here](https://github.com/NikolasKotsikos/tabletopready/)

2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.

     ![forking](readme/media/fork.png)

3. You should now have a copy of the original repository in your GitHub account.

</p>
</details>

When you clone a repository, the repository is copied on to your local machine, allowing you to use the project as a starting point for your own idea.

<details>
<summary>Making a Local Clone</summary>
<p>

1. Log in to GitHub and locate the GitHub Repository.
   
   The Tabletop-Ready repository can be found [here](https://github.com/NikolasKotsikos/tabletopready/)

2. Under the repository name, click the "download code" option.

   ![Clone](readme/media/clone.png)

3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.

   ![Clone-link](readme/media/clone-link.png)

4. Open Git Bash

5. Change the current working directory to the location where you want the cloned directory to be made.

6. Type git clone, and then paste the URL you copied in Step 3.

    ```
    $ git clone https://github.com/YOUR-USERNAME/tabletopready.git
    ```

7. Press Enter. Your local clone will be created.

    ```
    $ git clone https://github.com/YOUR-USERNAME/tabletopready.git

    > Cloning into `tabletopready`...
    > remote: Enumerating objects: 299, done.
    > remote: Counting objects: 100%, (299/299),  done.
    > remote: Compressing objects: 100% (156/156), done.
    > Receiving objects: remove: Total 299 (delta 145), reused 267 (delta 126), pack-reused 0
    > Receiving objects: 100% (299/299), 4.61MiB | 2.98 MiB/s, done.
    > Resolving deltas: 100% (145/145), done. Unpacking objects: 100% (10/10), done.
    ```

    Now, you have a local copy of your fork of the tabletopready repository.

    > **Note:** The repository name and output numbers that you see on your computer, representing the total file size, etc, may differ from the example I have provided above.

8. Either store your sensitive data in your environment settings or add an env.py file to your workspace (More details above).

   > **Note:** Contact the site owner if you want more information on the environment variables that have been included.

9. Install all requirements using the following command;

    `$ pip3 install -r requirements.txt`

10. Apply all migrations using the following command;

    `$ python3 manage.py migrate`
    
    Your database should now be all set up.

11. Create a superuser to log in with using the following command;

    `$ python3 manage.py createsuperuser`

12. You can now run your project locally using the following command;

    `$ python3 manage.py runserver`

</p>
</details>

## &rarr; **Credits**

#### Content

- 

#### Media

> **Please note:** The images on this site are only being used for non-profit educational purposes.

- The callout image on the homepage is from ['Wallpaper Access'](https://www.wallpaperaccess.com).

- Platform images found on the homepage are from [Wikipedia](https://en.wikipedia.org/).

- The images used for the review cards are images accompanying the individual original reviews.

- The mockup image showing all devices on my README.md was created using [Photoshop CC 2019](http://www.adobe.com/).

#### Acknowledgments

- My Mentor, [Aaron Sinnott](https://www.linkedin.com/in/aaronsinnott/) for his help and support throughout the project.

- The help and support received from the tutors at [Code Institute](https://codeinstitute.net/).

- The [Code Institute](https://codeinstitute.net/) Slack Community.

- My wife [Lida](https://www.linkedin.com/in/lidadimitriou/) for her love and support.

- Friends and family members for their feedback and support.

## &rarr; **Contact**

#### Contact details

Created by @NikolasKotsikos

If you have any problems, questions or, suggestions for my project please contact me on the email below:

```
kotsikn@gmail.com
```

Thanks for visiting.

&copy;
Nikolas Kotsikos
 

 


 