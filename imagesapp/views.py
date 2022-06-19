import mimetypes
from django.shortcuts import redirect
from django.http import Http404, HttpResponse, StreamingHttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotAuthenticated
from .models import Image, TemporaryURL
from .serializers import ImageSerializer, ImageCreateSerializer, ImageListSerializer

# Create your views here.

class ImageListView(generics.ListCreateAPIView):
    queryset = Image.objects.all()

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise NotAuthenticated("No Token Provided")
        user = self.request.user
        queryset = Image.objects.all().filter(owner=user)
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ImageCreateSerializer
        elif self.request.method == 'GET':
            return ImageListSerializer

class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise NotAuthenticated("No Token Provided")
        user = self.request.user
        queryset = Image.objects.all().filter(owner=user)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner.tier.original_link_visible == False:
            instance.image_url = ""
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class CreateTemporaryView(APIView):
    def get(self, request, pk, seconds):
        if request.user.is_anonymous:
            raise NotAuthenticated("No Token Provided")
        user = request.user
        image = Image.objects.filter(owner=user, id=pk).first()


        url = request.build_absolute_uri().split('images/')[0]
        if not image:
            return Response({"info": "Image not found"})
        if not image.owner.tier.expireable:
            return Response({"info": "This Tier does not include generating expire URL"})
        if seconds >= 300 and seconds <= 30000:
            tempurl = TemporaryURL.objects.create(original_image=image, expire_after=seconds)
            return Response({"url": "{url}tempurl/{id}".format(url=url, id=tempurl.id)})
        else:
            return Response({"info": "Seconds value must be between 300 and 30000"})

def redirectImageURL(request, pk):
    temp_url = TemporaryURL.objects.filter(id=pk).first()

    if not temp_url:
        return HttpResponse("URL does not exist.")

    if temp_url.is_expired():
        image = temp_url.original_image
        filename = image.image_url
        size = filename.size

        content_type_file = mimetypes.guess_type(filename.path)[0]

        response = StreamingHttpResponse(open(image.image_url.path, 'rb'), content_type=content_type_file)
        response['Content-Disposition'] = "attachment; filename=%s" % str(filename)
        response['Content-Length'] = size

        return response
    else:
        return HttpResponse("URL has expired.")