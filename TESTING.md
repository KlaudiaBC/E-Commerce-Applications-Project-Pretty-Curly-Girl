# Full Stack Toolkit: "Empire of Thoughts" Portfolio Project - TESTING

<p id="welcome"></p>

## **Table Of Contents**

- [**Testing**](#testing)
  - [**Mannual Testing**](#mannual-testing)
  - [**W3C Validator**](#w3c-validator)
  - [**PEP8**](#pep8)
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
    <td>Make sure that all the images: have a good quality, display correctly on every size of the screen and do not interffere with a text provided on the oposite sides.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Registration Form</td>
    <td>Check if the registration form saves the data about the new User when the User provides the correct data. Make sure all password validators work correctly and display the error message. Email is mandatory. After submitting a valid form, User should receive the confirmation email on the email provided during registration.</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Login/Logout</td>
    <td>Check if the login form allows User who had created his account correctly - to access the profile page for authorised users - after providing the correct login credentials. Check if the button "Logout" bring the User back into the "annonymous" mode.</td>
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
    <td>Make sure the search input is connected with a search function which iterate through the products items (the title and the describtion) and display the results that match User's search request.</td>
    <td>Pass</td>
  </tr>
        <tr>
    <td>URLs</td>
    <td>Make sure all url paths are connected in the correct way and the User is redirected after submitting any form into the correct view.</td>
    <td>Pass</td>
  </tr>
        <tr>
    <td>Messages</td>
    <td>Check if messages display in the top of the page as an alert when User taken certain actions on the page: add product to the bad, change product quantity, remove product, register, login, logout, successfuly process the payment, missmatch the search criteria.</td>
    <td>Pass</td>
  </tr>
        <tr>
    <td>Error pages</td>
    <td>Check if error 404 and 500 display customised html pages.</td>
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

**Add Post Page**

<p align="center">
  <img src="" alt="w3c-add-post">
</p>

**Edit Post Page**

<p align="center">
  <img src="" alt="w3c-checkout-success">
</p>

**Detete Post Page**

<p align="center">
  <img src="" alt="w3c-checkout">
</p>

**Add Comment Page**

<p align="center">
  <img src="" alt="w3c-bag">
</p>

**MyPage - filered view of User posts**

<p align="center">
  <img src="" alt="w3c-home">
</p>

**Categories/List Page**

<p align="center">
  <img src="" alt="w3c-product/list">
</p>

**Categories/Filtered Posts Page**

<p align="center">
  <img src="" alt="w3c-about-us-page">
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
  <img src="" alt="w3c-css">
</p>

<p align="right"><a href="#welcome">Bact to top</a></p>
<br />

<p align="right"><a href="#welcome">Bact to top</a></p>

### **PEP8**

- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-urls-empire.png?raw=true">empire_blog/urls.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-admin-blog.png?raw=true">blog/admin.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-views-blog.png?raw=true">blog/views.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-forms-blog.png?raw=true">blog/forms.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-models-blog.png?raw=true">blog/models.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-test-views-blog.png?raw=true">blog/test_views.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-test-urls-blog.png?raw=true">blog/test_urls.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-test-models.png?raw=true">blog/test_models</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-test-forms-blog.png?raw=true">blog/test_forms.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-forms-members.png?raw=true">members/forms.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-urls-members.png?raw=true">members/urls.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-test-forms-members.png?raw=true">members/test_forms.py</a>
- <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/testing/pep-views-members.png?raw=true">members/views.py</a>

<p align="right"><a href="#welcome">Bact to top</a></p>
<br />

### **Lighthouse**

<br/>

<p align="center">
  <img src="" alt="lighthouse">
</p>

The tests were performed on:

- different browsers: Google Chrome, Firefox, Internet Explorer, Opera and Safari
- different devices: Samsung Galaxy S20+, Samsung Note 10+, iPhone 11, Lenovo TAB m10.

<p align="right"><a href="#welcome">Bact to top</a></p>
<hr>

<a href=""></a>

<p align="center">
<img src="" alt="solution">
<br />

<p align="center">
<img src="" alt="solution">
<br />

**Solution:**

<a href=""></a>

<p align="center">
<img src="" alt="solution">
<br />
<br />
<p align="right"><a href="#welcome">Bact to top</a></p>
