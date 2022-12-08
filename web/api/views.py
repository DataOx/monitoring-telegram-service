from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from .models import MessageInfo
from .serializers import MessageInfoSerializer


class MessagesInfoView(APIView):
    """ View for get messages info """

    @staticmethod
    def validate_token(token):
        if token is None:
            raise APIException(detail='Required field [TOKEN]', code=400)

        if token != settings.TOKEN:
            raise APIException(detail='Invalid field [TOKEN]', code=400)

    def get(self, request):
        token = request.headers.get('TOKEN')
        self.validate_token(token=token)
        queryset = MessageInfo.objects.all()
        serializer = MessageInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request):
        token = request.headers.get('TOKEN')
        self.validate_token(token=token)
        MessageInfo.objects.all().delete()
        return Response({'detail': 'All data successfully deleted'})



