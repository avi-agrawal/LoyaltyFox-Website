#imports
# from Loyal_Fox.codes.mailing import mail_company, mail_viwer
import os
from datetime import datetime
from enum import unique
from logging import debug

from flask import Flask, flash, redirect, render_template, request, make_response
from flask_login import (LoginManager, UserMixin, current_user, login_required, login_user, logout_user)
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

# from mailing import *


#global
# frontend_url = "http://localhost:3000"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = "./static/blogs_images"


#configuring
app = Flask(__name__)
app.config["SECRET_KEY"]= "KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blogs.db"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///User.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

login_manager = LoginManager()
login_manager.init_app(app)

app.config.update(
    DEBUG=True,
    
    # for actual code running on AWS
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
   
    MAIL_SERVER = "email-smtp.ap-south-1.amazonaws.com",
    MAIL_USERNAME = "AKIAZXXKXWLK4PLL4OHQ",
    MAIL_PASSWORD = "BDl2EYN45O31YT2+n2o1P+RQ8A7dtn6i0GZFXWVqldQB"
)
mail = Mail(app)


#creating flask object models or database table
class blogs_table(db.Model):
    id = db.Column("Id",db.Integer, primary_key=True)
    timestamp = db.Column("Timestamp",db.DateTime,default=datetime.now(), nullable=False)
    title  = db.Column("Title",db.String(200),nullable=False)
    abstract = db.Column("Abstract",db.Text)
    # author = db.Column(db.String(20))
    image = db.Column("Image",db.String(500))
    content = db.Column("Content",db.Text,nullable=False)


class User(UserMixin, db.Model):
    id = db.Column("ID",db.Integer, primary_key=True)
    username = db.Column("Username",db.String(100),unique=True, nullable=False)
    password = db.Column("Password",db.String(100), nullable=False)


#functions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# login manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#APIs routes

#Home
@app.route("/")
# @app.route("/home/")
@app.route("/home")
def home():
    return render_template("home.html")

# -----------------------------------------------

#About US
# @app.route("/who_we_are/")
@app.route("/who_we_are")
def who_we_are():
    return render_template("who_we_are.html")

# @app.route("/what_we_do/")
@app.route("/what_we_do")
def what_we_do():
    return render_template("what_we_do.html")

# @app.route("/our_mission/")
@app.route("/our_mission")
def our_mission():
    return render_template("our_mission.html")

# ------------------------------------------------------

#Our Solutions
# @app.route("/multi-tenant-loyalty/")
@app.route("/multi-tenant-loyalty")
def multi_tenant_loyalty():
    return render_template("multi-tenant-loyalty.html")

# @app.route("/marketing-campaigns/")
@app.route("/marketing-campaigns")
def marketing_campaigns():
    return render_template("marketing-campaigns.html")

# @app.route("/helpdesk-services/")
@app.route("/helpdesk-services")
def helpdesk_services():
    return render_template("helpdesk-services.html")

# @app.route("/data-analytics/")
@app.route("/data-analytics")
def data_analytics():
    return render_template("data-analytics.html")

# @app.route("/instant-rewards/")
@app.route("/instant-rewards")
def instant_rewards():
    return render_template("instant-rewards-new.html")
    #return redirect("/404")

# @app.route("/content-and-creatives/")
@app.route("/content-and-creatives")
def content_and_creatives():
    return render_template("content-and-creatives.html")

# @app.route("/robust-tech/")
@app.route("/robust-tech")
def robust_tech():
    return render_template("robust-tech.html")





#----------------------------------------------------

# @app.route("/ourteam/")
@app.route("/ourteam")
def ourteam():
    return render_template("ourteam.html")

# @app.route("/navbar/")
@app.route("/navbar")
def navbar():
    return render_template("navbar.html")
    
#--------------------------------------------------------


# @app.route("/productfulfillment/")
@app.route("/productfulfillment")
def product():
    return render_template("product.html")

@app.route("/admin")
def admin():
    return render_template("admin_login.html")


