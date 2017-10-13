from flask import Flask, request, render_template, redirect,flash
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://build-a-blog:Pass@123#@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO']=True
app.secret_key="asfdgfhghjjk"

db=SQLAlchemy(app)
class	Blog(db.Model):
		id= db.Column(db.Integer, primary_key= True)
		title= db.Column(db.String(120))
		body= db.Column(db.String(500))
def __init__(self,title,body):
		self.title=title
		self.body=body
blogs=[]
@app.route('/')
def index():
	blogs=Blog.query.order_by("id desc").all()
	return render_template('index.html',title='Build a Blog!',blogs=blogs)

@app.route('/newpost')
def newpost():
	return render_template('post.html',title='New Post Entry!')

@app.route('/blog')
def blog():
	if request.method=='GET':
		if not request.args.get('id') is None:
			
			id=(int)(request.args.get('id'))
			blogs=Blog.query.filter_by(id=id).first()
			return render_template('single.html',title='Single Post!',blogs=blogs)
	blogs=Blog.query.order_by("id desc").all()	
	return render_template('blog.html',title='Blog!',blogs=blogs)
	
	
	

@app.route('/',methods=['POST'])
def register():	
	if	request.method=='POST':
		title=request.form['title']
		body=request.form['body']
		newpost=Blog(title=title,body=body)
		db.session.add(newpost)
		db.session.commit()
		blogs=Blog.query.order_by("id desc").all()
		
	return render_template('blog.html',title='Build a Blog!', blogs=blogs)

@app.route('/newpost',methods=['POST'])
def submitpost():

	if request.method=='POST':
		title=request.form['title']
		body=request.form['body']
		if title=="" or body=="" or title==" " or body==' ':
			flash("invalid")
			return render_template('post.html')

		
		newpost=Blog(title=title,body=body)
		db.session.add(newpost)
		db.session.commit()
		blogs=Blog.query.order_by("id desc").all()
		
	return render_template('blog.html',title='Build a Blog!', blogs=blogs)

if __name__=='__main__':
	app.run()