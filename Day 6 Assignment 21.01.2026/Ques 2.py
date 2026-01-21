from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    if not request.json or "name" not in request.json or "email" not in request.json:
        return jsonify({"error": "Invalid input"}), 400

    new_id = max([u["id"] for u in users], default=0) + 1
    new_user = {
        "id": new_id,
        "name": request.json["name"],
        "email": request.json["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(debug=True)
