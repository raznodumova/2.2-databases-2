from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scope = models.ManyToManyField(Tag, through='Scope', verbose_name='Раздел')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, related_name='scopes', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='scopes', on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['-is_main']

    def __str__(self):
        return self.tag.name

