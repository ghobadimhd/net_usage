"""mointor views"""
from datetime import date
from django.http import Http404
from django.template import Context
from django.shortcuts import render_to_response
from vnstat import vnstat

DEFUALT_REMOTE_PORT = 1234

def net_usage(request, interface=None, traffic_set='days',
              from_date=date(1, 1, 1), to_date=date.today()):
    """read data from vnstat from localhost or remote and represent """
    if request.method == 'GET':

        remote_address = request.GET.get('remote_address', '')
        remote_port = int(request.GET.get('remote_port', 1234))
        if remote_address:
            # check for valid address
            data = vnstat.remote_read(remote_address, remote_port)
        else:
            data = vnstat.read()
        vnstat.format_data(data)
        vnstat.convert_unit(data)
        interfaces = vnstat.get(data, traffic_set, interface, from_date, to_date)
        context = Context({'interfaces':interfaces})
        return render_to_response('net_usage.html', context)
    raise Http404
