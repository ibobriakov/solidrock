# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PaperItemType'
        db.create_table(u'dynamic_paper_paperitemtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'dynamic_paper', ['PaperItemType'])


    def backwards(self, orm):
        # Deleting model 'PaperItemType'
        db.delete_table(u'dynamic_paper_paperitemtype')


    models = {
        u'dynamic_paper.paperitemtype': {
            'Meta': {'object_name': 'PaperItemType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['dynamic_paper']