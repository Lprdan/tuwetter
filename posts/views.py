from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Like


@login_required
def home(request):
    if request.method == "POST":
        content = request.POST.get("content")

        if content:
            Post.objects.create(
                author=request.user,
                content=content
            )
            return redirect('home')

    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/home.html', {'posts': posts})


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if post.author == request.user:
        post.delete()

    return redirect('home')

@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    like = Like.objects.filter(user=request.user, post=post).first()

    if like:
        like.delete()
    else:
        Like.objects.create(user=request.user, post=post)

    return redirect('home')


@login_required
def notifications(request):
    # Busca todos os likes nos posts do usuário logado
    user_posts = Post.objects.filter(author=request.user)
    likes = Like.objects.filter(post__in=user_posts).select_related('user', 'post').order_by('-id')
    
    return render(request, 'posts/notifications.html', {'likes': likes})
