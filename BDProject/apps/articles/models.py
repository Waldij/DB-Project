from django.db import models
from PIL import Image

class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length = 200)
    article_text = models.TextField('Текст статиь')
    pub_date = models.DateTimeField('Дата публикации')




class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('Имя автора', max_length = 200)
    comment_text = models.TextField('Текст коментария', max_length = 200)

    def __str__(self):
        return self.author_name


class Photo(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    title = models.CharField(max_length=128)
    description = models.TextField()
    care = models.TextField()
    photo = models.ImageField(upload_to='user_photos')

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url