# Dragons Nest Gaming

![amiresponsive](readme/img/responsive.jpg)

Live App link : [Dragons Nest Gaming](https://dngshop.herokuapp.com/)
Git Hub Repository : [Dragons Nest Gaming](https://gurranasan-dragonsnestg-ojigzz9jbaa.ws-eu90.gitpod.io/)

Dragons Nest Gaming is a gamingstore in Norway I started together with my brothers. It started with my biggest brother who
sold Magic the Gathering cards on auction sites. All went well and they saw the intresset in the market in Stavanger there we lived and we started a pysical store there like minded could meet up. The store goes well and we sell some stuff through Facebook. But it is time for a E-commerce webpage so we can reach a bigger clientele. It is a business site that sells products to private custumers and it is singel payment. 

* Key featueres Include:
  - search and filters: User can search and filter products to easy find what they want.
  - Real-time availability: User can see if products is in stock and how many.
  - Cart & Stripe checkout: Users can add multiple products in there cart, see a total and then go to checkout with stripe. See [Stripes testing card details](https://stripe.com/docs/testing?testing-method=card-numbers#visa) to place an order on the website.
  - Ratings: A signd in user can leave rating and/or review on the products.
  - Authentication: User can create a account to save shipping details and leave reviews.
  - Event Calendar: A calender for the users to see if there are any Events going on in the store.

## Contents

+ [User Experience(UX)](#user-experience-ux)
     + [Color Scheme](#color-scheme)
     + [Icons](#icons)
     + [Wireframes](#wireframe)
 + [Agile Method](#agile-method)
      + [User Stories](#user-stories "User Stories")
      + [Data modal](#data-modal)
      + [Future Features](#future-features)
+ [Margeting](#margeting)
    + [E-Commerce Application](#E-Commerce-Application)
    + [Marketing Strategy](#Marketing-Strategy)
    + [Search Engine Optimization](#search-engine-optimization)
    + [XML Sitemap](#XML-sitemap)
+ [Page Features](#page-features)
   + [nav bar](#nav-bar)
   + [Index](#index-page)
   + [Shop](#shop)
      + [Products](#products)
      + [Cart](#cart)
      + [Checkout](#checkout)
      + [Confirmation](#confirmation)  
   + [Event](#forum)
      + [Calendar](#calendar)
      + [Event detail](#event-details)
   + [Profile](#profile)
      + [My profile](#my-profile)
      + [Add Review](#add-review)  
   + [Admin](#radmin)
      + [Manage products](#manage-products)
      + [Manage event](#Manage-event)
   
+ [Technologies](#Technologies)
   + [Programming Languages](#programming-languages)
   + [Support Programs & libraries](#support-programs-libraries)

+ [Testing](#Testing)
    + [Bugs](#bugs)
    + [ManuelTesting](#manuel-testing)
    + [NavigationHeader](#navigation-header)
    + [PageManualTesting](#home-page-maual-testing)
    + [Index page](#testing-index-page)
    + [SignInManualTesting](#sign-in-manual-testing)
    + [Shop](#teseting-forum)  
        + [Products](#category-page-testing)
        + [Cart](#cart-testing)
        + [Checkout](#checkout-testing)
        + [Confirmation](#confirmation-testing) 
    + [Calender](#teseting-forum)  
        + [Calender](#calender-testing)
        + [add/edit event](#add/edit-testingt)
    + [Profile](#profile-testing)  
        + [profile info](#profile-info-testing)
        + [add/edit rating](#add/edit-rating)             
    + [Validation](#Validation)
        + [HTML](#html)
        + [CSS](#css)
        + [Python](#python)
        + [Javascrip](#javascript)
        + [Lighthouse](#lighthouse)
   
+ [Deployment](#deployment)
   + [Github](#github)
   + [Gitpod and Django](#gitpod-and-django)
   + [Heroku](#heroku)   
   
+ [Acknowledgments](#acknowledgments)
    + [Credits](#credits)
    + [Copied Code](#copied-code)

### User Experience UX
  
  The plan for the site was to build a slim site that was easy for users to use and find what thay want. I also wanted to build a event calendar for the users that live close to the store so they could meet up. 
  The font name for the page is: K2D a slim but easy to read. 
  
#### Color Scheme

I choose to use limited color scheme of Orange #f29100, Black and White. I got the Orange color from the logo 
so it feels like everyting fits in. And with Black and white it is easy to make contrast. 

In some placees i used Green for succes/Add, Red for warning/delete to get a more user friendly experience.

#### Icons
I used icons from Font Awsome extensivley on the website. They are used within the nav bar to reduce the need for verbose descriptions such as 'search. I have used them on buttons to reinforce the action of the button.

#### Wireframes

When I started the project I made up some wire frames to the core structure for the page. 

![index_wireframe](readme/img/index_wireframe.jpg)

This is for the Homepage/Index page I wanted it to be slim with not that much text. But easy nav menu so the user could find what they wanted fast. I also draw up 
an idea for the footer. But as you can see i did some changes,i moved down the nav menu abit and rearranged the footer. But the original content is there. 


![product_wireframe](readme/img/products_wirefram.jpg)

This was my idea for the product page, where you could see and filter the products. I change so there was only 3 products in a row. I also added a in stuck icon so the user could see if there was in stock.


![product_details_wireframes](readme/img/product_details_wireframes.jpg)

For the product details page i moved around the content to, I felt there was better to have the put in bvag button over the description so it would be easyer to press
if the description was long. I also added a average rating so user could now what other thinhgs and a carousel for reviews if there is any. 


![cart_wireframe](readme/img/cart_wireframe.jpg)

The final cart page looks like the origninal idea. 
  
### Agile Method 

I used the github projects as a agile tool to manage the planning and implamentation of functions to the site. 
[Project Board](https://github.com/users/GurraNasan/projects/6)

#### User Stories
  Before I started to code a took a meeting with my brothers to tall about what they wanted on the site and we put up some user-stories and prioritized using MoSCoW. This is the user stories:
  + [USER STORY: Manage products](https://github.com/GurraNasan/dragons-nest-gaming/issues/1)
    [USER STORY: Event handling](https://github.com/GurraNasan/dragons-nest-gaming/issues/2)
    [USER STORY: Send newsletter](https://github.com/GurraNasan/dragons-nest-gaming/issues/3)
    [USER STORY: Moderate ratings](https://github.com/GurraNasan/dragons-nest-gaming/issues/4)
    [USER STORY: See products](https://github.com/GurraNasan/dragons-nest-gaming/issues/5)
    [USER STORY: Product details](https://github.com/GurraNasan/dragons-nest-gaming/issues/6)
    [USER STORY: Find offers](https://github.com/GurraNasan/dragons-nest-gaming/issues/7)
    [USER STORY: See new products](https://github.com/GurraNasan/dragons-nest-gaming/issues/8)
    [USER STORY: Cart total](https://github.com/GurraNasan/dragons-nest-gaming/issues/9)
    [USER STORY: Search product](https://github.com/GurraNasan/dragons-nest-gaming/issues/10)
    [USER STORY: Shopping cart](https://github.com/GurraNasan/dragons-nest-gaming/issues/11)
    [USER STORY: See event calendar](https://github.com/GurraNasan/dragons-nest-gaming/issues/12)
    [USER STORY: Register user](https://github.com/GurraNasan/dragons-nest-gaming/issues/13)
    [USER STORY: Recover password](https://github.com/GurraNasan/dragons-nest-gaming/issues/14)
    [USER STORY: View user profile](https://github.com/GurraNasan/dragons-nest-gaming/issues/15)
    [USER STORY: Log in/out](https://github.com/GurraNasan/dragons-nest-gaming/issues/16)
    [USER STORY: Rate product](https://github.com/GurraNasan/dragons-nest-gaming/issues/17)
    [USER STORY: Sign up newsletter](https://github.com/GurraNasan/dragons-nest-gaming/issues/18)
    [USER STORY: View cart](https://github.com/GurraNasan/dragons-nest-gaming/issues/19)
    [USER STORY: Cart quantity](https://github.com/GurraNasan/dragons-nest-gaming/issues/20)
    [USER STORY: Payment information](https://github.com/GurraNasan/dragons-nest-gaming/issues/21)
    [USER STORY: Order confirmation](https://github.com/GurraNasan/dragons-nest-gaming/issues/21)
    [USER STORY: Confirmation email](https://github.com/GurraNasan/dragons-nest-gaming/issues/21)
    [USER STORY: One product in many categories](https://github.com/GurraNasan/dragons-nest-gaming/issues/21)
    
#### Future Features

I got two user storie left, that I did not have time to implant. The most importent one is that one product can be seen in many categories, this will help them be more exposed on the site. 
One other big feature is to add a wishlist for the Users. 
I want to expand the calander function to be a better layout and have abit better style.


### Margeting

#### E-Commerce Application

Dragons Nest Gaming is a small business and with a E-commerce Application it can expand to reach more customers. The store is selling directly to consumers and the site is designed to sell quickly. Thats why lots of the functions is focused on the user experience.

#### Marketing Strategy 
Dragons nest gaming is not that big yet and the marketing budget is limited. But there is some ways to reach out to customers and driv traffic to the site and the store. One is with Facebook, the store is activ with new content everyday and tell the customers what is happening. And then we have had some collaborations with local brands like LERVIG a beer company.

#### XML Sitemap
Additionally to help the search engines crawl the website, I've added an XML sitemap file to the main root directory. The file was created using the free service through XML-Sitemaps.com. A sitemap is a way of organizing a website, identifying the URLs and the data under each section. Previously, the sitemaps were primarily geared for the users of the website. However, Google's XML format was designed for the search engines, allowing them to find the data faster and more efficiently.

A robots.txt file has also be included in the build to tell the search engine crawlers which URLs the crawler can access on this site. This is used mainly to avoid overloading the site with requests.

![Facebook](readme/img/facebook.jpg)
Take a look a the [page](https://www.facebook.com/DragonsNestGaming/)

#### Search Engine Optimization

SEO research is the key to get traffic to the site. 

![SEO](readme/img/SEO.jpg) 

I set up a couple of categories and find word to them and the researched the word to meet the compitions for everyone. 
The words i came up with was: "magic the gathering, board game, pokemon, Norway, gamesworkshop, game webstore wpn-store.
To improve the search engine ranking I ensured the site carries meta tags for a description and keywords which encapsulate the general content.


### Page Features 
   #### Nav Bar
   ![Nav_Bar](readme/img/nav_menu_big.jpg)
   ![Nav_Bar](readme/img/small_nav_bar.jpg)
   Here you can see the logo and name of the sore, find a search bar, the diffrent product categories, my account and the cart. You can see the value of the cart if you have something in it. 
   
   #### Index
   
   ![Index](readme/img/home.jpg)
   
   There is not alot of content here, but there is SEO Keywords in the text and a button to start shopping.
   
   #### Shop
   ##### Products
   
   ![products](readme/img/all_product.jpg)
   
   Here we can see all the products with price, rating, instock symbol, new/deal tag and name. You can filter after price or name. And    see how many products there is.  
   
   ![product_info](readme/img/product_info.jpg)
   
   On this page you get the description for the product, name, price, rating and reviews if there is one. You can put the product in your cart or go back to the store. If you are admin you get buttons for delete or Edit the product. 
   
   ##### Cart
   ![carts](readme/img/cart.jpg)
   
   Here you can see what you have in you cart and see the total and delivery cost. From here you can go to the checkout.
   If you want you can change the quantity or remove products from the cart.
   
   ##### Checkout
   
   ![checkout](readme/img/checkout.jpg)
   
   On the check out page you can fill in you shipping address and card credentiel. You can save you info if you are logged in. 
   
   ##### Confirmation 
   
   ![confirmations](readme/img/confirmations.jpg)
   
   Here you can see your order information and the total value. You get a pop up that says it it successfull too.
   
   #### Event
   
   ##### Calendar 
   
   ![calendar](readme/img/calendar.jpg)
    Here you can see a calendar and events on the diffrent days, You can press the events to get more details. As a admin you can add events. 
    
   ##### Event detail
   ![event](readme/img/event.jpg)
   Here you can see more details and a picture for the event
   
   #### Profile
   ##### My profile
   
   ![profile](readme/img/profile.jpg)
   
   On this page you can see you order history, billing information and you can go to your reviews.
   
   ##### Review  
   
   ![rating](readme/img/rating.jpg)
   
   As a site uesr you can rate and give reviewvs to products. 
   
   #### Admin
   ##### Add products
+ [Technologies](#Technologies)
   + [Programming Languages](#programming-languages)
   + [Support Programs & libraries](#support-programs-libraries)

+ [Testing](#Testing)
    + [Bugs](#bugs)
    + [ManuelTesting](#manuel-testing)
    + [NavigationHeader](#navigation-header)
    + [PageManualTesting](#home-page-maual-testing)
    + [Index page](#testing-index-page)
    + [SignInManualTesting](#sign-in-manual-testing)
    + [Shop](#teseting-forum)  
        + [Products](#category-page-testing)
        + [Cart](#cart-testing)
        + [Checkout](#checkout-testing)
        + [Confirmation](#confirmation-testing) 
    + [Calender](#teseting-forum)  
        + [Calender](#calender-testing)
        + [add/edit event](#add/edit-testingt)
    + [Profile](#profile-testing)  
        + [profile info](#profile-info-testing)
        + [add/edit rating](#add/edit-rating)             
    + [Validation](#Validation)
        + [HTML](#html)
        + [CSS](#css)
        + [Python](#python)
        + [Javascrip](#javascript)
        + [Lighthouse](#lighthouse)
   
+ [Deployment](#deployment)
   + [Github](#github)
   + [Gitpod and Django](#gitpod-and-django)
   + [Heroku](#heroku)   
   
+ [Acknowledgments](#acknowledgments)
    + [Credits](#credits)
    + [Copied Code](#copied-code)
