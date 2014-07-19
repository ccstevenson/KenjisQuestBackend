# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'public_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('username', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('password', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('characters', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['public.Character'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'public', ['User'])

        # Adding model 'Character'
        db.create_table(u'public_character', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('owner', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['public.User'], unique=True, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'public', ['Character'])

        # Adding M2M table for field weapon on 'Character'
        m2m_table_name = db.shorten_name(u'public_character_weapon')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('character', models.ForeignKey(orm[u'public.character'], null=False)),
            ('weapon', models.ForeignKey(orm[u'public.weapon'], null=False))
        ))
        db.create_unique(m2m_table_name, ['character_id', 'weapon_id'])

        # Adding model 'Enemy'
        db.create_table(u'public_enemy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['Enemy'])

        # Adding model 'Game'
        db.create_table(u'public_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('scenario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['public.Scenario'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'public', ['Game'])

        # Adding M2M table for field players on 'Game'
        m2m_table_name = db.shorten_name(u'public_game_players')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm[u'public.game'], null=False)),
            ('user', models.ForeignKey(orm[u'public.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_id', 'user_id'])

        # Adding model 'Scenario'
        db.create_table(u'public_scenario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['Scenario'])

        # Adding model 'Weapon'
        db.create_table(u'public_weapon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['Weapon'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'public_user')

        # Deleting model 'Character'
        db.delete_table(u'public_character')

        # Removing M2M table for field weapon on 'Character'
        db.delete_table(db.shorten_name(u'public_character_weapon'))

        # Deleting model 'Enemy'
        db.delete_table(u'public_enemy')

        # Deleting model 'Game'
        db.delete_table(u'public_game')

        # Removing M2M table for field players on 'Game'
        db.delete_table(db.shorten_name(u'public_game_players'))

        # Deleting model 'Scenario'
        db.delete_table(u'public_scenario')

        # Deleting model 'Weapon'
        db.delete_table(u'public_weapon')


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
            'email': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'password': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'username': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        u'public.weapon': {
            'Meta': {'object_name': 'Weapon'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['public']