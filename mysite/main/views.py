from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_POST


def index(request):
    return render(request, "main/index.html")


@require_POST
def recieve(request):
    from .models import create
    responce = create(
        request.POST["email"],
        request.POST["phone"],
        request.POST["company"],
        request.POST["contactName"],
        request.POST["projectName"],
        request.POST["description"],
        request.POST["goals"],
        request.POST["price"],
        request.POST["projectLength"],
        request.POST["criteria"],
        request.POST["timeframe"],
        request.POST["target"],
        request.POST["technologies"],
        request.POST["mockup"],
        request.POST["comments"])
    return render(request, "main/result.html", context={"br": responce})