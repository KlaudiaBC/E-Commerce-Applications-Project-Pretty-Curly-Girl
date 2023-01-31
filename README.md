# E-Commerce Application: "Pretty Curly Girl" Portfolio Project
## Welcome!

<p id="welcome"></p>

## This is my Portfolio 5 Project regarding the Code Institute's Diploma in Software Development (E-commerce Applications).

<img src="https://img.shields.io/badge/django-v4.0.0.-blue"> <img src="https://img.shields.io/badge/django--allauth-v0.51.0-yellowgreen"> <img src="https://img.shields.io/badge/python-v3.8.11-blue"> <img src="https://img.shields.io/badge/javascript-js-blue"> <img src="https://img.shields.io/badge/jQuery-ajax-blue"> <img src="https://img.shields.io/badge/bootstrap-v4.6-orange"> <img src="https://img.shields.io/badge/google--auth-v2.15.0-yellowgreen"> <img src="https://img.shields.io/badge/gunicorn-v20.0.4-orange"> <img src="https://img.shields.io/badge/stripe-v4.2.0-blueviolet"> <img src="https://img.shields.io/badge/aws-s3%20bucket-blueviolet"> <img src="https://img.shields.io/badge/heroku-v7.64.0-green">

Fully responsive e-commerce application built with: Django 4.0 Framework, Python3, JavaScript and jQuery (AJAX).
Bootstrap4 as a front-end framework.
Deployed on Heroku.
Database hosted via AWS S3 Bucket.
Stripe payments - including webhooks. Saving bag on the session.
Google social accounts authorization with OAuth/django-allauth.
User registration with required email confirmation.
Subscription form with MailChimp.


See the deployed project <a href="https://pretty-curly-girl.herokuapp.com/" target="_blank">here</a>.<br>
See the Jira Board for this project: <a href="https://emporiumofthoughts.atlassian.net/jira/software/projects/PCG/boards/2" target="_blank">here</a>.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/respo_dark.png?raw=true" alt="responsive view">
</p>

