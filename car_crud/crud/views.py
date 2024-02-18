from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Cars
from .serializers import CarSerializer
from helpers import pagination


class CarViewSet(ModelViewSet):
    pagination_class = pagination.CustomPagination
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)
    queryset = Cars.objects.all()

#
# class CarApiView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = CarSerializer(data=request.data)
#         print('---------', request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request, *args, **kwargs):
#         producer = KafkaProducer(bootstrap_servers=conf.KafkaSettings.get_bootstrap_server)
#         v = {
#             'msg'.encode('utf-8'): {
#                 'hello': 'world',
#             },
#         }
#
#         serialized_data = pickle.dumps(v, pickle.HIGHEST_PROTOCOL)
#         producer.send('myTestTopic', serialized_data)
#         print('kafka is working')
#         return HttpResponse(200)
