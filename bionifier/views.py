from django.shortcuts import render

from bionifier.utils.bionic import BionicCheaper

# Create your views here.
def index(request):
    context = {}
    context["input_placeholder"], context["output_placeholder"] = BionicCheaper.sample()

    return render(request, "index.html", context)
