from django.shortcuts import render, redirect
from bson.objectid import ObjectId
from . import dbcon
from datetime import datetime

def create_registration(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        participant_name = request.POST.get('participant_name')
        participant_email = request.POST.get('participant_email')
        registration_date = request.POST.get('registration_date')
        college_name = request.POST.get('college_name')



        dbcon.col.insert_one({
            'event_name': event_name,
            'participant_name': participant_name,
            'participant_email': participant_email,
            'registration_date': registration_date,
            'college_name': college_name,
        })
        return redirect('read_registrations')

    return render(request, 'create.html')


def read_registrations(request):
    registrations = list(dbcon.col.find())
    for reg in registrations:
        reg['id'] = str(reg['_id'])
    return render(request, 'read.html', {'registrations': registrations})


def update_registration(request, reg_id):
    reg = dbcon.col.find_one({'_id': ObjectId(reg_id)})
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        participant_name = request.POST.get('participant_name')
        participant_email = request.POST.get('participant_email')
        registration_date = request.POST.get('registration_date')
        college_name = request.POST.get('college_name')

        dbcon.col.update_one(
            {'_id': ObjectId(reg_id)},
            {'$set': {
                'event_name': event_name,
                'participant_name': participant_name,
                'participant_email': participant_email,
                'registration_date': registration_date,
                'college_name': college_name,
            }}
        )
        return redirect('read_registrations')

    return render(request, 'update.html', {'registration': reg})


def delete_registration(request, reg_id):
    dbcon.col.delete_one({'_id': ObjectId(reg_id)})
    return redirect('read_registrations')