# @app.route("/experiences/")
@app.route("/experiences")
def experiences():
    return render_template("experiences.html")
    #return redirect("/404")


#--------------------------------------------------------

# @app.route("/404/")
@app.route("/404")
def func_404():
    return render_template("404.html")

@app.errorhandler(404)
def not_found(e):
    return redirect("/404")


#--------------------------------------------------------

# @app.route("/rewards/", methods=["GET","POST"])
@app.route("/rewards", methods=["GET","POST"])
def rewards():
    if request.method == "POST":
        # try
        name = request.form.get("user_name")
        # name = request.form["name"]
        phone = request.form.get("phone")
        email = request.form.get("email")
        note = request.form.get("note")
                                          
        # mail_msg = """
        # Response from 'Apply for Gift Vouchers': \n
        # Name : """ + str(name) + """
        # Phone : """ + str(phone) + """ 
        # Email ID : """ + str(email) + """ 
        # Any Note : """ + str(note) + """ \n
        # """
        # print(mail_msg)


        # if no entry in the form
        # if(not name or not phone or not email or not note):
        #     err_msg = "Give all the inputs"
        #     print(err_msg)
        #     flash(err_msg,"error")
        #     return redirect("/rewards")

        #check whether phoneNO is 10 digits
        # if(len(str(phone))!=10 or str(phone)[0]=='0'):
        #     err_msg = "Enter 10 digits Phone no."
        #     print(err_msg)
        #     flash(err_msg,"error")
        #     return redirect("/rewards")


        mail_msg = """
        Response from 'Apply for Gift Vouchers': \n
        Name : """ + str(name) + """
        Phone : """ + str(phone) + """ 
        Email ID : """ + str(email) + """ 
        Any Note : """ + str(note) + """ \n
        """

        print(mail_msg)

        print("\n  Mailing..........")
        msg_company = Message(
            # sender = ("Test","testing0963@gmail.com"),
            sender = ("Website","info@loyaltyfox.com"),
            recipients=["info@loyaltyfox.com","testing0963@gmail.com"],
            body = mail_msg
            # subject = "ContactUS form"
        )
        # msg.body = "Hey avi"
        msg_company.subject = "Loyalty Fox Website | Apply For Gift Vouchers Response"
        mail.send(msg_company)

        # mail_company(mail_msg)
        print("mailed to loyality fox..")
        

        #mail the the person whom want to be contacted
        msg_viewer = Message(
            sender = ("Website","info@loyaltyfox.com"),
            recipients=[email],
            body = mail_msg
            # subject = "ContactUS form"
        )
        # msg.body = "Hey avi"
        msg_viewer.subject = "Loyalty Fox | Apply For Gift Vouchers Response"
        # mail.send(msg_viewer)

        # mail_viwer(email,mail_msg)
        print("mailed to user.")
        flash("Thank you for your interest, we'll contact you soon. For any other query, you can call us on 8802065822 or write to us on info@loyaltyfox.com. ","success")
    
    return render_template("rewards.html")
    # return redirect(frontend_url)

    # except Exception as e:
        # print(e)
        # err_msg = "Error in contactUS: " + str(e)
        # print(err_msg)
        # flash(err_msg,"error")
        # return redirect("/rewards")



