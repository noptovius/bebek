from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Assistant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    initial = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.initial

class Semester(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AssistantMapping(models.Model):
    ast = models.ForeignKey(Assistant, on_delete=models.DO_NOTHING, related_name='ast')
    leader = models.ForeignKey(Assistant, on_delete=models.DO_NOTHING, related_name='leader')
    inspector = models.ForeignKey(Assistant, on_delete=models.DO_NOTHING, related_name='inspector')
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.ast.initial

class Swap(models.Model):
    requester = models.ForeignKey(Assistant, on_delete=models.DO_NOTHING, related_name='requester')
    approver = models.ForeignKey(Assistant, on_delete=models.DO_NOTHING, related_name='approver')
    ast_before = models.ForeignKey(Assistant, on_delete=models.DO_NOTHING, related_name='ast_before')
    ast_after = models.ForeignKey(Assistant, on_delete=models.DO_NOTHING, related_name='ast_after')
    date_requested = models.DateTimeField(default=timezone.now)
    date_approved = models.DateTimeField(null=True)

    def __str__(self):
        return 'Swap of %s, from %s to %s with %s' % (self.requester.initial,
                                                      self.ast_before.initial,
                                                      self.ast_after.initial,
                                                      self.approver.initial)

class Transaction(models.Model):
    ast_mapping = models.ForeignKey(AssistantMapping, on_delete=models.DO_NOTHING)
    partner = models.ForeignKey(Assistant, on_delete=models.DO_NOTHING)
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)
    class_id = models.CharField(max_length=20)
    course_id = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    shift = models.IntegerField()
    room = models.IntegerField()
    date = models.DateTimeField(null=True)

    def __str__(self):
        return 'Transsaction %s & %s, %s - %s (%s), shift %s room %s' \
            % (self.ast_mapping.ast.initial, self.partner.initial, self.course_id, self.course_name,
            self.class_id, self.shift, self.room)

class KeyIndicator(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)

    def __str__(self):
        return 'Key Indicator Title: %s Description: %s' % (self.title, self.desc)

class Indicator(models.Model):
    key_indicator = models.ForeignKey(KeyIndicator, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)

    def __str__(self):
        return 'Indicator Title: %s Description: %s' % (self.title, self.desc)

class Review(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.DO_NOTHING)
    indicator = models.ForeignKey(Indicator, on_delete=models.DO_NOTHING)
    result = models.BooleanField()
    comments = models.CharField(max_length=255, default='-')

