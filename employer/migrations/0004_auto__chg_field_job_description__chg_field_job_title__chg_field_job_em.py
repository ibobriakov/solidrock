# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Job.description'
        db.alter_column(u'employer_job', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Job.title'
        db.alter_column(u'employer_job', 'title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Job.employment_type'
        db.alter_column(u'employer_job', 'employment_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.EmploymentType'], null=True))

        # Changing field 'Job.hours'
        db.alter_column(u'employer_job', 'hours_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.Hour'], null=True))

        # Changing field 'Job.location'
        db.alter_column(u'employer_job', 'location_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.JobLocation'], null=True))

        # Changing field 'Job.contact_name'
        db.alter_column(u'employer_job', 'contact_name', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

        # Changing field 'Job.name'
        db.alter_column(u'employer_job', 'name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Job.description'
        raise RuntimeError("Cannot reverse this migration. 'Job.description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Job.title'
        raise RuntimeError("Cannot reverse this migration. 'Job.title' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Job.employment_type'
        raise RuntimeError("Cannot reverse this migration. 'Job.employment_type' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Job.hours'
        raise RuntimeError("Cannot reverse this migration. 'Job.hours' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Job.location'
        raise RuntimeError("Cannot reverse this migration. 'Job.location' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Job.contact_name'
        raise RuntimeError("Cannot reverse this migration. 'Job.contact_name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Job.name'
        raise RuntimeError("Cannot reverse this migration. 'Job.name' and its values cannot be restored.")

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
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'employer.desireable': {
            'Meta': {'object_name': 'Desireable'},
            'desireable': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.Job']"})
        },
        u'employer.employmenttype': {
            'Meta': {'object_name': 'EmploymentType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'employer.essential': {
            'Meta': {'object_name': 'Essential'},
            'essential': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.Job']"})
        },
        u'employer.hour': {
            'Meta': {'object_name': 'Hour'},
            'hour': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'employer.job': {
            'Meta': {'object_name': 'Job'},
            'award': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['employer.JobCategory']", 'through': u"orm['employer.JobSelectedCategory']", 'symmetrical': 'False'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'contact_phone': ('userprofile.models.fields.PhoneField', [], {'default': "''", 'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'employment_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.EmploymentType']", 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.Hour']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.JobLocation']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'open_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'other_conditions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'salary_range': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.SalaryRange']", 'null': 'True', 'blank': 'True'}),
            'special_conditions': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.SpecialCondition']", 'null': 'True', 'blank': 'True'}),
            'sub_categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['employer.JobSubCategory']", 'through': u"orm['employer.JobSelectedCategory']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'employer.jobcategory': {
            'Meta': {'object_name': 'JobCategory'},
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.Job']"}),
            'sub_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.JobSubCategory']"})
        },
        u'employer.jobsubcategory': {
            'Meta': {'object_name': 'JobSubCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subcategories_set'", 'to': u"orm['employer.JobCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sub_category_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'employer.salaryrange': {
            'Meta': {'object_name': 'SalaryRange'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'salary_range': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'employer.specialcondition': {
            'Meta': {'object_name': 'SpecialCondition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'special_condition': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['employer']