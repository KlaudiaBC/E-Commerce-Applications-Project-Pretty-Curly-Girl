# E-Commerce Application: "Pretty Curly Girl" Portfolio Project
## Welcome!

<p id="welcome"></p>

## This is my Portfolio 5 Project regarding the Code Institute's Diploma in Software Development (E-commerce Applications).
It is an e-commerce application - built with Django / Python / Bootstrap and deployed on Heroku.

See the live project <a href="https://pretty-curly-girl.herokuapp.com/">here</a>.

<p align="center">
  <img src="" alt="">
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
    * [**Typography**](#typography)
* [**Implementation**](#implementation)
    * [**Branches in GIT**](#branches-in-git)
    * [**Performance**](#performance)
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

In this file I have documented all insights, steps and the obstacles I have met during implementation. All technical issues have been documented also in the Jira - you can access the board of this project here.
In addition, you can also find a basic e-commerce marketing strategy which includes critical points for the web implementation process like the SEO keywords.
--> For more, please see: Marketing


### **Product roadmap**
Following the Agile principles, I have created the *User Stories*, which helped me to map out the work required to develop this application. In order to easily manage the workflow, I have used the <a href="https://jira.atlassian.com/" target="_blank">Jira software</a>.

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
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/static/images/README/jira_backlog_sprint_one.png?raw=true" alt="backlog_sprint_one">
</p>


**Jira backlog - Sprint 2:**
<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/static/images/README/jira_backlog_sprint_two.png?raw=true" alt="backlog_sprint_two">
</p>


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
- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/static/images/README/wireframes/PCG-home_desktop.png?raw=true" target="_blank">Wireframe for the home page - desktop</a>
- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/static/images/README/wireframes/PCG_product_list_page_desktop.png?raw=true" target="_blank">Wireframe for the product list page - desktop</a>
- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/static/images/README/wireframes/PCG_product_detail_desktop.png?raw=true" target="_blank">Wireframe for the product detail page - desktop</a>
- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/static/images/README/wireframes/PCG_locations_desktop.png?raw=true" target="_blank">Wireframe for the locations page - desktop</a>

- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/static/images/README/wireframes/PCG_landing_page_mobile.png?raw=true" target="_blank">Wireframe for home page - mobile devices</a>
- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/static/images/README/wireframes/PCG_product_list_mobile.png?raw=true" target="_blank">Wireframe for the product list page - mobile devices</a>
- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/static/images/README/wireframes/product_detail_page_mobile.png?raw=true" target="_blank">Wireframe for the product detail page - mobile devices</a>
- <a href="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/static/images/README/wireframes/PCG_locations_mobile.png?raw=true" target="_blank">Wireframe for the locations page - mobile devices</a>

#### **Database Schema**
I have implemented **PostgreSQL (Postgres)** - the open-source database object-relational database system, which is an extension of the SQL language.
<p align="center">
  <img src="https://github.com/KlaudiaBC/E-Commerce-Applications-Project-Pretty-Curly-Girl/blob/main/static/images/README/heroku_data_postgres.png?raw=true" alt="postgres">
</p>

Entity relationship diagram for all the models included in the application:
<p align="center">
  <img src="#" alt="entity relationship diagram">
</p>


### **Surface**

#### **Base (common for each page of application):**

**Logo and navbar:**
Sticky top, includes logo (left side) and the navbar on the right side (burder-menu on the mobile devices)
Menu includes following:

<p align="center">
  <img src="#" alt="landing page desktop">
</p>

**Footer** - on the bottom of the page, contains information about the author, links to social media accounts (buttons/icons) and link to the Regulations.


#### **Content of the pages:**

Register page - contains one card with registration form and buttons to submit or to go back.

<p align="center">
  <img src="#" alt="register_page">
</p>

Login page - contains one card with login form and buttons to submit or go back.

<p align="center">
  <img src="#" alt="login_page">
</p>

Newsfeed page (Home): The posts are wrapped in the card element and displayed in descending order. Each card has the same size and contains: the category, topic, date of creation, the author, snippet of the post content. Button *"Read more"* moves the User to the detalic view of the chosen post.

<p align="center">
  <img src="#" alt="home_page">
</p>

MyPage - render the same view as the home page, but display filtered posts- only the one which was created by the User. There are two buttons added into a post card: *"Edit"* and *"Delete"*.


Detalic view page - render the: title, author, date and body of the particular post. Below there is a *"like"* button - User can like and unlike the post by clicking the *"like"* icon. Third part of the container is a comment section, where all added and approved by Admin comments are displayed in ascending order. On top of this section is located an *"Add comment"* button which render the Add Comment Form.

<p align="center">
  <img src="#" alt="view_page">
</p>


#### **Color scheme**


<p align="center">
  <img src="#" alt="colors">
</p>

#### **Typography**


<p align="right"><a href="#welcome">Bact to top</a></p>

## **Implementation**

### **Branches in GIT**
The implementation of this project was done in Gitpod (the virtual environment). At first I was working in the main branch where I have set and configured my Django project, created a home app and the base template.
After initial deployment on Heroku (see: Deployment) I have followed the suggestion of my Mentor to create separate branches for different tasks.

Using the Jira automation tools, I have connected this repository on GitHub with my project board. The names of the branches follow the Jira story numbers. Each commit message contains the story number of the task that was done and is visible in the Jira backlog. I have also added comments and images to the particular tickets with information that can make the code more readable and easily accessible during the future implementations.


### **Performance**
• In some cases I have been using the code provided by external sources (see: Acknowledgements). Some of them contained jQuery which I have changed to vanilla Javascript.

• I have stored images of all icons used in the project in my internal static files and manually customized them in order to avoid using Font Awesome because of its extensive size.


### **Defensive design**
**Error pages (404 and 500)**

If 404 or 500 error occurs within the site, User will see the customized page that contains the information about the error and button to go back to the Home page.


### **Features**
1. Create a basic Django project and first application
2. Initial deployment
3. Create Superuser
4. User authentication
5. Create product model
6. Add templates
6. CRUD for Users
7. Reviews
8. Categories
9. Messages
10. Error pages
11. Email API

<p align="center">
  <img src="#" alt="jira_sprint">
</p>

<p align="right"><a href="#welcome">Bact to top</a></p>

## **Business model**


### **Marketing strategy**
#### **Content marketing:**
The marketing plan is aimed at:
<ul>
  <li> determining of the target group</li>
  <li> determining the trends prevailing mostly in the Dutch society (but also worldwide) in matters of online shopping</li>
  <li> appointment of tasks aimed at reaching the above-mentioned target group</li>
  <li> determining the budget for marketing purposes</li>
  <li> planning activities related to communication with a potential client</li>
  <li> defining specific actions related to running a 360 degree marketing strategy, and thus:
      a) a plan of content marketing: social media accounts / blogging / newsletter,
    b) a plan of experiential marketing activities (events)</li>
  <li> defining the methods and tools used to measure the effectiveness of the strategy</li>
  <li> defining deadlines associated with specific activities in the future</li>
  <li> forecasts of results and determination of efficiency targets</li>
</ul>

**Time frame of the project:** After the first month of operation, the project will be evaluated for effectiveness. Then a decision will be made as to whether the planned campaign is efficient or there are any necessary changes.


#### **Social Media**
Facebook / Instagram / TikTok:
  <ul>
  <li> advertisement on FB, IG</li>
  <li> regular posting, photos, videos</li>
  <li> thematic drawings or pictures (holidays, Valentine's Day etc.) - designed and created directly for the brand (not copied from other websites)</li>
  <li> personal message (eg. “behind the scenes” of creating products)</li>
  <li> leveling up with the average pole, follow the statistics and adjust the strategy to meet New Users</li>
  </ul>


**Posts:** For the first 3 months posts should be added at least 2x a week and should be: interesting, divided, personalized, regular. Routine - add one post at a constant time of the day every day: eg in the morning or in the evening (make the User adjust to regular contact, schedule and create a trust tower, expectations).


**Theme post:**
  - Posts related to current celebrations, holidays etc.
  - Hair care, skin care and wellbeing
  - Questions about opinions, it is best to ask a question in a personal form, eg "This morning I thought about putting on a dress, I'm counting down the days until spring with impatience! Are you cold? Do any of you share my ideas for today's creations?" (the same applies to instagram: it is important to ALWAYS post also all the content on the “story” - FB and IG).


#### **Newsletter**
Collecting data for the newsletter via *"Subscribe for newsletter"* button on the website. Once a week: "Smart Collection" - Updates on items exhibited by our customers. Additionally: wishes for Christmas, Easter, Women / Men's Day, referring to children's day, birthday, Valentine's Day, Halloween, etc.


#### **Public Relations**
  - opening gala (contact local press)
  - contact via social media
  - contact via form located on the web page
  - after 12 months of functioning - a charity event
  - remember: respond to the customer within one working day, be polite and professional


#### **Search Engine Optimization**
In order to find the most effective **keywords** for my SEO, I have followed those steps:
1. Write down all the keywords that match the website and its purpose.
2. Take away the most common keywords (too popular keywords are too competitive)
3. Search for keywords in Google:
    - check autocomplete predictions
    - check "People also ask" section
    - check "People also search for" section
    - check "Related searches" section
4. I have used the Wordtracker in order to see the quantity of particular words exciting on the web and compare them to other keywords I collected, trying to choose the one that is less competitive.
5. I have used the Google Trends platform to search for related keywords and check geographical keyword variations.

#### **Control and updating procedures**
  - BUZZSUMO - monitors the internet in terms of making a given article available to users, has internet monitoring functions in terms of content and competition (keywords)
  - FACEBOOK AUDIENCE INSIGHTS - information about: how big is the target group on Facebook, how it behaves (which pages User likes, how many times in a month
he clicks "I like it" etc)
  - Programs for editing / graphic processing: PIXLR, Canva
  - Programs useful for updating / publishing new content - PHOTO BANKS: Shutterstock, Fotolia (PAID) + Site Builder Report (FREE OF CHARGE)
  - Sotrender - the best social media tool on the market, which will allow you to analyze activities on Facebook, Twitter, YouTube, Instagram, and suggest what can be improved to make the engagement on these channels higher
  - Brand24 and Sentione are two tools for monitoring social media as well as broadly understood Internet (portals, websites). These tools will tell you if internet users are talking about the brand and where exactly.
  - Google Analytics

<p align="right"><a href="#welcome">Bact to top</a></p>

## **Testing**
The testing documentation is in separate file: <a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/TESTING.md">TESTING.md</a> 

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
  <img src="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/static/images/readme/deploy_cli.png?raw=true" alt="cli">
</p>

8. At this stage your app should be correctly deployed on Herokuapp.

9. Connect Github to Heroku
In order to avoid deploying changes in the terminal twice, you can connect your project on Heroku to your Gitpod.
In order to do so - in the *"Deploy"* tab scroll down and click the button *"Connect to GitHub"*. Then set: *deploy automatically*. You can also disable automatic deployment and run your deployment manually at your own chosen time.

10. Final deployment
Before the application will be handeled to the client in the realise 1.0 stage, there are two very important steps to be taken:
- detele DISABLE_COLLECTSTATIC from your confiv VARS in Heroku
- in the setting.py file, set the **DEBUG=False** in order to protect sensitive information - IMPORTANT!

By now your app should be ready and running.
Unless your Django project will not read the staticfiles with the Debug set to *False*.
See how to handle that in the TESTING.md file / Errors and bugs.
<a href="https://github.com/KlaudiaBC/FST-Project-Empire-of-Thoughts/blob/main/TESTING.md#errors-and-bugs" target="_blank">You can find it here.</a>


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
- <a href="https://developer.chrome.com/docs/devtools/">Chrome DevTools</a> (for testing throughout the workflow)
- <a href="https://www.atlassian.com/" target="_blank">Jira Software</a> for Agile Scrum
- <a href="https://app.diagrams.net/" target="_blank">Draw.io</a> for wireframes
- <a href="https://fonts.google.com/" target="_blank">Google Fonts</a> for the "logo" font
- <a href="https://www.flaticon.com/" target="_blank">Flaticon</a> by Freepik / for all icons included
- <a href="https://coolors.co/" target="_blank">Coolors</a> for a color pallete
- <a href="https://pdfhost.io/" target="_blank">PDF Host</a> for hosting the document with User Stories

<p align="right"><a href="#welcome">Bact to top</a></p>


## **Acknowledgements**

In this place I would like to thank everyone, who added an knowledge and value to this project:
- <a href="https://codeinstitute.net/" target="_blank">Code Institute</a> course, materials and walkthroughs - A great part of this project is done in accordance to the last walktrough: "Boutique Ado"
- lead and support of my Code Institute Mentor - Guido Cecilio
- Code Institute Slack Community
- <a href="https://stackoverflow.com/" target="_blank">Stack Overflow</a>
- <a href="https://www.w3schools.com/" target="_blank">W3schools</a>
- 
- <a href="#">Some title</a> by ??
- 
- <a href="https://ordinarycoders.com/blog/article/django-user-register-login-logout" target="_blank">"A Guide to User Registration, Login, and Logout in Django"</a> by < ordinary > coders
- <a href="https://dev.to/lawrence_eagles/causes-of-heroku-h10-app-crashed-error-and-how-to-solve-them-3jnl" target="_blank">"Causes of Heroku H10-App Crashed Error And How To Solve Them"</a> by Dev.to
- <a href="https://realpython.com/django-hosting-on-heroku/" target="_blank">"Hosting a Django Project on Heroku"</a> by Real Python
- <a href="https://www.atlassian.com/agile/project-management/user-stories" target="_blank">"User stories with examples and a template"</a> by Atlassian
- <a href="https://www.easyagile.com/blog/how-to-write-good-user-stories-in-agile-software-development/" target="_blank">"How to Write Good User Stories in Agile Software Development"</a> by EasyAgile
- <a href="https://www.knowledgehut.com/blog/agile/powerful-tips-for-writing-the-best-user-stories-in-scrum" target="_blank">"Powerful Tips for Writing the Best User Stories in Scrum"</a> by Knowledgehut
- <a href="[https://www.canva.com/learn/social-media-design-trends-2022/](https://dribbble.com/tags/ecommerce_app)" target="_blank">"Ecommerce App (design inspirations)"</a> by Dribbble.com
- <a href="https://www.google.com/amp/s/appinventiv.com/blog/ecommerce-app-features-for-startups-and-enterprises/">"Top 10 eCommerce app features for startups and enterprises"</a> by Appinventiv.com
- <a href="https://mindsea.com/mobile-app-marketing/">"Mobile app marketing"</a> by Mindsea
- <a href="https://mindster.com/mindster-blogs/ecommerce-applications/">"How e-Commerce Applications Help Your Business Grow?"</a> by Mindster
- <a href="https://buildfire.com/mobile-app-ecommerce-marketing-ideas/">"Mobile ecommerce marketing ideas"</a> by Buildfire
- <a href="https://blog.hubspot.com/marketing/ecommerce-marketing">"Everything you need to know about ecommerce marketing"</a> by HubSpot
- <a href="https://www.zoho.com/inventory/sku-generator/">Sku generator</a>
- <a href="https://www.pythonmorsels.com/breaking-long-lines-code-python/">"Breaking long lines of code in Python</a> by Python Morsels
- <a href="#">Some title</a> by ??
- <a href="#">Some title</a> by ??
- <a href="#">Some title</a> by ??
- <a href="https://www.djangoproject.com/" target="_blank">Django documentation</a> by Django

Media used:
- All images of the products are coming directly from the Client: <a href="https://prettycurlygirl.store/">Pretty Curly Girl</a>
- Image of persona: <a href="https://www.pexels.com/photo/women-wearing-black-clothes-7623816/">Photo by Mikhail Nilov</a> via Pexels


<p align="right"><a href="#welcome">Bact to top</a></p>
