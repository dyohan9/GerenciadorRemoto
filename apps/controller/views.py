from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from apps.controller.tasks import sendPacket


@method_decorator(csrf_exempt, name='dispatch')
class CallCelery(View):
    def get(self, request, **kwargs):
        sendPacket.delay()
        return JsonResponse(
            {
                "status": True
            }, status=200
        )