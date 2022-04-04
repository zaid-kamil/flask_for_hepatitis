from flask_app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)
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
    def __init__(self, age):
        self.age=age

def creatuser(new_age):
    user = User(new_age)            # Create a data with the provided input
    db.session.add(user)        # Actually add data to the database
    db.session.commit()      # Save all pending changes to the database
    return user

if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.create_all()
    print("Done!")