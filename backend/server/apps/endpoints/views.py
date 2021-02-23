# backend/server/apps/endpoints/views.py file
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins

from apps.endpoints.models import Endpoint
from apps.endpoints.serializers import EndpointSerializer

from apps.endpoints.models import MLAlgorithm
from apps.endpoints.serializers import MLAlgorithmSerializer

from apps.endpoints.models import MLAlgorithmStatus
from apps.endpoints.serializers import MLAlgorithmStatusSerializer

from apps.endpoints.models import MLRequest
from apps.endpoints.serializers import MLRequestSerializer
# Create your views here.

class EndpointViewSet(
   		mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
	):
    	serializer_class = EndpointSerializer
    	queryset = Endpoint.objects.all()

class MLAlgorithmViewSet(
		mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
	):
		serializer_class = MLAlgorithmSerializer
		queryset = MLAlgorithm.objects.all()

class MLAlgorithmStatusViewSet(
		mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
		mixins.CreateModelMixin
	):
		serializer_class = MLAlgorithmStatusSerializer
		queryset = MLAlgorithmStatus.objects.all()
		def perform_create(self, serializer):
			try:
				with transaction.atomic():
					instance = serializer.save(active=True)
					# set active=False for other statuses
					deactivate_other_statuses(instance)
			except Exception as e:
				raise APIException(str(e))					 

class MLRequestViewSet(
   		mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    	mixins.UpdateModelMixin
	):
    	serializer_class = MLRequestSerializer
    	queryset = MLRequest.objects.all()				
