from flask import Flask,render_template,send_from_directory,request,redirect
import os,csv

app = Flask(__name__)
print(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:link>")
def master(link=None):
    return render_template(link)



def write_data_csv(database):
    with open('database.csv','a',newline='') as file:
        mail=database['email']
        sub=database['subject']
        msg=database['message']
        csv_writer=csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([mail,sub,msg])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        try:
            write_data_csv(data)
            return redirect('thankyou.html')
        except:
            return "error occured"
    else:
        return"unsuccessful"

