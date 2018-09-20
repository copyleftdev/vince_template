from flask import Flask, jsonify, request

app = Flask(__name__)


class FormulaUtils(object):

    def formula_add(n1, n2):
        return n1 + n2

    def formula_sub(n1, n2):
        return n1 - n2

    def formula_multi(n1, n2):
        return n1 * n2

    def formula_div(n1, n2):
        return n1 / n2


KEY_ERROR = {"Error": "please use key names n1 and n2 of type int"}


@app.route("/api/add", methods=['POST'])
def add_calc():
    try:

        result = request.json
        if "n1" and "n2" in result:

            n1 = result['n1']
            n2 = result['n2']
        else:
            return jsonify(KEY_ERROR)
        cal_result = FormulaUtils.formula_add(n1, n2)
        return jsonify({"result": cal_result})
    except Exception as e:
        return jsonify({"developer_error": e})


@app.route("/api/sub", methods=['POST'])
def sub_calc():
    try:

        result = request.json
        if "n1" and "n2" in result:

            n1 = result['n1']
            n2 = result['n2']
        else:
            return jsonify(KEY_ERROR)
        cal_result = FormulaUtils.formula_sub(n1, n2)
        return jsonify({"result": cal_result})
    except Exception as e:
        return jsonify({"developer_error": e})


@app.route("/api/multiply", methods=['POST'])
def mult_calc():
    try:

        result = request.json
        if "n1" and "n2" in result:
            n1 = result['n1']
            n2 = result['n2']
        else:
            return jsonify(KEY_ERROR)
        cal_result = FormulaUtils.formula_multi(n1, n2)
        return jsonify({"result": cal_result})
    except Exception as e:
        return jsonify({"developer_error": e})


@app.route("/api/divide", methods=['POST'])
def div_calc():
    try:

        result = request.json

        result = request.json
        if "n1" and "n2" in result:
            n1 = result['n1']
            n2 = result['n2']
        else:
            return jsonify(KEY_ERROR)
        cal_result = FormulaUtils.formula_multi(n1, n2)
        return jsonify({"result": cal_result})
    except Exception as e:
        return jsonify({"developer_error": e})


if __name__ == '__main__':
    app.run()
