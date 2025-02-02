from datetime import datetime

def createResult(resultData):
    from db import result_collection
    
    result = {
        'userId': resultData['userId'],
        'quizId': resultData['quizId'],
        'score': resultData['score'],
        'totalQuestions': resultData['totalQuestions'],
        'created_at': datetime.utcnow()
    }
    
    response = result_collection.insert_one(result)
    return str(response.inserted_id)

def getResult(userId, quizId):
    from db import result_collection
    result = result_collection.find_one({
        'userId': userId,
        'quizId': quizId
    })
    if result:
        result['_id'] = str(result['_id'])
    return result