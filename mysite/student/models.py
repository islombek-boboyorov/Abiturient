from django.db import models


class About(models.Model):
    title = models.TextField(blank=False, null=True)
    name = models.CharField(max_length=128, blank=True, null=False)
    degree = models.CharField(max_length=128, blank=True, null=False)
    image = models.ImageField(upload_to='image/', blank=True, null=False)
    description = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    class Meta:
        db_table = "about"


class Courses(models.Model):
    picture = models.ImageField(upload_to='image/', blank=False, null=False)
    profession = models.CharField(max_length=128, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False, default=0)
    direction = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    name = models.CharField(max_length=128, blank=False, null=False)
    students = models.IntegerField(blank=False, null=False, default=0)
    like = models.IntegerField(blank=False, null=False, default=0)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "courses"


class Trainers(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    profession = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    twitter = models.CharField(max_length=150, blank=False, null=False)
    facebook = models.CharField(max_length=150, blank=False, null=False)
    instagram = models.CharField(max_length=150, blank=False, null=False)
    inn = models.CharField(max_length=150, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "trainers"


class Pricing(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "pricing"


class Pricings(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    pricing = models.ForeignKey(Pricing, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "pricings"


class Events(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    time = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "events"


class Contact(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=200, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "contact"


class Info(models.Model):
    location = models.TextField(blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        db_table = "info"


class Courses_details(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False, default=0)
    pupils_count = models.IntegerField(blank=False, null=False, default=0)
    time = models.CharField(max_length=150, blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    subject = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "courses_info"
