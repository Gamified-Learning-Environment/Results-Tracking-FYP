from flask import Flask, request, jsonify
from init import app
import db
from models.resultModel import createResult, getResult
from bson import ObjectId

# Test route to check connection
@app.route('/')
def home():
    print("successful connection to Results Service")
    return "Results Service"

# Test route to create a result
@app.route('/api/results', methods=['POST'])
def create_result():
    try:
        result_data = request.json
        result_id = createResult(result_data)
        return jsonify({
            "message": "Result created successfully",
            "result_id": result_id
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Test route to get a result
@app.route('/api/results/<userId>/<quizId>', methods=['GET'])
def get_result(userId, quizId):
    try:
        result = getResult(userId, quizId)
        if result:
            return jsonify(result)
        return jsonify({"message": "Result not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8070)