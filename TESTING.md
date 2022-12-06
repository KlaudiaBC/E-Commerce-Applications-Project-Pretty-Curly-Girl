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
    <td>Check if messages display in the top of the page as an alert when User taken certain actions on the page: add product to the bad, change product quantity, remove product, register, login, logout, successfully  process the payment, mismatch the search criteria.</td>
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
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/testing/w3c_home.png?raw=true" alt="w3c-home">
</p>


**Products**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/testing/w3c_products.png?raw=true" alt="w3c-products">
</p>


**About Us**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/testing/w3c_about.png?raw=true" alt="w3c-about">
</p>


**Privacy Policy**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/testing/w3c_policy.png?raw=true" alt="w3c-bag">
</p>


**Bag**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/testing/w3c_bag.png?raw=true" alt="w3c-bag">
</p>


**Checkout**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/testing/w3c_checkout.png?raw=true" alt="w3c-product/list">
</p>


**Checkout/Success**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/testing/w3c_checkout_success.png?raw=true" alt="w3c-about-us-page">
</p>


**Terms and Conditions Page**

<p align="center">
  <img src="" alt="w3c-terms">
</p>

**Terms and Conditions Page**

<p align="center">
  <img src="" alt="w3c-terms">
</p>


<br />
<hr>
<br />

- **W3C validator - CSS**
<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/testing/valid_css.png?raw=true" alt="w3c-css">
</p>

<p align="right"><a href="#welcome">Bact to top</a></p>

<br />

### **Lighthouse Desktop**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/testing/lighthouse_last.png?raw=true" alt="lighthouse-desktop">
</p>


### **Lighthouse Mobile**

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/testing/mobile_lighthouse.png?raw=true" alt="lighthouse-mobile">
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

Below you will find an image of error/bug and image with a fix that I have found online or figured out by myself.

The most troubling in the beginning was working on the git-branches, because I haven't been prepared for any eventual issues with creating pull requests and merging the data into the main branch. See below:

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/pr_20_one.png?raw=true" alt="git-conflict"></p>
<br/>

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/pr_20_two.png?raw=true" alt="git"></p>
<br>
  
<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/pr_20_three.png?raw=true" alt="git"></p>
<br/><br> 
  
**Migrations errors:**

<p align="center">
<a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/migrations_error.png?raw=true"></a></p>

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/migrations_error_solution.png?raw=true" alt="solution"></p>
<br/>


**Merge conflict again**
<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/merge_conflict_pull_main.png?raw=true" alt="issue"></p>
<br />

**I also wanted to 'undo' previous commit what was pretty easy forward now, since I have been working with branches:**
<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/git_log.png?raw=true" alt="solution"></p>

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/git_fetch_pull.png?raw=true" alt="solution"></p>
<br />

**While working with validation forms and API tokens, I also meet a sensitive data issue / csrf:
<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/error_no_login_as_admin.png?raw=true" alt="issue"></p>

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/csrf_solution.png?raw=true" alt="solution"></p>
<br />

**Some bugs affected the code that was working perfectly fine before - most od them was the case of typo/bad spell or not closed tag - or simply forgeting about some small - but very cruicial configuration:**
<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/error_post_not_function.png?raw=true" alt="solution"></p>
<br />

<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/readme/README/error_post_solution.png?raw=true" alt="solution"></p>
<br />
<p align="right"><a href="#welcome">Bact to top</a></p>
