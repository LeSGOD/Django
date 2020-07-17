from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_data = models.DateTimeField(default=timezone.now())
    published_data = models.DataTimeField(blank=True, null=True)

    def publish(self):
        self.published_data = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approve_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_data = models.DateTimeField(default=timezone.now())
    approve_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('post_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.text
