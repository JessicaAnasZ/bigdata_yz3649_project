from django.http import HttpResponse
from django.shortcuts import render
import pandas_gbq
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('/Users/zhangyixiao/Downloads/root-augury-317503-cba05307f1d5.json')


def connection(request):
    pandas_gbq.context.credentials = credentials
    pandas_gbq.context.project = "root-augury-317503"

    data = {'n':'no', 'e':'no', 'error':'false'}


    if request.POST:
        category = request.POST['category']
        try:
            SQL1 = " Select node from root-augury-317503.bigdata_project_yz3649.nodes_table_cs_{}".format(category)
            df1 = pandas_gbq.read_gbq(SQL1)

            SQL2 = " Select source, target from root-augury-317503.bigdata_project_yz3649.edges_table_cs_{}".format(category)
            df2 = pandas_gbq.read_gbq(SQL2)

            # TODO: Popoluate this dict as instructed below
            data = {'n':list(df1.T.to_dict().values()),'e':list(df2.T.to_dict().values())}
            
            
        except:
            data['error'] = 'true'

    return render(request, 'connection.html', data)
    
