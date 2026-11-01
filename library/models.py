from django.db import models
from django.utils.text import slugify

class AuthorModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    biography = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    # there is a save() method inside each model which is used to save data.
    # we can modify the save() method with logics 
    def save(self, *args, **kwargs):
            # if the current author does not have a slug, create a slug using his name() 
            if not self.slug:
                # create a slug using author name. the base slug will never change
                base_slug = slugify(self.name)

                # keep the base slug in another variable so that we can change or modify it
                slug = base_slug

                # the first slug will be normal. but further slug with same name will have suffix -2
                # just like, first instance will have stan-lee(base slug) as slug
                # but the second instance should be stan-lee-2
                # that's why the counter starts from 2
                counter = 2

                # the while loop will search for instances with existing slug value
                while AuthorModel.objects.filter(slug=slug).exists():
                    # if an existing slug is found, the new slug will have the counter number as suffix
                    slug = f"{base_slug}-{counter}"
                    # then the counter will be incremented
                    counter +=1

                # if no previous instance is found,  then it will simply return the slug value                
                self.slug = slug

            # and finally,  django's original save method will be called to save the object to the db
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class CategoryModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
    
            slug = base_slug
            counter = 2
    
            while CategoryModel.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter +=1         
            
            self.slug = slug
    
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class BookModel(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, default='')
    author = models.ForeignKey(
        AuthorModel,
        on_delete=models.PROTECT,
        related_name= 'books'
    )
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        related_name='books'
    )
    isbn = models.CharField(max_length=20, unique=True)
    published_date = models.DateField(null=True, blank=True)
    available_copies = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
    
            slug = base_slug
            counter = 2
    
            while BookModel.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter +=1         
            
            self.slug = slug
    
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title