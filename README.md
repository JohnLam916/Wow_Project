# Wow_Project

**Project synopsis**

One of the most difficult things for any investors whether they are novices or professionals is knowing when to buy or sell a particular security. Herein lies our solution to this 200 year conundrum that has persisted since the founding of the New York Stock Exchange in 1792. Today, we have created a user friendly tool that will inform an investor when to buy or sell a particular crypto currency in plain English - later version will include a google translater which will make our tool literally available to anyone around the world.

The mission of democratizing investment is the heart of our project which is why we have decided to focus on crypto currency. Crypto currency has a few benefits that lends itself well for later project scalability, but importantly it has a low bar for frequent trading or what is known as "daily trading". With traditional stocks on the New York Stock Exchange or the Nasdaq, you would need to meet the minium of having $25,000 in your trading account before you are allowed to become a day trader, one who buys and sells more than three securities in a day. If you were to attempt to be a day trader with less than $25,000, you would be locked out of your account for up to 3 months. However, with crypto currency you can trade as frequently as you like, with as much or little money as you want. As an added bonus you can do it 24/7 unlike stocks which opens 9am EST and closes 4pm EST and operates Monday - Friday, Crypto exchanges also don't reccognize holidays, so you can make green gravy even on thanksgiving. 

For all the above reasons, we chose to focus on crypto currencies over stocks. Along that line, we selected Binance.us as a platform because the site has the highest volume of trades for crypto currency. This is key as we will want to scale this project to automation later, and higher the volume activity allows quicker execution of trades. As the adage goes, "without a buyer, you can't sell Jack" - a wise person said this, I think his name was John.

Furthermore, All a user will have do to utilize our site is to create a Binance.us api_key and api_secret by opening an account through binance.us which takes about 5 minutes. For further guidance on how to create a binance account watch this short video: https://www.youtube.com/watch?v=hYSdULDAmbc. Once a binance account is created, a person will need to create an API KEY and Secret, which takes less than 5 minutes. Watch a 2 minute video on how to create API Key: https://www.youtube.com/watch?v=FPUHU7THD64

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

**Next Upgrades**

1. Automate the mechanical trading to a fully self functioning bot that takes user parameters on how to trade and "is user friendly"
2. Along with the bot, we will make a fully functional webpage that will provide investors with resources on best practices on how to use the bot.
3. Allow users to back trade on historical data to test out how the bot will perform with settings to help investors fine tune their investment strategy
4. A key tool we will implement in the next phase of the development will include a technical indicator called the Relative Strength Index which will accept user input to adjust the RSI feedback to the bot on how to trade. A more risk prone investor can make a few simple adjustments that will make the bot trade more aggressively, while a more conservative investor can make a few simple adjustments and make the bot trade more conservatively.







