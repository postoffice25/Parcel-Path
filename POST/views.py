import email
from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from .import models
from .models import USER,Feedback,postoffice,postman,stamp,postmodel,Reschedule
from django.contrib.auth.hashers import make_password
def index(request):
    return render(request,'index.html')
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import USER
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import USER
def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincodeno')
        district = request.POST.get('districtname')
        image = request.FILES.get('image')  
        if USER.objects.filter(email=email).exists():
            return render(request, 'userreg.html', {'error': 'Email already in use'})
        hashed_password = make_password(password)
        user = USER(
            username=name,
            password=hashed_password,
            email=email,
            address=address,
            phone=phone,
            pincodeno=pincode,
            districtname=district,
            image=image, 
            status='applied'
        )
        user.save()
        subject = "New User Registration"
        message = f"A new user has registered with the following details:\n\n" \
                  f"Username: {name}\n" \
                  f"Email: {email}\n" \
                  f"Address: {address}\n" \
                  f"Phone: {phone}\n" \
                  f"Pincode: {pincode}\n" \
                  f"District: {district}\n\n" \
                  f"Please review the registration details."
        from_email = settings.DEFAULT_FROM_EMAIL  
        recipient_list = ['jagadeeshnandana805@gmail.com']  
        send_mail(subject, message, from_email, recipient_list)
        return redirect('login')  
    return render(request, 'userreg.html')
from django.contrib.auth.hashers import check_password
from .models import USER
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import USER
from django.shortcuts import render, redirect
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = USER.objects.get(email=email)
        except USER.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
        if check_password(password, user.password):  
            request.session['email'] = user.email
            if user.status == 'approved':
                next_page = request.GET.get('next', 'home')
                return redirect(next_page)
            else:
                return render(request, 'login.html', {'error':'Your account is not yet approved. Please wait until the admin approves your registration.'})
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')
def home(request):
    return render(request,'home.html')
def logout(request):
    request.session.flush()
    return redirect('index')
def user_parcels(request):
        semail=request.session['email']
        user=USER.objects.get(email=semail)
        parcels = postmodel.objects.filter(receiver_email=user.email)  
        return render(request, 'user_parcels.html', {'parcels': parcels}) 
def parcel_detail(request, id):
    parcel = get_object_or_404(postmodel,id=id)
    return render(request, 'parcel_detail.html', {'parcel': parcel})  
def posthome(request):
    return render(request,'posthome.html')
def postman_profile(request):
    semail=request.session['email']
    postman=models.postman.objects.get(email=semail)
    return render(request,'postman_profile.html',{'postman':postman})
def postman_profile_delete(request,pid):
    postman=models.postman.objects.get(id=pid)
    postman.delete()
    return redirect('index')
def postman_profile_edit(request, pid):
    postman = models.postman.objects.get(id=pid)
    if request.method == 'POST':
        addparcel2 = request.POST.get('name')
        postman.age = request.POST.get('age')
        postman.gender = request.POST.get('gender')
        postman.address = request.POST.get('address')
        postman.phone = request.POST.get('phone')
        postman.email = request.POST.get('email') 
        if request.FILES.get('image'):
            postman.image = request.FILES['image'] 
        postman.save()
        return redirect('postman_profile') 
    return render(request, 'postman_profile_edit.html', {'postman': postman})
def userlist(request):
    users = USER.objects.all().order_by('pincodeno')
    return render(request, 'userlist.html', {'user': users})
def userlist2(request):
    user=USER.objects.all()
    return render(request,'userlist2.html',{'user':user})
def deleteuser(request,did):
    d=USER.objects.get(id=did)
    d.delete()
    return redirect('userlist')
def deleteuser2(request,did):
    d=USER.objects.get(id=did)
    d.delete()
    return redirect('userlist2')
def profile(request):
    if 'email' in request.session:
        semail = request.session['email']
        try:
            user = USER.objects.get(email=semail)
        except USER.DoesNotExist:
            alert = "<script> alert('User not found.'); window.location.href='/login/'; </script>"
            return HttpResponse(alert)
    else:
        alert = "<script> alert('Email not found in session. Please log in.'); window.location.href='/login/'; </script>"
        return HttpResponse(alert)
    return render(request, 'profile.html', {'user': user})
