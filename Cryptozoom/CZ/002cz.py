#!/usr/bin/env python3

import json, gspread, pprint, os, smtplib, hmac, hashlib, time, urllib.request, urllib.error, urllib.parse, cexio, sys, tabulate
import time, websocket, requests
from tabulate import tabulate
from cexio import *
from auth_key import *
from twilio_creds import *
from twilio.rest import Client
from requests import Session, Request
from oauth2client.service_account import ServiceAccountCredentials
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

##-----------------------------------------This will be the start of the main menu--------------------------------------------##
#--Link: https://www.teachyourselfpython.com/challenges.php?a=04_Mini_Projects_NEA_Samples_Tutorials&t=01_Form_Tutor_System_NEA_OCR_Task1&s=02_MainMenu_Define_Functions

'''
#Set environment variables
username = os.environ['USER']
api_key = os.environ['KEY']
api_secret = os.environ['SECRET']
'''

#Get Keys
username = username 
api_key = api_key
api_secret = api_secret


#-------Color Coding Variables------#
O = '\033[33m'
G = '\033[32m'
W = '\033[0m'
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   O = '\033[33m'
   G = '\033[32m'
   W = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


'''
##############################################################################################################
## Send Email ## https://www.youtube.com/watch?v=B1IsCbXp0uE&t=31s 
def email_alert():

	guser = "clockwork360.dv@gmail.com"
	gpass = "ibeenextfndyonvu"

#----------Taken from https://stackabuse.com/how-to-send-emails-with-gmail-using-python/ ------------
	sent_from = guser
	to = ['clockwork360.dv@gmail.com']
#	to = ['3177341051@tmomail.net']
	subject = 'Got dat shorty doo wop'
	body = 'Fuks wit cha boi'

	email_text = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (sent_from, ", " .join(to), subject, body)

#----------------------------------------------------------------------------------------------------

	server = smtplib.SMTP('smtp.gmail.com', 587)
	#server.helo()
	server.starttls()
	server.login(guser, gpass)
	server.sendmail(sent_from, to, email_text)

	server.close()

	print ('Email Sent')
#	print ('SMS Sent')
##############################################################################################################
'''

##############################################################################################################
## CEX API ##   https://github.com/matveyco/cex.io-api-python
myapi = cexio.Api(username, api_key, api_secret)

'''
# Print open orders
o_orders = myapi.open_orders('BTC/USD')
print ("OPEN ORDERS:")
print ("---------------")
pprint.pprint(o_orders)
print ("\n")

btcbal = myapi.balance["BTC"]
print ("BTC BALANCE")
print ("--------------")
pprint.pprint(btcbal)
print ("\n")

xrpbal = myapi.balance["XRP"]     
print ("XRP BALANCE")
print ("--------------")
pprint.pprint(xrpbal)
print ("\n")

xlmbal = myapi.balance["XLM"]     
print ("XLM BALANCE")
print ("--------------")
pprint.pprint(xlmbal)
print ("\n")

print ("-----------------------------------------------------------------")
print ("\n")


print ("\n")
ob = myapi.order_book()
print ("ORDER BOOK")
print ("---------------")
pprint.pprint(ob)
print ("\n")
print ("\n")


trhis = myapi.trade_history()
print ("TRADE HISTORY")
print ("-------------")
pprint.pprint(trhis)
print ("\n")


print ("\n")
op = myapi.open_positions("BTC/USD")
print ("OPEN POSITIONS")
print ("---------------")
pprint.pprint(op)
print ("\n")



print ("\n")
arch_orders = myapi.archived_orders('BTC/USD', )
print ("ARCHIVED ORDERS")
print ("---------------")
pprint.pprint(arch_orders)
print ("\n")
'''
'''
order_id = 22035453211 
gorder = myapi.get_order(order_id)
print ("GET ORDER")
print ("---------------")
pprint.pprint(gorder)
print ("\n")
'''
##--------------------------------------------------------------- Ticker Symbols ---------------------------------------------------------------------##
#----------BTC/USD-----------#
btc_usd659 = "Ticker (BTC/USD)"
last_price = (myapi.ticker()['last'])
#----------ETH/USD-----------#
etc_usd103 = "Ticker (ETH/USD)"
et1 = (myapi.ticker("ETH/USD")['last'])
#----------XLM/USD-----------#
xlm_usd315 = "Ticker (XLM/USD)"
xl1 = (myapi.ticker("XLM/USD")['last'])
#----------DASH/USD-----------#
dash_usd886 = "Ticker (DASH/USD)"
da1 = (myapi.ticker("DASH/USD")['last'])
#----------XRP/USD-----------#
xrp_usd237 = "Ticker (XRP/USD)"
xr1 = (myapi.ticker("XRP/USD")['last'])
#----------BAT/USD-----------#
bat_usd105 = "Ticker (BAT/USD)"
bat = (myapi.ticker("BAT/USD")['last'])
#----------LTC/USD-----------#
ltc_usd105 = "Ticker (LTC/USD)"
lt1 = (myapi.ticker("LTC/USD")['last'])
#----------BCH/USD-----------#
bch_usd105 = "Ticker (BCH/USD)"
bc1 = (myapi.ticker("BCH/USD")['last'])

