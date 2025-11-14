from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "age": self.age}

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Hello!"

# GET
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([s.to_dict() for s in students])

# POST  :
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "name et age sont requis"}), 400

    student = Student(name=data["name"], age=data["age"])
    db.session.add(student)
    db.session.commit()

    return jsonify(student.to_dict()), 201

# GET
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": "student not found"}), 404
    return jsonify(student.to_dict())

# PUT
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": "student not found"}), 404

    data = request.get_json() or {}

    if "name" in data:
        student.name = data["name"]
    if "age" in data:
        student.age = data["age"]

    db.session.commit()
    return jsonify(student.to_dict()), 200

# DELETE
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"success": False, "error": "Student not found"}), 404

    db.session.delete(student)
    db.session.commit()
    return jsonify({"success": True}), 200

if __name__ == '__main__':
    app.run(debug=True)
