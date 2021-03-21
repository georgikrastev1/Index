from django.shortcuts import render
import json
import pandas as pd
from Main.models import Peer_group_Financial_data, Financial_data

# Create your views here.

def home_user(request):
    chart_data_source=Peer_group_Financial_data.objects.all()
    #print(chart_data_source[0].Market_capitalization_percent)
    source_data=list(Peer_group_Financial_data.objects.values_list('created_at','Peer_group','Market_capitalization_percent'))
    print(source_data)
    t_data=list(zip(*source_data))
    print(t_data)
    exams=Peer_group_Financial_data.objects.values('created_at','Peer_group__Group_name','Market_capitalization_percent')
    transposed = {}
    for exam in exams:
        transposed.setdefault(exam['created_at'], {}).update(
            {exam['Peer_group__Group_name']: exam['Market_capitalization_percent']})

    exams_test=pd.DataFrame(list(Peer_group_Financial_data.objects.all().values('created_at','Peer_group__Group_name','Market_capitalization_percent')))
    x=exams_test.pivot(index="created_at", columns="Peer_group__Group_name", values="Market_capitalization_percent")
    print("test")
    x.reset_index(inplace=True)
    print(x["created_at"])
    y=x.values.tolist()
    print(y[0][0])

    context = {
        'array': y,
    }

    return render(request, "index-youtub61.html",context)
    #return render(request, "dashboard.html", context)