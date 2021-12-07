# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnswerTb(models.Model):
    answer_id = models.AutoField(db_column='ANSWER_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.ForeignKey('StudentTb', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    question_id = models.ForeignKey('QuestionTb', models.DO_NOTHING, db_column='QUESTION_ID')  # Field name made lowercase.
    answer_id = models.CharField(db_column='ANSWER', max_length=1000)  # Field name made lowercase.
    posted_time = models.DateTimeField(db_column='POSTED_TIME')  # Field name made lowercase.
    good_count = models.IntegerField(db_column='GOOD_COUNT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANSWER_TB'


class GroupTb(models.Model):
    group_id = models.AutoField(db_column='GROUP_ID', primary_key=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='GROUP_NAME', max_length=30)  # Field name made lowercase.
    group_type = models.ForeignKey('GroupTypeTb', models.DO_NOTHING, db_column='GROUP_TYPE_ID', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GROUP_TB'


class GroupTypeTb(models.Model):
    group_type_id = models.AutoField(db_column='GROUP_TYPE_ID', primary_key=True)  # Field name made lowercase.
    group_type = models.CharField(db_column='GROUP_TYPE', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GROUP_TYPE_TB'


class HourTb(models.Model):
    hour_id = models.CharField(db_column='HOUR_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    start_time = models.TimeField(db_column='START_TIME')  # Field name made lowercase.
    ending_time = models.TimeField(db_column='ENDING_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HOUR_TB'


class NgWordTb(models.Model):
    ng_word_id = models.AutoField(db_column='NG_WORD_ID', primary_key=True)  # Field name made lowercase.
    ng_word = models.CharField(db_column='NG_WORD', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NG_WORD_TB'


class QuestionTb(models.Model):
    question_id = models.AutoField(db_column='QUESTION_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.ForeignKey('StudentTb', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    q_category_id = models.ForeignKey('QCategoryTb', models.DO_NOTHING, db_column='Q_CATEGORY_ID')  # Field name made lowercase.
    question = models.CharField(db_column='QUESTION', max_length=1000)  # Field name made lowercase.
    posted_time = models.DateTimeField(db_column='POSTED_TIME')  # Field name made lowercase.
    reply_limit = models.DateTimeField(db_column='REPLY_LIMIT')  # Field name made lowercase.
    q_state_id = models.ForeignKey('QStateTb', models.DO_NOTHING, db_column='Q_STATE_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QUESTION_TB'


class QCategoryTb(models.Model):
    q_category_id = models.AutoField(db_column='Q_CATEGORY_ID', primary_key=True)  # Field name made lowercase.
    q_category = models.CharField(db_column='Q_CATEGORY', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Q_CATEGORY_TB'


class QStateTb(models.Model):
    q_state_id = models.AutoField(db_column='Q_STATE_ID', primary_key=True)  # Field name made lowercase.
    q_state = models.CharField(db_column='Q_STATE', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Q_STATE_TB'


class ReminderCategoryTb(models.Model):
    reminder_category_id = models.AutoField(db_column='REMINDER_CATEGORY_ID', primary_key=True)  # Field name made lowercase.
    reminder_category = models.CharField(db_column='REMINDER_CATEGORY', max_length=30)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REMINDER_CATEGORY_TB'


class ReminderTb(models.Model):
    reminder_id = models.AutoField(db_column='REMINDER_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=8)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=30)  # Field name made lowercase.
    reminder_category = models.ForeignKey(ReminderCategoryTb, models.DO_NOTHING, db_column='REMINDER_CATEGORY_ID')  # Field name made lowercase.
    group_id = models.ForeignKey(GroupTb, models.DO_NOTHING, db_column='GROUP_ID', blank=True, null=True)  # Field name made lowercase.
    limit_time = models.DateTimeField(db_column='LIMIT_TIME', blank=True, null=True)  # Field name made lowercase.
    contents = models.CharField(db_column='CONTENTS', max_length=300, blank=True, null=True)  # Field name made lowercase.
    file_url = models.CharField(db_column='FILE_URL', max_length=2048, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REMINDER_TB'


class ReportTb(models.Model):
    report_id = models.AutoField(db_column='REPORT_ID', primary_key=True)  # Field name made lowercase.
    report_time = models.DateTimeField(db_column='REPORT_TIME')  # Field name made lowercase.
    question_id = models.ForeignKey(QuestionTb, models.DO_NOTHING, db_column='QUESTION_ID')  # Field name made lowercase.
    answer_id = models.ForeignKey(AnswerTb, models.DO_NOTHING, db_column='ANSWER_ID', blank=True, null=True)  # Field name made lowercase.
    report_type_id = models.ForeignKey('ReportTypeTb', models.DO_NOTHING, db_column='REPORT_TYPE_ID')  # Field name made lowercase.
    user_id = models.ForeignKey('StudentTb', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REPORT_TB'


class ReportTypeTb(models.Model):
    report_type_id = models.AutoField(db_column='REPORT_TYPE_ID', primary_key=True)  # Field name made lowercase.
    report_type = models.CharField(db_column='REPORT_TYPE', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REPORT_TYPE_TB'


class RoleTb(models.Model):
    role_id = models.AutoField(db_column='ROLE_ID', primary_key=True)  # Field name made lowercase.
    role = models.CharField(db_column='ROLE', max_length=30)  # Field name made lowercase.
    level = models.IntegerField(db_column='LEVEL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROLE_TB'


class ScheduleTb(models.Model):
    schedule_id = models.AutoField(db_column='SCHEDULE_ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=30)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=8)  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='START_TIME')  # Field name made lowercase.
    ending_time = models.DateTimeField(db_column='ENDING_TIME')  # Field name made lowercase.
    place = models.CharField(db_column='PLACE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    group_id = models.ForeignKey(GroupTb, models.DO_NOTHING, db_column='GROUP_ID', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SCHEDULE_TB'


class ShareReminderTb(models.Model):
    share_reminder_id = models.AutoField(db_column='SHARE_REMINDER_ID', primary_key=True)  # Field name made lowercase.
    reminder_id = models.ForeignKey(ReminderTb, models.DO_NOTHING, db_column='REMINDER_ID')  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=8)  # Field name made lowercase.
    check_flg = models.IntegerField(db_column='CHECK_FLG')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SHARE_REMINDER_TB'
        unique_together = (('share_reminder_id', 'reminder_id', 'user_id'),)


class StudentBelongTb(models.Model):
    belong_id = models.AutoField(db_column='BELONG_ID', primary_key=True)  # Field name made lowercase.
    join_day = models.DateField(db_column='JOIN_DAY')  # Field name made lowercase.
    user_id = models.ForeignKey('StudentTb', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    group_id = models.ForeignKey(GroupTb, models.DO_NOTHING, db_column='GROUP_ID')  # Field name made lowercase.
    leave_day = models.DateField(db_column='LEAVE_DAY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STUDENT_BELONG_TB'
        unique_together = (('belong_id', 'join_day', 'user_id', 'group_id'),)


class StudentTb(models.Model):
    user_id = models.CharField(db_column='USER_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    attendance_number = models.IntegerField(db_column='ATTENDANCE_NUMBER', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=60)  # Field name made lowercase.
    mail = models.CharField(db_column='MAIL', max_length=254)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=30)  # Field name made lowercase.
    furigana = models.CharField(db_column='FURIGANA', max_length=60)  # Field name made lowercase.
    nickname = models.CharField(db_column='NICKNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    icon_url = models.CharField(db_column='ICON_URL', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    role_id = models.ForeignKey(RoleTb, models.DO_NOTHING, db_column='ROLE_ID')  # Field name made lowercase.
    user_state_id = models.ForeignKey('UserStateTb', models.DO_NOTHING, db_column='USER_STATE_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STUDENT_TB'


class TeacherBelongTb(models.Model):
    belong_id = models.AutoField(db_column='BELONG_ID', primary_key=True)  # Field name made lowercase.
    join_day = models.DateField(db_column='JOIN_DAY')  # Field name made lowercase.
    user_id = models.ForeignKey('TeacherTb', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    group_id = models.ForeignKey(GroupTb, models.DO_NOTHING, db_column='GROUP_ID')  # Field name made lowercase.
    leave_day = models.DateField(db_column='LEAVE_DAY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEACHER_BELONG_TB'
        unique_together = (('belong_id', 'join_day', 'user_id', 'group_id'),)


class TeacherTb(models.Model):
    user_id = models.CharField(db_column='USER_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=30)  # Field name made lowercase.
    furigana = models.CharField(db_column='FURIGANA', max_length=60)  # Field name made lowercase.
    mail = models.CharField(db_column='MAIL', max_length=254)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=60)  # Field name made lowercase.
    role_id = models.ForeignKey(RoleTb, models.DO_NOTHING, db_column='ROLE_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEACHER_TB'


class TimetableDetailTb(models.Model):
    detail_id = models.AutoField(db_column='DETAIL_ID', primary_key=True)  # Field name made lowercase.
    timetable_id = models.ForeignKey('TimetableTb', models.DO_NOTHING, db_column='TIMETABLE_ID')  # Field name made lowercase.
    hour_id = models.ForeignKey(HourTb, models.DO_NOTHING, db_column='HOUR_ID')  # Field name made lowercase.
    subjects = models.CharField(db_column='SUBJECTS', max_length=30)  # Field name made lowercase.
    room = models.CharField(db_column='ROOM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIMETABLE_DETAIL_TB'
        unique_together = (('detail_id', 'timetable_id', 'hour_id'),)


class TimetableTb(models.Model):
    timetable_id = models.AutoField(db_column='TIMETABLE_ID', primary_key=True)  # Field name made lowercase.
    created_day = models.DateTimeField(db_column='CREATED_DAY')  # Field name made lowercase.
    timetable_name = models.CharField(db_column='TIMETABLE_NAME', max_length=30)  # Field name made lowercase.
    user_id = models.ForeignKey(TeacherTb, models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIMETABLE_TB'


class UserStateTb(models.Model):
    user_state_id = models.AutoField(db_column='USER_STATE_ID', primary_key=True)  # Field name made lowercase.
    user_state = models.CharField(db_column='USER_STATE', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_STATE_TB'