#print ("CEX:" + " "+ G + btc_usd659, O + last_price, G + etc_usd103, O + et1, G + xlm_usd315, O + xl1, G + dash_usd886, O + da1, G + xrp_usd237, O + xr1, G + ltc_usd105, O + lt1)

##########################################################################################################>
### Start of the Google Sheets Api Script  | Documentation https://gspread.readthedocs.io/en/latest/
## https://www.techwithtim.net/tutorials/google-sheets-python-api-tutorial/  |  https://www.youtube.com/watch?v=cnPlKLEGR7E
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("/home/kali/Desktop/Projects/everything_python/Cryptozoom/creds.json", scope)
client = gspread.authorize(creds)

#------------------------------------------------------------------ Google Sheets API Primer --------------------------------------------------------------------------------------------#
                                                          # How to use the sheets api will be placed here
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                    ## Get a specific row, column, and the value of a specific cell examples
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#row23 = sheet.row_values(23)
#colA = sheet.col_values(1)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                             ## Insert the row and  the list as a row at index 4 Example:
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#--insertRow = ["hello", 5, "red", "blue"]
#--sheet.insert_row(insertRow, 4)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                                                    ## Update one cell
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#--var = sheet.cell(1,1).value



########################################################################################################################################################################

#-------------------------------------------------------- Open the Spreadsheet and grab all the Data  --------------------------------------------------------#
## Open the spreadsheet
sheet = client.open("CryptoZoom").sheet1
## Get a list of all the records
#---------------------------------------#
data = sheet.get_all_records()

##------------------------------------------------------------- BTC_USD SECTION Live Crypto Percent Changes ------------------------------------------------------##

### BTC/USD Function Calls to My Purchased Crypto Live Percent Changes ###
#buyin = float(sheet.cell(24,5).value)
'''
buyin = 39727.3
data24 = 0
print ("\n")
print ("Current Bitcoin Price: " + last_price)
print ("\n")
while buyin > data24:
    print ("Checking status of BTC Investment...")
    def btc_usd1():
#        _bi = sheet.cell(24,5).value
        _bi = 39727.3
        _lp = last_price
        tpercent = 0.50
        droppercent = 0.02
        ttpercent = 0.02
        eresult = ((float(_lp) - float(_bi))/abs(float(_bi)))
#        btcusd1_sheet = sheet.update_cell(24,8, "{:.0%}".format(eresult))
        #Get Current Price
#        btcusd1_cp = sheet.update_cell(24,9, _lp)
        if eresult >= tpercent:
            print ("Current Price is greater than target percent...")
        ## Twilio ## Also update credentials to environment variable : https://www.twilio.com/docs/usage/secure-credentials
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone
            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="BTC/USD_1 Has reached it's target Limit!")
            print ("BTC USD has reached limit, sending SMS...")
        elif eresult <= droppercent:
            print ("Current Price is less than target percent...")
            ## Sell Limit Order Call
            amount = .0004
            price = last_price
            market = 'BTC/USD'
            sell = myapi.sell_limit_order(amount,price,market)
            ## Twilio ## Order Executed Update
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone
            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="BTC/USD_1 Sell Order Executed!")
            print ("Executing Stop Loss, Sending SMS")
            #only using this break here but should be placed at the bottom of complete code on last if statement

        else:
            pass
    time.sleep(5)
    btc_usd1()

else:
    pass
'''

