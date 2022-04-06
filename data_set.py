from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String)
    steroid = db.Column(db.String)
    antivirals = db.Column(db.String)
    fatigue = db.Column(db.String)
    malaise = db.Column(db.String)
    anorexia = db.Column(db.String)
    liver_big = db.Column(db.String)
    liver_firm = db.Column(db.String)
    spleen_palable = db.Column(db.String)
    spiders = db.Column(db.String)
    ascites = db.Column(db.String)
    varices = db.Column(db.String)
    bilirubin=db.Column(db.Float)
    alk_phosphate = db.Column(db.Integer)
    sgot = db.Column(db.Integer)
    albumin = db.Column(db.Integer)
    protime = db.Column(db.Integer)
    histology  = db.Column(db.String)
    def __init__(self,age,sex,steroid,antivirals,fatigue,malaise,anorexia,liver_big,liver_firm,spleen_palable,
            spiders,ascites,varices,bilirubin,alk_phosphate,sgot,albumin,protime,histology):
        self.age = age
        self.sex = sex
        self.steroid = steroid
        self.antivirals = antivirals
        self.fatigue = fatigue
        self.malaise = malaise
        self.anorexia = anorexia
        self.liver_big = liver_big
        self.liver_firm = liver_firm
        self.spleen_palable = spleen_palable
        self.spiders = spiders
        self.ascites = ascites
        self.varices = varices
        self.bilirubin = bilirubin
        self.alk_phosphate = alk_phosphate
        self.sgot = sgot
        self.albumin = albumin
        self.protime = protime
        self.histology = histology

def creatuser(new_age,n_sex,n_steroid,n_antivirals,n_fatigue,n_malaise,n_anorexia,n_liver_big,n_liver_firm,n_spleen_palable,
            n_spiders,n_ascites,n_varices,n_bilirubin,n_alk_phosphate,n_sgot,n_albumin,n_protime,n_histology):
    user = User(new_age,n_sex,n_steroid,n_antivirals,n_fatigue,n_malaise,n_anorexia,n_liver_big,n_liver_firm,n_spleen_palable,
            n_spiders,n_ascites,n_varices,n_bilirubin,n_alk_phosphate,n_sgot,n_albumin,n_protime,n_histology)            # Create a data with the provided input
    db.session.add(user)        # Actually add data to the database
    db.session.commit()      # Save all pending changes to the database
    return user