## **Table Of Contents**
* [**Agile Scrum**](#agile-scrum)
  * [**Planning Phase**](#planning-phase)
  * [**Product roadmap**](#product-roadmap)
  * [**Release planning**](#release-planning)
  * [**Sprint planning**](#sprint-planning)
  * [**Daily stand-ups**](#daily-stand-ups)
  * [**Sprint review and retrospective**](#sprint-review-and-retrospective)
* [**UX Design**](#ux-design)
  * [**Scope**](#scope)
  * [**Skeleton**](#skeleton) 
    * [**Wireframes**](#wireframes)
    * [**Database Schema**](#database-schema)
  * [**Surface**](#surface)
    * [**Base**](#base-common-for-each-page-of-application)
    * [**Content**](#content-of-the-pages)
    * [**Color scheme**](#color-scheme)
* [**Implementation**](#implementation)
    * [**Branches in GIT**](#branches-in-git)
    * [**Defensive design**](#defensive-design)
* [**Business model**](#business-model)
  * [**Marketing strategy**](#marketing-strategy)
     * [**Content marketing**](#content-marketing)
     * [**Social media**](#social-media)
     * [**Newsletter**](#newsletter)
     * [**Public Relations**](#public-relations)
     * [**Search Engine Optimization**](#search-engine-optimization)
     * [**Control and updating procedures**](#control-and-updating-procedures)
* [**Testing**](#testing)
* [**Deployment**](#deployment)
    * [**Fork this Project**](#fork-this-project)
    * [**Clon this Project**](#clon-this-project)
* [**Technologies used**](#technologies-used)
* [**Acknowledgements**](#acknowledgements)


## **Agile Scrum**
### **Planning Phase**
Pretty Curly Girl is an exciting business which provides hair care products designed for curly hair treatments.
Hanan - the owner of the brand (further called: *Client*), has started her online sales via one of e-commerce builders. Once her business has grown, the need for a professional website became one of the important factors that could have a positive impact on the further development of the brand.

At first, I have become familiar with the mission of the business, the offer and mainly the actual website used to provide online sales. I have listed all components and features of the current application. I also pointed out UX issues I have found to make sure we could address them during the development.
Then, I have discussed those aspects with the Client and proceeded with brainstorm sessions, which over a time have brought the final results.

In this file I have documented all insights, steps and the obstacles I have met during implementation. All technical issues have been documented also in the Jira - you can access the board via link provided below.
In addition, you can also find a basic e-commerce marketing strategy which includes critical points for the web implementation process like the SEO keywords.
--> For more, please see: Marketing


### **Product roadmap**
Following the Agile principles, I have created the *User Stories*, which helped me to map out the work required to develop this application. In order to easily manage the workflow, I have used the <a href="https://jira.atlassian.com/" target="_blank">Jira software</a>.

Please, see the board of my project in Jira, including User Stories, automation with GIT branches and commits, pointed out errors and fixes, comments, images and many more: <a href="https://emporiumofthoughts.atlassian.net/jira/software/projects/PCG/boards/2" target="_blank">click here</a>

Each User Story has assigned a *Story Points*.
I have used the Fibonacci scale (1,2,3,5,8) to represent complexity and estimated amount of effort/time it takes to complete the task (story).
The higher the number, the more involvement the task requires.

Story Points | Importance | Time
---|---|---
1p | small task - easy | up to 2 hours of work
2p | small task - complex | up to 3 hours of work
3p | midlle task | up to 4 hours of work
5p | large task - easy | from 4-6 hours of work
8p | large task - complex | more than 6 hours of work

The large task should not take more than 8h of work.


### **Release planning**
I split the work evenly into two Sprints (duration: 2 weeks).
I also connected my Jira Board to GitHub and had followed the naming convention for commits and branches, which automatically synchronized the progress of implementation with the jira tickets.


### **Sprint planning**
In the first part of work (Sprint 1) the team should deliver Minimum Variable Product. In the case of this project MVP includes the home page, registration and login page, product list page, product detail page, search engine and Admin Panel with all functionality (CRUD for Admin - Product).

The Second Sprint contains adding more features like: Users Profile page, checkout (including the secure payment) and blog.
Before the second Sprint begins, the realization should be discussed with the Client and necessary changes should be added to the workflow.


See the Sprints as planned in the begging of implementation:

**Jira backlog - Sprint 1:**
<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/jira_backlog_sprint_one.png?raw=true" alt="backlog_sprint_one">
</p>
<br>

**Jira backlog - Sprint 2:**
<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/jira_backlog_sprint_two.png?raw=true" alt="backlog_sprint_two">
</p>
<br>

**Jira board - during 2nd Sprint:**
<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/jira_middle.png?raw=true">
</p>
<br>

**Jira board - Sprint 3:**
<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/sprint3.png?raw=true"></p>
<br>


**Jira board - during 3rd Sprint:**
<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/jira_board_bugs_three.png?raw=true"></p>
<br>


**Jira Insights / 1:**
<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/insights.png?raw=true"></p>
<br>


**Jira board - Sprint 4 - adding a missing elements:**
<p align="center">
<img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/sprint4a.png?raw=true"></p>
<br>


### **Sprint 4 - adding a missing elements**
In order to meet the requirements of 5th portfolio assessment, there were a few elements that had to be added and the fix of registration form (please, see the Jira Board where all the issues and tasks are listed and explained). I had introduced two new models: review and request refund. I added a views and templates accordingly. Reviews can be added only by registered Users, however, every (also anonymous user) can fill and send the request of refund.
The other missing element was feedback of successful and unsuccessful payment, which was also implemented together with an address form which was integrated with user profile model. Testing was handled through the entire process (you can find more about it in the "TESTING.md" file.


### **Daily stand-ups**
This point of agile development would be necessary, if there was more than one developer working on the project. The short daily stand-up meeting helps the team accomplish their tasks by brief update on the work done and work which is planned for that day. I have been reviewing the workflow on the beginning of each day of development to keep track of the achieved tasks in comparison to the estimated time so that I could later implement the changes into a Second Sprint.


### **Sprint review and retrospective**
After the end of the First Sprint I had scheduled a meeting with my mentor to discuss the current development and seek further review or advice. Secondly I have also presented the deployed page to the Client and had another brainstorm session to discuss further developments. With all the changes included in the backlog, I was then ready to begin working on the Second Sprint.

<p align="right"><a href="#welcome">Bact to top</a></p>


## **UX Design**

### **Scope**
With the development of technology, the comfort level of our life increases. The use of the Internet has become an everyday reality. In connection with this, we can observe emerging trends in the market related to the use of mobile devices and the easy accessibility they provide. One of the rapidly growing trends is online shopping. In response to the growing interest in virtual trading, Pretty Curly Girls has prepared an easy-to-use e-commerce application that is fully responsive and designed in the spirit of the greatest user experience.
Particular attention will be placed on the smooth navigation through the page, easy checkout process and user-friendly features like: the wish list, rating scale or advanced search engine.

### **Skeleton** 
#### **Wireframes:**
Please, see the wireframes - created via <a href="https://app.diagrams.net/" target="_blank">Draw.io</a>:
- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/wireframes/PCG-home_desktop.png?raw=true" target="_blank">Wireframe for the home page - desktop</a>
- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/wireframes/PCG_product_list_page_desktop.png?raw=true" target="_blank">Wireframe for the product list page - desktop</a>
- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/wireframes/PCG_product_detail_desktop.png?raw=true" target="_blank">Wireframe for the product detail page - desktop</a>
- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/wireframes/PCG_locations_desktop.png?raw=true" target="_blank">Wireframe for the locations page - desktop</a>

- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/wireframes/PCG_landing_page_mobile.png?raw=true" target="_blank">Wireframe for home page - mobile devices</a>
- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/wireframes/PCG_product_list_mobile.png?raw=true" target="_blank">Wireframe for the product list page - mobile devices</a>
- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/wireframes/product_detail_page_mobile.png?raw=true" target="_blank">Wireframe for the product detail page - mobile devices</a>
- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/wireframes/PCG_locations_mobile.png?raw=true" target="_blank">Wireframe for the locations page - mobile devices</a>

#### **Database Schema**
I have implemented **PostgreSQL (Postgres)** - the open-source database object-relational database system, which is an extension of the SQL language.
Because Heroku is not longer offering free usage of Postgres, I had migrated my database into a new free service called **ElephantSQL** 

Entity relationship diagram for all the models included in the application:
<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/ERD_PCG.png?raw=true" alt="entity relationship diagram">
</p>

### **Surface**

#### **Base (common for each page of application):**

**Logo and navbar:**
Sticky top, includes logo (left side) and the button to access the basket/profile page on the right side. On the mobile: burger menu from the left - logo - shopping bag.
Menu includes following:

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/homepage.png?raw=true" alt="landing page desktop">
</p>

**Footer** - on the bottom of the page, contains information about the author, links to social media accounts (buttons/icons) and disclaimer with information about an actual owner of the brand presented in this application.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/footer.png?raw=true" alt="landing page desktop">
</p>


#### **Content of the pages:**

**Authorization pages** - are implemented from the django-allauth library and customized.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/sign1.jpg?raw=true" alt="register_page">
</p>
<br>
<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/sign2.jpg?raw=true" alt="register_page">
</p>

**Home page - Section 1: Hero Image** (like on the image above)
<br>
**Home page - Section 2: Insights** - why the customer should choose us? Short, catchy messages - loaded with keywords and decorated with a simple icon.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/section2.png?raw=true" alt="home">
</p><br>

**Home page - Section 3: Blog** / Content marketing: I have added random articles about hair care, however this place is designed to publish a blog by the owner of the application, providing to customer an extra value into the purchase-sell process. It could be also a section where the partners/connected businesses are promoted - the higher recognizable are they, the better chances has an application in the SEO rankings.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/blog_cont.png?raw=true" alt="home_page">
</p><br>

**Home page - Section 4 - Testimonials** - because the whispered marketing tends to be the most effective.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/testimonials.png?raw=true" alt="home_page">
</p><br>

**Home page - Section 5 - Subscription form** as another marketing tool that allows the seller to bulit relationship with his customers

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/subscrib.png?raw=true" alt="home_page">
</p>

<hr>

**Product list page** - display the cards with products - with image, name and sub-name.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/produst-list.png?raw=true" alt="view_page">
</p>
<br>

**Detail view page** - All information about one product. Buttons: *Add to the bag* and *Go back*

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/prod_deatils.png?raw=true" alt="view_page">
</p>
<br>

**Bag page** - list of all the products User added to the basket and desire to purchase. Buttons: *Checkout*, *Go back*, *Increment/decrement quantity*, *Remove from the basket*

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/bag.png?raw=true" alt="view_page">
</p>
<br>

**Checkout page** - contains the form for shipping address of the customer as well as his bank card credentials - Stripe element.
If you would like to test the funcionality of this component - you can do it anonymously, following Stripe:
"...use a card number, such as 4242 4242 4242 4242. Use a valid future date, such as 12/34. Use any three-digit CVC (four digits for American Express cards). Use any value you like for other form fields. The success transaction will redirect you to the "Checkout success page".

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/checkout.png?raw=true" alt="checkout">
</p>
<br>

**Wishlist** - User personal account. In order to collect the favorite products in one private list, the Registration is required. User can add the item to his wishlist via clicking in the "heart" icon placed in the right-bottom corner of the product card.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/wishlist.png?raw=true" alt="wishlist">
</p>
<br>

**Dashboard** - The information about the User that is automatically implemented in the checkout form.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/dashboard.png?raw=true" alt="dashboard">
</p>
<br>

**Reviews** - Reviews section is on the product details page - registered User can add, edit and remove the review.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/reviews.png?raw=true" alt="reviews">
</p>
<br>

**Request Refund** - This page is providing a User with the simple form, where he can request a refund but also send a complaint or any other message to the store owner.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/refund.png?raw=true" alt="refund">
</p>
<br>


#### **Color scheme**

Following the color scheme of the current store of my Client - I have stayed with the shades of gray: a lot of white space and high-contrast elements in black.
I added a soft touch of color "Teal Blue", which brought little dynamics into a page and is working well with the css animations I have implemented.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/my-col.png?raw=true">
</p>
<br>
<p align="right"><a href="#welcome">Back to top</a></p>

## **Implementation**

### **Branches in GIT**
The implementation of this project was done in Gitpod (the virtual environment). At first, I was working in the main branch where I have set and configured my Django project, created a home app and the base template.
After initial deployment on Heroku (see: Deployment) I have followed the suggestion of my Mentor to create separate branches for different tasks.

Using the Jira automation tools, I have connected this repository on GitHub with my project board. The names of the branches follow the Jira story numbers. Each commit message contains the story number of the task that was done and is visible in the Jira backlog. I have also added comments and images to the particular tickets with information that can make the code more readable and easily accessible during the future implementations.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/git_fetch_pull_second.png?raw=true" alt="git">
</p>
<br>
<p>Automation with Jira:

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/jira_autom.png?raw=true" alt="jira_automation">
</p>
<br>

### **Defensive design**
**Error pages (404 and 500)**

If 404 or 500 error occurs within the site, User will see the customized page that contains the information about the error and button to go back to the Home page.
<br>
Inspiration --> CodePen: <a href="https://codepen.io/mhdmhsni/pen/NmRojB" target="_blank">"Simple 404 Page" by Mehdi Mohseni</a>

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/error404.png?raw=true" alt="error page">
</p>
<br>

### **Features**
<br>

**Stripe payment**
<br>
During the implementation of this project I have been closely following the last tutorial provided by Code Institute: "Boutique Ado ''. All code connected with Stripe payments as well as configuration of webhooks is based on the code provided by CI. I have implemented a few changes required by the difference between the Order models, however I can not take any accreditation for this part of my application.
<br>
Thanks to setting up the webhooks, every intent of the payment is registered by Stripe and accessible in the Stripe administration panel.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/payment_intend.png?raw=true" alt="payment intend">
</p>

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/stripe_success.png?raw=true" alt="payment-success"></p>
<br><br>
                                                                                                                                                     
**Google Auth**
<br>
I have added to my application the social account authorization - firstly it was possible to login via Facebook and Google. Unfortunately during the process, I have lost the access to the facebook authorization tokens and did not have time to configure the login again - this is why I left only the Google authorization available and surely will be expanding the social accounts more as it is very popular way to encourage Users to log into our page and allows owners of the page to collect (some) data, which may be useful in marketing/economy planning.
<br>

In order to connect the Django App with Google API, I created a project: "PCG-Heroku" and connected it with OAuth consent screen to finally receive the credentials: Client_ID and Client Secret Key --> attached them to my Heroku Vars list.
<br>

**Subscription via MailChimp**
<br>
This is another interesting feature which is a good practice in terms of marketing planning, trying to gain information about your potential customer as well as get into a direct contact with customer, which allows to build the trust and create positive B2C relationship.
<br>

**Hosting the database in AWS S3 Bucket**
<br>
Similary to setting up API with Google Cloud, there was a necessity to sign up for a developers account and follow a specific path of creation a group, then User and via adding those objects into an S3 forms. I was able to obtain the sensitive credentials which I have set in Heroku Vars.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/aws-bucket.png?raw=true" alt="aws"></p>
<br>

**Star Rating**
<br>
I have implemented a star-rating django library as the rating system is well known to be a strong selling point - however the code that I've fetched from the library was very chaotic and unclear - this is why finally I have decided to resign from using the version that may cause further issues and errors. I decided it will be more efficient to wait with implementation of this feature and provide good quality code to handle it.

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/star_ratings.png?raw=true" alt="star rating"></p>           <br>
  
**Further implementations**
<br>
There are a few features that should have place in the further implementations – before the application could go into actual use:
- Locations page: includes the Google Maps widget with pins that shows the locations of the stores <br> *(You can find this feature in my <a href="https://github.com/KlaudiaBC/Resume-Project" target="_blank">Resume Project</a>)*
- Improvement of the wishlist functionality
- Save billing address of the registered customer
- Allow adding more images of the products and add carousel that allows to swipe them
- A contact form
- The profile page with possibilities to update and remove information
- Admin in-app functionality
- More social accounts providers

<br>
<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/further_impl.png?raw=true" alt="futher implementations"></p>
<br>

<p align="right"><a href="#welcome">Back to top</a></p>

## **Business model**
  - Who is the customer? --> B2C - individual customer
  - What will they buy? --> The deliverable is a product.
  - How will they pay? --> Single payment, which means the transaction is finished after the single payment is done.

1. Individual customers are more likely to purchase the product impulsively, therefore it is important to make the check out process as quick and easy as possible.
2. While the product is a deliverable, the database should include: product details, stock numbers, shipping or delivery costs, postal address of the customer, who purchased the order, ratings/reviews of the product as well as its image. The features should include: search tools, notice when the product is out-of-stock and notification for the customer about the order.


### **Marketing strategy**           
                                   
 <p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/persona.png?raw=true"></p>                                                         
<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/core_points.png?raw=true" alt="core points"></p>
                          
                                   
#### **Content marketing:**
The marketing plan is aimed at:
<ul>
  <li> determining of the target group</li>
  <li> determining the trends prevailing mostly in the Dutch society (but also worldwide) in matters of online shopping</li>
  <li> appointment of tasks aimed at reaching the above-mentioned target group</li>
  <li> determining the budget for marketing purposes</li>
  <li> planning activities related to communication with a potential client</li>
  <li> defining specific actions related to running a 360-degree marketing strategy, and thus:
      a) a plan of content marketing: social media accounts / blogging / newsletter,
    b) a plan of experiential marketing activities (events)</li>
  <li> defining the methods and tools used to measure the effectiveness of the strategy</li>
  <li> defining deadlines associated with specific activities in the future</li>
  <li> forecasts of results and determination of efficiency targets</li>
</ul>
<br>

**Time frame of the project:**
<br>
After the first month of operation, the project will be evaluated for effectiveness. Then a decision will be made as to whether the planned campaign is efficient or there are any necessary changes.
<br>

#### **Social Media**
Facebook / Instagram / TikTok:
  <ul>
  <li> advertisement on FB, IG</li>
  <li> regular posting, photos, videos</li>
  <li> thematic drawings or pictures (holidays, Valentine's Day etc.) - designed and created directly for the brand (not copied from other websites)</li>
  <li> personal message (e.g. “behind the scenes” of creating products)</li>
  <li> leveling up with the average pole, follow the statistics and adjust the strategy to meet New Users</li>
  </ul>
<br>

**Posts:**
<br>
For the first 3 months posts should be added at least 2x a week and should be: interesting, divided, personalized, regular. Routine - add one post at a constant time of the day every day: e.g. in the morning or in the evening (make the User adjust to regular contact, schedule and create a trust tower, expectations).
<br>

**Theme post:**
<br>
  - Posts related to current celebrations, holidays etc.
  - Hair care, skin care and wellbeing
  - Questions about opinions, it is best to ask a question in a personal form, eg "This morning I thought about putting on a dress, I'm counting down the days until spring with impatience! Are you cold? Do any of you share my ideas for today's creations?" (the same applies to instagram: it is important to ALWAYS post also all the content on the “story” - FB and IG).
<br>

#### **Newsletter**
Collecting data for the newsletter via *"Subscribe for newsletter"* button on the website. Once a week: "Smart Collection" - Updates on items exhibited by our customers. Additionally: wishes for Christmas, Easter, Women / Men's Day, referring to children's day, birthday, Valentine's Day, Halloween, etc.
<br>

#### **Public Relations**
  - opening gala (contact local press)
  - contact via social media
  - contact via form located on the web page
  - after 12 months of functioning - a charity event
  - remember: respond to the customer within one working day, be polite and professional
<br>

#### **Search Engine Optimization**

SEO including descriptive meta tags, keywords included in the "alt" attribute of images. Links to high-ranked websites that are connected with the content of the page. Robots.txt and sitemaps.xml are included.
                                                                                                                          
 <p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/words1.jpg?raw=true"></p>
  
  
  <p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/words2.jpg?raw=true"></p>
  
  
  <p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/words3.jpg?raw=true"></p>
  
  
  <p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/words4.jpg?raw=true"></p>
                                                                                                                                                                                                                                                                          
In order to find the **most effective keywords** for my SEO, I have followed those steps:
1. Write down all the keywords that match the website and its purpose.
2. Take away the most common keywords (too popular keywords are too competitive)
3. Search for keywords in Google:
    - check autocomplete predictions
    - check "People also ask" section
    - check "People also search for" section
    - check "Related searches" section
4. I have used the Wordtracker in order to see the quantity of particular words exciting on the web and compare them to other keywords I collected, trying to choose the one that is less competitive.
5. I have used the Google Trends platform to search for related keywords and check geographical keyword variations.
                              
                              
  <p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/keywords_table.png?raw=true"></p>                             <br>            

#### **Control and updating procedures**
  - BUZZSUMO - monitors the internet in terms of making a given article available to users, has internet monitoring functions in terms of content and competition (keywords)
  - FACEBOOK AUDIENCE INSIGHTS - information about: how big is the target group on Facebook, how it behaves (which pages User likes, how many times in a month
he clicks "I like it" etc.)
  - Programs for editing / graphic processing: PIXLR, Canva
  - Programs useful for updating / publishing new content - PHOTO BANKS: Shutterstock, Fotolia (PAID) + Site Builder Report (FREE OF CHARGE)
  - Sotrender - the best social media tool on the market, which will allow you to analyze activities on Facebook, Twitter, YouTube, Instagram, and suggest what can be improved to make the engagement on these channels higher
  - Brand24 and Sentione are two tools for monitoring social media as well as broadly understood Internet (portals, websites). These tools will tell you if internet users are talking about the brand and where exactly.
  - Google Analytics
 
  <p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/sitemaps.png?raw=true"></p>      

<p align="right"><a href="#welcome">Bact to top</a></p>

## **Testing**
The testing documentation is in separate file: <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/TESTING.md" target="_blank">TESTING.md</a> 

<p align="right"><a href="#welcome">Bact to top</a></p>

## **Deployment**
1. Installing project requirements.
In the terminal run commands pip3 install (i used pip3 instead of pip - in order to specify the Python version that is used, by default it is version 2):
- Green unicorn, server used to run Django on Heroku: *gunicorn*
- PostgreSQL libraries:
*dj_database_url*
*psycopg2*

Create the *requirements.txt* via command in the terminal:
*pip3 freeze --local > requirements.txt*

2. Add env.py
In the main repository create a new file called *"env.py"* in order to store sensitive information. Make sure the *env.py* file is included in the *.gitignore* file and will not be saved while the changes are committed.
(You can create the env.py file in the terminal via command: *touch env.py*)

In the *env.py file*: import operating system (os) and add following variables: *SECRET_KEY, DATABASE_URL*.
In *settings.py* find a variable called *SECRET_KEY* and cut its value. Paste the value into *env.py*.
Then in the *settings.py* refer to this value via function: *os.environ.get()*

3. Create a heroku app via CLI.
- At first, you have to create an account on *Herokuapp*.
- Next step is to install the heroku CLI in Gitpod and login into your Heroku account via command: *heroku login -i*
- In order to create an app, follow the command:
*heroku apps:create my_appname*
In order to set the region to EU, add to the command: *--region eu*
Otherwise, by default the region will be set to US.

4. Create a database on Heroku.
- In the *"Resources"* Tab find *"Heroku Postgres"* and add it to your app.
- Go to *"Settings"*, click on: *"Reveal Vars"* and copy the value of *DATABASE_URL* key.
- Go back to your workspace. In the *env.py* file paste value into the variable *DATABASE_URL*.
- In the *settings.py* file: comment out the *DATABASE* settings and set the *DATABASE* to the Postgres database accessible via *DATABASE_KEY*
- import *dj_database_urls*
- run migrations
You will see that all the migrations are happening because of the database connection. Now the project is using the Heroku database as backend.

5. Prepare your environment
- From the *env.py* copy the value of *SECRET_KEY* variable.
- Go to Herokuapp --> Settings/ reveal and add the following Vars:
SECRET_KEY (value: paste)
HEROKU_HOSTNAME - the url of your heroku app
PORT - 8000
DISABLE_COLLECTSTATIC - give it value of 1 in order to get the empty project running as if there are no static files at the moment of initial deployment (later this variable must be removed).

6. Create a Procfile
In the *Procfile* (make sure the name is starting with capital letter) you need to specify the commands that are executed by the app on startup. In this case, it is:  *web: gunicorn empire_blog.wsgi*

7. Commit and push.
In my case, that was the first commit since creating the Django project. In other cases, I would have to make some changes which would allow me to run the push command.
- Commit all changes.
- Push the commit into: origin main
- Push the commit into: heroku main

<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/README/deploy_cli.png?raw=true" alt="cli">
</p>

8. At this stage your app should be correctly deployed on Herokuapp.

9. Connect Github to Heroku
In order to avoid deploying changes in the terminal twice, you can connect your project on Heroku to your Gitpod.
In order to do so - in the *"Deploy"* tab scroll down and click the button *"Connect to GitHub"*. Then set: *deploy automatically*. You can also disable automatic deployment and run your deployment manually at your own chosen time.

10. Final deployment
Before the application will be handeled to the client in the realise 1.0 stage, there are two very important steps to be taken:
- detele DISABLE_COLLECTSTATIC from your confiv VARS in Heroku
- in the setting.py file, set the **DEBUG=False** in order to protect sensitive information - *IMPORTANT!*

By now your app should be ready and running.
Unless your Django project will not read the staticfiles with the Debug set to *False*.
See how to handle that in the TESTING.md file / Errors and bugs.
<a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/TESTING.md" target="_blank">You can find it here.</a>


### **Fork this Project**
At first, make sure you are logged into your GitHub account.
Fork this repository by clicking the button "Fork", placed in the top right corner of the page.
Once the button is clicked, the repository will be copied to your GitHub account and shown in the list of your repositories.


### **Clon this Project**
At first, make sure you are logged into your GitHub account.
Click the drop-down button "Code" located above the list of files, on the right side.
Chose one of the options in the tab menu, to clone the repository using:
  • HTTPS,
  • SSH key
  • Git CLI


In order to process the clone request, copy the link provided in the tab of your choice via clicking the clipboard icon.
In the new terminal, change the current working directory to the location where you want the cloned repository to be stored.
Use the command: "git clone" + the copied URL.

Eg. If you cloning the repository using HTTPS, the command should look like this:

https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl.git

You can now access your local clone created in the specified earlier directory.

<p align="right"><a href="#welcome">Bact to top</a></p>

## **Technologies Used**
I have used the following technologies and support sources:
- <a href="https://www.w3schools.com/html/html_intro.asp" target="_blank">HTML5</a>
- <a href="https://www.w3schools.com/css/" target="_blank">CSS3</a>
- <a href="https://www.djangoproject.com/" target="_blank">Django 3.2.15</a> as a back-end framework
- <a href="https://www.python.org/" target="_blank">Python 3.8.11</a> as a main programming language
- <a href="https://www.djangoproject.com/" target="_blank">JavaScript</a> as a additional programming language
- <a href="https://getbootstrap.com/" target="_blank">Bootstrap v.4.6</a> as a front-end framework
- <a href="https://github.com/" target="_blank">GitHub</a> for hosting and managing my Git repositories
- <a href="https://git-scm.com/" target="_blank">Git</a> for managing and keeping track of my source code history
- <a href="https://www.heroku.com/" target="_blank">Heroku</a> for deployment
- <a href="https://developer.chrome.com/docs/devtools/" target="_blank">Chrome DevTools</a> (for testing throughout the workflow)
- <a href="https://www.atlassian.com/" target="_blank">Jira Software</a> for Agile Scrum
- <a href="https://app.diagrams.net/" target="_blank">Draw.io</a> for wireframes
- <a href="https://www.xml-sitemaps.com/" target="_blank">XML-Sitemaps</a> for the sitemaps.xml
- <a href="https://fontawesome.com//" target="_blank">FontAwesome for all for all icons included in the page 
- <a href="https://www.flaticon.com/" target="_blank">Flaticon</a> by Freepik / for all vector images (checkout success/empty shopping bag)
- <a href="https://coolors.co/" target="_blank">Coolors</a> for a color pallete
- <a href="https://ezgif.com/" target="_blank">Ezgif</a> for optimization of the images used in the project


*API services:*
- <a href="https://stripe.com/" target="_blank">Stripe for secure, online payment system</a>
- <a href="https://dashboard.heroku.com/" target="_blank">Heroku for the application deployment</a>
- <a href="https://us21.admin.mailchimp.com/" target="_blank">MailChimp for subscribtion automation</a>
- <a href="https://cloud.google.com/" target="_blank">Google Cloud for authorisation</a>
- <a href="https://https://aws.amazon.com/" target="_blank">AWS S3 bucket for storing the data
                                                                                            
<p align="right"><a href="#welcome">Bact to top</a></p>

                                   
## **Acknowledgements**

In this place I would like to thank everyone, who added an knowledge and value to this project:
- <a href="https://codeinstitute.net/" target="_blank">Code Institute</a> course, materials and walkthroughs - A great part of this project is done in accordance to the last walktrough: "Boutique Ado" - Stripe payments, checkout page and functionality / and probably many many more as the walktrough's during all my journey with CI was the most suffitient way to learn and understand coding
- lead and support of my Code Institute Mentor - Guido Cecilio - also great patience!
- Hanan el Fizazi - for allowing me to build my own e-store using her brand, product images and story --> all product images included in this project are copied directly from the Pretty Curly Store website. Social media links also provide direction to PCG Original Pages as it allowed me to create very realistic demo of e-commerce application
- Code Institute Slack Community
- <a href="https://stackoverflow.com/" target="_blank">Stack Overflow</a>
- <a href="https://www.w3schools.com/" target="_blank">W3schools</a>
- <a href="https://www.djangoproject.com/" target="_blank">Django documentation</a> by Django
- <a href="https://developer.chrome.com/docs/" target="_blank">Chrome Developers</a> documentation
- <a href="https://www.djangoproject.com/" target="_blank">Django</a> documentation
- <a href="https://developers.google.com/identity/protocols/oauth2" target="_blank">Google Developers</a> documentation for OAuth
- <a href="https://docs.aws.amazon.com/s3/index.html?nc2=h_ql_doc_s3#amazon-s3" target="_blank">Amazon AWS</a> documentation for Amazon S3
- <a href="https://devcenter.heroku.com/categories/python-support" target="_blank">Heroku Dev Center</a> - Python Support
- <a href="https://console.cloud.google.com/apis" target="_blank">Google Cloud Console</a> for Google API
- <a href="https://ordinarycoders.com/blog/article/django-user-register-login-logout" target="_blank">"A Guide to User Registration, Login, and Logout in Django"</a> by < ordinary > coders
- <a href="https://dev.to/lawrence_eagles/causes-of-heroku-h10-app-crashed-error-and-how-to-solve-them-3jnl" target="_blank">"Causes of Heroku H10-App Crashed Error And How To Solve Them"</a> by Dev.to
- <a href="https://realpython.com/django-hosting-on-heroku/" target="_blank">"Hosting a Django Project on Heroku"</a> by Real Python
- <a href="https://www.atlassian.com/agile/project-management/user-stories" target="_blank">"User stories with examples and a template"</a> by Atlassian
- <a href="https://www.easyagile.com/blog/how-to-write-good-user-stories-in-agile-software-development/" target="_blank">"How to Write Good User Stories in Agile Software Development"</a> by EasyAgile
- <a href="https://www.knowledgehut.com/blog/agile/powerful-tips-for-writing-the-best-user-stories-in-scrum" target="_blank">"Powerful Tips for Writing the Best User Stories in Scrum"</a> by Knowledgehut
- <a href="https://dribbble.com/tags/ecommerce_app" target="_blank">"Ecommerce App (design inspirations)"</a> by Dribbble.com
- <a href="https://www.google.com/amp/s/appinventiv.com/blog/ecommerce-app-features-for-startups-and-enterprises/" target="_blank">"Top 10 eCommerce app features for startups and enterprises"</a> by Appinventiv.com
- <a href="https://mindsea.com/mobile-app-marketing/" target="_blank">"Mobile app marketing"</a> by Mindsea
- <a href="https://mindster.com/mindster-blogs/ecommerce-applications/" target="_blank">"How e-Commerce Applications Help Your Business Grow?"</a> by Mindster
- <a href="https://buildfire.com/mobile-app-ecommerce-marketing-ideas/" target="_blank">"Mobile ecommerce marketing ideas"</a> by Buildfire
- <a href="https://blog.hubspot.com/marketing/ecommerce-marketing" target="_blank">"Everything you need to know about ecommerce marketing"</a> by HubSpot
- <a href="https://www.zoho.com/inventory/sku-generator/" target="_blank">Sku generator</a>
- <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication" target="_blank">"HTTP Authentication"</a> by MDN Web Docs
- <a href="https://www.hostinger.com/tutorials/how-to-fix-the-401-unauthorized-error#1_Confirm_the_URL_Is_Correct" target="_blank">"401 Error: 5 Ways to Troubleshoot and Fix It"</a> by Hostinger Tutorials
- <a href="https://www.pythonmorsels.com/breaking-long-lines-code-python/" target="_blank">"Breaking long lines of code in Python"</a> by Python Morsels


Media used:
- All images of the products are coming directly from the Client: <a href="https://prettycurlygirl.store/" target="_blank">Pretty Curly Girl</a>
- Image of persona: <a href="https://www.pexels.com/photo/women-wearing-black-clothes-7623816/" target="_blank">Photo by Mikhail Nilov</a> via Pexels
- Google Logo Icon: <a href="https://icons8.com/icon/17949/google" target="_blank">Google icon</a>
- Favicon Generator: <a href="https://favicon.io/favicon-generator/" target="_blank">Favicon</a>
- Images in the "blog" section / home page:
<a href="https://www.pexels.com/photo/back-view-of-woman-with-curly-hair-8377518/" target="_blank">PNW Production</a>, 
<a href="https://www.pexels.com/photo/girl-wearing-pink-white-teal-and-blue-crew-neck-cold-shoulder-standing-near-fence-1068205/" target="_blank">Photo by nappy</a> and 
<a href="https://www.pexels.com/@cottonbro/" target="_blank">Cottonbro</a>
- Hero Image <a href="https://www.pexels.com/photo/women-s-pink-sweatshirt-and-brown-plaid-skirt-794064/" target="_blank"> Photo by Godisable Jacob from Pexels</a>


<p align="right"><a href="#welcome">Bact to top</a></p>
