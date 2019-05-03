#!/usr/bin/python3

from flask import Flask, render_template, request

import search

application = app = Flask(__name__)
app.debug = True

@app.route('/search', methods=["GET"])
def dosearch():
<<<<<<< HEAD
    query = request.args['query']
    qtype = request.args['query_type']

    """multidict = request.args.get()
    for value in multidict:
        print(value)"""
    
    """print(query)
    print(qtype)"""
=======
>>>>>>> 6539dd7543ad5aaca58b3a432940ac639d6eb25e
    """
    TODO:
    Use request.args to extract other information
    you may need for pagination.
    """

    query = request.args['query']
    qtype = request.args['query_type']

    """print("Page number: {page}".format(page = request.args.get('page')))"""
    page = request.args.get('page', 1)
    page = int(page)
    offset = (page - 1) * 20

    next = page + 1
    previous = page - 1
    if previous < 1:
        previous = 1

    search_results = search.search(query, qtype, offset)

    length = int(search_results[-1][0])
    del search_results[-1]
    upper_bound = ((offset + 1) * 20)
    if upper_bound > length:
        upper_bound = length
    
    return render_template('results.html',
            query=query,
            results=length,
            search_results=search_results,
            x=(offset * 20) + 1,
            y=upper_bound)

@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        pass
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
