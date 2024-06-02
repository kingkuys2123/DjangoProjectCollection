from django.shortcuts import render, redirect
from .models import TourPackage, Review


def home(request):
    tour_packages = TourPackage.objects.all()

    return render(request, 'home.html', {'tour_packages': tour_packages})


def package_details(request, package_id):
    tour_package = TourPackage.objects.get(id=package_id)
    reviews = Review.objects.filter(tour_package=tour_package)

    return render(request, 'package_details.html', {'tour_package': tour_package, 'reviews': reviews})


def add_package_review(request, package_id):
    tour_package = TourPackage.objects.get(id=package_id)

    if request.method == 'POST':
        review_customer_name = request.POST.get('customer_name')
        review_rating = request.POST.get('rating')
        review_text = request.POST.get('review_text')

        review = Review.objects.create(tour_package=tour_package, customer_name=review_customer_name, rating=review_rating,
                                       review_text=review_text)
        review.save()

    return redirect('package_details', package_id)
