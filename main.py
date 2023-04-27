## Integrate HTML with Flask
## HTTP verb GET And POST

##Jinja2 template
'''
{%.....%} for statement, if-else statement, any kind of statement
{{  }} expression to print output
{#.....#} this is for the comments 
'''

from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')

#dynamic url: append score value to the url
@app.route('/sucess/<int:score>') 
def sucess(score):
	res=""
	if score>=50:
		res ="PASS"
	else:
		res = "FAIL"
	exp={'Score':score,'Result':res}
	return render_template('result.html',result=exp)
	

## Result checker submit html page	
@app.route('/submit',methods=['POST','GET'])
def submit():
	total_score=0
	if request.method=='POST':
		science=float(request.form['science'])
		maths=float(request.form['maths'])
		english=float(request.form['english'])
		hindi=float(request.form['hindi'])
		total_score = (science+maths+english+hindi)/4

	return redirect(url_for('sucess',score=total_score))

if __name__ == '__main__':
	app.run(debug=True)
