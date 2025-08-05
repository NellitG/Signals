from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/contact.html')
    else:
        form = ContactForm()

    return render(request, 'accounts/contact.html', {'form': form})