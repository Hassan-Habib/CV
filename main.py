from flask import Flask, render_template, redirect, url_for, request
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
sur_list1=['Impaction Case1', 'Impaction Case1', 'Impaction Case1', 'Impaction Case1', 'Impaction Case2',
           'Impaction Case2', 'Impaction Case 3', 'Extraction', 'Extraction', 'Extraction']
sur_list2=['Clinical Picture before surgery', 'X-ray before surgery', 'X-ray after surgery', 'After suturing',
           'X-ray before surgery', 'X-ray after surgery', 'X-ray before surgery', 'Clinical Picture after extraction',
           'Clinical Picture after extraction', 'Clinical Picture after extraction' ]
end_list1 = ["Upper 6", "Lower 6", "Upper 6", "Lower 6", "Lower 6,7", "Upper Central", "Upper 6", "Upper 6", "Lower 7", "Lower 5",
             "Lower 6", ]
end_list2= ["retreatment of pulpotec case(calcified canals)", "tooth bud", "Mb2", "suuuuuper tight canals", "bypass", " ", " ", "MB2", " "," ", " "]
ped_list1 = ["Pulpotomy", "Pulpotomy", "Pulpectomy", "Pulpectomy", "Pulpectomy", "SSC", " Happy Patient :)"]
ped_list2 = ["", "", "", "", "", "", ""]
op_list1 = ["Double Class 2", "After restoration", "Double Class 2", "After restoration", "Class 1", "Removing caries",
            "After restoration", "Class 3", "After restoration", "Replacement of old restoration", "After restoration"]
op_list2 = ["", "", "", "", "", "", "", "", "", "", "", ]
fix_list1= [""]
fix_list2= ['']

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/CV")
def cv():
    return render_template("CV.html")

@app.route("/Surgery")
def surgery():
    return render_template("cases.html", hi="Surgery", file="static/Cases/images/surgery", titles1=len(sur_list1),
                           talk=sur_list1, talk1=sur_list2)

@app.route("/Endo")
def endo():
    return render_template("cases.html", hi="Endodontic Ttt", file="static/Cases/images/endo", titles1=len(end_list1),
                           talk=end_list1, talk1=end_list2)

@app.route("/Operative")
def operative():
    return render_template("cases.html", hi="Operative", file="static/Cases/images/operative", titles1=len(op_list1),
                           talk=op_list1, talk1=op_list2)

@app.route("/Fixed")
def pedo():
    return render_template("cases.html", hi="pedo", file="static/Cases/images/pedo", titles1=len(ped_list1),
                           talk=ped_list1, talk1=ped_list2)

if __name__ == "__main__":
    app.run(debug=True)