'''
### BTC_USD2 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(25,5).value)
data25 = 0
if buyin > data25:
    def btc_usd2():
        _btcusd2bi = sheet.cell(25,5).value
        _btcusd2lp = last_price 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_btcusd2lp) - float(_btcusd2bi))/abs(float(_btcusd2bi)))
        btcusd2_sheet = sheet.update_cell(25,8, "{:.0%}".format(eresult))
        #Get Current Price
        btcusd2_cp = sheet.update_cell(25,9, _btcusd2lp)
        result2 = ((float(_btcusd2lp) - float(_btcusd2bi))/abs(float(_btcusd2bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="BTC_USD2 Has reached it's target Limit!")
        else:
            return
            pass
    btc_usd2()

else:
    pass


### BTC_USD3 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(26,5).value)
data26 = 0
if buyin > data26:
    def btc_usd3():
        _btcusd3bi = sheet.cell(26,5).value
        _btcusd3lp = last_price 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_btcusd3lp) - float(_btcusd3bi))/abs(float(_btcusd3bi)))
        btcusd3_sheet = sheet.update_cell(26,8, "{:.0%}".format(eresult))
        #Get Current Price
        btcusd3_cp = sheet.update_cell(26,9, _btcusd3lp)
        result2 = ((float(_btcusd3lp) - float(_btcusd3bi))/abs(float(_btcusd3bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="BTC_USD2 Has reached it's target Limit!")
        else:
            return
            pass
    btc_usd3()

else:
    pass

##------------------------------------------------------------------- ETH_USD SECTION Live Crypto Percent Changes ----------------------------------------------------------------------##
### ETH_USD1 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(28,5).value)
data28 = 0
if buyin > data28:
    def eth_usd1():
        _ethusd1bi = sheet.cell(28,5).value
        _ethusd1lp = et1 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_ethusd1lp) - float(_ethusd1bi))/abs(float(_ethusd1bi)))
        ethusd1_sheet = sheet.update_cell(28,8, "{:.0%}".format(eresult))
        #Get Current Price
        ethusd1_cp = sheet.update_cell(28,9, _ethusd1lp)
        result2 = ((float(_ethusd1lp) - float(_ethusd1bi))/abs(float(_ethusd1bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="ETH_USD1 Has reached it's target Limit!")
        else:
            return
            pass
    eth_usd1()

else:
    pass

### ETH_USD2 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(29,5).value)
data29 = 0
if buyin > data29:
    def eth_usd2():
        _ethusd2bi = sheet.cell(29,5).value
        _ethusd2lp = et1 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_ethusd2lp) - float(_ethusd2bi))/abs(float(_ethusd2bi)))
        ethusd2_sheet = sheet.update_cell(29,8, "{:.0%}".format(eresult))
        #Get Current Price
        ethusd2_cp = sheet.update_cell(29,9, _ethusd2lp)
        result2 = ((float(_ethusd2lp) - float(_ethusd2bi))/abs(float(_ethusd2bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="ETH_USD2 Has reached it's target Limit!")
        else:
            return
            pass
    eth_usd2()

else:
    pass


### ETH_USD3 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(30,5).value)
data30 = 0
if buyin > data30:
    def eth_usd3():
        _ethusd3bi = sheet.cell(30,5).value
        _ethusd3lp = et1
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_ethusd3lp) - float(_ethusd3bi))/abs(float(_ethusd3bi)))
        ethusd3_sheet = sheet.update_cell(30,8, "{:.0%}".format(eresult))
        #Get Current Price
        ethusd3_cp = sheet.update_cell(30,9, _ethusd3lp)
        result2 = ((float(_ethusd3lp) - float(_ethusd3bi))/abs(float(_ethusd3bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="ETH_USD3 Has reached it's target Limit!")
        else:
            return
            pass
    eth_usd3()

else:
    pass

##------------------------------------------------------------------- XLM_USD SECTION Live Crypto Percent Changes ----------------------------------------------------------------------##

### XLM_USD1 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(32,5).value)
data32 = 0
if buyin > data32:
    def xlm_usd1():
        _xlmusd1bi = sheet.cell(32,5).value
        _xlmusd1lp = xl1 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_xlmusd1lp) - float(_xlmusd1bi))/abs(float(_xlmusd1bi)))
        xlmusd1_sheet = sheet.update_cell(32,8, "{:.0%}".format(eresult))
        #Get Current Price
        xlmusd1_cp = sheet.update_cell(32,9, _xlmusd1lp)
        result2 = ((float(_xlmusd1lp) - float(_xlmusd1bi))/abs(float(_xlmusd1bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="XLM_USD1 Has reached it's target Limit!")
        else:
            return
            pass
    xlm_usd1()

else:
    pass

### XLM_USD2 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(33,5).value)
data33 = 0
if buyin > data33:
    def xlm_usd2():
        _xlmusd2bi = sheet.cell(33,5).value
        _xlmusd2lp = xl1 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_xlmusd2lp) - float(_xlmusd2bi))/abs(float(_xlmusd2bi)))
        xlmusd2_sheet = sheet.update_cell(33,8, "{:.0%}".format(eresult))
        #Get Current Price
        xlmusd2_cp = sheet.update_cell(33,9, _xlmusd2lp)
        result2 = ((float(_xlmusd2lp) - float(_xlmusd2bi))/abs(float(_xlmusd2bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="XLM_USD2 Has reached it's target Limit!")
        else:
            return
            pass
    xlm_usd2()

else:
    pass

### XLM_USD3 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(34,5).value)
data34 = 0
if buyin > data34:
    def xlm_usd3():
        _xlmusd3bi = sheet.cell(34,5).value
        _xlmusd3lp = xl1 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_xlmusd3lp) - float(_xlmusd3bi))/abs(float(_xlmusd3bi)))
        xlmusd3_sheet = sheet.update_cell(34,8, "{:.0%}".format(eresult))
        #Get Current Price
        xlmusd3_cp = sheet.update_cell(34,9, _xlmusd3lp)
        result2 = ((float(_xlmusd3lp) - float(_xlmusd3bi))/abs(float(_xlmusd3bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="XLM_USD3 Has reached it's target Limit!")
        else:
            return
            pass
    xlm_usd3()

else:
    pass
##------------------------------------------------------------------ DASH_USD SECTION Live Crypto Percent Changes ----------------------------------------------------------------------##
### DASH_USD1 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(36,5).value)
data36 = 0
if buyin > data36:
    def dash_usd1():
        _dashusd1bi = sheet.cell(36,5).value
        _dashusd1lp = da1 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_dashusd1lp) - float(_dashusd1bi))/abs(float(_dashusd1bi)))
        dashusd1_sheet = sheet.update_cell(36,8, "{:.0%}".format(eresult))
        #Get Current Price
        dashusd1_cp = sheet.update_cell(36,9, _dashusd1lp)
        result2 = ((float(_dashusd1lp) - float(_dashusd1bi))/abs(float(_dashusd1bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="DASH_USD1 Has reached it's target Limit!")
        else:
            return
            pass
    dash_usd1()

else:
    pass

### DASH_USD2 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(37,5).value)
data37 = 0
if buyin > data37:
    def dash_usd2():
        _dashusd2bi = sheet.cell(37,5).value
        _dashusd2lp = da1
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_dashusd2lp) - float(_dashusd2bi))/abs(float(_dashusd2bi)))
        dashusd2_sheet = sheet.update_cell(37,8, "{:.0%}".format(eresult))
        #Get Current Price
        dashusd1_cp = sheet.update_cell(37,9, _dashusd2lp)
        result2 = ((float(_dashusd2lp) - float(_dashusd2bi))/abs(float(_dashusd2bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="DASH_USD2 Has reached it's target Limit!")
        else:
            return
            pass
    dash_usd2()

else:
    pass

### DASH_USD3 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(38,5).value)
data38 = 0
if buyin > data38:
    def dash_usd3():
        _dashusd3bi = sheet.cell(38,5).value
        _dashusd3lp = da1
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_dashusd3lp) - float(_dashusd3bi))/abs(float(_dashusd3bi)))
        dashusd3_sheet = sheet.update_cell(38,8, "{:.0%}".format(eresult))
        #Get Current Price
        dashusd3_cp = sheet.update_cell(38,9, _dashusd3lp)
        result2 = ((float(_dashusd3lp) - float(_dashusd3bi))/abs(float(_dashusd3bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="DASH_USD3 Has reached it's target Limit!")
        else:
            return
            pass
    dash_usd3()

else:
    pass

##------------------------------------------------------------------- XRP_USD SECTION Live Crypto Percent Changes ----------------------------------------------------------------------##
#/#/#/ Still need to update this section

### Function Calls to My Purchased Crypto Live Percent Changes XRP/USD Order ID:19694843237 ###
def xrp_usd1():
    _xrp1lp = xr1
    _xrp1bi = sheet.cell(40,5).value
    tpercent = 0.50
    goalpercent = 0.50
    ttpercent = 0.02
    xr1result = ((float(_xrp1lp) - float(_xrp1bi))/abs(float(_xrp1bi)))
    if xr1result >= tpercent:
        sid = account_sid
        token = auth_token
        twphone = tphone
        pnum = myphone 
        client = Client(sid, token)
        client.messages.create(to=pnum,from_=twphone,body="XRP/USD 1 Has reached it's target Limit!")
    if xr1result >= goalpercent:
         sell_limit_order(617,0.31,xrp/usd)
    else:
        return
        pass
xrp_usd1()

### XRP/USD 2 Function Calls to My Purchased Crypto Live Percent Changes ###
def xrp_usd2():
    _xrp1lp = xr1
    _xrp1bi = sheet.cell(41,5).value
    tpercent = 0.50
    ttpercent = 0.02
    xr1result = ((float(_xrp1lp) - float(_xrp1bi))/abs(float(_xrp1bi)))
    if xr1result >= tpercent:
        sid = account_sid
        token = auth_token
        twphone = tphone
        pnum = myphone 
        client = Client(sid, token)
        client.messages.create(to=pnum,from_=twphone,body="XRP/USD 2 Has reached it's target Limit!")
    else:
        return
        pass
xrp_usd2()

### XRP/USD 3 Function Calls to My Purchased Crypto Live Percent Changes ###
sheet42 = sheet.cell(42,5).value
data42 = 0
if float(sheet42) > data42:
    def xrp_usd3():
        _xrp3lp = xr1
        _xrp3bi = sheet.cell(42,5).value
        tpercent = 0.05
        ttpercent = 0.02
        xr3result = ((float(_xrp3lp) - float(_xrp3bi))/abs(float(_xrp3bi)))
        if xr3result >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 
            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="XRP/USD 3 Has reached it's target Limit!")
        else:
            return
            pass
    xrp_usd3()
else:
    pass

##------------------------------------------------------------------- BAT_USD SECTION Live Crypto Percent Changes ----------------------------------------------------------------------##

### BAT_USD1 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(44,5).value)
data44 = 0
if buyin > data44:
    def bat_usd1():
        _batusd1bi = sheet.cell(44,5).value
        _batusd1lp = bat 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_batusd1lp) - float(_batusd1bi))/abs(float(_batusd1bi)))
        batusd1_sheet = sheet.update_cell(44,8, "{:.0%}".format(eresult))
        #Get Current Price
        batusd1_cp = sheet.update_cell(44,9, _batusd1lp)
        result2 = ((float(_batusd1lp) - float(_batusd1bi))/abs(float(_batusd1bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="BAT_USD1 Has reached it's target Limit!")
        else:
            return
            pass
    bat_usd1()

else:
    pass

### BAT_USD2 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(45,5).value)
data45 = 0
if buyin > data45:
    def bat_usd2():
        _batusd2bi = sheet.cell(45,5).value
        _batusd2lp = bat 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_batusd2lp) - float(_batusd2bi))/abs(float(_batusd2bi)))
        batusd2_sheet = sheet.update_cell(45,8, "{:.0%}".format(eresult))
        #Get Current Price
        batusd2_cp = sheet.update_cell(45,9, _batusd2lp)
        result2 = ((float(_batusd2lp) - float(_batusd2bi))/abs(float(_batusd2bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="BAT_USD2 Has reached it's target Limit!")
        else:
            return
            pass
    bat_usd2()

else:
    pass

### BAT_USD3 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(46,5).value)
data46 = 0
if buyin > data46:
    def bat_usd3():
        _batusd3bi = sheet.cell(46,5).value
        _batusd3lp = bat 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_batusd3lp) - float(_batusd3bi))/abs(float(_batusd3bi)))
        batusd3_sheet = sheet.update_cell(46,8, "{:.0%}".format(eresult))
        #Get Current Price
        batusd3_cp = sheet.update_cell(46,9, _batusd3lp)
        result2 = ((float(_batusd3lp) - float(_batusd3bi))/abs(float(_batusd3bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="BAT_USD3 Has reached it's target Limit!")
        else:
            return
            pass
    bat_usd3()

else:
    pass

##------------------------------------------------------------------- BCH_USD SECTION Live Crypto Percent Changes ----------------------------------------------------------------------##

### BCH_USD1 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(48,5).value)
data48 = 0
if buyin > data48:
    def bch_usd1():
        _bchusd1bi = sheet.cell(48,5).value
        _bchusd1lp = bc1
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_bchusd1lp) - float(_bchusd1bi))/abs(float(_bchusd1bi)))
        bchusd1_sheet = sheet.update_cell(48,8, "{:.0%}".format(eresult))
        #Get Current Price
        bchusd1_cp = sheet.update_cell(48,9, _bchusd1lp)
        result2 = ((float(_bchusd1lp) - float(_bchusd1bi))/abs(float(_bchusd1bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="BCH_USD1 Has reached it's target Limit!")
        else:
            return
            pass
    bch_usd1()

else:
    pass

### BCH_USD2 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(49,5).value)
data49 = 0
if buyin > data49:
    def bch_usd2():
        _bchusd2bi = sheet.cell(49,5).value
        _bchusd2lp = bc1 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_bchusd2lp) - float(_bchusd2bi))/abs(float(_bchusd2bi)))
        bchusd2_sheet = sheet.update_cell(49,8, "{:.0%}".format(eresult))
        #Get Current Price
        bchusd1_cp = sheet.update_cell(49,9, _bchusd2lp)
        result2 = ((float(_bchusd2lp) - float(_bchusd2bi))/abs(float(_bchusd2bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="BCH_USD2 Has reached it's target Limit!")
        else:
            return
            pass
    bch_usd2()

else:
    pass

### BCH_USD3 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(50,5).value)
data50 = 0
if buyin > data50:
    def bch_usd3():
        _bchusd3bi = sheet.cell(50,5).value
        _bchusd3lp =bc1 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_bchusd3lp) - float(_bchusd3bi))/abs(float(_bchusd3bi)))
        bchusd3_sheet = sheet.update_cell(50,8, "{:.0%}".format(eresult))
        #Get Current Price
        bchusd3_cp = sheet.update_cell(50,9, _bchusd3lp)
        result2 = ((float(_bchusd3lp) - float(_bchusd3bi))/abs(float(_bchusd3bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="BCH_USD3 Has reached it's target Limit!")
        else:
            return
            pass
    bch_usd3()

else:
    pass

##------------------------------------------------------------------- LTC_USD SECTION Live Crypto Percent Changes ----------------------------------------------------------------------##

### LTC_USD1 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(52,5).value)
data52 = 0
if buyin > data52:
    def ltc_usd1():
        _ltcusd1bi = sheet.cell(52,5).value
        _ltcusd1lp = lt1 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_ltcusd1lp) - float(_ltcusd1bi))/abs(float(_ltcusd1bi)))
        ltcusd1_sheet = sheet.update_cell(52,8, "{:.0%}".format(eresult))
        #Get Current Price
        ltcusd1_cp = sheet.update_cell(52,9, _ltcusd1lp)
        result2 = ((float(_ltcusd1lp) - float(_ltcusd1bi))/abs(float(_ltcusd1bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="LTC_USD Has reached it's target Limit!")
        else:
            return
            pass
    ltc_usd1()

else:
    pass

### LTC_USD2 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(53,5).value)
data53 = 0
if buyin > data53:
    def ltc_usd2():
        _ltcusd2bi = sheet.cell(53,5).value
        _ltcusd2lp = lt1 
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_ltcusd2lp) - float(_ltcusd2bi))/abs(float(_ltcusd2bi)))
        ltcusd2_sheet = sheet.update_cell(53,8, "{:.0%}".format(eresult))
        #Get Current Price
        ltcusd2_cp = sheet.update_cell(53,9, _ltcusd2lp)
        result2 = ((float(_ltcusd2lp) - float(_ltcusd2bi))/abs(float(_ltcusd2bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="LTC_USD2 Has reached it's target Limit!")
        else:
            return
            pass
    ltc_usd2()

else:
    pass

### LTC_USD3 Function Calls to My Purchased Crypto Live Percent Changes ###
buyin = float(sheet.cell(54,5).value)
data54 = 0
if buyin > data54:
    def ltc_usd3():
        _ltcusd3bi = sheet.cell(54,5).value
        _ltcusd3lp = lt1
        tpercent = 0.50
        ttpercent = 0.02
        eresult = ((float(_ltcusd3lp) - float(_ltcusd3bi))/abs(float(_ltcusd3bi)))
        ltcusd3_sheet = sheet.update_cell(54,8, "{:.0%}".format(eresult))
        #Get Current Price
        ltcusd3_cp = sheet.update_cell(54,9, _ltcusd3lp)
        result2 = ((float(_ltcusd3lp) - float(_ltcusd3bi))/abs(float(_ltcusd3bi)))
        if result2 >= tpercent:
            sid = account_sid
            token = auth_token
            twphone = tphone
            pnum = myphone 

            client = Client(sid, token)
            client.messages.create(to=pnum,from_=twphone,body="LTC_USD3 Has reached it's target Limit!")
        else:
            return
            pass
    ltc_usd3()

else:
    pass


'''
#----------------------------- Show Actual Percent Change in Cell and Most current price in Another-------------------------------------------#

