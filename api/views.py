from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from .permissions import IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadonly
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer, AuthorSerializer
from django.contrib.auth import get_user_model

# Create your views here.
class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    # filtering method by 'django_filters'
    filterset_fields = ['status', 'author__username']
    ordering_fields = ['status', 'publish']
    search_fields = [
                     'title',
                     'content',
                     'author__username',
                     'author__first_name',
                     'author__last_name'
                     ]

    def get_permissions(self):
        if self.action in ['list','create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadonly,)

class AuthorRetrieve(RetrieveAPIView):
    queryset = get_user_model().objects.filter(is_staff=True)
    serializer_class = AuthorSerializer