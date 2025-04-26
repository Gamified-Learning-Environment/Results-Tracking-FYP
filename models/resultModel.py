from datetime import datetime

def createResult(resultData):
    from db import results_collection

    # Validate required fields
    required_fields = ['userId', 'quizId', 'score', 'totalQuestions', 'questionAttempts', 'category']
    for field in required_fields:
        if field not in resultData: # check if all required fields are present in the resultData
            raise ValueError(f"Missing required field: {field}")
        
    # Calculate percentage
    percentage = (resultData['score'] / resultData['totalQuestions']) * 100
    
    result = { # create a new result object
        'userId': resultData['userId'],
        'quizId': resultData['quizId'],
        'score': resultData['score'],
        'totalQuestions': resultData['totalQuestions'],
        'percentage': percentage,
        'questionAttempts': resultData['questionAttempts'],
        'category': resultData['category'],
        'created_at': datetime.utcnow()
    }
    
    try: # insert the result into the database
        response = results_collection.insert_one(result)
        return str(response.inserted_id)
    except Exception as e:
        print(f"Database errorL {str(e)}")
        raise

def getResult(userId, quizId):
    from db import results_collection
    result = results_collection.find_one({
        'userId': userId,
        'quizId': quizId
    })
    if result:
        result['_id'] = str(result['_id'])
    return result

def getResultsByCategory(userId, category):
    from db import results_collection
    results = list(results_collection.find({
        'userId': userId,
        'category': category
    }))
    for result in results:
        result['_id'] = str(result['_id'])
    return results