#-------------------------------XRP------------------------------------------#
'''
def xrp1_cell():
    # Get Buyin Price
    lprice = xr1
    xr1_in = sheet.cell(40,5).value
    xrp1result = ((float(lprice) - float(xr1_in))/abs(float(xr1_in)))
    # Get Percentage
    xrp1usd_sheet = sheet.update_cell(40,8, "{:.0%}".format(xrp1result))
    # Get current price and ouput to cell
    xrp1usd_cp = sheet.update_cell(40,9, lprice)
    #---------------Start price drop detection--------------------#
    pbuyin = 1 # Get negative percent by using a positive whole number
    pcent = (pbuyin * float(lprice))/100 # Calculate percent loss position
    loss = (float(lprice) - pcent)
    print ("\n")
    print ("XRP/USD Percent Loss Detection")
    print ("-------------------------")
    print ("Last Price Equals:" + lprice)
    print ("Loss Equals: " + str(loss))
    print ("-------------------------")
    # Add (DD) Drop Detection to cell
    dd = sheet.update_cell(40,10, loss)
    # Add statements
    llprice = lprice
    nodrop = float(llprice) > float(loss)


##-------------------------------------------------------------------------------------------------------------
    dropped = float(llprice) <= float(loss)
    if nodrop: 
        print ("Nothing has Dropped, trying again...")
        print ("\n")
#        dropped = float(lprice) <= float(loss)
    #    s = sched.scheduler(time.time, time.sleep)
    #    s.enter(60,1, (s,))
    #    s.run()
    #    print ("Seeing if this prints every 60 seconds.")
    elif dropped:
        sid = account_sid
        token = auth_token
        twphone = tphone
        pnum = myphone 

        client = Client(sid, token)
        client.messages.create(to=pnum,from_=twphone,body="XRP/USD Dropped! Check for buy potential!")
        print ("Should be receiving a text message.")
    else:
        print ("Something went wrong...")
xrp1_cell()


def xrp2usd_cell():
    lprice = xr1
    xr2_in = sheet.cell(41,5).value
    xrp2result = ((float(lprice) - float(xr2_in))/abs(float(xr2_in)))
    xrp2usd_sheet = sheet.update_cell(41,8, "{:.0%}".format(xrp2result))
    # Get current price
    xrp2usd_cp = sheet.update_cell(41,9, lprice)
xrp2usd_cell()


def xrp3_cell():
    lprice = xr1
    xr3_in = sheet.cell(42,5).value
    xrp3result = ((float(lprice) - float(xr3_in))/abs(float(xr3_in)))
    xrp3usd_sheet = sheet.update_cell(42,8, "{:.0%}".format(xrp3result))
    # Get current price
    xrp3usd_cp = sheet.update_cell(42,9, lprice)
xrp3_cell()
'''
#---------------------------------------#
## Dewayne's CEX Crypto Exchange Chart ##
'''
O = '\033[33m'
G = '\033[32m'
W = '\033[0m'
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   O = '\033[33m'
   G = '\033[32m'
   W = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

'''


