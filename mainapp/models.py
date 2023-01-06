from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    preamble = models.CharField(max_length=1024, verbose_name='Вступление')

    body = models.TextField(verbose_name='Содержание')
    body_as_markdown = models.BooleanField(default=False, verbose_name='Разметка в формате Markdown')

    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self) -> str:
        return f"{self.pk} {self.title}"

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class CoursesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class Course(models.Model):
    objects = CoursesManager()

    name = models.CharField(max_length=256, verbose_name="Название")
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    description_as_markdown = models.BooleanField(verbose_name="As markdown", default=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='', default=0)
    cover = models.CharField(max_length=25, default="no_image.svg", verbose_name="Cover")

    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self) -> str:
        return f"{self.pk} {self.name}"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Название курса')
    num = models.PositiveIntegerField(default=0, verbose_name='Номер урока')

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    description_as_markdown = models.BooleanField(
        verbose_name="As markdown", default=False
    )

    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self) -> str:
        return f"{self.course.name} | {self.num} | {self.title}"

    class Meta:
        ordering = ("course", "num")
        verbose_name = _('Урок')
        verbose_name_plural = _('Уроки')

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class CourseTeacher(models.Model):
    courses = models.ManyToManyField(Course)
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')
    day_birth = models.DateField(verbose_name="День рождения")

    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self) -> str:
        return "{0:0>3} {1} {2}".format(self.pk, self.last_name, self.first_name)

    class Meta:
        verbose_name = _('Курс к учителю')
        verbose_name_plural = _('Курсы к учителям')

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class CourseFeedback(models.Model):
    RATING = (
        (5, "⭐⭐⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (3, "⭐⭐⭐"),
        (2, "⭐⭐"),
        (1, "⭐")
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Курс"))
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    feedback = models.TextField(default=_("No feedback"), verbose_name=_("Отзыв"))
    rating = models.SmallIntegerField(choices=RATING, default=5, verbose_name=_("Рейтинг"))
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.course} ({self.user})"