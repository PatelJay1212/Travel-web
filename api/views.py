from api import serialize
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import status
from api.serialize import UserSerialize,PackagesSerialize
from django.contrib.auth import login,authenticate
from rest_framework.authtoken.models import Token
from myadmin.models import Packages





@api_view(['POST'])
def homeview(request):
    if request.method == "POST":
       seri = serialize.CategorySerialize(data=request.data)
       if seri.is_valid():
           seri.save()
       else:
            print(seri.errors)
    return Response("Data added successfully")



@api_view(['POST'])
def registerview(request):
    seri = UserSerialize(data=request.data)
    if seri.is_valid():
        username = seri.validated_data['username']
        password = seri.validated_data['password']
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        seri.save()
        return Response({"success": "User created successfully"}, status=status.HTTP_201_CREATED)
    return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def loginview(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    print("sdfvgbndsfg",user)
    if user:
        # token, user = Token.objects.get_or_create(user=user)
        return Response('User login Successfully')
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def additem(request):
    s = serialize.PackagesSerialze(data=request.data)
    if s.is_valid():
        s.save()
    else:
        return Response(s.errors)
    return Response("data Added Sucessully")


@api_view(['POST'])
def deleteitem(request,id):
    data = Packages.objects.get(id=id)
    data.delete()
    return Response("data deleted successfully")

@api_view(['POST'])
def updateitem(request, id):
    try:
        package = Packages.objects.get(id=id)
    except Packages.DoesNotExist:
        return Response("Package not found", status=status.HTTP_404_NOT_FOUND)
    
    seri = PackagesSerialize(instance=package, data=request.data, partial=True)
    if seri.is_valid():
        seri.save()
        return Response("Data updated successfully")
    else:
        return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def updateitem(request,id):
#     data = Packages.objects.get(id=id)
#     seri = serialize.PackagesSerialize(Packages,data=request.data,partial=True)
#     if seri.is_valid():
#         seri.save()
#         return Response(" data updated successfully")
#     else:
#         print(seri.errors)
#         return Response(seri.errors)  
    


        
        





























# @api_view(['POST'])
#def registerview(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             try :
#                 User.objects.get(username=serializer.validated_data['username'])
#                 return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
#             except User.DoesNotExist:
#                 serializer.save()
#                 return Response({"success": "User created successfully"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def updateitem(request, id):
#     try:
#         package = Packages.objects.get(id=id)
#     except Packages.DoesNotExist:
#         return Response("Package not found", status=status.HTTP_404_NOT_FOUND)
#     seri = PackagesSerialize(package, data=request.data)
#     if seri.is_valid():
#         seri.save()
#         return Response("Data updated successfully")
#     else:
#         return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST) 
    


