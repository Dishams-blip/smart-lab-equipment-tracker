from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///equipment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Home page
@app.route('/')
def home():
    equipment_list = Equipment.query.all()
    return render_template('index.html', equipment_list=equipment_list)

# Add equipment
@app.route('/add', methods=['POST'])
def add_equipment():

    name = request.form['name']
    category = request.form['category']
    quantity = request.form['quantity']
    status = request.form['status']

    new_equipment = Equipment(
        name=name,
        category=category,
        quantity=quantity,
        status=status
    )

    db.session.add(new_equipment)
    db.session.commit()

    return redirect('/')

# Create database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)