from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps
from emirokart_backend.helpers import get_dynamic_form_models, get_dynamic_form_fields
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.serializers import serialize
import json

class DynamicFormController(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, modelName, id=None):
        model_map = get_dynamic_form_models()
        if modelName not in model_map:
            return Response(
                {"data": "Model Not Found", "message": "Model Not Found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        model_class = apps.get_model(model_map[modelName])
        if model_class is None:
            return Response(
                {"data": "Model Not Found", "message": "Model Not Found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if id:
            model_instance = model_class.objects.filter(
                id=id,
                domain_user_id=request.user.domain_user_id
            ).first()
            if not model_instance:
                return Response(
                    {"data": "Model Item Not Found", "message": "Model Item Not Found"},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            model_instance = model_class()

        fields = get_dynamic_form_fields(model_instance)

        return Response(
            {"data": fields, "message": "Form fields fetched successfully"},
            status=status.HTTP_200_OK
        )
    
    def post(self, request, modelName, id=None):
        model_map = get_dynamic_form_models()
        if modelName not in model_map:
            return Response(
                {"data": "Model Not Found", "message": "Model Not Found"},
                status=status.HTTP_404_NOT_FOUND
            )

        model_class = apps.get_model(model_map[modelName])
        if model_class is None:
            return Response(
                {"data": "Model Not Found", "message": "Model Not Found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if id:
            instance = model_class.objects.filter(
                id=id, domain_user_id=request.user.domain_user_id
            ).first()
            if not instance:
                return Response(
                    {"data": "Model Item Not Found", "message": "Model Item Not Found"},
                    status=status.HTTP_404_NOT_FOUND
                )
            for key, value in request.data.items():
                setattr(instance, key, value)
            instance.save()
        else:
            instance = model_class.objects.create(
                **request.data, domain_user_id=request.user.domain_user_id
            )

        serialized = serialize("json", [instance])
        model_json = json.loads(serialized)[0]["fields"]
        model_json["id"] = instance.id

        return Response(
            {"data": model_json, "message": "Data saved successfully"},
            status=status.HTTP_200_OK
        )