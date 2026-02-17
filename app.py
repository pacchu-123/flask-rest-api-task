from flask import Flask, request, jsonify

app = Flask(__name__)

# temporary database (memory)
users = []

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST add user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User added"}), 201

# PUT update user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    if id < len(users):
        users[id] = request.json
        return jsonify({"message": "User updated"})
    return jsonify({"error": "User not found"}), 404

# DELETE user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    if id < len(users):
        users.pop(id)
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

