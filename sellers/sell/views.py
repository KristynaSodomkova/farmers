from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class RegisterProducerView(View):
    def get(self, request):
        context = {
            "some_var": "something"
        }
        return render(request, "register_producer.html", context)


class ProducerDetailView(View):
    def get(self, request, producer_id):
        context = {
            "producer_id": producer_id
        }
        return render(request, "producer_detail.html", context)


class ProducersListView(View):
    def get(self, request):
        return HttpResponse("Here will be a list of producers")
