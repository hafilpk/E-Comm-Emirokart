from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps
from emirokart_backend.helpers import get_dynamic_form_models, get_dynamic_form_fields

class DynamicFormController(APIView):
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
