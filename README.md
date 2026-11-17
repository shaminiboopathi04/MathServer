# Ex.03 Design a Website for Server Side Processing
## Date:

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:

math.html

```
<html>
    <head>
        <title>Calculator</title>
    </head>
    <body>
        <h1 align="center">Churn Rate Calculator</h1>
        <h2 align="center">shamini (26016698)</h2>
        <form method="POST">
            {%csrf_token%}
            <label>Initial Customer:</label>
            <input type="text" value="{{ic}}" name="Initial_Cust"><br><br>
            <label>Present Customer:</label>
            <input type="text" value="{{pc}}" name="Present_Cust"><br><br>
            <input type="submit" value="Calculate"><br><br>
            <label>Churn Rate:</label>
            <input type="text" value="{{churn}}"><br><br>
        </form>
    </body>
</html>
```
views.py

```
from django.shortcuts import render
def churn_rate(request):
    ic= float(request.POST.get('Initial_Cust', '0'))
    pc=float(request.POST.get('Present_Cust', '0'))
    churn = ic/pc if request.method=='POST' else 0
    print("Initial Customer =",ic)
    print("Present Customer =",pc)
    print("Churn Rate =",churn)
    return render(request, 'shanu/math.html',{'ic': ic, 'pc': pc, 'churn': churn})
```
urls.py

```
from django.contrib import admin
from django.urls import path
from shanu import views

urlpatterns = [path('', views.churn_rate, name='churn_rate'),]
```




## OUTPUT - SERVER SIDE:

![alt text](<Screenshot 2026-11-17 133056.png>)

## OUTPUT - WEBPAGE:

![alt text](<Screenshot (141).png>)

## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
