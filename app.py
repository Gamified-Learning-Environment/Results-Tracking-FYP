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
    
# Route to get all results for a user
@app.route('/api/results/user/<userId>', methods=['GET'])
def get_user_results(userId):
    try:
        results = db.results_collection.find({'userId': userId})
        formatted_results = []
        for result in results:
            result['_id'] = str(result['_id'])
            formatted_results.append({
                'quizId': result['quizId'],
                'score': result['score'],
                'totalQuestions': result['totalQuestions'],
                'percentage': result.get('percentage', (result['score'] / result['totalQuestions']) * 100),
                'questionAttempts': result['questionAttempts'],
                'created_at': result['created_at'].isoformat()
            })
        return jsonify(formatted_results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Route to get all results for a user in a specific category
@app.route('/api/results/category/<user_id>/<category>', methods=['GET'])
def get_category_results(user_id, category):
    try:
        from db import results_collection
        results = list(results_collection.find({
            'userId': user_id,
            'category': category
        }).sort('created_at', 1))  # Sort by date ascending
        
        # Convert ObjectId to string for JSON serialization
        for result in results:
            result['_id'] = str(result['_id'])
            if 'percentage' not in result:
                result['percentage'] = (result['score'] / result['totalQuestions']) * 100
            result['percentage'] = float(result['percentage'])
            
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8070)
