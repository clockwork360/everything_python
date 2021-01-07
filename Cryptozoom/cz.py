#!/usr/bin/env python3

import json, gspread, pprint, os, smtplib, hmac, hashlib, time, urllib.request, urllib.error, urllib.parse, cexio
import time, websocket, requests, sched
from twilio_creds import *
from twilio.rest import Client
from requests import Session, Request
from oauth2client.service_account import ServiceAccountCredentials
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

'''
#Set environment variables
username = os.environ['USER']
api_key = os.environ['KEY']
api_secret = os.environ['SECRET']
'''

#Get Keys
username = 'up125942624' 
api_key = 'QwHotLUGHkmShCNaYgjN52WC56Q'
api_secret = 'XLMwB6aqxy9BULyua7u6im73E48'



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


# Print open orders
o_orders = myapi.open_orders('BTC/USD')
print ("Open Orders:")
print (o_orders)
print ("\n")

#Print Buy Limit Order
#buy = myapi.buy_limit_order()

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

print ("CEX:" + " "+ G + btc_usd659, O + last_price, G + etc_usd103, O + et1, G + xlm_usd315, O + xl1, G + dash_usd886, O + da1, G + xrp_usd237, O + xr1, G + ltc_usd105, O + lt1)

##############################################################################################################

##########################################################################################################>
### Start of the Google Sheets Api Script  | Documentation https://gspread.readthedocs.io/en/latest/
## https://www.techwithtim.net/tutorials/google-sheets-python-api-tutorial/  |  https://www.youtube.com/watch?v=cnPlKLEGR7E
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("/home/kali/Desktop/Projects/everything_python/Cryptozoom/creds.json", scope)
client = gspread.authorize(creds)

#----Google Sheets API Primer----#

# How to use the sheets api will be placed here

#--------------------------------#

## Open the spreadsheet
sheet = client.open("CryptoZoom").sheet1

#---------------------------------------#
## Get a list of all the records
data = sheet.get_all_records()

#----------------------------------------------------------------#
## Get a specific row, column, and the value of a specific cell
#row23 = sheet.row_values(23)
#row24 = sheet.row_values(24)
#row25 = sheet.row_values(25)
#row26 = sheet.row_values(26)
#row27 = sheet.row_values(27)
#row28 = sheet.row_values(28)
#row29 = sheet.row_values(29)
#--colA = sheet.col_values(1)

### BTC/USD Order ID:20746142724 Function Calls to My Purchased Crypto Live Percent Changes ###
def btc_usd1():
    _bi = sheet.cell(24,5).value
    _lp = last_price
    tpercent = 0.01
    ttpercent = 0.02
    eresult = ((float(_lp) - float(_bi))/abs(float(_bi)))
    if eresult >= tpercent:
    ## Twilio ## Also update credentials to environment variable : https://www.twilio.com/docs/usage/secure-credentials
        sid = account_sid
        token = auth_token
        twphone = tphone
        pnum = myphone
        client = Client(sid, token)
        client.messages.create(to=pnum,from_=twphone,body="BTC/USD_1 Has reached it's target Limit!")
'''
    elif eresult <= ttpercent:
        bal = myapi.balance('balance')
        print ("\n")
        print ("Buy Order Setup")
        print ("-----------------")
        print (bal)
        print ("-----------------") 
        print ("\n")
    else:
        print ("Check BTC/USD Fuction on line 134")
'''
btc_usd1()



### Function Calls to My Purchased Crypto Live Percent Changes ETH/USD Order ID: 19513647103 ###
def btc_usd2():
    _ethbi = sheet.cell(25,5).value
    _ethlp = et1
    tpercent = 0.01
    ttpercent = 0.02
    result2 = ((float(_ethlp) - float(_ethbi))/abs(float(_ethbi)))
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

'''
### Function Calls to My Purchased Crypto Live Percent Changes XLM/USD Order ID: 19694465315 ###
def percentchange3():
    _xlmlp = xl1
    _xlmbi = sheet.cell(26,5).value
    num3 = 0.2
    xresult = ((float(_xlmlp) - float(_xlmbi))/abs(float(_xlmbi)))
    if xresult >= num3:
        sid = account_sid
        token = auth_token
        twphone = tphone
        pnum = myphone 

        client = Client(sid, token)
        client.messages.create(to=pnum,from_=twphone,body="XLM/USD Has reached the target Limit!")
    else:
        return
        pass
percentchange3()
'''
'''
### Function Calls to My Purchased Crypto Live Percent Changes DASH/USD Order ID: 19694671886 ###
def percentchange4():
    _dashlp = da1
    _dashbi = sheet.cell(27,5).value
    num4 = 0.03
    dresult = ((float(_dashlp) - float(_dashbi))/abs(float(_dashbi)))
    if dresult >= num4:
        sid = account_sid
        token = auth_token
        twphone = tphone
        pnum = myphone 

        client = Client(sid, token)
        client.messages.create(to=pnum,from_=twphone,body="DASH/USD Has reached the target Limit!")
    else:
        return
        pass
percentchange4()
'''

### Function Calls to My Purchased Crypto Live Percent Changes XRP/USD Order ID:19694843237 ###
def xrp_usd1():
    _xrp1lp = xr1
    _xrp1bi = sheet.cell(40,5).value
    tpercent = 0.50
    ttpercent = 0.02
    xr1result = ((float(_xrp1lp) - float(_xrp1bi))/abs(float(_xrp1bi)))
    if xr1result >= tpercent:
        sid = account_sid
        token = auth_token
        twphone = tphone
        pnum = myphone 
        client = Client(sid, token)
        client.messages.create(to=pnum,from_=twphone,body="XRP/USD Has reached the target Limit!")
    else:
        return
        pass
