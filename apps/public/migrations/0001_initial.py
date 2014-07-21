# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Enemy'
        db.create_table(u'public_enemy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['Enemy'])

        # Adding model 'Item'
        db.create_table(u'public_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['Item'])

        # Adding model 'Weapon'
        db.create_table(u'public_weapon', (
            (u'item_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['public.Item'], unique=True, primary_key=True)),
            ('damage', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
        ))
        db.send_create_signal(u'public', ['Weapon'])

        # Adding model 'Inventory'
        db.create_table(u'public_inventory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'public', ['Inventory'])

        # Adding M2M table for field items on 'Inventory'
        m2m_table_name = db.shorten_name(u'public_inventory_items')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('inventory', models.ForeignKey(orm[u'public.inventory'], null=False)),
            ('item', models.ForeignKey(orm[u'public.item'], null=False))
        ))
        db.create_unique(m2m_table_name, ['inventory_id', 'item_id'])

        # Adding model 'Skill'
        db.create_table(u'public_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['Skill'])

        # Adding model 'Race'
        db.create_table(u'public_race', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['Race'])

        # Adding model 'Nationality'
        db.create_table(u'public_nationality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['Nationality'])

        # Adding model 'Character'
        db.create_table(u'public_character', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['auth.User'], to_field='username')),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=50)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['public.Race'])),
            ('nationality', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['public.Nationality'])),
            ('hit_points', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('inventory', self.gf('django.db.models.fields.related.OneToOneField')(default='', to=orm['public.Inventory'], unique=True)),
        ))
        db.send_create_signal(u'public', ['Character'])

        # Adding M2M table for field skills on 'Character'
        m2m_table_name = db.shorten_name(u'public_character_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('character', models.ForeignKey(orm[u'public.character'], null=False)),
            ('skill', models.ForeignKey(orm[u'public.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['character_id', 'skill_id'])

        # Adding model 'Battle'
        db.create_table(u'public_battle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['Battle'])

        # Adding M2M table for field enemies on 'Battle'
        m2m_table_name = db.shorten_name(u'public_battle_enemies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('battle', models.ForeignKey(orm[u'public.battle'], null=False)),
            ('enemy', models.ForeignKey(orm[u'public.enemy'], null=False))
        ))
        db.create_unique(m2m_table_name, ['battle_id', 'enemy_id'])

        # Adding M2M table for field characters on 'Battle'
        m2m_table_name = db.shorten_name(u'public_battle_characters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('battle', models.ForeignKey(orm[u'public.battle'], null=False)),
            ('character', models.ForeignKey(orm[u'public.character'], null=False))
        ))
        db.create_unique(m2m_table_name, ['battle_id', 'character_id'])

        # Adding model 'Scenario'
        db.create_table(u'public_scenario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['Scenario'])

        # Adding M2M table for field battles on 'Scenario'
        m2m_table_name = db.shorten_name(u'public_scenario_battles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm[u'public.scenario'], null=False)),
            ('battle', models.ForeignKey(orm[u'public.battle'], null=False))
        ))
        db.create_unique(m2m_table_name, ['scenario_id', 'battle_id'])

        # Adding model 'Game'
        db.create_table(u'public_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=50)),
            ('scenario', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['public.Scenario'])),
        ))
        db.send_create_signal(u'public', ['Game'])

        # Adding M2M table for field players on 'Game'
        m2m_table_name = db.shorten_name(u'public_game_players')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm[u'public.game'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_id', 'user_id'])

        # Adding M2M table for field characters on 'Game'
        m2m_table_name = db.shorten_name(u'public_game_characters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm[u'public.game'], null=False)),
            ('character', models.ForeignKey(orm[u'public.character'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_id', 'character_id'])


    def backwards(self, orm):
        # Deleting model 'Enemy'
        db.delete_table(u'public_enemy')

        # Deleting model 'Item'
        db.delete_table(u'public_item')

        # Deleting model 'Weapon'
        db.delete_table(u'public_weapon')

        # Deleting model 'Inventory'
        db.delete_table(u'public_inventory')

        # Removing M2M table for field items on 'Inventory'
        db.delete_table(db.shorten_name(u'public_inventory_items'))

        # Deleting model 'Skill'
        db.delete_table(u'public_skill')

        # Deleting model 'Race'
        db.delete_table(u'public_race')

        # Deleting model 'Nationality'
        db.delete_table(u'public_nationality')

        # Deleting model 'Character'
        db.delete_table(u'public_character')

        # Removing M2M table for field skills on 'Character'
        db.delete_table(db.shorten_name(u'public_character_skills'))

        # Deleting model 'Battle'
        db.delete_table(u'public_battle')

        # Removing M2M table for field enemies on 'Battle'
        db.delete_table(db.shorten_name(u'public_battle_enemies'))

        # Removing M2M table for field characters on 'Battle'
        db.delete_table(db.shorten_name(u'public_battle_characters'))

        # Deleting model 'Scenario'
        db.delete_table(u'public_scenario')

        # Removing M2M table for field battles on 'Scenario'
        db.delete_table(db.shorten_name(u'public_scenario_battles'))

        # Deleting model 'Game'
        db.delete_table(u'public_game')

        # Removing M2M table for field players on 'Game'
        db.delete_table(db.shorten_name(u'public_game_players'))

        # Removing M2M table for field characters on 'Game'
        db.delete_table(db.shorten_name(u'public_game_characters'))


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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'public.battle': {
            'Meta': {'object_name': 'Battle'},
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Character']", 'symmetrical': 'False'}),
            'enemies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Enemy']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '50'})
        },
        u'public.character': {
            'Meta': {'object_name': 'Character'},
            'hit_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.OneToOneField', [], {'default': "''", 'to': u"orm['public.Inventory']", 'unique': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '50'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['public.Nationality']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['auth.User']", 'to_field': "'username'"}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['public.Race']"}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Skill']", 'symmetrical': 'False'})
        },
        u'public.enemy': {
            'Meta': {'object_name': 'Enemy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '50'})
        },
        u'public.game': {
            'Meta': {'object_name': 'Game'},
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Character']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '50'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'}),
            'scenario': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['public.Scenario']"})
        },
        u'public.inventory': {
            'Meta': {'object_name': 'Inventory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Item']", 'symmetrical': 'False'})
        },
        u'public.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '50'})
        },
        u'public.nationality': {
            'Meta': {'object_name': 'Nationality'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '50'})
        },
        u'public.race': {
            'Meta': {'object_name': 'Race'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '50'})
        },
        u'public.scenario': {
            'Meta': {'object_name': 'Scenario'},
            'battles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Battle']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '50'})
        },
        u'public.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '50'})
        },
        u'public.weapon': {
            'Meta': {'object_name': 'Weapon', '_ormbases': [u'public.Item']},
            'damage': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            u'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['public.Item']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['public']