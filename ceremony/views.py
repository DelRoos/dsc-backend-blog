from django.db.models import Q
from .models import Ceremony
from utils.pagination import PostPageNumberPagination
from rest_framework.filters import (    
    SearchFilter,
    OrderingFilter,
    )

from rest_framework.generics import (
    ListAPIView,
    )

from .serializers import (  
    CeremonyListSerializer,
    )

class CeremonyListView(ListAPIView):
    serializer_class = CeremonyListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['titre', 'description', 'speaker']
    pagination_class = PostPageNumberPagination

    # how to use search or q
    def get_queryset(self, *args, **kwargs):
        queryset_list = Ceremony.objects.all().order_by('-created_at')
        query = self.request.GET.get("q")
        if query :
            queryset_list = queryset_list.filter(
                Q(description__icontains=query)|
                Q(titre__icontains=query)|
                Q(speaker__icontains=query)
                #Q(user__username__icontains=query)
            ).distinct()
        return queryset_list
