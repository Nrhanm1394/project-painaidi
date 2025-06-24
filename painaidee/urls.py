from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('ภาคของไทย',views.region,name='region'),
    path('หมวดเที่ยว',views.group,name='group'),
    path('เกี่ยวกับฉัน',views.q,name='q'),
    path('signin',views.signin,name='signin'),
    path('contact',views.contact,name='contact'),

    path('ภาคกลาง',views.central,name='central'),
    path('บ้านตาหรั่ง',views.c1,name='c1'),
    path('สวนหลังบ้าน',views.c2,name='c2'),
    path('โรงงานกระดาษ',views.c3,name='c3'),
    path('หาดเจ้าสำราญ',views.c4,name='c4'),
    path('ริมธารา สวนผึ้ง',views.c5,name='c5'),
   
    path('นครนายก ตอนที่ 1',views.c7,name='c7'),

 
    path('นครนายก ตอนที่ 3',views.c11,name='c11'),
    path('น้ำตกเอราวัญ',views.c12,name='c12'),

    path('ภาคเหนือ',views.north,name='north'),
   
    path('ภูเขาเดียวดาย',views.n3,name='n3'),
    path('ปางอุ๋ง',views.n4,name='n4'),
    path('บ้านจ่าโบ่',views.n5,name='n5'),
    path('ดอยอ่างขาง',views.n6,name='n6'),
    
    path('ภาคอีสาน',views.northeast,name='northeast'),
    path('วัดภูทอก',views.ne1,name='ne1'),
    path('วัดถ้ำแสงธรรม',views.ne2,name='ne2'),
    path('ภูกระดึง',views.ne3,name='ne3'),

    path('ภาคใต้',views.south,name='south'),
    path('เชี่ยวหลาน',views.s1,name='s1'),
    path('ท่าปอม คลองสองน้ำ',views.s2,name='s2'),
    path('หาดถ้ำพระนาง',views.s3,name='s3'),
    path('ปราณบุรี',views.s4,name='s4'),
    path('Memory House Cafe Huahin',views.s5,name='s5'),
    path('ควนนกเต้น',views.s6,name='s6'),

    path('camping',views.camping,name='camping'),
    path('nature',views.nature,name='nature'),
    path('sea',views.sea,name='sea'),
    path('photograph',views.photograph,name='photograph'),
]
