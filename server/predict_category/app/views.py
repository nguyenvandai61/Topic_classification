from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from predict_category.predict_models import predict
@csrf_exempt 
def index(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        url = body['url']
        res = predict.predict_category(url)
        response_data = {}
        response_data['result'] = res
        return JsonResponse(response_data)