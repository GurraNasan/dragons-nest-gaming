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
    
      + [Data modal](#data-modal)
      + [Future Features](#future-features)
+ [Margeting](#margeting)
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
