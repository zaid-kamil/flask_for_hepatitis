from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String)
    steroid = db.Column(db.Integer)
    antivirals = db.Column(db.Integer)
    fatigue = db.Column(db.Integer)
    malaise = db.Column(db.Integer)
    anorexia = db.Column(db.Integer)
    liver_big = db.Column(db.Integer)
    liver_firm = db.Column(db.Integer)
    spleen_palable = db.Column(db.Integer)
    spiders = db.Column(db.Integer)
    ascites = db.Column(db.Integer)
    varices = db.Column(db.Integer)
    bilirubin = db.Column(db.Integer)
    alk_phosphate = db.Column(db.Integer)
    sgot = db.Column(db.Integer)
    albumin = db.Column(db.Integer)
    protime = db.Column(db.Integer)
    histology = db.Column(db.Integer)

    def __init__(self,age,sex,steroid,antivirals,fatigue,malaise,anorexia,liver_big,liver_firm,spleen_palable,
            spiders,ascites,varices,bilirubin,alk_phosphate,sgot,albumin,protime,histology):
        self.age=age
        self.sex=sex
        self.steroid=steroid
        self.antivirals=antivirals
        self.fatigue=fatigue
        self.malaise=malaise
        self.anorexia=anorexia
        self.liver_big=liver_big
        self.liver_firm=liver_firm
        self.spleen_palable=spleen_palable
        self.spiders=spiders
        self.ascites=ascites
        self.varices=varices
        self.bilirubin=bilirubin
        self.alk_phosphate=alk_phosphate
        self.sgot=sgot
        self.albumin=albumin
        self.protime=protime
        self.histology=histology

def creatuser(new_age,sex,steroid,antivirals,fatigue,malaise,anorexia,liver_big,liver_firm,spleen_palable,
            spiders,ascites,varices,bilirubin,alk_phosphate,sgot,albumin,protime,histology):
    user = User(new_age,sex,steroid,antivirals,fatigue,malaise,anorexia,liver_big,liver_firm,spleen_palable,
            spiders,ascites,varices,bilirubin,alk_phosphate,sgot,albumin,protime,histology)            # Create a data with the provided input
    db.session.add(user)        # Actually add data to the database
    db.session.commit()      # Save all pending changes to the database
    return user

