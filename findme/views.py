
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404 
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import ItemLost
from .forms import Lost
from django.contrib import messages
from django.views.generic.detail import DetailView
from .forms import ContactForm
from django.http import JsonResponse
from django.http import HttpResponse

@login_required
def itemfound(request):
    query = request.GET.get('q', '').upper()

    if query:
        # Filter found items where title starts with the provided letter
        items = ItemLost.objects.filter(title__istartswith=query, found=True)
    else:
        # No search query, return all found items
        items = ItemLost.objects.filter(found=True)

    context = {
        'items': items,
        'search_query': query  # Pass the search query to the template
    }
    return render(request, 'findme/found.html', context)

@login_required
def home(request):
    query = request.GET.get('q', '').upper()

    if query:
        # Filter items where title starts with the provided letter
        items = ItemLost.objects.filter(title__istartswith=query, found=False)
    else:
        # No search query, return all items
        items = ItemLost.objects.filter(found=False)

    context = {
        'items': items,
        'search_query': query  # Pass the search query to the template
    }
    return render(request, 'findme/home.html', context)

def contact(request):
    return render(request, 'findme/contact.html', {'title': 'contact'})

@login_required
def found(request, ItemID):
    item = get_object_or_404(ItemLost, ItemID=ItemID)
    itemlost_author = item.name
    itemfound_author = request.user

    if request.method == "POST":
        if itemlost_author != itemfound_author:
            location = request.POST.get("location")
            item.item_found_by = request.user
            item.found = True
            item.found_location = location
            item.save()

            # Create a notification message
            notification_message = (
                f"Item '{item.title}' marked as found by {itemfound_author.username}. "
                f"Found at {location}."
            )
            messages.info(request, notification_message)
        else:
            messages.info(request, "An item cannot be lost and found by the same person")

    return redirect('findme-home')


class ItemDetail(LoginRequiredMixin, DetailView):
    model = ItemLost
class ItemDetailView:
    def get(self, request, pk, *args, **kwargs):
        item = get_object_or_404(ItemLost, pk=pk)
        # Redirect to the home view if you moved the detail view code there
        return redirect('home')
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = ItemLost
    template_name = 'findme/item_form.html'
    form_class = Lost

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)
        return redirect(reverse('home'))

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ItemLost
    form_class = Lost
    template_name = 'findme/item_form.html'

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.name:
            return True
        return False

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ItemLost
    template_name = 'findme/itemdelete_form.html'
    success_url = '/'

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.name:
            return True
        return False






def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your message has been sent successfully!')
            # Process the form data
            return redirect(home)
        
    else:
        form = ContactForm()

    return render(request, 'findme/contact.html', {'form': form})

