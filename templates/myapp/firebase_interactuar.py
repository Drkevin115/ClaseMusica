from django.shortcuts import render
from myapp.firebase_config import db

def contact(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    db.collection('contact_messages').document().set({
      'name': name,
      'email': email,
      'message': message
    })
    return render(request, 'myapp/contact.html', {'success': True})
  else:
    return render(request, 'myapp/contact.html')