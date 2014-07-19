# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Nationality'
        db.create_table(u'public_nationality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['Nationality'])

        # Adding model 'Item'
        db.create_table(u'public_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['Item'])

        # Adding model 'Skill'
        db.create_table(u'public_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['Skill'])

        # Adding model 'Race'
        db.create_table(u'public_race', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['Race'])

        # Adding field 'Character.hit_points'
        db.add_column(u'public_character', 'hit_points',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.race'
        db.add_column(u'public_character', 'race',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['public.Race'], unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Character.nationality'
        db.add_column(u'public_character', 'nationality',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['public.Nationality'], unique=True, null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field weapon on 'Character'
        db.delete_table(db.shorten_name(u'public_character_weapon'))

        # Adding M2M table for field items on 'Character'
        m2m_table_name = db.shorten_name(u'public_character_items')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('character', models.ForeignKey(orm[u'public.character'], null=False)),
            ('item', models.ForeignKey(orm[u'public.item'], null=False))
        ))
        db.create_unique(m2m_table_name, ['character_id', 'item_id'])

        # Adding M2M table for field weapons on 'Character'
        m2m_table_name = db.shorten_name(u'public_character_weapons')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('character', models.ForeignKey(orm[u'public.character'], null=False)),
            ('weapon', models.ForeignKey(orm[u'public.weapon'], null=False))
        ))
        db.create_unique(m2m_table_name, ['character_id', 'weapon_id'])

        # Adding M2M table for field skills on 'Character'
        m2m_table_name = db.shorten_name(u'public_character_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('character', models.ForeignKey(orm[u'public.character'], null=False)),
            ('skill', models.ForeignKey(orm[u'public.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['character_id', 'skill_id'])


    def backwards(self, orm):
        # Deleting model 'Nationality'
        db.delete_table(u'public_nationality')

        # Deleting model 'Item'
        db.delete_table(u'public_item')

        # Deleting model 'Skill'
        db.delete_table(u'public_skill')

        # Deleting model 'Race'
        db.delete_table(u'public_race')

        # Deleting field 'Character.hit_points'
        db.delete_column(u'public_character', 'hit_points')

        # Deleting field 'Character.race'
        db.delete_column(u'public_character', 'race_id')

        # Deleting field 'Character.nationality'
        db.delete_column(u'public_character', 'nationality_id')

        # Adding M2M table for field weapon on 'Character'
        m2m_table_name = db.shorten_name(u'public_character_weapon')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('character', models.ForeignKey(orm[u'public.character'], null=False)),
            ('weapon', models.ForeignKey(orm[u'public.weapon'], null=False))
        ))
        db.create_unique(m2m_table_name, ['character_id', 'weapon_id'])

        # Removing M2M table for field items on 'Character'
        db.delete_table(db.shorten_name(u'public_character_items'))

        # Removing M2M table for field weapons on 'Character'
        db.delete_table(db.shorten_name(u'public_character_weapons'))

        # Removing M2M table for field skills on 'Character'
        db.delete_table(db.shorten_name(u'public_character_skills'))


    models = {
        u'public.character': {
            'Meta': {'object_name': 'Character'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hit_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['public.Item']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'nationality': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['public.Nationality']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['public.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['public.Race']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['public.Skill']", 'null': 'True', 'blank': 'True'}),
            'weapons': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['public.Weapon']", 'null': 'True', 'blank': 'True'})
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
        u'public.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'public.nationality': {
            'Meta': {'object_name': 'Nationality'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'public.race': {
            'Meta': {'object_name': 'Race'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'public.scenario': {
            'Meta': {'object_name': 'Scenario'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'public.skill': {
            'Meta': {'object_name': 'Skill'},
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