##-------------------------------------------##




##--------------------------------------------------------------- CEX CRYPTO EXCHANGE CHART ------------------------------------------------------------------##
## This part is designed to be the console version of the google sheets CEX Crypto Exchange Chart. 
#1 User defined function to write buyin values.
#2. Table that defines chart     ##https://www.geeksforgeeks.org/texttable-module-in-python/         <--- use this site for table reference

btc_chart = True
if btc_chart == True:
    print ('_________________________')
    print ('CEX Crypto Exchange Chart')
    print ('-------------------------')
    question = input("Was Bitcoin Purchased[1] Sold[2] or Neither[3] ")
    if question == 1: # Bitcoin was Purchased
        order_id = int(input("Please Enter The Order ID: ")[:11])
        gorder = myapi.get_order(order_id)['id']
        gorder2 = myapi.get_order(order_id)
        #Get information for gorder3 (the get order function from cexio api) ~
        if int(order_id) == int(gorder):
            gorder3 = gorder2
        else:
            print ("This Order ID does not exist! Try Again: ")
        # Check OrderID in BTC Block 1 Chart to see if it is empty ~
        order_id1 = 0 
        btc_block1 = ["BTC/USD 1", 2021131, order_id1, .021, buyprice1, 2.07, 207.27, pchange1, lastp, paction1, buyprice1, fgain1]
        if order_id1 == gorder3["id"]:
            print ("Order ID Already Exists! Exiting To Menu.") 
            ##########Function to take user back to the main menu goes here::::::
        elif order_id1 > 0 and != gorder3["id"]:
            # Can't use this slot
            print ("BTC slot 1 occupied... Checking slot 2.")
            pass
        elif order_id1 == 0:
            btc_block1[2] = gorder3["id"]
            cextable_b1 = [btc_block1]
            print (tabulate(cextable_b1))
        else:
            print ("Somethings going on with btc_block1")

        # Check OrderID in BTC Block 2 Chart to see if it is empty 
        order_id2 = 0 
        btc_block2 = ["BTC/USD 2", 2021131, order_id2, .021, buyprice2, 2.07, 207.27, pchange2, lastp, paction2, buyprice2, fgain2]
        if order_id2 == gorder3["id"]:
            print ("Order ID Already Exists! Exiting To Menu.") 
            ##########Function to take user back to the main menu goes here::::::
        elif order_id2 > 0 and != gorder3["id"]:
            # Can't use this slot
            print ("BTC slot 2 occupied... Checking slot 2.")
            pass
        elif order_id2 == 0:
            btc_block2[2] = gorder3["id"]
            cextable_b2 = [btc_block2]
            print (tabulate(cextable_b2))
        else:
            print ("Somethings going on with btc_block1")

        # Check OrderID in BTC Block 3 Chart to see if it is empty ~
        order_id3 = 0 
        btc_block3 = ["BTC/USD 3", 2021131, order_id3, .021, buyprice3, 2.07, 207.27, pchange3, lastp, paction3, buyprice3, fgain3]
        if order_id3 == gorder3["id"]:
            print ("Order ID Already Exists! Exiting To Menu.") 
            ##########Function to take user back to the main menu goes here::::::
        elif order_id3 > 0 and != gorder3["id"]:
            # Can't use this slot
            print ("Buyprice slot 3 occupied... All slots are full, wait until there is a free space.")
            ##########Function to take user back to the main menu goes here::::::
            pass
        elif order_id3 == 0:
            btc_block3[2] = gorder3["id"]
            cextable_b3 = [btc_block3]
            print (tabulate(cextable_b3))
        else:
            print ("Somethings going on with btc_block1")
