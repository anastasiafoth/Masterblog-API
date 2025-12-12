from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET', 'POST'])
def get_post_posts():

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


def find_post_by_id(id):
    """ Find the book with the id `book_id`.
      If there is no book with this id, return None. """
    for post in POSTS:
        if id == post['id']:
            return post
    return None


@app.route('/api/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    """ Deletes a post based on given ID """
    post_to_delete = find_post_by_id(id)
    # If post is not found, return error
    if post_to_delete is None:
        return jsonify({"error": "No post found under this ID"}), 404

    # Remove post from the list
    POSTS.remove(post_to_delete)

    return jsonify({"message": f"Post with id {id} has been deleted successfully."}), 200


@app.route('/api/posts/<int:id>', methods=['PUT'])
def update_post(id):
    """ Updates a post based on given ID """
    post_to_update = find_post_by_id(id)
    # If post is not found, return error
    if post_to_update is None:
        return jsonify({"error": "No post found under this ID"}), 404

    # Update the post found with the new data
    new_data = request.get_json()
    post_to_update.update(new_data)


    return jsonify(post_to_update), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
