from flask import Flask, render_template
import os
app = Flask(__name__)

picFolder= os.path.join('static','graphs')
app.config['UPLOAD_FOLDER'] = picFolder



@app.route("/")

@app.route("/index")
def index():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'pic1.png')
    pic2 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic2.png')
    pic3 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic3.png')
    pic4 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic4.png')
    pic5 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic5.png')
    pic6 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic6.png')
    pic7 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic7.png')
    pic8 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic8.png')
    pic9 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic9.png')
    pic10 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic10.png')
    pic11 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic11.png')
    
    pic12 = os.path.join(app.config['UPLOAD_FOLDER'], 'pic12.png')
    pic13 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic13.png')
    pic14 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic14.png')
    pic15 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic15.png')
    pic16 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic16.png')
    pic17 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic17.png')
    pic18 =os.path.join(app.config['UPLOAD_FOLDER'], 'pic18.png')

    return render_template("index.html",user_image = pic1)




if __name__ == "__main__":
    app.run()