'''
data = True
buyprice1 = 39727.3
buyprice2 = 34770.7
buyprice3 = 40078.1


while data != False:
    header = ["USD PAIRS", "DATE", "ORDER ID", "AMOUNT", "BUYIN", "FEE", "TOTAL", "%CHANGE", "CURRENT PRICE", "PRICE ACTION", "BUYIn PRICE", "FLASH GAIN"]
    lastp = float(myapi.ticker()['last'])
    if buyprice1 != 0:
        paction1 = "Market Up"
        change1 = ((float(lastp) - float(buyprice1))/abs(float(buyprice1)))
        pchange1 = "{:.0%}".format(change1)
        fgain1 = float(buyprice1 * 0.02)+float(buyprice1)
        btc_block1 = ["BTC/USD 1", 2021131, 27008976, .021, buyprice1, 2.07, 207.27, pchange1, lastp, paction1, buyprice1, fgain1]
    else:
        pass
    if buyprice2 != 0:
        paction2 = "Market Sideways"
        change2 = ((float(lastp) - float(buyprice2))/abs(float(buyprice2)))
        pchange2 = "{:.0%}".format(change2)
        fgain2 = float(buyprice2 * 0.02)+float(buyprice2)
        btc_block2 = ["BTC/USD 2", 2021151, 29008418, .024, buyprice2, 3.21, 207.27, pchange2, lastp, paction2, buyprice2, fgain2]
    else:
        pass
    if buyprice3 != 0:
        paction3 = "Market Down"
        change3 = ((float(lastp) - float(buyprice3))/abs(float(buyprice3)))
        pchange3 = "{:.0%}".format(change3)
        fgain3 = float(buyprice3 * 0.02)+float(buyprice3)
        btc_block3 = ["BTC/USD 3", 2021151, 29008418, .024, buyprice3, 3.21, 207.27, pchange3, lastp, paction3, buyprice3, fgain3]
    else:
        pass
    cextable = [header, btc_block1, btc_block2, btc_block3]
    print (tabulate(cextable, headers="firstrow"))
    print ("\n")
    time.sleep(30)
else:
    pass
'''



#print  ("USD PAIRS | DATE | ORDER ID | AMOUNT | BUYIN | FEE | TOTAL | % CHANGE | CURRENT PRICE | PRICE ACTION | BUYIn PRICE | PAIR PERCENT |")



'''
##------------------------------ Order History Section ----------------------------------------------------##
## Links: How to change cell color in google sheets: https://www.maketecheasier.com/change-cell-color-google-sheet/
print ('ORDER HISTORY')
print (color.UNDERLINE + 'USD PAIRS |    DATE    |  ORDER ID   |  AMOUNT  |  BUYIN PRICE  |  FEE  |  TOTAL  | % CHANGE' + color.END)
print (color.UNDERLINE + 'BTC/USD  | 12/21/2020 | 20841191289 |  0.0221  |   23121.9     |  1.28 |  512.27 |   1%' + color.END)
#---------------------------------------#

## Get the number of rows in the sheet
#--numRows = sheet.row_count
#################################################################################################################

## Calling Email Function ##
#--email_alert()
'''
