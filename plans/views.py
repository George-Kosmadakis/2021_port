from django.shortcuts import render

# Create your views here.
def subscirption(request):
    return render(request, 'plans/subscription.html')



