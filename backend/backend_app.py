from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET', 'POST'])
def get_posts():

    if request.method == 'POST':
        new_post = request.get_json()

        # Checking if input is empty
        if not new_post['title']:
            return jsonify({"error": "Missing required field", "missing": "title"}), 400
        if not new_post['content']:
            return jsonify({"error": "Missing required field", "missing": "content"}), 400
        # Generates a new id for new post
        new_id = max(post['id'] for post in POSTS) + 1
        new_post['id'] = new_id

        # Adds new post to POSTS
        POSTS.append(new_post)
        return jsonify(new_post), 201

    # Handles GET request
    return jsonify(POSTS)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
