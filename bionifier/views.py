from django.shortcuts import render

from bionifier.utils.bionic import BionicCheaper

# Create your views here.
def index(request):
    context = {}
    bc = BionicCheaper(BionicCheaper.SAMPLE, "<b>", "</b>")

    if request.method == "POST":
        bc.og_text = request.POST.get("input").strip()

    context["input_text"], context["output_text"] = bc.og_text, bc.bc_text

    return render(request, "bionifier/index.html", context)
