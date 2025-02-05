from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ComentarioSerializer, ProjetoCreateSerializer, ProjetoSerializer, EquipeSerializer
from .models import Projeto, Equipe, Comentario
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import MyRogerPermissions

# Viewset for Comentario
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticated, MyRogerPermissions]


# POST e GET em /api/equipes/
class EquipeListCreateView(generics.ListCreateAPIView):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        ativo = self.request.query_params.get('ativo') or None

        queryset = super().get_queryset()

        if ativo is not None:
            valor = True if ativo == '1' else False
            queryset = Equipe.objects.filter(ativa=valor)

        return queryset


# GET, DELETE, PUT, PATCH em /api/equipes/<int:pk>
class EquipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

   












# class EquipeListAPIView(APIView):
    
#     # GET /api/equipes/
#     def get(self, request):
#         equipes = Equipe.objects.all()
#         serializer = EquipeSerializer(equipes, many=True)
#         return Response(serializer.data)


class ProjetoListAPIView(APIView):
    
    # GET /api/projetos/
    def get(self, request):
        projetos = Projeto.objects.all()
        serializer = ProjetoSerializer(projetos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjetoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST)

   