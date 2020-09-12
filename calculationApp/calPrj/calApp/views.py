from django.shortcuts import render, redirect
from calApp.models import Data
import math

def index(request):
	data = Data.objects.last() #Getting only last value from the Data model
	r1 = (float(data.pod)-2*(float(data.pwt)))/2 #Pipe Inside Radius
	r2 = (float(data.pod))/2 #Pipe Outside Radius
	r3 = r2+float(data.fbet)/2 #Outer Radius Of Coating
	tpod = r3*2 #Total Pipeline Outside Diameter
	pwpu = math.pi*(((r2*r2))-((r1*r1)))/144*float(data.pd) #Pipe Weight per Unit Length in Air (lb/ft)
	c1wpu = math.pi*((r3*r3)-(r2*r2))/144*float(data.fbed) #Coating 1 Wt. per Unit Length in Air (lb/ft)
	cwpu = math.pi*(r1*r1)/144*float(data.ad) #Contents Wt. Per Unit Length in Air (lb/ft)
	twpu = (pwpu + c1wpu + cwpu) #Total Weight per Unit Length in Air (lb/ft)
	bfpu = math.pi*(r3*r3)/144*float(data.swd) #Buoyant Force per Unit Length (lb/ft)
	swul = (twpu - bfpu) #Submerged Weight/Unit Length (lb/ft)
	ssg = (twpu / bfpu) #Subm. Specific Gravity with respect to S.W.

	context = {'r1':r1, 'r2':r2, 'r3':r3, 'tpod':tpod, 'pwpu':pwpu, 
						'c1wpu':c1wpu, 'cwpu':cwpu, 'twpu':twpu, 'bfpu':bfpu, 'swul':swul, 'ssg':ssg}
	return render(request, "index.html", context)

def show(request):
	if request.method == "POST":
		pod = request.POST.get('pod') #Pipe Outside Diameter(OD)
		pwt = request.POST.get('pwt') #Pipe Wall Thickness(t)
		pd = request.POST.get('pd') #Pipe Density
		ca = request.POST.get('ca') #Corrosion Allowlance
		fbet = request.POST.get('fbet') #FBE (Thickness)
		fbed = request.POST.get('fbed') #FBE (Density)
		ad = request.POST.get('ad') #Installation Empty (Air Density)
		wd = request.POST.get('wd') #Flooded (Water Density)
		swd = request.POST.get('swd') #Hydrotest (Sea Water Density)
		data = Data(pod=pod, pwt=pwt, pd=pd, ca=ca, fbet=fbet, fbed=fbed, ad=ad, wd=wd, swd=swd)
		data.save() #All inputs are saved in Data model
		return redirect("index")