from rest_framework import permissions, status, generics, viewsets
from rest_framework.response import Response
from .models import Todo, Contact
from rest_framework.views import APIView
from .serializers import TodoViewSerializer, TodoCreateSerializer, UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )


class ContactView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        contact = Contact.objects.create(
            name=request.data['name'],
            email=request.data['email'],
            text=request.data['text']
        )
        contact.save()
        return Response(status=status.HTTP_201_CREATED, data={'detail': "created"})


class TodoGetView(generics.ListAPIView):
    serializer_class = TodoViewSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)


class TodoCreateView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, format=None):
        user = request.user
        empty_fields = {}
        message = "field value not provided"
        keys = ['title', 'is_active', 'is_paused',
                'is_visible', 'date', 'time']
        for key in keys:
            if key not in request.data:
                empty_fields[key] = message
        if len(empty_fields) != 0:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=empty_fields)
        todo = Todo.objects.create(
            title=request.data["title"],
            user=user,
            is_active=request.data['is_active'],
            is_paused=request.data['is_paused'],
            is_visible=request.data['is_visible'],
            date=request.data['date'],
            time=request.data['time']
        )
        todo.save()
        return Response(data={"detail": "created"}, status=status.HTTP_200_OK)


class TodoUpdateView(APIView):
	permission_classes = (permissions.IsAuthenticated, )
	def patch(self, request, id):

		if Todo.objects.filter(id=id).exists():

			result = Todo.objects.get(id=id)
			serializer = TodoCreateSerializer(
				result, data=request.data, partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response({"status": "success", "data": serializer.data})
			else:
				return Response({"status": "error", "data": serializer.errors})

		else:
			return Response(data={"detail": "this key is not available"}, status=status.HTTP_406_NOT_ACCEPTABLE)


class TodoDelView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def delete(self, request, id, format=None):
        if Todo.objects.filter(id=id).exists():
            user = request.user
            todo = get_object_or_404(Todo, id=id, user=user)
            todo.delete()
            return Response(data={"detail": "deleted"}, status=status.HTTP_200_OK)
        else:
            return Response(data={"detail": "this key is not available"}, status=status.HTTP_406_NOT_ACCEPTABLE)
