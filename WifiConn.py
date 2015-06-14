#!/usr/bin/env python

# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('registration.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/hello/', methods=['POST'])
def hello():
    ssid=request.form['ssid']
    wifipass=request.form['wifipass']

    #Write SSID and PSK to wpa_supplicant.conf
    file = open('/etc/wpa_supplicant/wpa_supplicant.conf','a')
    file.write('\n\nnetwork={\n     ssid="')
    file.write(ssid)
    file.write('"\n     psk="')
    file.write(wifipass)
    file.write('"\n}')
    file.close()
        
    return render_template('result.html', ssid=ssid, wifipass=wifipass)

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("80")
  )
