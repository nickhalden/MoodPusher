
from flask import make_response,url_for
from flask import request
from flask import Flask,jsonify

from flask import Flask, render_template, request, redirect, url_for, abort, session


from data_service_provider import DataServiceProvider

DATA_PROVIDER=DataServiceProvider(15)

app = Flask(__name__)

# Routing
# One way to configure routing is to user @app.route() decorator

#gives all the paths configured in the root

def abort(value):
    return {"ITEM not found":value}

@app.route('/api',methods=["GET"])
def list_routes():
    result = []
    for rt in app.url_map.iter_rules():
        result.append({
            "methods":list(rt.methods),
            "route":str(rt)
        })
    return jsonify({"routes":result,"total":len(result)})

#gives all the candidates
# @app.route("/api/candidates")

def candidate():
    candidates = DATA_PROVIDER.get_candidates()
    return jsonify({"candidates":candidates,"total":len(candidates)})

app.add_url_rule("/api/candidate","candidate",candidate)  #another way to configure routes


@app.route("/api/candidate/<string:id>",methods=["GET"])

def candidate_by_id(id):
    candidate=DataServiceProvider.get_candidates(id)
    if candidate:
        return jsonify({"candidate":candidate})
    else:
        abort(404)

#This method can handle multiple multiple routes, whcha was found by it's id,
#PUT verb is used

@app.route("/api/candidate/<string:id>/name/<string:new_name>",methods=["PUT"])
def update_name(id,new_name):
    nr_of_updated_items= DataServiceProvider.update_name(id, new_name)
    if nr_of_updated_items ==0:
        abort(404)
    else:
        return jsonify({"total_updated":nr_of_updated_items})


""" One method can handle multiple routes, like in this case we specify
the default number of items to 1 so this methd woyd be invoke
The <int:numberoftems> is variable parameter and the init is a converter which voncersts
the request parameter to an interger value
"""
@app.route("/api/random/candidate",defaults={"nrOfItems":1},methods=["GET"])

@app.route("/api/random/candidate/<string:nrOfItems>",methods=["GET"])

def random(nrOfItems):
    candidates =DATA_PROVIDER.get_random_candidates(nrOfItems)
    return jsonify({
        "candidates":candidates,
        "total":len(candidates)
    })


@app.route("/api/candidate/delete/<string:id>",methods=["DELETE"])

def delete(id):
    if DATA_PROVIDER.delete_candidate(id):
        return make_response(id,200)
    else :
        abort(404)

@app.route("/api/candidate",methods=["POST"])
def add_candidate():
    first_name= request.form["first_name"]
    last_name = request.form["last_name"]

    new_candidate_id= DATA_PROVIDER.add_candidate(first_name,last_name)
    return jsonify({
        "id":new_candidate_id,
        "url": url_for("candidate_by_id",id=new_candidate_id)
    })
@app.route('/',methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

with app.test_request_context():
     print '********'
     print url_for('candidate')


"""
Template Filters
"""
@app.template_filter('senior_candidates')
def senior_candidates(candidates):
    result=[]
    for candidate in candidates:
        for experience in candidates:
            if experience['years']>=5:
                result.append({
                    'first_name':candidate['first_name'],
                    'last_name': candidate['last_name'],
                    'years': experience['years'],
                    'domain': experience['domain']
                })
                break
    return result


if __name__ == '__main__':
    app.run(debug=True)
