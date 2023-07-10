from django.shortcuts import render 
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def homes(request):
    if request.method=="POST":
        fname = str(request.POST.get('pname'))
        famount = request.POST.get('amount')
        fdtime = request.POST.get('ptime')
        futime = request.POST.get('utime')
        print(futime)
        image = Image.open(r"C:\Users\ANKIT\Desktop\DJANGO-PAYTM\paytm\app\media\fail.png")

    # Create a drawing object
        draw = ImageDraw.Draw(image)

    # Define the font to use
        name = "Nandan Singh"
        amount = str(1000)
        if len(fname)<15:
            a=49
        else:
            a=40
        font = ImageFont.truetype("arialbd.ttf", size=a)
        font1 = ImageFont.truetype("arial.ttf", size=77)
        font2 = ImageFont.truetype("arial.ttf", size=40)
        font3 = ImageFont.truetype("arial.ttf", size=29)
        font4 = ImageFont.truetype("arial.ttf", size=29)

    # Draw the text on the image
    # Split the name into words
        words = fname.split()

    # Get the first and last words
        first_word, last_word = words[0], words[-1]

    # Extract the first letter of each word and join as string
        first_letters = ''.join([first_word[0], last_word[0]])

    # Print the result
        print(first_letters)
        if len(famount)==4:
            x1=180
            y1=380
            x2=230
            y2=380
        elif len(famount)==5:
            x1=150
            y1=380
            x2=190
            y2=380
        elif len(famount)==3:
            x1=230
            y1=380
            x2=275
            y2=380
        elif len(famount)==2:
            x1=270
            y1=380
            x2=315
            y2=380
        else:
            x1=320
            y1=380
            x2=365
            y2=380

        draw.text((210, 240), fname, fill=(0,0,0), font=font)
        draw.text((x1, y1), "₹", fill=(0,0,0), font=font1)
        draw.text((x2, y2), famount , fill=(0,0,0), font=font1)
        draw.text((111, 257), first_letters, fill=(255,255,255), font=font2)
        draw.text((230, 550), fdtime, fill=(0, 0, 0), font=font3)
        draw.text((17,26), futime, fill=(0,0,0), font=font4)

        blur_radius = 1
        blur_box = (5 - blur_radius, 26 - blur_radius, 100 + blur_radius, 85 + blur_radius)
        blur_region = image.crop(blur_box)
        blur_region = blur_region.filter(ImageFilter.GaussianBlur(blur_radius))
        image.paste(blur_region, blur_box)

    # Save the modified image
        response = HttpResponse(content_type="image/png")
        image.save(response, "PNG")
        return response
    return render (request , "index.html")

# Create your views here.





def homes2(request):
    if request.method=="POST":
        fname = str(request.POST.get('pname'))
        famount = request.POST.get('amount')
        fdtime = request.POST.get('ptime')
        futime = request.POST.get('utime')
        print(futime)
        image = Image.open(r"C:\Users\ANKIT\Desktop\DJANGO-PAYTM\paytm\app\media\new.jpg")

# Create a drawing object
        draw = ImageDraw.Draw(image)

# Define the font to use

# Draw the text on the image
        
        if len(fname)<15:
            a=49
        else:
            a=40
        font = ImageFont.truetype("arialbd.ttf", size=a)
        font1 = ImageFont.truetype("arial.ttf", size=77)
        font2 = ImageFont.truetype("arial.ttf", size=40)
        font3 = ImageFont.truetype("arialbd.ttf", size=33)
        font4 = ImageFont.truetype("arial.ttf", size=29)

# Split the name into words
        words = fname.split()

# Get the first and last words
        first_word, last_word = words[0], words[-1]

# Extract the first letter of each word and join as string
        first_letters = ''.join([first_word[0], last_word[0]])

# Print the result
        print(first_letters)
        if len(famount)==4:
            x1=178
            y1=390
            x2=230
            y2=390
        elif len(famount)==5:
            x1=150
            y1=390
            x2=190
            y2=390
        elif len(famount)==3:
            x1=230
            y1=390
            x2=275
            y2=390
        elif len(famount)==2:
            x1=270
            y1=390
            x2=315
            y2=390
        else:
            x1=320
            y1=390
            x2=365
            y2=390

        draw.text((210, 240), fname, fill=(0,0,0), font=font)

        draw.text((x1, y1), "₹", fill=(0,0,0), font=font1)
        draw.text((x2, y2), famount , fill=(0,0,0), font=font1)
        draw.text((110, 258), first_letters, fill=(255,255,255), font=font2)
        draw.text((170, 530), fdtime, fill=(26, 178, 255), font=font3)
        draw.text((17,28), futime, fill=(0,0,0), font=font4)


        blur_radius = 1
        blur_box = (5 - blur_radius, 26 - blur_radius, 100 + blur_radius, 85 + blur_radius)
        blur_region = image.crop(blur_box)
        blur_region = blur_region.filter(ImageFilter.GaussianBlur(blur_radius))
        image.paste(blur_region, blur_box)


# Save the modified image

    # Save the modified image
        response = HttpResponse(content_type="image/png")
        image.save(response, "PNG")
        return response
    return render (request , "index2.html")
