from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm
from .serializers import EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def  register(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect(reverse_lazy('login'))
    else:
        form= UserCreationForm()
    return render(request, 'register.html', {'form': form})



class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event_form.html'
    success_url = reverse_lazy('event_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user  # Assign the current user as the creator
        return super().form_valid(form)

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event_form.html'
    success_url = reverse_lazy('event_list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = '/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')
    
    
class EventDetailAPIView(APIView):
    def get(self, request, pk, format=None):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.status == 'Completed' or event.status == 'Ongoing':
        return HttpResponse("You can't register for this event.", status=400)
    if event.users.count() >= event.capacity:
        return HttpResponse("Sorry, this event is full.", status=400)

    event.users.add(request.user)
    return redirect('event_list')