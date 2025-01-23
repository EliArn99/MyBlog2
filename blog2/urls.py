# In your app's urls.py

from django.urls import path
from . import views

urlpatterns = [
    # HOME PAGE DISPLAY
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('register/', views.register, name='register'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),




    # path('category/book-reviews/', views.book_reviews, name='book_reviews'),  # Book Reviews page
    # path('books/', views.book_reviews, name='book_reviews'),
    # path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    # path('books/add/', views.add_review, name='add_review'),
    #
    # path('category/lifestyle/', views.lifestyle, name='lifestyle'),  # Lifestyle page
    # path('category/technology/', views.technology, name='technology'),  # Technology page
    #
    # path('technology/', technology, name='technology'),
    # path('technology/add/', add_technology_article, name='add_technology_article'),
    # path('technology/<int:article_id>/', technology_article_detail, name='technology_article_detail'),
    #
    # path('category/education/', views.education, name='education'),  # Education & Learning page
    # path('category/environment/', views.environment, name='environment'),  # Environment & Nature page
    # path('category/art-and-culture/', views.art_and_culture, name='art_and_culture'),  # Art & Culture page
    # path('category/gaming/', views.gaming, name='gaming'),  # Gaming page
    # path('login/', views.login_view, name='login'),  # Login page
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
