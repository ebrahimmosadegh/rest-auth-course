from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadonly
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth import get_user_model

# Create your views here.
class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer

    # filtering method
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Article.objects.all()
        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)

        author = self.request.query_params.get('author')
        if author is not None:
            queryset = queryset.filter(author__username=author)
        return queryset

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