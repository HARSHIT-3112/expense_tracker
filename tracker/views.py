from django.shortcuts import render,redirect
from django.contrib import messages
from tracker.models import Transaction

# Create your views here.
def index(request):
    if request.method == "POST":
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        
        print(description, amount)
        if description is None:
           messages.info(request,"description can not be done")
           return redirect("/")
    

        try:
            amount = float(amount)  # Try to convert to float
        except ValueError:
            messages.info(request, "Amount should be a valid number.")
            return redirect("/")
        
        Transaction.objects.create(
            description=description,
            amount=amount,
            )
        
        return redirect("/")

    return render(request, "index.html")