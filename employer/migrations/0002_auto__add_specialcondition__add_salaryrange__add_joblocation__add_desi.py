# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SpecialCondition'
        db.create_table(u'employer_specialcondition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('special_condition', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'employer', ['SpecialCondition'])

        # Adding model 'SalaryRange'
        db.create_table(u'employer_salaryrange', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('salary_range', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'employer', ['SalaryRange'])

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

        # Adding model 'Job'
        db.create_table(u'employer_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.JobLocation'])),
            ('award', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('salary_range', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.SalaryRange'], null=True, blank=True)),
            ('hours', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.Hour'])),
            ('employment_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.EmploymentType'])),
            ('special_conditions', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.SpecialCondition'], null=True, blank=True)),
            ('other_conditions', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('open_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('contact_phone', self.gf('userprofile.models.fields.PhoneField')(default='', max_length=11, null=True, blank=True)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'employer', ['Job'])

        # Adding model 'Hour'
        db.create_table(u'employer_hour', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hour', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'employer', ['Hour'])

        # Adding model 'EmploymentType'
        db.create_table(u'employer_employmenttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'employer', ['EmploymentType'])

        # Adding model 'Essential'
        db.create_table(u'employer_essential', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employer.Job'])),
            ('essential', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'employer', ['Essential'])


    def backwards(self, orm):
        # Deleting model 'SpecialCondition'
        db.delete_table(u'employer_specialcondition')

        # Deleting model 'SalaryRange'
        db.delete_table(u'employer_salaryrange')

        # Deleting model 'JobLocation'
        db.delete_table(u'employer_joblocation')

        # Deleting model 'Desireable'
        db.delete_table(u'employer_desireable')

        # Deleting model 'Job'
        db.delete_table(u'employer_job')

        # Deleting model 'Hour'
        db.delete_table(u'employer_hour')

        # Deleting model 'EmploymentType'
        db.delete_table(u'employer_employmenttype')

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
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'contact_phone': ('userprofile.models.fields.PhoneField', [], {'default': "''", 'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'employment_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.EmploymentType']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.Hour']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.JobLocation']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'open_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'other_conditions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'salary_range': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.SalaryRange']", 'null': 'True', 'blank': 'True'}),
            'special_conditions': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employer.SpecialCondition']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'employer.joblocation': {
            'Meta': {'object_name': 'JobLocation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '150'})
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