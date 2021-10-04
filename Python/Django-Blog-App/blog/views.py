from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import POST
from .forms import PostForm
from django.contrib.auth.decorators import login_required



def blogPage(request):
    posts = POST.objects.all()



    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)

def blogContent(request, pk):
    posts = POST.objects.all()
    content = posts.get(id=pk)
    print(content)



    context = {'content': content}
    return render(request, 'blog/blog-content.html', context)


@login_required(login_url='login')
def createPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('blog')

    context = {'form': form}
    return render(request, 'blog/create-post.html', context)


@login_required(login_url='login')
def updatePost(request, pk):
    posts = POST.objects.all()

    content = posts.get(id=pk)

    form = PostForm(instance=content)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=content)

        if form.is_valid():
            form.save()

            return redirect('blog')

    context = {'form': form}
    return render(request, 'blog/update-post.html', context)


@login_required(login_url='login')
def deletePost(request, pk):
    posts = POST.objects.all()

    content = posts.get(id=pk)


    if request.method == 'POST':
        content.delete()
        return redirect("blog")

    context = {'content': content}
    return render(request, 'blog/delete-post.html', context)