#contact us API
# @app.route("/contactUS/", methods=["GET","POST"])
@app.route("/contactUS", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        # try
        name = request.form.get("user_name")
        # name = request.form["name"]
        phone = request.form.get("phone")
        email = request.form.get("email")
        company = request.form.get("company")
        note = request.form.get("note")
                                          
        # mail_msg = """
        # Response from Contact Us: \n
        # Name : """ + str(name) + """
        # Phone : """ + str(phone) + """ 
        # Email ID : """ + str(email) + """
        # Company : """ + str(company) + """ 
        # Any Note : """ + str(note) + """ \n
        # """
        # print(mail_msg)


        # if no entry in the form
        # if(not name or not phone or not email or not note):
        #     err_msg = "Give all the inputs"
        #     print(err_msg)
        #     flash(err_msg,"error")
        #     return redirect("/contactUS")

        #check whether phoneNO is 10 digits
        # if(len(str(phone))!=10 or str(phone)[0]=='0'):
        #     err_msg = "Enter 10 digits Phone no."
        #     print(err_msg)
        #     flash(err_msg,"error")
        #     return redirect("/contactUS")


        mail_msg = """
        Response from Contact Us: \n
        Name : """ + str(name) + """
        Phone : """ + str(phone) + """ 
        Email ID : """ + str(email) + """
        Company : """ + str(company) + """ 
        Any Note : """ + str(note) + """ \n
        """

        print(mail_msg)

        print("\n  Mailing..........")
        msg_company = Message(
            # sender = ("Test","testing0963@gmail.com"),
            sender = ("Website","info@loyaltyfox.com"),
            recipients=["info@loyaltyfox.com","testing0963@gmail.com"],
            body = mail_msg
            # subject = "ContactUS form"
        )
        # msg.body = "Hey avi"
        msg_company.subject = "Loyalty Fox Website | Contact US Response"
        mail.send(msg_company)

        # mail_company(mail_msg)
        print("mailed to loyality fox..")
        

        #mail the the person whom want to be contacted
        msg_viewer = Message(
            sender = "testing0963@gmail.com",
            recipients=[email],
            body = mail_msg
            # subject = "ContactUS form"
        )
        # msg.body = "Hey avi"
        msg_viewer.subject = "Loyalty Fox | Contact US Response"
        # mail.send(msg_viewer)

        # mail_viwer(email,mail_msg)
        print("mailed to user.")
        flash("Thank you for your interest, we'll contact you soon. For any other query, you can call us on 8802065822 or write to us on info@loyaltyfox.com. ","success")
    
    return render_template("contactus.html")
    # return redirect(frontend_url)

    # except Exception as e:
        # print(e)
        # err_msg = "Error in contactUS: " + str(e)
        # print(err_msg)
        # flash(err_msg,"error")
        # return redirect("/contactUS")
   
# ---------------------------------------------------------------------------------


#ppc-channel landing page API
@app.route("/ppc-channel-loyalty-program/", methods=["GET","POST"])
@app.route("/ppc-channel-loyalty-program", methods=["GET","POST"])
def ppc():
    if request.method == "POST":
        # try
        name = request.form.get("name")
        # name = request.form["name"]
        phone = request.form.get("phone")
        email = request.form.get("email")
        note = request.form.get("message")
                                          
        # mail_msg = """
        # Response from Contact Us: \n
        # Name : """ + str(name) + """
        # Phone : """ + str(phone) + """ 
        # Email ID : """ + str(email) + """
        # Company : """ + str(company) + """ 
        # Any Note : """ + str(note) + """ \n
        # """
        # print(mail_msg)


        # if no entry in the form
        # if(not name or not phone or not email or not note):
        #     err_msg = "Give all the inputs"
        #     print(err_msg)
        #     flash(err_msg,"error")
        #     return redirect("/contactUS")

        #check whether phoneNO is 10 digits
        # if(len(str(phone))!=10 or str(phone)[0]=='0'):
        #     err_msg = "Enter 10 digits Phone no."
        #     print(err_msg)
        #     flash(err_msg,"error")
        #     return redirect("/contactUS")


        mail_msg = """
        Response from PPC-channel-loyalty-program landing page: \n
        Name : """ + str(name) + """
        Phone : """ + str(phone) + """ 
        Email ID : """ + str(email) + """ 
        Any Note : """ + str(note) + """ \n
        """

        print(mail_msg)

        print("\n  Mailing..........")
        msg_company = Message(
            # sender = ("Test","testing0963@gmail.com"),
            sender = ("Website","info@loyaltyfox.com"),
            recipients=["info@loyaltyfox.com","testing0963@gmail.com"],
            body = mail_msg
            # subject = "ContactUS form"
        )
        # msg.body = "Hey avi"
        msg_company.subject = "Loyalty Fox Website | ppc-channel-loyalty-program Response"
        mail.send(msg_company)

        # mail_company(mail_msg)
        print("mailed to loyality fox..")
        

        #mail the the person whom want to be contacted
        msg_viewer = Message(
            sender = ("Website","info@loyaltyfox.com"),
            recipients=[email],
            body = mail_msg
            # subject = "ContactUS form"
        )
        # msg.body = "Hey avi"
        msg_viewer.subject = "Loyalty Fox | ppc-channel-loyalty-program Response"
        # mail.send(msg_viewer)

        # mail_viwer(email,mail_msg)
        print("mailed to user.")
        flash("Thank you for your interest, we'll contact you soon. For any other query, you can call us on 8802065822 or write to us on info@loyaltyfox.com. ","success")
    
    return render_template("ppc-channel.html")


@app.route("/gift-vouchers/", methods=["GET","POST"])
@app.route("/gift-vouchers", methods=["GET","POST"])
def gifts():
    if request.method == "POST":
        # try
        name = request.form.get("name")
        # name = request.form["name"]
        phone = request.form.get("phone")
        email = request.form.get("email")
        note = request.form.get("message")
                                          
        # mail_msg = """
        # Response from Contact Us: \n
        # Name : """ + str(name) + """
        # Phone : """ + str(phone) + """ 
        # Email ID : """ + str(email) + """
        # Company : """ + str(company) + """ 
        # Any Note : """ + str(note) + """ \n
        # """
        # print(mail_msg)


        # if no entry in the form
        # if(not name or not phone or not email or not note):
        #     err_msg = "Give all the inputs"
        #     print(err_msg)
        #     flash(err_msg,"error")
        #     return redirect("/contactUS")

        #check whether phoneNO is 10 digits
        # if(len(str(phone))!=10 or str(phone)[0]=='0'):
        #     err_msg = "Enter 10 digits Phone no."
        #     print(err_msg)
        #     flash(err_msg,"error")
        #     return redirect("/contactUS")


        mail_msg = """
        Response from Gift-vouchers landing page: \n
        Name : """ + str(name) + """
        Phone : """ + str(phone) + """ 
        Email ID : """ + str(email) + """ 
        Any Note : """ + str(note) + """ \n
        """

        print(mail_msg)

        print("\n  Mailing..........")
        msg_company = Message(
            # sender = ("Test","testing0963@gmail.com"),
            sender = ("Website","info@loyaltyfox.com"),
            recipients=["info@loyaltyfox.com","testing0963@gmail.com"],
            body = mail_msg
            # subject = "ContactUS form"
        )
        # msg.body = "Hey avi, get lost"
        msg_company.subject = "Loyalty Fox Website | gift-vouchers page Response"
        mail.send(msg_company)

        # mail_company(mail_msg)
        print("mailed to loyality fox..")
        

        #mail the the person whom want to be contacted
        msg_viewer = Message(
            sender = ("Website","info@loyaltyfox.com"),
            recipients=[email],
            body = mail_msg
            # subject = "ContactUS form"
        )
        # msg.body = "Hey avi, get lost"
        msg_viewer.subject = "Loyalty Fox | gift-vouchers Response"
        # mail.send(msg_viewer)

        # mail_viwer(email,mail_msg)
        print("mailed to user.")
        flash("Thank you for your interest, we'll contact you soon. For any other query, you can call us on 8802065822 or write to us on info@loyaltyfox.com. ","success")
    
    return render_template("gift-vouchers.html")


# --------------------------------------------------------------------------------

# Blog page
# @app.route("/add_blog/", methods=["GET","POST"])
@app.route("/add_blog", methods=["GET","POST"])
@login_required
def add_blog():
    # try:

    if(request.method == "POST"):
        title = request.form.get("title")
        abstract = request.form.get("abstract")
        file = request.files["image_file"]
        content = request.form.get("content")

        filename = secure_filename(file.filename)

        if not content:
            err_msg = "Content/Main body field empty !"
            flash(err_msg,"error")
            return redirect("/add_blog")

        if(file and len(filename)>100):
            flash("Please upload file with shorter filename","error")
            return redirect("/add_blog")

        imagename = str(filename) + "_--_" + str(title)
        imagename_secure = secure_filename(imagename)
        print(imagename_secure)

        
        if file:
            if allowed_file(file.filename):
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], imagename_secure))

                # file_path = UPLOAD_FOLDER + "/" + str(imagename_secure)
                # file.save(file_path)

                #adding row in table
                new_blog_entry = blogs_table(title=title,abstract=abstract,content=content, image=imagename_secure)

                db.session.add(new_blog_entry)
                db.session.commit()

                flash("Blog added successfully","success")
                return redirect("/dashboard")

            else:
                flash('Invalid, Upload only png, jpg, jpeg, gif')

    return render_template("add_blog.html")

    # except Exception as e:
        # print(e)
        # err_msg = "Error in add_blog: " + str(e)
        # print(err_msg)
        # flash(err_msg,"error")
        # return redirect("/add_blog")

