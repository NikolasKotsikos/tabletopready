## <ins>Testing</ins>

**<details open><summary> Testing Documentation</summary>**
  - [Testing user stories](#testing-user-stories)
  - [Manual function testing](#manual-function-testing)
  - [Validator checks](#validator-checks)
  - [Audits](#audits)
  - [Responsive Design](#responsive-design)
  - [Additional Testing](#additional-testing)
  - [Bugs](#bugs)
</details>

---

### **Testing user stories**


#### <ins>Viewing and Navigation</ins>

**1. View a gallery of painted models**

I created a 'Gallery' page and added the 'Latest from our Gallery' section on the home page so that the user can see finished work from Tabletop-Ready.


**2. Easily navigate the shop**

The main menu navigation is always available and visible to the user using high contrast colours to make the options stand out visually. The dropdown menus provide options to filter the selection of miniatures and display it as the user selects.


**3. Easily view the total of my commission anytime.**

The cart icon is always visible to the user, displaying both the amount of items it contains as well as their grand total. The price is updated when items are added or removed from the cart.


#### <ins>Registration and User Accounts</ins>

**4. Easily register for an account**

The 'My Account' button is located in the main site navigation and opens a menu giving the user the option to register. The link takes them to an easily comprehensible registration page, customized from django allauth.

**5. Easily login or logout**

The 'My Account' button also provides users with the option to log in if they already have a registered account. The link takes them to an easily comprehensible and aesthetically coherent page, customized from django allauth.

**6. Receive an email confirmation after registering**

After registering their account the user will receive an automatically generated email confirmation send to the address they entered when registering.

**7. Have a personalized user profile**

The profile page is specific to each user with a personalised username greeting, the option to save their own entered details, and a log of their order history.

### <ins>Sorting and Searching</ins>

**8. Sort the list of available miniatures by keyword**

Using the search icon on the main navigation the user can search the database using keywords such as name, army, game system or a word contained in the miniature's description. They are then directed to a page containing the results of their query.


**9. Sort miniatures by game system (i.e. WH40K) I am interested in**

The user cam either use the sort selector on the miniatures page to sort by game system, or use the game systems dropdown menu in the main navigation to navigate directly to the game system of their choice, which sorts miniatures by their specific game system.


**10. Sort miniatures by army**

The user cam either use the sort selector on the miniatures page to sort by army, or use the armies dropdown menu in the main navigation to navigate directly to the army of their choice, which sorts miniatures by their specific army.


**11. Easily see what I've searched for and the number of results**

When entering a query in the expandable search bar, the user is directed to a page containing the results that contained their query, with the option to sort and their total number displayer above them.


### <ins>Ordering and Checkout</ins>

**12. Easily adjust the quantity of my selection**

Visually intuitive quantity selection controls are featured on both the 'Miniature Details' and 'Your Cart' pages enabling the user to adjust the quantity of their selection, or remove them completely.


**13. View items in my order to be purchased**

After adding an item to the cart the user is given visual feedback via a pop up message under the cart icon. The message contains a summary of the item added, including faction choice where applicable.


**14. Easily enter my payment information**

The Stripe payment form is familiar and easily comprehensible while providing secure and robust checkouts.


**15. Easily update my personal details**

Each registered user has their own profile page where they can store their personal details including name, email, and delivery details. This information can be easily updated by filling in any field and then clicking 'update details'.


**16. Receive an email confirmation after checking out**

The order summary is emailed to the email address provided by the user during checkout in an automated message.


### <ins>Admin and Store Management</ins>

**17. Add a miniature, army or game system**

The store owner has the option to easily add a miniature army or game system to the shop, by navigating to the relevant all page. There the 'Add' button avaiable directs them to an empty for where they can enter the new item in the database.


**18. Edit/update a miniature, army or game system**

Either from the individual miniature cards or from the details page for each miniature the store owner has the option to edit it. For armies and game systems the option is given by navigating to the relevant all page. The user is presented with a prefiled form containing the existing item data.
After done editing they can use the 'Update' button to save their changes and be redirected to the relevant all page or they can cancel and lose all changes.

**19. Delete a miniature, army or game system**

Either from the individual miniature cards or from the details page for each miniature the store owner has the option to delete it. For armies and game systems the option is given by navigating to the relevant all page. The user is presented with a modal confirmation prompt 
warning that the item will be permanently deleted. After confirmation the item is deleted from the database.


## [&#8679;](#testing)
---

### **Manual function testing**

To ensure my site was working correctly I carried out manual function testing on all my apps;

#### General

- [x] Cursor pointer is present when hovering button and link elements 
- [x] User is directed to a custom 404 page if directed to a non-existent domain

    <img src="readme/media/404-page.png">

- [x] User is directed to a custom 500 page if they are trying to access a file that is not on the server.

    <img src="readme/media/500-page.png">

- [x] The 'Back to Home' button on the 404 page directs user as expected
- [x] The 'Back to Home' button on the 500 page directs user as expected


#### Navigation bar

- [x] The user can toggle the menu by touching the hamburger menu icon in mobile
- [x] The user can close dropdown menus when open by clicking outside the menu area
- [x] If the user clicks a social icon on the footer the expected page opens on a new tab
- [x] The 'Gallery' link on main dropdown menu directs the user to the 'Gallery' page
- [x] The 'All Miniatures' link on the All Miniatures dropdown menu directs the user to the 'Miniatures' page displaying all miniatures
- [x] The 'All Armies' link on main dropdown menu directs the user to the 'All Armies' page displaying all armies
- [x] The 'Register' link is only visible on the main menu when a user is not logged in
- [x] The 'Register' link directs the user to the 'Register' page
- [x] Clicking the brand logo from any page on the site navigates the user back to the homepage
- [x] Search icon search bar showing the correct format based on device size
- [x] After inputting keywords and hitting enter or the icon, user is directed to the search page template with appropriate results
- [x] If user enters a keyword with no results the correct message is displayed
- [x] If user submits a search with no keywords they are directed to the search page with no results and receive a warning message
- [x] When not logged in, under the 'My Account' icon user has the options of 'Register' and 'Login'
- [x] When logged in, under the 'My Account' icon user has the options of 'Profile' and 'Logout'
- [x] All links displayed on the 'My Account' dropdown menu direct the user to the expected page
- [x] When the cart icon is clicked user is directed to the cart template
- [x] Before adding to cart, user is directed to the correct empty cart template
- [x] After adding to cart, user is directed to the cart template displaying the items they have added

#### Sort and Filter
> **Note:** All the below checks were tested on the miniatures, armies and game systems pages
- [x] The sort functionality returns items in the order expected. 
- [x] The filter functionality returns only items matching the chosen criteria
- [x] If user selects 'clear all' the filter is removed and all items are displayed

#### Authorisation

- [x] On the 'Register' page, if the user clicks 'Sign in' they are redirected to the 'Login' page
- [x] If the user completes the registration form with non-existent user details their registration is successful
- [x] After successful registration the user is navigated to the 'Verification email sent' page and an email is sent to the user with link to confirm
- [x] After user clicks link in email they are redirected to 'Verify your email' page 
- [x] After user clicking 'Confirm' on verify your email' page they receive a success message and are redirected to the login page
- [x] If the user completes the registration form with an already registered username and password they receive an error message
- [x] On the login page, if the user clicks 'Sign up' they are redirected to the 'Register' page
- [x] If the user completes the login form with an already registered username and password they are logged in successfully
- [x] If the user completes the login form with non-existent user details they receive an error message
- [x] If the user selects a social login option they are directed to the correct external platform for authorisation
- [x] If the user clicks 'Forgot password?' they are directed to the forgotten password page as expected
- [x] If the user enters their email and clicks 'Reset my password' they are directed to the password reset page as expected
- [x] If the user enters their email and clicks 'Reset my password' they receive an email with a link to reset their password
- [x] After user clicks the link in their email they are redirected to the 'Change password' page
- [x] After submitting a new password the user is presented with a success message 'Your password is now changed' and they can log in with their new password
- [x] If the user clicks 'Remember me' their username and password is automatically available next time logging in
    - 'Remember me' is thought to introduce unwanted security issues and therefore may be blocked on some devices
- [x] If a user is logged in, the 'Logout' option is visible in the profile icon menu
- [x] If a user clicks 'Logout' they are directed to the 'Logout' page where they can confirm their action

#### Home
- [x] The callout carousel automatically cycles through two callout images and messages with a preset interval time
- [x] The messages on the callout carousel are displayed appropriately dependent on whether a user is logged in or not
- [x] The links featured on the callout carousel direct the user to the expected page
- [x] The 'Latest from our Gallery' section shows the latest items added to the gallery.
- [x] All contact form fields are empty if user is not logged in
- [x] Full name and email fields are pre-populated on contact form if user is logged in and information is available in their profile
- [x] All contact form fields are empty if user is logged in but information is not available in their profile
- [x] If user information entered in contact form is valid, and form submission is successful, an email is sent to the expected Gmail account
- [x] If contact form submission is successful the user receives success toast
- [x] After submission the input fields are cleared
- [x] When input is missing in a required field there is an error response
- [x] When input format is incorrect the field validation errors are present

#### Miniatures

- [x] Each miniature card directs the user to the 'Miniature Detail' page displaying the correct information
- [x] Clicking the increment and decrement on the quantity selector changes the value as expected
- [x] User can not decrement below 0 or increment above the available stock
- [x] User can not type in a value out of the range 1-miniature stock
- [x] Selecting a value from the size selector dropdown updates the field correctly
- [x] Miniature is added to the cart successfully after clicking 'Add to cart'
- [x] If miniature is already in cart, quantity is incremented and miniature is not duplicated

<ins>Admin</ins>

When logged in as Admin user...
- [x] When input is missing in a required field there is an error response
- [x] When input format is incorrect the field validation errors are present
- [x] After successfully adding a new miniature I am redirected to the 'Miniature Detail' page with the correct information and success toast
- [x] If no image is added to the form submission, the expected 'no image' png file is present 
- [x] The 'Add a Miniature' button is visible on the 'Miniatures' page and each miniature card displays the 'Edit' and 'Delete' buttons
- [x] The 'Add an Army' button is visible on the 'All Armies' page and each army card displays the 'Edit' and 'Delete' buttons
- [x] The 'Add a Game System' button is visible on the 'All Game Systems' page and each game system card displays the 'Edit' and 'Delete' buttons
- [x] Clicking the 'Edit' button directs the user to the 'Edit Miniature' page with fields prefilled with current information
- [x] An info toast message is present after clicking the 'Edit' button
- [x] After selecting an image the file name appears as expected
- [x] Selecting 'Remove' and saving changes removes current image as expected
- [x] After submitting the Edit form user is redirected to the 'Miniature Detail' page with updated the information and success toast
- [x] The 'Delete' button is visible on the 'miniatures' page and on each 'Miniature Detail' page
- [x] After clicking the 'Delete' button the miniature is no longer visible on the site
- [x] After clicking the 'Delete' button the delete miniature modal appears
- [x] The modal closes when you press the 'Cancel' button without deleting the item
- [x] A success toast message is present after clicking the 'Confirm' button

#### Armies

- [x] Each army card directs the user to a page displaying miniatures with that army value
- [x] 'Edit' and 'Delete' buttons are available on each army card in 'All Armies' page


<ins>Admin</ins>

When logged in as Admin user...
- [x] The 'army Management' option is available in the Profile menu
- [x] When input is missing in a required field there is an error response
- [x] When input format is incorrect the field validation errors are present
- [x] After successfully adding a new army I am redirected to the 'army Detail' page with the correct information and success toast
- [x] If no image is added to the form submission, the expected 'no image' png file is present 
- [x] The 'Edit' button is visible on the 'armys' page and each 'army Detail' page
- [x] Clicking the 'Edit' button directs the user to the 'Edit army' page with fields prefilled with current information
- [x] An info toast message is present after clicking the 'Edit' button 
- [x] After selecting an image the file name appears as expected
- [x] Selecting 'Remove' and saving changes removes current image as expected
- [x] After submitting the Edit form user is redirected to the 'army Detail' page with the updated information and success toast
- [x] The 'Delete' button is visible on the 'armys' page and each 'army Detail' page
- [x] After clicking the 'Delete' button the army is no longer visible on the site
- [x] After clicking the 'Delete' button the army is still available in Django admin

#### Cart

- [x] After adding to cart all details are listed in the cart template as expected.     
- [x] Clicking 'Keep Shopping' navigates the user back to the 'Miniatures' page
- [x] Clicking 'Secure checkout' navigates the user to the 'Checkout' page as expected
- [x] By using the increment and decrement buttons, and clicking 'Update' I can to amend the quantity of an item in the cart
- [x] I can enter a numeric value into the field to update the quantity
- [x] I am not able to enter a non-numeric value into the fields

- [x] I can remove the item from the cart by clicking 'Remove'
- [x] I can remove the item from the cart by entering 0 into the quantity field and clicking 'Update'
- [x] If amendments are made in the cart subtotal is updated accordingly
- [x] Toast success message is present when item is adjusted
- [x] Toast success message is present when item is removed
- [x] Clicking arrow at bottom of cart navigates user to top of page

#### Checkout

- [x] The order summary contains the correct details of the items listed in the cart
- [x] If a site visitor the user input fields are all empty 
- [x] If a site member and details have been previously saved in 'My Profile' the checkout fields are already prefilled
- [x] When input is missing in a required field there is an error response
- [x] When input format is incorrect the field validation errors are present
- [x] If user enters details and checks 'Save this delivery information to my profile', the information is saved to their profile after submission
- [x] If user enters details and doesn't check 'Save this delivery information to my profile', the information is not saved to their profile after submission
- [x] After entering details and clicking 'Checkout' the loading page is present
- [x] The user is redirected to the checkout success page after completing order
- [x] The checkout success page contains all the correct personal details for the user and items purchased
- [x] After successful checkout the user receives an email with their order details
- [x] After successful checkout the user receives toast success message
- [x] User can checkout successfully as both a site user (not logged in) and member (logged in)
- [x] The delivery amount is showing as 10% of the subtotal cost
- [x] If the order is over £40 the delivery amount is 0

#### Gallery

- [x] The edit and delete buttons are visible when logged in as admin
- [x] After clicking the edit button the user is presented with a prefiled form containing the gallery item's data
- [x] After clicking update the gallery item is succesfully updated and the user is redirected to the gallery page with a success toast
    - Had an issue with the update taking place but the user receiving a 500 error, more about this in Bugs
- [x] After clicking the delete button the user is presented with a modal to confirm their action
- [x] After clicking 'Confirm' in the delete modal, the gallery item is deleted and success toast is presented to user


#### Profile

- [x] The welcome message is personalised with the correct username for the logged in user
- [x] The user's order history is listed with previous purchases
- [x] The order history is listed in date descending order with most recent showing first
- [x] After clicking 'View order details' the user is directed to the 'Checkout Success page' showing all details of their order
- [x] On the 'Checkout Success' page, clicking 'Back to profile' navigates the user back to their profile
- [x] If user enters details and clicks 'Update Information' their details are saved to their profile with success toast present
- [x] If user edits their details and clicks 'Update Information' their details are updated on their profile with success toast present
- [x] No fields on user profile are required allowing user to only fill in desired fields
- [x] If user updates their information in their profile this is reflected on the checkout page


## [&#8679;](#testing)
---

### **Validator checks**

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. The code was entered through direct input. 

- [**HTML Validator**](https://validator.w3.org/)
    - To get the most accurate read of my HTML for validation, I ran my app and extracted my code from the 'View page source'.

    No error or warning messages were received.

- [**CSS Validator**](https://jigsaw.w3.org/css-validator/)

    No error or warning messages were received.

[**JS hint**](https://jshint.com/) was used to check for any errors with my Javascript files. 
JS was also tested by opening the developer console window on Chrome and checking for any errors as I clicked through the site.

- <ins>Warnings received;</ins>

    `let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).`
    
    `'template literal syntax' is only available in ES6 (use 'esversion: 6').`

    Warnings occurred as JShint is using ECMAScript 5.1 specification and my code uses ECMAScript 6 specific syntax. However, all code is valid.

- <ins>Undefined variable;</ins>

    `$`

    `stripe`

    $ (Jquery) and stripe are all defined in base.html.

[**PEP8 online checking tool**](http://pep8online.com/checkresult) was used to inspect my Python code against the style conventions in PEP 8.

[**Flake8**](http://pep8online.com/checkresult) was a python code linting tool also used to help verify pep8, pyflakes and circular complexity. By using the following command I was able to check the problems across all my files without having to open each individual file.

`$ python3 - m flake8`

<ins>PEP8 Issues:</ins>
- I chose to ignore any warnings on migration files since these are automatically generated files so may ignore style rules for efficiency reasons. Also as developers, we usually don't need to touch them so they don't need to be perfectly readable.

- `DJ01 Avoid using null=True on string-based fields`

    As referenced on [stackoverflow](https://stackoverflow.com/questions/59836736/django-why-only-string-based-field-cant-have-null-true), Django allows the use of NULL in string-based fields but it is suggested to avoid it and use '' to represent the empty value. As in most cases, both values (NULL and '') represent the same thing for string-based fields I have chosen to disregard this warning. 

- `E501 line too long`

    This error has been fixed on the majority of my code but some lines in widgets and settings file have been left to avoid breaking up variables.

## [&#8679;](#testing)
---

### **Audits**

[Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to run a series of audits to improve the quality of web pages. Overall performance and errors are highlighted below.

> **Note:** The [performance score](https://web.dev/performance-scoring/) can fluctuate because of changes in underlying conditions.
<p align="center">

<img src="readme/media/lighthouse.png">

<p>
<details>
<summary>More specific details</summary>
<p>

<ins>Performance</ins>

The high perfomance review is due to best practices applied throughout the development of the site. Suggestions and imporvement have been applied where necessary. 

Actions taken:

[`Eliminate render-blocking resources`](https://web.dev/render-blocking-resources/)
- Lazy loading - added class 'lazy' to img tags
- Added 'rel="preload" as="style"' attributes to base.css file
- Added 'async' to JS script tags to indicate to the browser that the script file can be executed asynchronously. However, no improvement was made to performance so these were removed.

[`Serve images in next-gen formats`](https://web.dev/uses-webp-images/?utm_source=lighthouse&utm_medium=lr)
- I tried converting my images to JPEG 2000 as suggested, however, the images were not loading due to their limitations of only working on certain browsers. Therefore I have kept my image in a PNG and JPG format.


<ins>Accessibility</ins>

`Background and foreground colors do not have a sufficient contrast ratio`

I didn't take any actions as none of my users experienced difficulty reading the text in question. 


</details>

## [&#8679;](#testing)
---

### **Responsive Design**

- Site created as a mobile-first design.

- Responsive layout achieved through utilising the Bootstrap grid system and applying my own media queries.

- Viewport tag included in the head of HTML files to tell the browser how to respond to different resolutions, particularly mobile ones.

## [&#8679;](#testing)
---

### **Additional Testing**

- Google Chrome was the main site used throughout testing but the application was also trialled on Safari, Opera, Firefox, and Microsoft Edge browsers. 
    
- The website was viewed on a variety of devices including ACER Laptop, Dell Notebook, Ipad, IPhones (Version 5, 6, XR), Huawei P20.

- Friends and family members were asked to review the site to point out any bugs, user experience issues, and/or suggestions.

    Feedback action:
    - More search queries so I can search forum topics
    - Add a number count onto the cart icon so I can easily see how many items are in my cart
    - Ability to autofill address by entering postcode 
   

## [&#8679;](#testing)
---

### **Bugs**

|     | Bug                                                                           | Action                                                            |
|-----|-------------------------------------------------------------------------------|-------------------------------------------------------------------|
| [] | Main callout image appears blurry on larger devices                   |  Could not find an appropriate image of better quality so this had to do!  |
| [] | Quantity +/- inputs allow user to enter invalid values in desktop view |  After hours of talking with tutors I was baffled that some of them got this error and some didn't. The problem is addressed by adding defensive Python code that stops invalid entries from going through, and by implementing a JS script that empties the HTML from the form that is not used while setting the other ones display to block. The script works for some but not for all and me Johann and Sean couldn't figure out why |
| [x] | User able to type in any quantity value for item when in shopping cart                  |  Changed 'quantity > 0' to 'quantity in range(1, stock)' or send an error message to the user if the value exceeds that. |
| [x] | When editing a gallery item a 500 would be returned after clicking update |  The reason for that was that the redirect was asking for an itemId. By removing that the bug was fixed and the update now redirects to the gallery page. |
| [x] | Contact us form was displayed taking up 50% of available width in mobile |  This bug was fixed easily by removing an excessive col-12 class from the element's class list |
