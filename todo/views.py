from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bucket
from .forms import BucketForm

def bucket_list(request):
    buckets = Bucket.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'todo/bucket_list.html', {'buckets':buckets})

def bucket_detail(request, pk):
    bucket = get_object_or_404(Bucket, pk=pk)
    return render(request, 'todo/bucket_detail.html', {'bucket': bucket})

def bucket_new(request):
    if request.method == "POST":
       form = BucketForm(request.POST)
       if form.is_valid():
           bucket = form.save(commit=False)
           bucket.author = request.user
           bucket.created_date = timezone.now()
           bucket.save()
           return redirect('bucket_detail', pk=bucket.pk)
    else:
        form = BucketForm()
    return render(request, 'todo/bucket_edit.html', {'form': form})

def bucket_edit(request, pk):
    bucket = get_object_or_404(Bucket, pk=pk)
    if request.method == "POST":
        form = BucketForm(request.POST, instance=bucket)
        if form.is_valid():
            bucket = form.save(commit=False)
            bucket.author = request.user
            bucket.created_date = timezone.now()
            bucket.save()
            return redirect('bucket_detail', pk=bucket.pk)
    else:
        form = BucketForm(instance=bucket)
    return render(request, 'todo/bucket_edit.html', {'form': form})
