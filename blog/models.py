from django.db import models


class Writer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default="")
    date_public = models.DateTimeField()
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    date_comm = models.DateTimeField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, default="")
    comment = models.ForeignKey('blog.Comment',
                                on_delete=models.CASCADE,
                                default="",
                                null=True,
                                blank=True,
                                related_name="comments")

    def __str__(self):
        return f'{self.text} by {self.writer}'


class LikeToArticle(models.Model):
    Like = 'L'
    Dislike = 'D'
    LIKEDISLIKE = [
        (Like, 'Like'),
        (Dislike, 'Dislike')
    ]
    like_choice = models.CharField(max_length=1, choices=LIKEDISLIKE, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, default="")

    class Meta:
        unique_together = ['article', 'writer']

    def __str__(self):
        return self.like_choice


class LikeToComment(models.Model):
    Like = 'L'
    Dislike = 'D'
    LIKEDISLIKE = [
        (Like, 'Like'),
        (Dislike, 'Dislike')
    ]
    like_choice = models.CharField(max_length=1, choices=LIKEDISLIKE, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, default="")
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, default="")

    class Meta:
        unique_together = ['comment', 'writer']

    def __str__(self):
        return self.like_choice

