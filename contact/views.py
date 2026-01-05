from django.shortcuts import render, redirect
from .forms import TextUploadForm
from .models import TextUpload

def upload_text(request):
    if request.method == 'POST':
        form = TextUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TextUploadForm()
    return render(request, 'contact/form.html', {'form': form})

def success(request):
    return render(request, 'contact/success.html')

def submissions(request):
    texts = TextUpload.objects.all()
    return render(request, 'contact/submissions.html', {'texts': texts})
