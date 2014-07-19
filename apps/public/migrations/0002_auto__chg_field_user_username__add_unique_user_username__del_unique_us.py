# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'User', fields ['name']
        db.delete_unique(u'public_user', ['name'])


        # Changing field 'User.username'
        db.alter_column(u'public_user', 'username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50))
        # Adding unique constraint on 'User', fields ['username']
        db.create_unique(u'public_user', ['username'])


        # Changing field 'User.email'
        db.alter_column(u'public_user', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75))

        # Changing field 'User.password'
        db.alter_column(u'public_user', 'password', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):
        # Removing unique constraint on 'User', fields ['username']
        db.delete_unique(u'public_user', ['username'])


        # Changing field 'User.username'
        db.alter_column(u'public_user', 'username', self.gf('django.db.models.fields.TextField')(null=True))
        # Adding unique constraint on 'User', fields ['name']
        db.create_unique(u'public_user', ['name'])


        # Changing field 'User.email'
        db.alter_column(u'public_user', 'email', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'User.password'
        db.alter_column(u'public_user', 'password', self.gf('django.db.models.fields.TextField')(null=True))

    models = {
        u'public.character': {
            'Meta': {'object_name': 'Character'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'owner': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['public.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'weapon': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['public.Weapon']", 'null': 'True', 'blank': 'True'})
        },
        u'public.enemy': {
            'Meta': {'object_name': 'Enemy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'public.game': {
            'Meta': {'object_name': 'Game'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['public.User']", 'null': 'True', 'blank': 'True'}),
            'scenario': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['public.Scenario']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'public.scenario': {
            'Meta': {'object_name': 'Scenario'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'public.user': {
            'Meta': {'object_name': 'User'},
            'characters': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['public.Character']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '50'}),
            'username': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '50'})
        },
        u'public.weapon': {
            'Meta': {'object_name': 'Weapon'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['public']