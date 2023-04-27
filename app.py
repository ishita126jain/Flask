from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def hello():
	return "hello! world" 

#dynamic url: append score value to the url
@app.route('/sucess/<int:score>') 
def sucess(score):
	return "The person has passed and the marks is "+str(score)
	
@app.route('/fail/<int:score>') 
def fail(score):
	return "The person has failed and the marks is "+str(score)

#result checker	
@app.route('/results/<int:marks>') 
def results(marks):
	result=""
	if marks<50:
		result='fail'
	else:
		result='sucess'
	return redirect(url_for(result,score=marks))

if __name__ == '__main__':
	app.run(debug=True)
