from django.shortcuts import render
def churn_rate(request):
    ic= float(request.POST.get('Initial_Cust', '0'))
    pc=float(request.POST.get('Present_Cust', '0'))
    churn = ic/pc if request.method=='POST' else 0
    print("Initial Customer =",ic)
    print("Present Customer =",pc)
    print("Churn Rate =",churn)
    return render(request, 'shanu/math.html',{'ic': ic, 'pc': pc, 'churn': churn})