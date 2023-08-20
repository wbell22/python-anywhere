from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('index.html')

@app.route("/index.html")
def landing_page_alt():
    return render_template('index.html')

@app.route("/works.html")
def works_page():
    return render_template('works.html')

@app.route("/about.html")
def about_page():
    return render_template('about.html')

@app.route("/contact.html")
def contact_page():
    return render_template('contact.html')

def write_to_file(data):
    with open('database.txt','a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',mode='a') as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST': 
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('thankyou.html')
    else:
        return "something went wrong.."