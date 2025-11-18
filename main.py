import requests
import selectorlib
import smtplib, ssl
import os
import time


URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

"""this header tell to the webserver that this is the actually a browser so its behaving like a browser because some server don't like script program"""

def scrape(url):
    """scrape the page source from the url"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    """extract the html from the source"""
    extractor = selectorlib.Extractor.from_yaml_file("extractor.yaml")
    value = extractor.extract(source)["tours"]
    return value

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "anas.shaikh7827@gmail.com"
    password = "bovniwbuqljmesrz"

    receiver = "anas.shaikh7827@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    print("Email was sent !")

def store(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")

def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()

if __name__ == '__main__':
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        content = read(extracted)
        if extracted !="No upcoming tours found":
            if extracted not in content:
                store(extracted)
                send_email(message="Hey, new event is found")
        time.sleep(2)