from django.contrib.auth.hashers import make_password
def editprofile(request):
    email = request.session.get('email')
    if email:
        user = USER.objects.get(email=email)
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            email = request.POST.get('email')  
            pincodeno = request.POST.get('pincodeno')
            districtname = request.POST.get('districtname')
            profile_pic = request.FILES.get('profile_pic')
            if password:
                user.password = make_password(password)
            user.username = username
            user.phone = phone
            user.address = address
            user.email = email
            user.pincodeno = pincodeno
            user.districtname = districtname
            if profile_pic:
                user.image = profile_pic
            user.save()
            request.session['email'] = user.email
            return redirect('profile')
        return render(request, 'editprofile.html', {'user': user})
    else:
        return redirect('login')
def adminlogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        u='admin@gmail.com'
        p='admin'
        if email==u:
            if password==p:
                return redirect('adminhome')
    return render(request,'adminlogin.html')
def adminhome(request):
    return render(request,'adminhome.html')
def feedback_view(request):
    if request.method == "POST":
        feedback_text = request.POST.get('feedback_text')
        rating = request.POST.get('rating')
        if not feedback_text or not rating:
            alert_message = "<script>alert('Please fill in all required fields.'); window.location.href='/feedback_rate';</script>"
            return HttpResponse(alert_message)
        try:
            rating = int(rating)
            if rating not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid rating value")
        except (ValueError, TypeError):
            alert_message = "<script>alert('Invalid rating value. Please select a valid rating.'); window.location.href='/feedback_rate';</script>"
            return HttpResponse(alert_message)
        feedback=Feedback(
            feedback_text=feedback_text,
            rating=rating
        )
        feedback.save()
        return redirect('feedback_success')
    else:
        return render(request,'feedback_rate.html')
def feedback_success(request):
    return render(request,'feedback_success.html')
def feedbacklist(request):
    u=Feedback.objects.all()
    return render(request,'feedbacklist.html',{'Feedback':u})
def deletefeedback(request,id):
    d=Feedback.objects.get(id=id)
    d.delete()
    return redirect('feedbacklist')
def postofficereg(request):
    if request.method == 'POST':
        postoffice_id = request.POST.get('postoffice_id')
        max_postoffice_id = postoffice.objects.all().order_by('-postoffice_id').first()
        if max_postoffice_id:
            postoffice_id = int(max_postoffice_id.postoffice_id) + 1
        else:
            postoffice_id = 10000 
        postoffice_name = request.POST.get('postoffice_name')
        image = request.FILES.get('image')
        district = request.POST.get('district')
        description = request.POST.get('description')
        stationmaster = request.POST.get('stationmaster')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        postoffice.objects.create(
            postoffice_id=postoffice_id,
            postoffice_name=postoffice_name,
            image=image,
            district=district,
            description=description,
            stationmaster=stationmaster,
            contact=contact,
            email=email,
        )
        return redirect('adminhome')
    return render(request, 'postofficereg.html')
def postmanreg(request):
    if request.method == 'POST':
        postman_id = request.POST.get('postman_id')
        max_postman_id = postman.objects.all().order_by('-postman_id').first()
        if max_postman_id:
            postman_id = int(max_postman_id.postman_id) + 1
        else:
            postman_id = 10000  
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        image=request.FILES.get('image')
        postoffice_name = request.POST.get('postoffice_name')
        password = request.POST.get('password')
        status = request.POST.get('status')
        if postman.objects.filter(email=email).exists():
            return render(request,'postmanreg.html',{'error':'email already in use'})
        postman(
            postman_id=postman_id,
            name=name,
            age=age,
            gender=gender,
            address=address,
            image=image,
            phone=phone,
            email=email,
            postoffice_name=postoffice_name,
            password=password,
            status=status
        ).save()
        return redirect('adminhome')
    postoffices = postoffice.objects.all()
    print(postoffices)
    return render(request, 'postmanreg.html', {'postoffices': postoffices})
def postmanlist(request):
    a=postman.objects.all()
    return render(request,'postmanlist.html',{'postman':a})
