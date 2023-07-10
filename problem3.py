from flask import Flask, request, jsonify

app = Flask(__name__)

data=[]

@app.route('/',methods=['GET'])
def home_route():
    return "Welcome to Backend!!"

# For accessing all the posts
@app.route('/getposts',methods=['GET'])
def get_posts():
    return jsonify(data)

# For adding new posts
@app.route('/create',methods=['POST'])
def add_post():
    data=request.get_json()
    id=data['id']
    username=data['username']
    caption=data['caption']

    data.append({'id':id,'username':username,'caption':caption})
    return jsonify({"msg":"Post added successfully!!"})

# For deleting existing post
@app.route('/delete/<int:id>')
def delete_post(id):
    for item in data:
        if item['id']==id:
            del item
            return jsonify({"msg":"Post Deleted Successfully"})
    return jsonify({"msg":"Post Not Found!!"})

if __name__=='__main__':
    app.run()