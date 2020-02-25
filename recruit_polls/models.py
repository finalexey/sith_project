# from django.db import models
#
#
#
#
# class Question(models.Model):
#
#     question_text = models.CharField(
#         max_length=200,
#         verbose_name='Вопрос',)
#
#     def __str__(self):
#         return self.question_text
#
#
# class Answer(models.Model):
#
#     answer_choices = [
#         (True, 'Да'),
#         (False, 'Нет')]
#
#     answer = models.BooleanField(
#         max_length=32,
#         choices=answer_choices,
#         default=True,
#         verbose_name="Ответ")
#
#     def __str__(self):
#         return self.answer
#
#
# class Poll(models.Model):
#
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
#     recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, null=True)


from django.db import models
from recruit_app.models import Recruit


class Question(models.Model):
    title = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.choice_set.all()


class Choice(models.Model):
    question = models.ForeignKey('recruit_polls.Question', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.text

    @property
    def votes(self):
        return self.answer_set.count()


class Answer(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, null=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.recruit.name + '-' + self.choice.text