def postmanlist2(request):
    postoffices = postoffice.objects.all()
    selected_postoffice = request.GET.get('postoffice_name', None)
    if selected_postoffice:
        postmen = postman.objects.filter(postoffice_name=selected_postoffice)
    else:
        postmen = None 
    return render(request, 'postmanlist2.html', {
        'postoffices': postoffices,
        'postmen': postmen,
        'selected_postoffice': selected_postoffice,
    })
def postmanlist3(request):
    postoffices = postoffice.objects.all()
    selected_postoffice = request.GET.get('postoffice_name', None)
    if selected_postoffice:
        postmen = postman.objects.filter(postoffice_name=selected_postoffice)
    else:
        postmen = None  
    return render(request, 'postmanlist3.html', {
        'postoffices': postoffices,
        'postmen': postmen,
        'selected_postoffice': selected_postoffice,
    })    
def deletepostman(request,id):
    a=postman.objects.get(id=id)
    a.delete()
    return redirect('postmanlist')
def edit_postman(request, id):
    postmen = get_object_or_404(postman, id=id)
    if request.method == 'POST':
        postmen.postman_id = request.POST.get('postman_id')
        postmen.name = request.POST.get('name')
        postmen.age = request.POST.get('age')
        postmen.gender = request.POST.get('gender')
        postmen.address = request.POST.get('address')
        postmen.phone = request.POST.get('phone')
        postmen.email = request.POST.get('email')
        postmen.postoffice_name = request.POST.get('postoffice_name')
        postmen.password = request.POST.get('password')
        postmen.status = request.POST.get('status')
        postmen.save()
        return redirect('adminhome') 
    else:
        postoffices = postoffice.objects.all()
        return render(request, 'editpostman.html', {'postman': postmen, 'postoffices': postoffices})
