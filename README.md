quickecommerce/
├── apps/
│   ├── users/
│   ├── products/
│   ├── orders/
│   ├── payments/
│   ├── reports/
│   ├── notifications/
├── config/
│   ├── settings/
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
├── manage.py

# 1. Create a Django Project and Apps
# Run these commands in your terminal:
# django-admin startproject quickcommerce
# cd quickcommerce
# python manage.py startapp core # For shared models/utils
# python manage.py startapp users
# python manage.py startapp products
# python manage.py startapp carts
# python manage.py startapp orders
# python manage.py startapp payments
# python manage.py startapp notifications
# python manage.py startapp reports

# 2. Install necessary packages:
# pip install django djangorestframework django-allauth djangorestframework-simplejwt psycopg2-binary django-filter shortuuid django-autoslug
# (psycopg2-binary is for PostgreSQL, adjust if using a different DB)
# (djangorestframework-simplejwt for token authentication)
# (django-filter for filtering in DRF)
# (shortuuid for potentially shorter unique IDs if needed, though UUID is the primary request)
# (django-autoslug for automatic slug generation)

# 3. Update quickcommerce/settings.py

# Add to INSTALLED_APPS:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # Required by allauth

    # Third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Add social providers as needed, e.g.:
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
    'django_filters',
    'autoslug',

    # Your apps
    'core.apps.CoreConfig',
    'users.apps.UsersConfig',
    'products.apps.ProductsConfig',
    'carts.apps.CartsConfig',
    'orders.apps.OrdersConfig',
    'payments.apps.PaymentsConfig',
    'notifications.apps.NotificationsConfig',
    'reports.apps.ReportsConfig',
]

# Add SITE_ID for allauth
SITE_ID = 1

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # SessionAuthentication can be useful for browsable API
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Allauth settings
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Specify your custom user model
AUTH_USER_MODEL = 'users.User'

# Allauth configuration (minimal)
ACCOUNT_AUTHENTICATION_METHOD = 'email' # or 'username_email' or 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'optional' # or 'mandatory' or 'none'
ACCOUNT_USERNAME_REQUIRED = False # If using email as primary identifier

# For social accounts, you'll need to configure providers in the Django admin
# and add their respective keys/secrets to your settings or environment variables.
# Example for Google (you'd add more specific settings):
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         }
#     }
# }

# Configure email backend (for development, use console backend)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware', # Add this line
]

# Database - Ensure your chosen DB supports UUID fields natively or efficiently.
# PostgreSQL is highly recommended.
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'your_db_name',
#         'USER': 'your_db_user',
#         'PASSWORD': 'your_db_password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Static and Media files (basic setup)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# 4. Update quickcommerce/urls.py (Main URLs)
# This will be filled in more detail later, but for now:
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('allauth.urls')), # For allauth's provided views (login, signup, etc.)
    # You might use dj_rest_auth for better DRF integration with allauth:
    # path('api/auth/', include('dj_rest_auth.urls')),
    # path('api/auth/registration/', include('dj_rest_auth.registration.urls')), # For registration
    
    # App URLs will be added here
    # path('api/users/', include('users.urls')),
    # path('api/products/', include('products.urls')),
    # ... and so on
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
# Note: `dj_rest_auth` (previously `django-rest-auth`) is highly recommended for integrating
# allauth with DRF, providing token management, registration, password reset, etc., API endpoints.
# If you use `dj_rest_auth`, you'd typically include its URLs instead of `allauth.urls` directly for API purposes.
# For this example, I'll assume you might set up your own views or use `allauth`'s views directly for simplicity,
# but `dj_rest_auth` is the more common DRF approach.
# For JWT with dj_rest_auth, you'd also configure it to use SimpleJWT.

# 5. Create a base model in core/models.py
# This will be used by other models to have UUID primary keys and timestamps.
