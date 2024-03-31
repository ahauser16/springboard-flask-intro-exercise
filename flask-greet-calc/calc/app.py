from flask import Flask, request, abort
import operations

app = Flask(__name__)

operation_mapping = {
    'add': operations.add,
    'sub': operations.sub,
    'mult': operations.mult,
    'div': operations.div
}

@app.route('/math/<operation>')
def do_math(operation: str) -> str:
    """
    Perform the math operation specified in the URL path on the parameters 'a' and 'b' from the query string.  If the operation is not valid, or if 'a' or 'b' are not provided or are not integers, abort with a 400 status code.
    """
    if operation not in operation_mapping:
        abort(400, description="Invalid operation!")

    a = request.args.get('a')
    b = request.args.get('b')

    if not a or not b:
        abort(400, description="Missing parameters!")

    try:
        a, b = int(a), int(b)
    except ValueError:
        abort(400, description="Parameters must be integers!")

    result = operation_mapping[operation](a, b)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)