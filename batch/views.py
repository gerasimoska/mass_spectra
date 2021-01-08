from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .helpers import scrape
from django.shortcuts import redirect
import os
import json


def search_spectra(request):
    fileList = [f for f in os.listdir(os.path.join(os.getcwd(), "media"))]
    for f in fileList:
        os.remove(os.path.join(os.getcwd(), "media", f))
    if request.method == "POST":
        filters = json.loads(request.POST.get("filters"))
        myFile = request.FILES["file"]
        fs = FileSystemStorage()
        name = fs.save(myFile.name, myFile)
        ionMode = filters.get("ion_mode")
        msType = filters.get("ms_type")
        sourceIntroduction = filters.get("source_introduction")
        instrumentTypes = filters.get("other_instrument_types")
        library = filters.get("library")
        inputType = filters.get("input_type")
        tolerance = filters.get("tolerance")
        massSpectraLibrary = filters.get("mass_spectra_library")
        scrape(
            "./media/" + str(name),
            ionMode,
            msType,
            sourceIntroduction,
            instrumentTypes,
            library,
            inputType,
            tolerance,
            massSpectraLibrary,
        )
        return HttpResponse(
            json.dumps(
                {
                    "download": "http://127.0.0.1:8000/media/"
                    + str(name).replace(".csv", "_output.csv")
                }
            )
        )
    return render(request, "batch/search.html")


def download_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="input.csv"'

    # return response
