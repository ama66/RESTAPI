from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

Nodes=[
    { "node_no":30 ,
    "node_location":"NY",
    "component":["compressor","engine","turbine"]
      } ,
    {"node_no": 20,
     "node_location": "Calgary",
     "component": ["ICE","SIE","DIE"]}
]

Credits={"Author": "Ammar Abdighanie",
         "Company": "BHGE",
         "Location":"OKC"
         }

@app.route('/')
def home():
  return render_template('index.html')


@app.route('/Nodes')
def get_nodes():
  return jsonify({'All nodes': Nodes})


@app.route('/Credits')
def get_credits():
  return jsonify(Credits)



@app.route('/Nodes' , methods=['POST'])
def create_node():
    request_data = request.get_json()
    new_node = {
    'node_no':request_data['node_no'],
    'node_location':request_data['node_location'],
    'component':request_data['component']
    }
    Nodes.append(new_node)
    return jsonify(new_node)


@app.route('/Nodes/<string:nodeno>')
def get_node(nodeno):
  for node in Nodes:
    if node['node_no'] == int(nodeno):
          return jsonify(node)
  return jsonify ({'message': 'node not found'})


@app.route('/Nodes/<string:nodeno>/component' , methods=['POST'])
def create_component_in_node(nodeno):
  request_data = request.get_json()
  for node in Nodes:
    if node['node_no'] == int(nodeno):
        new_comp =request_data['component']
        node['component'].append(new_comp)
        return jsonify(new_comp)
  return jsonify ({'message' :'node not found'})



app.run(port=5001)
