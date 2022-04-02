from flask_app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    def __init__(self, age):
        self.age=age

def create_user(new_age):
    user = User(new_age)            # Create a data with the provided input
    db.session.add(user)        # Actually add data to the database
    db.session.commit()      # Save all pending changes to the database
    return user

if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.create_all()
    print("Done!")