# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JobSelectedSubCategory'
        db.create_table(u'employer_jobselectedsubcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.Job'])),
            ('sub_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.JobSubCategory'])),
        ))
        db.send_create_signal(u'employer', ['JobSelectedSubCategory'])

        # Adding model 'JobSubCategory'
        db.create_table(u'employer_jobsubcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sub_category_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'employer', ['JobSubCategory'])

        # Adding model 'SpecialCondition'
        db.create_table(u'employer_specialcondition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('special_condition', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'employer', ['SpecialCondition'])

        # Adding model 'JobSelectedCategory'
        db.create_table(u'employer_jobselectedcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.Job'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.JobCategory'])),
        ))
        db.send_create_signal(u'employer', ['JobSelectedCategory'])

        # Adding model 'JobExecutivePositions'
        db.create_table(u'employer_jobexecutivepositions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'employer', ['JobExecutivePositions'])

        # Adding model 'JobUploadDocumentType'
        db.create_table(u'employer_jobuploaddocumenttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('max_count', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal(u'employer', ['JobUploadDocumentType'])

        # Adding model 'JobArea'
        db.create_table(u'employer_jobarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'employer', ['JobArea'])

        # Adding model 'JobLocation'
        db.create_table(u'employer_joblocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'employer', ['JobLocation'])

        # Adding model 'Desireable'
        db.create_table(u'employer_desireable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.Job'])),
            ('desireable', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'employer', ['Desireable'])

        # Adding model 'Hour'
        db.create_table(u'employer_hour', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hour', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'employer', ['Hour'])

        # Adding model 'Job'
        db.create_table(u'employer_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.JobLocation'], null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.JobArea'], null=True, blank=True)),
            ('award', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('salary_range_min', self.gf('django.db.models.fields.IntegerField')(max_length=100, null=True, blank=True)),
            ('salary_range_max', self.gf('django.db.models.fields.IntegerField')(max_length=100, null=True, blank=True)),
            ('hours', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.Hour'], null=True, blank=True)),
            ('employment_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.EmploymentType'], null=True, blank=True)),
            ('special_conditions', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.SpecialCondition'], null=True, blank=True)),
            ('other_conditions', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('open_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('contact_phone', self.gf('userprofile.models.fields.PhoneField')(default='00000000000', max_length=11, null=True, blank=True)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('featured_job', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('executive_positions', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.JobExecutivePositions'], null=True, blank=True)),
        ))
        db.send_create_signal(u'employer', ['Job'])

        # Adding model 'EmploymentType'
        db.create_table(u'employer_employmenttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'employer', ['EmploymentType'])

        # Adding model 'JobCategory'
        db.create_table(u'employer_jobcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'employer', ['JobCategory'])

        # Adding model 'JobUploadDocument'
        db.create_table(u'employer_jobuploaddocument', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.Job'])),
            ('document_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.JobUploadDocumentType'])),
            ('document', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'employer', ['JobUploadDocument'])

        # Adding model 'Essential'
        db.create_table(u'employer_essential', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.Job'])),
            ('essential', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'employer', ['Essential'])


    def backwards(self, orm):
        # Deleting model 'JobSelectedSubCategory'
        db.delete_table(u'employer_jobselectedsubcategory')

        # Deleting model 'JobSubCategory'
        db.delete_table(u'employer_jobsubcategory')

        # Deleting model 'SpecialCondition'
        db.delete_table(u'employer_specialcondition')

        # Deleting model 'JobSelectedCategory'
        db.delete_table(u'employer_jobselectedcategory')

        # Deleting model 'JobExecutivePositions'
        db.delete_table(u'employer_jobexecutivepositions')

        # Deleting model 'JobUploadDocumentType'
        db.delete_table(u'employer_jobuploaddocumenttype')

        # Deleting model 'JobArea'
        db.delete_table(u'employer_jobarea')

        # Deleting model 'JobLocation'
        db.delete_table(u'employer_joblocation')

        # Deleting model 'Desireable'
        db.delete_table(u'employer_desireable')

        # Deleting model 'Hour'
        db.delete_table(u'employer_hour')

        # Deleting model 'Job'
        db.delete_table(u'employer_job')

        # Deleting model 'EmploymentType'
        db.delete_table(u'employer_employmenttype')

        # Deleting model 'JobCategory'
        db.delete_table(u'employer_jobcategory')

        # Deleting model 'JobUploadDocument'
        db.delete_table(u'employer_jobuploaddocument')

        # Deleting model 'Essential'
        db.delete_table(u'employer_essential')


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
        u'employer.jobuploaddocument': {
            'Meta': {'object_name': 'JobUploadDocument'},
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'document_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.JobUploadDocumentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.Job']"})
        },
        u'employer.jobuploaddocumenttype': {
            'Meta': {'object_name': 'JobUploadDocumentType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_count': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'employer.specialcondition': {
            'Meta': {'object_name': 'SpecialCondition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'special_condition': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['employer']