xrp_usd1()


#----------------------------------------------------#
## Insert the row and  the list as a row at index 4
#--insertRow = ["hello", 5, "red", "blue"]
#--sheet.insert_row(insertRow, 4)

#-----------------------------------#
## Update one cell

def btc_cell():
    lprice = last_price
    b_in = sheet.cell(24,5).value
    result = ((float(lprice) - float(b_in))/abs(float(b_in)))
    btcusd_sheet = sheet.update_cell(24,8, "{:.0%}".format(result))
   # Get current price
    btcusd_cp = sheet.update_cell(24,9, lprice)
btc_cell()


def btc2_cell():
    lprice = last_price
    b2_in = sheet.cell(25,5).value
    eresult = ((float(lprice) - float(b2_in))/abs(float(b2_in)))
    btc2usd_sheet = sheet.update_cell(25,8, "{:.0%}".format(eresult))
    # Get current price
    btc2usd_cp = sheet.update_cell(25,9, lprice)
btc2_cell()

'''
def xlm_cell():
    lprice = xl1
    x_in = sheet.cell(26,5).value
    xlresult = ((float(lprice) - float(x_in))/abs(float(x_in)))
    xlmusd_sheet = sheet.update_cell(26,8, "{:.0%}".format(xlresult))
    # Get current price
    xlmusd_cp = sheet.update_cell(26,9, lprice)
xlm_cell()
'''
'''
def dash_cell():
    lprice = da1
    d_in = sheet.cell(27,5).value
    dashresult = ((float(lprice) - float(d_in))/abs(float(d_in)))
    dashusd_sheet = sheet.update_cell(27,8, "{:.0%}".format(dashresult))
    # Get current price
    dashusd_cp = sheet.update_cell(27,9, lprice)
dash_cell()
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

'''
def xrp2_cell():
    lprice = xr1
    xr2_in = sheet.cell(29,5).value
    xrp2result = ((float(lprice) - float(xr2_in))/abs(float(xr2_in)))
    xrp2usd_sheet = sheet.update_cell(29,8, "{:.0%}".format(xrp2result))
    # Get current price
    xrp2usd_cp = sheet.update_cell(29,9, lprice)
xrp2_cell()
'''
'''
def xrp3_cell():
    lprice = xr1
    xr3_in = sheet.cell(34,5).value
    xrp3result = ((float(lprice) - float(xr3_in))/abs(float(xr3_in)))
    xrp3usd_sheet = sheet.update_cell(34,8, "{:.0%}".format(xrp3result))
    # Get current price
    xrp3usd_cp = sheet.update_cell(34,9, lprice)
xrp3_cell()
'''
'''
def xrp4_cell():
    lprice = xr1
    xr4_in = sheet.cell(35,5).value
    xrp4result = ((float(lprice) - float(xr4_in))/abs(float(xr4_in)))
    xrp4usd_sheet = sheet.update_cell(35,8, "{:.0%}".format(xrp4result))
    # Get current price
    xrp4usd_cp = sheet.update_cell(35,9, lprice)
xrp4_cell()
'''
'''
def bat_cell():
    lprice = bat
    b_in = sheet.cell(30,5).value
    result = ((float(lprice) - float(b_in))/abs(float(b_in)))
    batusd_sheet = sheet.update_cell(30,8, "{:.0%}".format(result))
   # Get current price
    batusd_cp = sheet.update_cell(30,9, lprice)
bat_cell()
'''
'''
def bat2_cell():
    lprice = bat
    b2_in = sheet.cell(31,5).value
    result = ((float(lprice) - float(b2_in))/abs(float(b2_in)))
    bat2usd_sheet = sheet.update_cell(31,8, "{:.0%}".format(result))
   # Get current price
    bat2usd_cp = sheet.update_cell(31,9, lprice)
bat2_cell()
'''
'''
def ltc_cell():
    lprice = lt1
    lt_in = sheet.cell(32,5).value
    result = ((float(lprice) - float(lt_in))/abs(float(lt_in)))
    ltcusd_sheet = sheet.update_cell(32,8, "{:.0%}".format(result))
   # Get current price
    ltcusd_cp = sheet.update_cell(32,9, lprice)
ltc_cell()
'''
'''
def bch_cell():
    lprice = bc1
    bc_in = sheet.cell(33,5).value
    result = ((float(lprice) - float(bc_in))/abs(float(bc_in)))
    bchusd_sheet = sheet.update_cell(33,8, "{:.0%}".format(result))
   # Get current price
    bchusd_cp = sheet.update_cell(33,9, lprice)
bch_cell()
'''
'''
def ltc_cell2():
    lprice = lt1
    lt_in = sheet.cell(36,5).value
    result = ((float(lprice) - float(lt_in))/abs(float(lt_in)))
    ltcusd_sheet = sheet.update_cell(36,8, "{:.0%}".format(result))
   # Get current price
    ltcusd_cp = sheet.update_cell(36,9, lprice)
ltc_cell2()
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
print ('ORDER HISTORY')
print ('USD PAIRS |    DATE    |  ORDER ID   |  AMOUNT  |  BUYIN PRICE  |  FEE  |  TOTAL  | % CHANGE')
print (' BTC/USD  | 12/21/2020 | 20841191289 |  0.0221  |   23121.9     |  1.28 |  512.27 |   1%')
#---------------------------------------#

## Get the number of rows in the sheet
#--numRows = sheet.row_count
#################################################################################################################

## Calling Email Function ##
#--email_alert()
