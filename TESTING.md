# Full Stack Toolkit: "Empire of Thoughts" Portfolio Project - TESTING

<p id="welcome"></p>

## **Table Of Contents**

- [**Testing**](#testing)
  - [**Mannual Testing**](#mannual-testing)
  - [**W3C Validator**](#w3c-validator)
  - [**Lighthouse**](#lighthouse)
- [**Errors and bugs**](#errors-and-bugs)

## **TESTING**

### **MANUAL TESTING**

Tests have been performed several times during all implementation process.
The features, which was taken into a testing in both scenarios: on the desktop and on the devices are listed below.

<table>
  <tr>
    <th>Element</th>
    <th>Expected result</th>
    <th>Status</th>
  </tr>
  <tr>
    <td>Logo and navbar</td>
    <td>Make sure that logo is displayed correctly in the top the page and buttons of the menu are: on the left top corner on desktop- in the burger button, which displays the dropdown menu/ on the mobile devices. On the desktop: they display in the sub-menu (horizontal). All buttons are working and sending User to desired urls.</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>'Home Page Images': Background image + Content/Blog Section </td>
    <td>Make sure that the dynamics of the background image does not interfere with the text and other elements (buttons) on the page. Check if all the images: have a good quality, display correctly on every size of the screen. Content section: images zoom on hover.</td>
    <td>Pass</td>
  </tr>
  <tr>
      <td>'About Us' Page Images: </td>
    <td>Make sure that all the images: have a good quality, display correctly on every size of the screen and do not interfere with a text provided on the opposite sides.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Registration Form</td>
    <td>Check if the registration form saves the data about the new User when the User provides the correct data. Make sure all password validators work correctly and display the error message. Email is mandatory. After submitting a valid form, User should receive the confirmation email on the email provided during registration.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Login/Logout</td>
    <td>Check if the login form allows User who had created his account correctly - to access the profile page for authorised users - after providing the correct login credentials. Check if the button "Logout" bring the User back into the "anonymous" mode.</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Login/Sign up via google</td>
    <td>Check if the login via google account is possible and go with no issues. After clicking the button "Log in via google" User should be redirected to the google auth window, where he can proviode his credentials and access the application.</td>
    <td>Pass</td>
    </tr>
    <tr>
    <td>Product</td>
    <td>Check if the product card display correctly: iname, title and price of the product. When user clicks on the picture of the product, he is taken to detail view of this product. (Render on the new page). List of the product should be tidy and easy to watch/scroll.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>CRUD: Product Bag</td>
    <td>User can: Add chosen product to his bag by clicking the button "Add to bag" on the product detail page. In the other template: "bag" User can access the list of his purchases and change their quantity as well as permanently remove them from the basket.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Checkout</td>
    <td>Every user can proceed with checkout, the registration is not required. Once chosen to check out, User is provided with an address form, bag/basket summary and the stripe-payment element, that allows to pay by credit or debit card. Once card have been filled correctly (using the test-card details/atm), the payment should be processed and User redirected to the checkout-success page.</td>
    <td>Pass</td>
  </tr>
      <tr>
    <td>Webhooks</td>
    <td>Make sure the webhooks works correctly and registed payment intend with all the data provided by the user via checkout form. If any interruption happens from the side of the internet connection or any other case where the payment was distrurbed, Administrator will still receive the information about the transaction intend and about the User who took this action.</td>
    <td>Pass</td>
  </tr>
      <tr>
    <td>Admin side: managing the products and the categories</td>
    <td>Check if: the "Add product" form is registered into an Admin Panel and contain a summernote text editor. Make sure all the fields are accessible by Admin and can be changed at any time as well as deleted. Admin can also manage: categories, user_profiles, social_profiles, add "SALE" subcategory category to the product.</td>
      <td>Pass</td>
  </tr>
      <tr>
    <td>Categories</td>
    <td>Check if categories filter the products in the correct way and display for a user a list of products from chosen category in the new page.</td>
    <td>Pass</td>
  </tr>
      <tr>
    <td>Search engine</td>
    <td>Make sure the search input is connected with a search function which iterate through the products items (the title and the description) and display the results that match User's search request.</td>
    <td>Pass</td>
  </tr>
        <tr>
    <td>URLs</td>
    <td>Make sure all url paths are connected in the correct way and the User is redirected after submitting any form into the correct view.</td>
    <td>Pass</td>
  </tr>
        <tr>
    <td>Messages</td>
    <td>Check if messages displayon the left side og the screen as an toast when User taken certain actions on the page: add product to the bad, change product quantity, remove product, register, login, logout, successfully  process the payment, mismatch the search criteria.</td>
    <td>Pass</td>
  </tr>
        <tr>
    <td>Error pages</td>
    <td>Check if error 404 and 500 display custom html pages.</td>
    <td>Pass</td>
  </tr>
          <tr>
    <td>Pages</td>
    <td>Check if all the pages display correct template and clear, easy to read view.</td>
    <td>Pass</td>
  </tr>
          <tr>
    <td>Footer</td>
    <td>Check if the links to social media accounts in the footer opens in the new tab.</td>
    <td>Pass</td>
  </tr>
</table>

<p align="right"><a href="#welcome">Bact to top</a></p>

### **W3C validator**

- **HTML Validator**

**Home**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/testing/w3c_home.png?raw=true" alt="w3c-home">
</p>


**Products**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/testing/w3c_products.png?raw=true" alt="w3c-products">
</p>


**About Us**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/testing/w3c_about.png?raw=true" alt="w3c-about">
</p>


**Privacy Policy**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/testing/w3c_policy.png?raw=true" alt="w3c-bag">
</p>


**Bag**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/testing/w3c_bag.png?raw=true" alt="w3c-bag">
</p>


**Checkout**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/testing/w3c_checkout.png?raw=true" alt="w3c-product/list">
</p>


**Checkout/Success**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/testing/w3c_checkout_success.png?raw=true" alt="w3c-about-us-page">
</p>


**Login Page**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/testing/w3c_login.png?raw=true" alt="w3c-terms">
</p>

**Sign up page**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/testing/w3c_signup.png?raw=true" alt="w3c-terms">
</p>


<br />
<hr>
<br />

- **W3C validator - CSS**
<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/testing/valid_css.png?raw=true" alt="w3c-css">
</p>

<p align="right"><a href="#welcome">Bact to top</a></p>

<br />

### **Lighthouse Desktop**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/testing/lighthouse_last.png?raw=true" alt="lighthouse-desktop">
</p>


### **Lighthouse Mobile**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/testing/mobile_lighthouse.png?raw=true">
</p>
<br>
<hr>
The tests were performed on:

- different browsers: Google Chrome, Firefox, Internet Explorer, Opera and Safari
- different devices: Samsung Galaxy S20+, Samsung Note 10+, iPhone 11, Lenovo TAB m10.

<p align="right"><a href="#welcome">Bact to top</a></p>
<hr>

## **Errors and Bugs**

Most of the challenges I have met during the implementation are included in the Jira Board, where it was easy and convenient to leave comments in attachment to the tickets I have been working on.

1. The most troubling in the beginning was working on the git-branches, because I haven't been prepared for any eventual issues with creating pull requests and merging the data into the main branch. See below:

From the GitHub side when merging your PR it can look like this:
<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/pcg_confict_merge.png?raw=true" alt="merge-issue"></p>
<br>

In CLI it is a rejected 'git-push':
<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/error_push_main_cli.png?raw=true" alt="git-conflict"></p>
<br>

Git-pull
<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/merge_conflict_pull_main.png?raw=true" alt="git"></p>
<br>

Open the working tree view to choose the changes that should be implemented and merge successfully.
<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/merge_cli.png?raw=true" alt="git"></p>
<br><br>

**Issue - 01**
**Migrations errors:**

Migration error happened to me at least 2 times and was caused by lack of continuous integration with database in the time, changes were applied. It van happen if you forget to make migrations on the time you made a change --> then apply more changes to the same object and try to make migrations. That can lead to real issues with the database like e.g., duplicate the name of the table, which will result with an error every time you want to apply any change to this table.

In my case, the issue was that when I tried to “migrate” I was getting an error message. Therefore I have tried to re-apply changes:

<p align="center">
<a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/migrations_error.png?raw=true"></a></p>

There was a table in the database which hasn't been removed and Django wanted to record the changes on that table, however in my code this table was removed several commits ago and there were no changes coming in. If I wanted to add the table to my code and apply the changes that supposedly happen, the error was: table with this name already exists.Solutions:I have tried to remove the migrations record from the django-migrations table, where all previous migrations were stored. That helped on time, other time I had to delete one of the elements from my model – as it was taken by migration as already "not-excisting" (still when I wanted to add it I was receiving a message: this table already excist") --> I have pushed all the changes, then added this element back and makemigrations.

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/migrations_error_solution.png?raw=true" alt="solution"></p>
<br/>


**Issue - 02**
**CSRF validation - no access to the admin page**

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/error_no_login_as_admin.png?raw=true" alt="issue"></p>
<br>

At first I have:
- refreshed my page and clean all the cookies/cache data
- checked if all the forms contain the "CSRF" token and if those tokens are placed in the correct place

The first bug was found:
<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/CRSF_WRONG_PLACE.png?raw=true" alt="csrf-bug"></p>
<br>

...but that was not a solution for me. Next I tried following:

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/csrf_solution.png?raw=true" alt="solution"></p>
<br>

That did not help. I have copied my curl --> open devtools --> open tab "network" --> you may need to refresh the page --> right-click on the page that is not working which is listed in the 'network' tab --> copy curl (bash). Then I used an online platform to test the curl:

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/convert_curl.png?raw=true" alt="curl"></p>
<br>

I found out that for some reason there are two csrf tokens being made during load of this page - however I also found the reason for that:

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/convert_curl_code.png?raw=true" alt="solution"></p>
<br>

After many trials I finally got into a short term solution to comment out the *"django.middleware.csrf.CsrfViewMiddleware"*. And that worked, for maybe a day. The issue came again and I asked the Student Support Group for help. The solution was incredibly simple:
**Solution**: In my list of "CSRF_TRUSTED_ORIGINS" was a bug with url spell, therefore the website I was trying to access wasn't on this list. Once the provided url was correct, I received back my access to the page.


**Issue - 03**
**The AJAX function doesn't work.**

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/error_post_not_function.png?raw=true" alt="error_ajax"></p>
<br>

Solution was just to update my jQuery scripy with non-slim version:

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/error_post_solution.png?raw=true" alt="solution"></p>
<br>

**Issue - 04**
**Favicon not found**

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/favicon-error.png?raw=true" alt="favicon-error"></p>
<br>

The solution was to make my won favicon - normally it would be a logo of the company, however I did not use the actual logo of the brand anywhere in the project to not bring any confusion, I had made a favicon with a first letter of the brand name: "P"

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/static/images/favicon.png?raw=true" alt="favicon"></p>
<br>

**Issue - 05**
**Dependency conflict: Boto3**

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/boto3-error.png?raw=true" alt="dependency-error"></p>
<br>

In order to host my static files in the AWS bucket, I had to add a Boto library to my application. It appeared to not match with some versions of other libraries I had already installed.
Solution: At first, I had checked in my CLI which dependencies were in conflict with the one I just added, and I tried to install versions that would match.
As soon as that happened, the other libraries appeared to not be compatible with the versions I added.
After a few times of re-installing various dependencies, I found out that the version of Boto which caused the issue in the first place was deprecated.

I uninstalled the invalid version and installed the “correct” one. That caused new issues with other dependencies, however this time I found the matching versions of all included dependencies- below you can see the set of “matching” ones.

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/aws-task-jira-boto.png?raw=true" alt="dependency-error"></p>
<br>

**Issue - 06**
**Not secure**

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/not_secure01.png?raw=true" alt="notsecure-error"></p>
<br>

As a solution for that I had un-commented the *"django.middleware.csrf.CsrfViewMiddleware"* in my Settings.py, which was not active before.

<p align="right"><a href="#welcome">Bact to top</a></p>
