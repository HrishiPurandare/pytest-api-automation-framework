from flask import Flask, jsonify, request

app = Flask(__name__)

# simple in-memory "DB"
_users = {
    1: {"id": 1, "name": "Hrishikesh Tester", "email": "hrishikesh@example.com"}
}
_next_id = 2

@app.route("/users/1")
def get_user_1():
    return jsonify(_users[1]), 200

@app.route("/users/<int:uid>")
def get_user(uid):
    if uid in _users:
        return jsonify(_users[uid]), 200
    return jsonify({"message": "not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    global _next_id
    body = request.get_json() or {}
    name = body.get("name", f"user{_next_id}")
    email = body.get("email", f"user{_next_id}@example.com")
    user = {"id": _next_id, "name": name, "email": email}
    _users[_next_id] = user
    _next_id += 1
    return jsonify(user), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
