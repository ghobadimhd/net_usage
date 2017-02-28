from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from datetime import date
from vnstat import vnstat

DEFUALT_REMOTE_PORT = 1234

def net_usage(request, interface=None, traffic_set='days', from_date=date(1, 1, 1), to_date=date.today()):
	
	if request.method == 'POST':
		remote_address = request.POST.get('remote_address','')
		remote_port = int(request.POST.get('remote_port',-1))
		remote_port = DEFUALT_REMOTE_PORT if remote_port == -1 else remote_port
		# check for valid address
		data = vnstat.remote_read(remote_address, remote_port)
	else:
		data = vnstat.read()
	vnstat.format_data(data)
	vnstat.convert_unit(data)
	interfaces = vnstat.get(data, traffic_set, interface, from_date, to_date)
	context = Context({'interfaces':interfaces})
	return render_to_response('net_usage.html', context)