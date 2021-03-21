from django.shortcuts import render, HttpResponse
import yfinance as yf
from .models import Companies, Financial_data, Peer_group_Financial_data, Peer_group_lists
from datetime import datetime, timedelta,timezone
from apscheduler.schedulers.background import BackgroundScheduler
from forex_python.converter import CurrencyRates
from tablib import Dataset



# Create your views here.


def home(request):
    # fix for yfinance: https://github.com/ranaroussi/yfinance/issues/208
    #https://datatables.net/
    # - ANTA.PA: No data found for this date range, symbol may be delisted
    # z=["MYM.F","MERC","METSA.HE","3864.T","MNDI.L","MPT.JO","NPK.JO","2689.HK","3861.T","PKG","RFP","RROS.ST","SAP.JO","ESSITY-B.ST","SEE","SKG.L","STERV.HE","SUZB3.SA","UPM.HE","VRTV","VRS","WRK","NVG.LS","KPT.TO","CFX.TO","SON","GLT","ANTA.PA","RANI3.SA","3880.T","3865.T","SCA-B.ST","HOLM-B.ST","3863.T","HUH1V.HE","8113.T","3941.T","HAP.TA","ENC.MC","INKP.JK","TKIM.JK","ARP.ST","1812.HK","BALLARPUR.BO","FASW.JK","1044.HK","BCC","BRG-B.ST","PCH","CFF.TO","LPX","SONI.LS","WY","WFT.TO","CFP.TO","IFP.TO","OSB.TO","SJ.TO","WEF.TO"]
    z=['^GSPC']
    # for i in z:
    #     print(i)
    #     msft = yf.Ticker(i)
    #     x = msft.history(period="2020-09-17")
    #     print(msft.info)

    #get price and convert
    list_comopanies = Companies.objects.values_list("Stock_code", flat=True)
    today_date=datetime.today().strftime('%Y-%m-%d')
    x = len(list_comopanies)
    c = CurrencyRates()
    for i in range(0,x):
        msft = yf.Ticker(list_comopanies[i])
        try:
            # x = msft.history(start="2020-09-02",
            #                  end="2020-10-02")  # works for the last day: yesterday - will need to load the rest of the data
            x=msft.history(start=today_date, end=today_date) #gets data from the previous day = today - 1 (example on the 12th it will get data from 11th)
            original_price=x.iloc[0][0] # we are using open price
            currency_comopanies = Companies.objects.filter(Stock_code=list_comopanies[i]).values_list("Fx_company", flat=True)
            if currency_comopanies!="EUR":
                new_price=c.convert(currency_comopanies[0], 'EUR', float(original_price))
            elif currency_comopanies=="EUR":
                new_price=original_price
            market_cap=msft.info["marketCap"]
            shares_number=market_cap/original_price
            Market_capitalization=new_price*shares_number

            Financial_data.objects.create(company_id=Companies.objects.filter(Stock_code=list_comopanies[i]).first(),
                market_capitalization_original = market_cap,
                market_capitalization_euro = Market_capitalization,
                share_price_original = original_price, share_price_euro = new_price,
                shares_number = shares_number)

        except:
            yesterday_date=datetime.today()- timedelta(days=1)
            x=Financial_data.objects.filter(created_at__date=yesterday_date,
                                            company_id=Companies.objects.filter(Stock_code=list_comopanies[i]).get())
            for object in x:
                Financial_data.objects.create(
                    company_id=Companies.objects.filter(Stock_code=list_comopanies[i]).first(),
                    market_capitalization_original=object.market_capitalization_original,
                    market_capitalization_euro=object.market_capitalization_euro,
                    share_price_original=object.share_price_original, share_price_euro=object.share_price_euro,
                    shares_number=object.shares_number)

    all_groups=Peer_group_lists.objects.all()
    for i in all_groups:
        x=i.id
        #sql_r=Financial_data.objects.raw('Select * FROM Main_Financial_data a WHERE DATE(a."created_at")=%s',[test])
        #sql_r = Financial_data.objects.raw('SELECT * FROM Main_Financial_data a WHERE DATE(a."created_at")=%s',[test])f
        sql_r=Financial_data.objects.filter(created_at__date__gte=today_date, company_id__Peer_group=x)
        calculated_group_market_cap=0
        for i in sql_r:
             company_calculated_current_market_cap=i.share_price_euro*i.shares_number
             calculated_group_market_cap=calculated_group_market_cap+company_calculated_current_market_cap
        base_market_record=Peer_group_Financial_data.objects.filter(Peer_group=x).order_by('created_at').first()
        base_market_capitalization=base_market_record.Market_capitalization
        print(base_market_capitalization)
        group_market_cap_rel=calculated_group_market_cap/base_market_capitalization
        print(group_market_cap_rel)
        Peer_group_Financial_data.objects.create(Peer_group=Peer_group_lists.objects.get(pk=x), Market_capitalization=calculated_group_market_cap,
                                                     Market_capitalization_percent=group_market_cap_rel)
    return render(request,"index-youtub3.html",)

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

# def test():
#     msft = yf.Ticker("ALTR.LS")
#     x=msft.info["marketCap"]
#     print("test:",msft)
#     print("test:",msft.history(start="2020-08-27", end="2020-08-27"))

# scheduler = BackgroundScheduler()
# scheduler.add_job(test, 'interval', seconds=5)
# scheduler.start()

