from django.shortcuts import render
from django.urls import reverse
from django.http import Http404
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CarOwner, Car
from .forms import CarOwnerForm, CarForm


def car_owner_detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist as e:
        raise Http404("Автовладельца не существует!") from e

    return render(
        request,
        "owner.html",
        {"owner": owner}
    )


def all_car_owners(request):
    car_owners = CarOwner.objects.all()
    return render(request, "all_car_owners.html", {"car_owners": car_owners})


def all_cars(request):
    cars = Car.objects.all()
    return render(request, "all_cars.html", {"cars": cars})


def car_detail(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist as e:
        raise Http404("Автомобиля не существует!") from e

    return render(request, "car_detail.html", {"car": car})


def add_car_owner(request):
    if request.method == 'POST':
        form = CarOwnerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car owner added successfully!')
        else:
            messages.error(request, 'Error adding car owner. Please check the form.')

    form = CarOwnerForm()

    return render(request, 'add_car_owner.html', {'form': form})


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Car added successfully')
        return self.request.path


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Car updated successfully')
        return self.request.path


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Car deleted successfully')
        return self.request.path
