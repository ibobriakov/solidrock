# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ApplyToJob.resume'
        db.add_column(u'job_seeker_applytojob', 'resume',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume.Resume'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'ApplyToJob.cover_letter'
        db.add_column(u'job_seeker_applytojob', 'cover_letter',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cover_letter.CoverLetter'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ApplyToJob.resume'
        db.delete_column(u'job_seeker_applytojob', 'resume_id')

        # Deleting field 'ApplyToJob.cover_letter'
        db.delete_column(u'job_seeker_applytojob', 'cover_letter_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_email_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'user_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cover_letter.coverletter': {
            'Meta': {'object_name': 'CoverLetter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'employer.employmenttype': {
            'Meta': {'object_name': 'EmploymentType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'employer.hour': {
            'Meta': {'object_name': 'Hour'},
            'hour': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'employer.job': {
            'Meta': {'object_name': 'Job'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.JobArea']", 'null': 'True', 'blank': 'True'}),
            'award': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['employer.JobCategory']", 'null': 'True', 'through': u"orm['employer.JobSelectedCategory']", 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'contact_phone': ('userprofile.models.fields.PhoneField', [], {'default': "'00000000000'", 'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'employment_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.EmploymentType']", 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'executive_positions': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.JobExecutivePositions']", 'null': 'True', 'blank': 'True'}),
            'featured_job': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hours': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.Hour']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.JobLocation']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'open_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'other_conditions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'salary_range_max': ('django.db.models.fields.IntegerField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'salary_range_min': ('django.db.models.fields.IntegerField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'special_conditions': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.SpecialCondition']", 'null': 'True', 'blank': 'True'}),
            'sub_categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['employer.JobSubCategory']", 'null': 'True', 'through': u"orm['employer.JobSelectedSubCategory']", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'employer.jobarea': {
            'Meta': {'object_name': 'JobArea'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'employer.jobcategory': {
            'Meta': {'object_name': 'JobCategory'},
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'employer.jobexecutivepositions': {
            'Meta': {'object_name': 'JobExecutivePositions'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position_name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'employer.joblocation': {
            'Meta': {'object_name': 'JobLocation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'employer.jobselectedcategory': {
            'Meta': {'object_name': 'JobSelectedCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.JobCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.Job']"})
        },
        u'employer.jobselectedsubcategory': {
            'Meta': {'object_name': 'JobSelectedSubCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.Job']"}),
            'sub_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.JobSubCategory']"})
        },
        u'employer.jobsubcategory': {
            'Meta': {'object_name': 'JobSubCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sub_category_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'employer.specialcondition': {
            'Meta': {'object_name': 'SpecialCondition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'special_condition': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'job_seeker.applytojob': {
            'Meta': {'unique_together': "(('job_seeker', 'job'),)", 'object_name': 'ApplyToJob'},
            'cover_letter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cover_letter.CoverLetter']", 'null': 'True', 'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.Job']"}),
            'job_seeker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'resume': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['resume.Resume']", 'null': 'True', 'blank': 'True'})
        },
        'resume.resume': {
            'Meta': {'object_name': 'Resume'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['job_seeker']