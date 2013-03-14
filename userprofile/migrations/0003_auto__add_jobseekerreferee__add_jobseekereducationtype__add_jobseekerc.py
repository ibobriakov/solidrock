# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JobSeekerReferee'
        db.create_table(u'userprofile_jobseekerreferee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address_first', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('address_second', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('job_seeker', self.gf('django.db.models.fields.related.ForeignKey')(related_name='referees_set', to=orm['userprofile.JobSeeker'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('position_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('phone_number', self.gf('userprofile.models.fields.PhoneField')(default='00000000000', max_length=11, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('is_for_interview', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('userprofile', ['JobSeekerReferee'])

        # Adding model 'JobSeekerEducationType'
        db.create_table(u'userprofile_jobseekereducationtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_name_slug', self.gf('django.db.models.fields.SlugField')(max_length=255, null=True, blank=True)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('userprofile', ['JobSeekerEducationType'])

        # Adding model 'JobSeekerCurrentEmployment'
        db.create_table(u'userprofile_jobseekercurrentemployment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address_first', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('address_second', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('job_seeker', self.gf('django.db.models.fields.related.OneToOneField')(related_name='current_employment', unique=True, to=orm['userprofile.JobSeeker'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('position_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('date_commenced', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('brief', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('job_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last_day_of_service', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('leaving_reason', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('userprofile', ['JobSeekerCurrentEmployment'])

        # Adding model 'JobSeekerPerviousEmployment'
        db.create_table(u'userprofile_jobseekerperviousemployment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address_first', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('address_second', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('job_seeker', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pervious_employments_set', to=orm['userprofile.JobSeeker'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('position_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('brief', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('leaving_reason', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('userprofile', ['JobSeekerPerviousEmployment'])

        # Adding model 'JobSeekerEducation'
        db.create_table(u'userprofile_jobseekereducation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job_seeker', self.gf('django.db.models.fields.related.ForeignKey')(related_name='educations_set', to=orm['userprofile.JobSeeker'])),
            ('education_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['userprofile.JobSeekerEducationType'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('userprofile', ['JobSeekerEducation'])

        # Adding model 'JobSeekerInformation'
        db.create_table(u'userprofile_jobseekerinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address_first', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('address_second', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('job_seeker', self.gf('django.db.models.fields.related.OneToOneField')(related_name='personal_information', unique=True, to=orm['userprofile.JobSeeker'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('home_phone', self.gf('userprofile.models.fields.PhoneField')(default='00000000000', max_length=11, null=True, blank=True)),
            ('daytime_phone', self.gf('userprofile.models.fields.PhoneField')(default='00000000000', max_length=11, null=True, blank=True)),
            ('mobile_phone', self.gf('userprofile.models.fields.PhoneField')(default='00000000000', max_length=11, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('can_contact_at_work', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_australian', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('have_visa', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_driver', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('userprofile', ['JobSeekerInformation'])


        # Changing field 'Employer.phone'
        db.alter_column(u'userprofile_employer', 'phone', self.gf('userprofile.models.fields.PhoneField')(max_length=11))

    def backwards(self, orm):
        # Deleting model 'JobSeekerReferee'
        db.delete_table(u'userprofile_jobseekerreferee')

        # Deleting model 'JobSeekerEducationType'
        db.delete_table(u'userprofile_jobseekereducationtype')

        # Deleting model 'JobSeekerCurrentEmployment'
        db.delete_table(u'userprofile_jobseekercurrentemployment')

        # Deleting model 'JobSeekerPerviousEmployment'
        db.delete_table(u'userprofile_jobseekerperviousemployment')

        # Deleting model 'JobSeekerEducation'
        db.delete_table(u'userprofile_jobseekereducation')

        # Deleting model 'JobSeekerInformation'
        db.delete_table(u'userprofile_jobseekerinformation')


        # Changing field 'Employer.phone'
        db.alter_column(u'userprofile_employer', 'phone', self.gf('django.db.models.fields.CharField')(max_length=11))

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
        'userprofile.employer': {
            'Meta': {'object_name': 'Employer'},
            'company': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('userprofile.models.fields.PhoneField', [], {'default': "'00000000000'", 'max_length': '11'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        'userprofile.jobseeker': {
            'Meta': {'object_name': 'JobSeeker'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        'userprofile.jobseekercurrentemployment': {
            'Meta': {'object_name': 'JobSeekerCurrentEmployment'},
            'address_first': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address_second': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'brief': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_commenced': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_seeker': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'current_employment'", 'unique': 'True', 'to': "orm['userprofile.JobSeeker']"}),
            'job_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_day_of_service': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'leaving_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'position_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'userprofile.jobseekereducation': {
            'Meta': {'object_name': 'JobSeekerEducation'},
            'education_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['userprofile.JobSeekerEducationType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_seeker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'educations_set'", 'to': "orm['userprofile.JobSeeker']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'userprofile.jobseekereducationtype': {
            'Meta': {'object_name': 'JobSeekerEducationType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type_name_slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'userprofile.jobseekerinformation': {
            'Meta': {'object_name': 'JobSeekerInformation'},
            'address_first': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address_second': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'can_contact_at_work': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'daytime_phone': ('userprofile.models.fields.PhoneField', [], {'default': "'00000000000'", 'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'have_visa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'home_phone': ('userprofile.models.fields.PhoneField', [], {'default': "'00000000000'", 'max_length': '11', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_australian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_driver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_seeker': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'personal_information'", 'unique': 'True', 'to': "orm['userprofile.JobSeeker']"}),
            'mobile_phone': ('userprofile.models.fields.PhoneField', [], {'default': "'00000000000'", 'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'userprofile.jobseekerperviousemployment': {
            'Meta': {'object_name': 'JobSeekerPerviousEmployment'},
            'address_first': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address_second': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'brief': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_seeker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pervious_employments_set'", 'to': "orm['userprofile.JobSeeker']"}),
            'leaving_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'position_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'userprofile.jobseekerreferee': {
            'Meta': {'object_name': 'JobSeekerReferee'},
            'address_first': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address_second': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_for_interview': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_seeker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referees_set'", 'to': "orm['userprofile.JobSeeker']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'phone_number': ('userprofile.models.fields.PhoneField', [], {'default': "'00000000000'", 'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'position_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['userprofile']