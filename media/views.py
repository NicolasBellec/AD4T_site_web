from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
import os
from AD4T.settings import BASE_DIR
from media.models import Media

# Create your views here.
def mediaView(request, slug):
    file = get_object_or_404(Media, slug=slug)
    try:
        if file.permission:
            if request.user.is_authenticated:
                path_file = os.path.join(BASE_DIR, 'media/'+str(file.path))
                content_type_file = file.content_type
                return FileResponse(open(path_file, 'rb'), content_type=content_type_file)
            else:
                raise Http404()
        else:
            path_file = os.path.join(BASE_DIR, 'media/'+str(file.path))
            content_type_file = file.content_type
            return FileResponse(open(path_file, 'rb'), content_type=content_type_file)

    except FileNotFoundError:
        raise Http404()
