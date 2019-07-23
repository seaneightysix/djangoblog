from django.shortcuts import render
from django.http import Http404
from myblog.models import Genre
from myblog.models import Post

def list_view(request):
    context = {'posts': Post.objects.all(),
    		   'genres': Genre.objects.all()
    		  }
    return render(request, 'myblog/list.html', context)

def detail_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    
    except Post.DoesNotExist:
    	raise Http404

    context = {'post': post}
    return render(request, 'myblog/detail.html', context)

def get_genres(request, genre):
	try:
		genre_pk = Genre.objects.get(genre=genre)
		results = Post.objects.all()
		results = results.filter(genre = genre_pk)
		
	except Post.DoesNotExist:
    	 raise Http404	

	context = {'results': results,
			   'genre': genre
			  }
	return render(request, 'myblog/genre_list.html', context)