#----------------------------------------------------
# @app.route("/blogs")
# @app.route("/blogs/")
# def blogsNew():
#     return render_template("blogs_new.html")




@app.route("/dashboard", methods=["GET","POST"])
@login_required
def blogs_dashboard():
    # try

    all_blogs_list = blogs_table.query.order_by(blogs_table.id.desc()).all()
    print(all_blogs_list)

    return render_template("blogs_dashboard.html",all_blogs_list=all_blogs_list)


@app.route("/delete/<int:blog_id>")
@login_required
def blog_delete(blog_id):

    image_obj = blogs_table.query.filter_by(id=blog_id).first()
    imagename_secure = image_obj.image
    print(imagename_secure)
    blogs_table.query.filter_by(id=blog_id).delete()
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], imagename_secure))
    # post.delete()
    db.session.commit()

    return redirect("/dashboard")


# @app.route("/blogs/", methods=["GET","POST"])
@app.route("/blogs", methods=["GET","POST"])
def blogs():
    # try

    all_blogs_list = blogs_table.query.order_by(blogs_table.id.desc()).all()
    print(all_blogs_list)

    return render_template("blogsx.html",all_blogs_list=all_blogs_list)


# @app.route("/blog_post")
@app.route("/blog_post/<int:blog_id>")
def blog_post(blog_id):
    post = blogs_table.query.filter_by(id=blog_id).first()

    return render_template("postx.html",post=post)


