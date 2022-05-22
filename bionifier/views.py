from django.shortcuts import render

from bionifier.utils.bionic import BionicCheaper

# Create your views here.
def index(request):
    context = {}

    bc = BionicCheaper(BionicCheaper.SAMPLE, "<b>", "</b>")

    context["input_placeholder"], context["output_placeholder"] = bc.og_text, bc.bc_text

    return render(request, "bionifier/index.html", context)
