# Wow_Project

**Project synopsis**

One of the most difficult things for any investors whether they are novices or professionals is knowing when to buy or sell a particular security. Herein lies our solution to this 200 year conundrum that has persisted since the founding of the New York Stock Exchange in 1792. Today, we have created a user friendly tool that will inform an investor when to buy or sell a particular crypto currency in plain English - later version will include a google translater which will make our tool literally available to anyone around the world.

All a user will have to create is a Binance.us api_key and api_secret by opening an account through binance.us which takes about 5 minutes. For further guidance on how to create a binance account watch this short video: https://www.youtube.com/watch?v=hYSdULDAmbc. Once a binance account is created a person will need to create an API KEY and Secret, which takes less than 5 minutes. Watch a 2 minute video on how to create API Key: https://www.youtube.com/watch?v=FPUHU7THD64

Once a user has a API Key and Secret they can go to our site to access our tools. 

**Libraries that needs to be installed**

1. Binance
2. Flask
3. Boot strap

**Below are the following steps to run/use our website:** 

1. Download our repository

2. Clone it to a folder on your computer

3. Use your chosen IDE to open the folder

4. Open your terminal, make sure you are in the correct folder and install the following libraries: Binance, Flask, Boot strap

5. Once the proper libraries are installed, and you are in the proper folder, on your terminal type in: flask run

6. When this happens, a link should appear that looks like this: http://127.0.0.1:5000/ 

7. Copy and paste that link into your preferred browser

8. Once that is completed a white page will be rendered that says: This Exchange is By Invitation Only, below which you are asked to enter in your API_key and API_Secret

9. If you enter a non-valid key and secret or attempt to press login without giving proper credentials, you will not be allowed to move pass the login page

10. If you entered in valid key and secret you will be redirected to the home page where you will be greeted with your current available to trade balance, your current crypto holdings, technical indicators at work, and a area where you can execute buy and sell orders through binance.us.

11. One of the key feature of our website is that it will stream live data from Binance that are processed through technical indicators that will let an investor know when to buy or sell a particular crypto currency based on a particular time frame a user selects

12. The technical indicators will allow investors the ability to select timeframes they want analyzed which makes it a more useful tool to a broader audience of investors. For example, day traders maybe more interested in the minute or hourly fluctuation of a particular security, while a swing trader are more concerned with the daily or weekly fluctuations.
 
13. Our technical ossicilator will allow users to select duration analysis by the minute up to a month. 