@app.route("/admin", methods=["GET","POST"])
def admin_login():
    if(request.method=="POST"):
        username = request.form.get("user_name")
        password = request.form.get("password")

        user_obj = User.query.filter_by(username=username).first()
        
        if user_obj:
            if(username==user_obj.username and password==user_obj.password):
                print(user_obj.username)
                login_user(user_obj)
                print(current_user)
                return redirect("/dashboard")
            
            else:
                err_msg = "Username/Password Incorrect !"
                flash(err_msg,"error")
        
        else:
            err_msg = "Username/Password Incorrect !"
            flash(err_msg,"error")

    
    return render_template("admin_login.html")
    

#logout API
@app.route("/logout")
@login_required
def logout():
    id = current_user.id
    user = User.query.filter_by(id=id).first()
    # print(user)
    logout_user()
    flash("You are logged out","success")
    return redirect("/admin")

# --------------------------------------------------------------------------


#API for sitemap.xml file
@app.route("/sitemap.xml")
def sitemap():
    template = render_template("sitemap.xml")
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'

    return response
    # return render_template("sitemap.xml")


@app.route("/abc.xml")
def abc():
    template = render_template("abc.xml")
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'

    return response

# --------------------------------------------------------------------------


if __name__ == "__main__":
    db.create_all()
    # admin = User(username="admin",password="admin")
    # db.session.add(admin)
    # db.session.commit()
    app.run(debug=True, port=5000, host="0.0.0.0")