def addparcel(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        sendername = request.POST.get('sendername')
        sender_address = request.POST.get('sender_address')
        sender_contact = request.POST.get('sender_contact')
        receivername = request.POST.get('receivername')
        receiver_address = request.POST.get('receiver_address')
        receiver_postoffice = request.POST.get('receiver_postoffice')
        receiver_contact = request.POST.get('receiver_contact')
        posted_date = request.POST.get('posted_date')
        remarks = request.POST.get('remarks')
        status = request.POST.get('status')
        weight = request.POST.get('weight')
        kms = request.POST.get('kms')
        price = request.POST.get('price')
        screenshot = request.FILES.get('screenshot')
        postman_name = request.POST.get('postman_name')
        parcel=postmodel(
            post_id=post_id,
            postoffice="mainpostoffice",
            sendername=sendername,
            sender_address=sender_address,
            sender_contact=sender_contact,
            receivername=receivername,
            receiver_address=receiver_address,
            receiver_postoffice=receiver_postoffice,
            receiver_contact=receiver_contact,
            posted_date=posted_date,
            remarks=remarks,
            status=status,
            weight=weight,
            kms=kms,
            price=price,
            screenshot=screenshot,
            postman_name=postman_name
        )
        parcel.save()
        parcel_id = parcel.parcel_id
        return render(request, 'addparcel.html', {
            'postoffices': postoffice.objects.all(),
            'p': postman.objects.all(),
            'parcel_id': parcel_id, 
            'message': "Parcel added successfully!"
        })
    postoffices = postoffice.objects.all()
    p = postman.objects.all()
    return render(request, 'addparcel.html', {'postoffices': postoffices, 'p': p})
def parcellist(request):
    p=postmodel.objects.all()
    return render(request,'parcellist.html',{'parcel':p})
def deleteparcel(request,id):
    p=postmodel.objects.get(id=id)
    p.delete()
    return redirect('parcellist')
def edit_parcel(request, id):
    parcellist= get_object_or_404(postmodel, id=id)
    if request.method == 'POST':
        parcellist.post_id = request.POST.get('post_id')
        parcellist.sendername = request.POST.get('sendername')
        parcellist.sender_address = request.POST.get('sender_address')
        parcellist.sender_contact = request.POST.get('sender_contact')
        parcellist.receivername = request.POST.get('receivername')
        parcellist.receiver_address = request.POST.get('receiver_address')
        parcellist.receiver_postoffice = request.POST.get('receiver_postoffice')
        parcellist.receiver_contact = request.POST.get('receiver_contact')
        parcellist.posted_date = request.POST.get('posted_date')
        parcellist.remarks = request.POST.get('remarks')
        parcellist.weight = request.POST.get('weight')
        parcellist.kms = request.POST.get('kms')
        parcellist.price = request.POST.get('price')
        parcellist.postman_name = request.POST.get('postman_name')
        parcellist.save()
        return redirect('parcellist')  
    else:
        parcel = postmodel.objects.all()
        return render(request, 'editparcel.html', {'parcellist': parcellist, 'parcel': parcel   })
def createstamp(request):
    if request.method=='POST':
        cost=request.POST.get('cost')
        weight=request.POST.get('weight')
        stamp_name=request.POST.get('stamp_name')
        image=request.FILES.get('image')
        description=request.POST.get('description')
        release_date=request.POST.get('release_date')
        status=request.POST.get('status')
        stamp(cost=cost,
              weight=weight,
              stamp_name=stamp_name,
              image=image,
              description=description,
              release_date=release_date,
              status=status).save()
        return redirect('adminhome')
    return render(request,'stamp.html')
def stamplist(request):
    u=stamp.objects.all()
    return render(request,'stamplist.html',{'s':u})
def deletestamp(request,id):
    d=stamp.objects.get(id=id)
    d.delete()
    return redirect('stamplist')
def edit_stamp(request, id):
    stamplist= get_object_or_404(stamp, id=id)
    if request.method == 'POST':
        stamplist.stamp_name = request.POST.get('stamp_name')
        stamplist.cost = request.POST.get('cost')
        stamplist.weight = request.POST.get('weight')
        stamplist.description = request.POST.get('description')
        stamplist.release_date = request.POST.get('release_date')
        stamplist.status = request.POST.get('status')
        stamplist.save()
        return redirect('stamplist')  
    else:
        stamps = stamp.objects.all()
        return render(request, 'editstamp.html', {'stamp': stamplist, 'stamps': stamps   })  
def postofficelist(request):
    a=postoffice.objects.all()
    return render(request,'postofficelist.html',{'postoffice':a})
from django.shortcuts import render
from .models import postoffice
def postofficelist2(request):
     a=postoffice.objects.all()
     return render(request,'postofficelist2.html',{'postoffices':a})
def postofficelist3(request):
    a=postoffice.objects.all()
    return render(request,'postofficelist3.html',{'postoffice':a})
def deletepostoffice(request,id):
    a=postoffice.objects.get(id=id)
    a.delete()
    return redirect('postofficelist')
def edit_postoffice(request, id):
    post = get_object_or_404(postoffice, id=id)
    if request.method == 'POST':
        post.postoffice_id = request.POST.get('postoffice_id')
        post.postoffice_name = request.POST.get('postoffice_name')
        post.district = request.POST.get('district')
        post.image=request.POST.get('image')
        post.description = request.POST.get('description')
        post.stationmaster = request.POST.get('stationmaster')
        post.contact = request.POST.get('contact')
        post.email = request.POST.get('email')
        post.save()
        return redirect('postofficelist') 
    else:
        postoffices = postoffice.objects.all()
        return render(request, 'editpostoffice.html', {'postoffice': post, 'postoffices': postoffices})
def adminlogin2(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        u='admin2@gmail.com'
        p='admin2'
        if email==u:
            if password==p:
                return redirect('adminhome2')
    return render(request,'adminlogin2.html')  
def stamplist2(request):
    u=stamp.objects.all()
    return render(request,'stamplist2.html',{'s':u}) 
def adminhome2(request):
    return render(request,'adminhome2.html')
from django.core.mail import send_mail
from django.conf import settings
def addparcel2(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        max_parcel_id = postmodel.objects.all().order_by('-parcel_id').first()
        if max_parcel_id:
            parcel_id = max_parcel_id.parcel_id + 1  
        else:
            parcel_id = 10000  
        sendername = request.POST.get('sendername')
        sender_address = request.POST.get('sender_address')
        sender_contact = request.POST.get('sender_contact')
        receivername = request.POST.get('receivername')
        receiver_address = request.POST.get('receiver_address')
        receiver_email = request.POST.get('receiver_email')
        receiver_postoffice = request.POST.get('receiver_postoffice')
        receiver_contact = request.POST.get('receiver_contact')  
        posted_date = request.POST.get('posted_date')
        remarks = request.POST.get('remarks')
        status = request.POST.get('status')
        weight = request.POST.get('weight')
        kms = request.POST.get('kms')
        price = request.POST.get('price')
        screenshot = request.FILES.get('screenshot')
        postman_name = request.POST.get('name')
        postmodel(
            post_id=post_id,
            postoffice="subpostoffice", 
            parcel_id=parcel_id,
            sendername=sendername,
            sender_address=sender_address,
            sender_contact=sender_contact,
            receivername=receivername,
            receiver_address=receiver_address,
            receiver_email=receiver_email,
            receiver_postoffice=receiver_postoffice,
            receiver_contact=receiver_contact, 
            posted_date=posted_date,
            remarks=remarks,
            status=status,
            weight=weight,
            kms=kms,
            price=price,
            screenshot=screenshot,
            postman_name=postman_name
        ).save()
        subject = 'A Parcel is Ready for Delivery'
        message = f'Hello {receivername},\n\nYour parcel with ID {parcel_id} is ready for delivery at the post office.\n\nThank you for using our service!'
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email,[receiver_email] )
        return redirect('adminhome2')
    postoffices = postoffice.objects.all()
    p = postman.objects.all()
    return render(request, 'addparcel2.html', {'postoffices': postoffices, 'p': p})
def parcellist2(request):
    p=postmodel.objects.filter(postoffice="subpostoffice")
    return render(request,'parcellist2.html',{'parcel':p})
def deleteparcel2(request,id):
    p=postmodel.objects.get(id=id)
    p.delete()
    return redirect('parcellist2')
def edit_parcel2(request, id):
    parcellist= get_object_or_404(postmodel, id=id)
    if request.method == 'POST':
        parcellist.post_id = request.POST.get('post_id')
        parcellist.sendername = request.POST.get('sendername')
        parcellist.sender_address = request.POST.get('sender_address')
        parcellist.sender_contact = request.POST.get('sender_contact')
        parcellist.receivername = request.POST.get('receivername')
        parcellist.receiver_address = request.POST.get('receiver_address')
        parcellist.receiver_postoffice = request.POST.get('receiver_postoffice')
        parcellist.receiver_contact = request.POST.get('receiver_contact')
        parcellist.posted_date = request.POST.get('posted_date')
        parcellist.remarks = request.POST.get('remarks')
        parcellist.status = request.POST.get('status')
        parcellist.weight = request.POST.get('weight')
        parcellist.kms = request.POST.get('kms')
        parcellist.price = request.POST.get('price')
        parcellist.screenshot = request.POST.get('screenshot')
        parcellist.postman_username = request.POST.get('postman_username')
        parcellist.save()
        return redirect('parcellist2')  
    else:
        parcel=postmodel.objects.all()
        return render(request,'editparcel2.html',{'parcellist2':parcellist,'parcel':parcel})        
def update_status(request):
    if request.method=="POST":
        email=request.POST.get('email')
        status=request.POST.get('status')
    if not email or not status:
        return redirect('userlist')
    if status not in['applied','approved','rejected']:
        return redirect('userlist')
    Constr=get_object_or_404(USER,email=email) 
    Constr.status=status
    Constr.save()
    if status == 'approved':
            subject = "Your Registration has been Approved"
            message =f"""
        Dear {Constr.username},
        Congratulations! Your registration has been approved. You can now log in and access your account.
        Best regards,
        Parcel Path
        """
            from_email = settings.DEFAULT_FROM_EMAIL  
            recipient_list = [Constr.email]
            send_mail(subject, message, from_email, recipient_list)
    return redirect(userlist)
def postmanlogin(request):
    if request.method =='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            log=models.postman.objects.get(email=email,password=password)
            email=log.email
            request.session['email']=email
            return redirect('posthome')
        except:
            msg="Invalid email or password"
            return render(request,'postmanlogin.html',{"msg":msg})
    return render(request,'postmanlogin.html')
def postmanparcel(request):
    p=postmodel.objects.filter(postoffice="subpostoffice")
    return render(request,'postmanparcel.html',{'parcel':p})
def delivered_status(request,id):
    parcellist=get_object_or_404(postmodel,id=id)
    parcellist.status="itemdelivered"
    parcellist.save()
    alert_message = "<script>alert('option changed as delivered'); window.location.href='/posthome/';</script>"
    return HttpResponse(alert_message)
def outdelivery_status(request,id):
    parcel=get_object_or_404(postmodel,id=id)
    parcel.status="itemoutfordelivery"
    parcel.save()
    alert_message = "<script>alert('option changed as  out for delivery'); window.location.href='/posthome/';</script>"
    return HttpResponse(alert_message)
def poststatus(request):
    return render(request,'poststatus.html')
def parcellist3(request):
    semail = request.session['email']
    postman = models.postman.objects.get(email=semail)
    parcels_assigned_to_postman = postmodel.objects.filter(postman_name=postman.name)
    return render(request, 'parcellist3.html', {'parcel': parcels_assigned_to_postman})
def postmanparcel2(request):
    semail = request.session['email']
    postman = models.postman.objects.get(email=semail)
    parcels_assigned_to_postman = postmodel.objects.filter(postman_name=postman.name, postoffice="subpostoffice")
    return render(request, 'postmanparcel2.html', {'parcel': parcels_assigned_to_postman})
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
def update_status1(request, id):
    parcellist = get_object_or_404(postmodel, id=id)
    if request.method == 'POST':
        status = request.POST.get('status')
        valid_statuses = ["itemdelivered", "doorclosed", "returned", "rescheduled"]
        if status in valid_statuses:
            parcellist.status = status
            parcellist.save()
            alert_message = f"""
                <script>
                    alert('Status changed to {status.replace('_', ' ').capitalize()}');
                    window.location.href = '/posthome/';
                </script>
            """
            return HttpResponse(alert_message)
        else:
            alert_message = """
                <script>
                    alert('Invalid status');
                    window.location.href = '/posthome/';
                </script>
            """
            return HttpResponse(alert_message)
    return HttpResponse("<script>alert('Invalid request'); window.location.href='/posthome/';</script>")
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from datetime import datetime
from django.core.mail import send_mail
def reschedule(request, id):
    parcel = get_object_or_404(postmodel, id=id)
    if request.method == 'POST':
        rescheduled_date = request.POST.get('rescheduled_date')
        if rescheduled_date:
            try:
                rescheduled_date = datetime.strptime(rescheduled_date, '%Y-%m-%d').date()
                data,created=models.Reschedule.objects.get_or_create(parcel=parcel,defaults={'rescheduled_date':rescheduled_date})
                parcel.reschedule_status=True 
                parcel.save()
                if created:
                    send_reschedule_email(parcel)
                    return redirect('user_parcels')
                else:
                    send_reschedule_email(parcel)
                    data.save()
                    return redirect('user_parcels')
            except ValueError:
                messages.error(request, 'Invalid date format. Please provide a valid date.')
        else:
            messages.error(request, 'Please provide a valid rescheduled date.')
    obj=models.Reschedule.objects.filter(parcel=parcel)
    return render(request, 'reschedule.html',{'obj':obj})
def send_reschedule_email(parcel):
    subject = f"Parcel {parcel.parcel_id} Reschedule"
    message = f"Dear{parcel.receivername},\n\n" \
              f"Your request to reschedule the delivery of parcel with ID {parcel.parcel_id} has been submitted. Please wait for approval, and we will notify you once the new delivery schedule is confirmed."\
              f"Parcel Delivery Service"
    from_email = 'your_email@gmail.com' 
    recipient_list = [parcel.receiver_email] 
    send_mail(subject, message, from_email, recipient_list)
    subject_admin = f"Parcel {parcel.parcel_id} Reschedule Request"
    message_admin = f"Dear Admin,\n\n" \
                    f"A reschedule request has been submitted for parcel with ID {parcel.parcel_id}. " \
                    f"The receiver, {parcel.receivername}, is waiting for approval. Please review the request and approve or reject the reschedule.\n\n" \
                    f"Parcel Delivery Service"
    recipient_list_admin = ['jagadeeshnandana805@gmail.com']  
    send_mail(subject_admin, message_admin, from_email, recipient_list_admin)
def rescheduled_details(request, id):
    parcel = get_object_or_404(postmodel, id=id)
    try:
        details = Reschedule.objects.get(parcel=parcel)
    except Reschedule.DoesNotExist:
        details = None    
    return render(request, 'reschedule_details.html', {'details': details})
def approve_reschedule(request, id):
    parcel = get_object_or_404(postmodel,parcel_id=id)
    reschedule_request = models.Reschedule.objects.get(parcel=parcel)
    reschedule_request.is_approved = True
    reschedule_request.save()
    rescheduled_date = reschedule_request.rescheduled_date
    subject = f"Your Parcel {parcel.parcel_id} Reschedule has been Approved"
    message = f"Dear {parcel.receivername},\n\n" \
                  f"Your request to reschedule the delivery for parcel ID {parcel.parcel_id} has been approved. " \
                  f"The delivery will proceed on {rescheduled_date}.\n\n" \
                  f"Thank you for your patience.\n\n" \
                  f"Best regards,\n" \
                  f"Parcel Delivery Service"
    from_email = 'your-email@example.com'
    recipient_list = [parcel.receiver_email] 
    send_mail(subject, message, from_email, recipient_list)
    postman_object = postman.objects.filter(name=parcel.postman_name).first()
    if postman_object:
            postman_email = postman_object.email
            subject_postman = f"Parcel {parcel.parcel_id} Reschedule Approved"
            message_postman = f"Dear Postman,\n\n" \
                              f"The reschedule request for parcel ID {parcel.parcel_id} has been approved. " \
                              f"The new delivery date is {rescheduled_date}.\n\n" \
                              f"Please ensure the delivery on this date.\n\n" \
                              f"Best regards,\n" \
                              f"Parcel Delivery Service"
            recipient_list_postman = [postman_email]
            send_mail(subject_postman, message_postman, from_email, recipient_list_postman)
    else:
            print(f"No postman found for {parcel.postman_name}")
    return render(request, 'adminhome2.html', {'details': parcel})
def reject_reschedule(request, id):
    parcel = get_object_or_404(postmodel, parcel_id=id)
    reschedule_request = models.Reschedule.objects.get(parcel=parcel)
    reschedule_request.is_approved = False
    reschedule_request.save()
    subject = f"Your Parcel {parcel.parcel_id} Reschedule has been Rejected"
    message = f"Dear {parcel.receivername},\n\n" \
              f"Your request to reschedule the delivery for parcel ID {parcel.parcel_id} has been rejected. " \
              f"Thank you for your patience.\n\n" \
              f"Best regards,\n" \
              f"Parcel Delivery Service"
    from_email = 'your-email@example.com'
    recipient_list = [parcel.receiver_email]
    send_mail(subject, message, from_email, recipient_list)
    return render(request, 'adminhome2.html', {'details': parcel})
import razorpay
from django.conf import settings
from django.shortcuts import render, redirect 
from django.http import JsonResponse
from .models import Reschedule
import json
from django.views.decorators.csrf import csrf_exempt
client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
def initiate_payment(request, reschedule_id):
    try:
        reschedule = Reschedule.objects.get(id=reschedule_id)
        if reschedule.payment_status:
            return JsonResponse({'error': 'Payment already made for this reschedule'}, status=400)
        amount = 50  
        order_data = {
            'amount': amount * 100, 
            'currency': 'INR',
            'payment_capture': '1',  
        }
        order = client.order.create(data=order_data)
        order_id = order['id']
        reschedule.razorpay_order_id = order_id
        reschedule.save()
        return JsonResponse({
            'order_id': order_id,
            'razorpay_key_id': settings.RAZOR_KEY_ID,
            'amount': amount
        })
    except razorpay.errors.RazorpayError as e:
        print(f"Razorpay error: {e}")
        return JsonResponse({'error': 'Error with Razorpay API'}, status=500)
    except Exception as e:
        print(f"General error: {e}")
        return JsonResponse({'error': str(e)}, status=400)
@csrf_exempt  
def payment_success(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            payment_id = data['razorpay_payment_id']
            order_id = data['razorpay_order_id']
            signature = data['razorpay_signature']
            params_dict = {
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            client.utility.verify_payment_signature(params_dict)
            reschedule = Reschedule.objects.get(razorpay_order_id=order_id)
            reschedule.payment_status = True
            reschedule.save()
            return JsonResponse({'status': 'success'})
        except razorpay.errors.SignatureVerificationError:
            return JsonResponse({'status': 'error', 'message': 'Payment verification failed'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
from django.shortcuts import render
from .models import postmodel
def user_delivery_history(request):
    semail = request.session['email']
    user = USER.objects.get(email=semail)
    userdelivered_items = postmodel.objects.filter(receiver_email=user.email, status='itemdelivered')
    return render(request, 'user_delivery_history.html', {'userdelivered_items': userdelivered_items})
def user_reschedule_history(request):
    semail = request.session['email']
    user = USER.objects.get(email=semail)
    userrescheduled_items = postmodel.objects.filter(receiver_email=user.email, status='rescheduled')
    return render(request, 'user_reschedule_history.html', {'userrescheduled_items': userrescheduled_items})
def delivered_parcels(request):
    semail = request.session['email']
    postman = models.postman.objects.get(email=semail)
    delivered_items = postmodel.objects.filter(status='itemdelivered', postman_name=postman.name)
    return render(request, 'delivered_parcels.html', {'delivered_items': delivered_items})
def rescheduled_parcels(request):
    semail = request.session['email']
    postman = models.postman.objects.get(email=semail)
    rescheduled_items = postmodel.objects.filter(status='rescheduled',postman_name=postman.name)
    return render(request,'rescheduled_parcels.html', {'rescheduled_items': rescheduled_items})
def returned_parcels(request):
    semail = request.session['email']
    postman = models.postman.objects.get(email=semail)
    returned_items = postmodel.objects.filter(status='returned',postman_name=postman.name)
    return render(request,'returned_parcels.html', {'returned_items': returned_items})
def doorclosed_parcels(request):
    semail = request.session['email']
    postman = models.postman.objects.get(email=semail)
    doorclosed_items = postmodel.objects.filter(status='doorclosed',postman_name=postman.name)
    return render(request,'doorclosed_parcels.html', {'doorclosed_items': doorclosed_items})
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from .models import USER
import random
import time
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = USER.objects.get(email=email)
            otp = random.randint(100000, 999999)
            user.otp = otp
            user.save()
            subject = "Password Reset OTP"
            message = f"Your OTP for password reset is: {otp}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
            request.session['reset_email'] = email
            request.session['otp_timestamp'] = time.time()
            return redirect('verify_otp')
        except USER.DoesNotExist:
            return HttpResponse("<script>alert('Email not found'); window.location.href='/forgot-password/';</script>")
    return render(request, 'forgot_password.html')
def verify_otp(request):
    if request.method == 'POST':
        email = request.session.get('reset_email')
        otp_entered = request.POST.get('otp')
        otp_timestamp = request.session.get('otp_timestamp', 0)
        if time.time() - otp_timestamp > 30:
            return HttpResponse("<script>alert('OTP expired! Request a new one.'); window.location.href='/forgot-password/';</script>")
        try:
            user = USER.objects.get(email=email)
            if str(user.otp) == otp_entered:
                return redirect('reset_password')
            else:
                return HttpResponse("<script>alert('Invalid OTP'); window.location.href='/verify-otp/';</script>")
        except USER.DoesNotExist:
            return redirect('forgot_password')
    return render(request, 'verify_otp.html')
def reset_password(request):
    if request.method == 'POST':
        email = request.session.get('reset_email')
        new_password = request.POST.get('new_password')
        try:
            user = USER.objects.get(email=email)
            user.password = make_password(new_password)
            user.otp = None
            user.save()
            request.session['reset_email'] = email
            request.session['otp_timestamp'] = time.time()
            return HttpResponse("<script>alert('Password reset successful! Please log in with your new password.'); window.location.href='/login/';</script>")
        except USER.DoesNotExist:
            return redirect('forgot_password')
    return render(request, 'reset_password.html')