# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'public_player', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'public', ['Player'])

        # Adding model 'GameMaster'
        db.create_table(u'public_gamemaster', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'public', ['GameMaster'])

        # Adding model 'Item'
        db.create_table(u'public_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=10)),
        ))
        db.send_create_signal(u'public', ['Item'])

        # Adding model 'Weapon'
        db.create_table(u'public_weapon', (
            (u'item_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['public.Item'], unique=True, primary_key=True)),
            ('damage', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
        ))
        db.send_create_signal(u'public', ['Weapon'])

        # Adding model 'Skill'
        db.create_table(u'public_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=10)),
        ))
        db.send_create_signal(u'public', ['Skill'])

        # Adding model 'Race'
        db.create_table(u'public_race', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=10)),
        ))
        db.send_create_signal(u'public', ['Race'])

        # Adding model 'Nationality'
        db.create_table(u'public_nationality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=10)),
        ))
        db.send_create_signal(u'public', ['Nationality'])

        # Adding model 'CharacterClass'
        db.create_table(u'public_characterclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=50)),
        ))
        db.send_create_signal(u'public', ['CharacterClass'])

        # Adding model 'Character'
        db.create_table(u'public_character', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['auth.User'], to_field='username')),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=10)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['public.Race'])),
            ('nationality', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['public.Nationality'])),
            ('character_class', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['public.CharacterClass'])),
            ('hit_points', self.gf('django.db.models.fields.IntegerField')(default=30)),
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

        # Adding M2M table for field inventory on 'Character'
        m2m_table_name = db.shorten_name(u'public_character_inventory')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('character', models.ForeignKey(orm[u'public.character'], null=False)),
            ('item', models.ForeignKey(orm[u'public.item'], null=False))
        ))
        db.create_unique(m2m_table_name, ['character_id', 'item_id'])

        # Adding model 'Encounter'
        db.create_table(u'public_encounter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=10)),
        ))
        db.send_create_signal(u'public', ['Encounter'])

        # Adding M2M table for field items on 'Encounter'
        m2m_table_name = db.shorten_name(u'public_encounter_items')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('encounter', models.ForeignKey(orm[u'public.encounter'], null=False)),
            ('item', models.ForeignKey(orm[u'public.item'], null=False))
        ))
        db.create_unique(m2m_table_name, ['encounter_id', 'item_id'])

        # Adding M2M table for field characters on 'Encounter'
        m2m_table_name = db.shorten_name(u'public_encounter_characters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('encounter', models.ForeignKey(orm[u'public.encounter'], null=False)),
            ('character', models.ForeignKey(orm[u'public.character'], null=False))
        ))
        db.create_unique(m2m_table_name, ['encounter_id', 'character_id'])

        # Adding model 'Scenario'
        db.create_table(u'public_scenario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=10)),
        ))
        db.send_create_signal(u'public', ['Scenario'])

        # Adding M2M table for field encounters on 'Scenario'
        m2m_table_name = db.shorten_name(u'public_scenario_encounters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scenario', models.ForeignKey(orm[u'public.scenario'], null=False)),
            ('encounter', models.ForeignKey(orm[u'public.encounter'], null=False))
        ))
        db.create_unique(m2m_table_name, ['scenario_id', 'encounter_id'])

        # Adding model 'Chapter'
        db.create_table(u'public_chapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=10)),
        ))
        db.send_create_signal(u'public', ['Chapter'])

        # Adding M2M table for field scenario on 'Chapter'
        m2m_table_name = db.shorten_name(u'public_chapter_scenario')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chapter', models.ForeignKey(orm[u'public.chapter'], null=False)),
            ('scenario', models.ForeignKey(orm[u'public.scenario'], null=False))
        ))
        db.create_unique(m2m_table_name, ['chapter_id', 'scenario_id'])

        # Adding model 'Game'
        db.create_table(u'public_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=10)),
            ('game_master', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
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

        # Adding M2M table for field chapters on 'Game'
        m2m_table_name = db.shorten_name(u'public_game_chapters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm[u'public.game'], null=False)),
            ('chapter', models.ForeignKey(orm[u'public.chapter'], null=False))
        ))
        db.create_unique(m2m_table_name, ['game_id', 'chapter_id'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table(u'public_player')

        # Deleting model 'GameMaster'
        db.delete_table(u'public_gamemaster')

        # Deleting model 'Item'
        db.delete_table(u'public_item')

        # Deleting model 'Weapon'
        db.delete_table(u'public_weapon')

        # Deleting model 'Skill'
        db.delete_table(u'public_skill')

        # Deleting model 'Race'
        db.delete_table(u'public_race')

        # Deleting model 'Nationality'
        db.delete_table(u'public_nationality')

        # Deleting model 'CharacterClass'
        db.delete_table(u'public_characterclass')

        # Deleting model 'Character'
        db.delete_table(u'public_character')

        # Removing M2M table for field skills on 'Character'
        db.delete_table(db.shorten_name(u'public_character_skills'))

        # Removing M2M table for field inventory on 'Character'
        db.delete_table(db.shorten_name(u'public_character_inventory'))

        # Deleting model 'Encounter'
        db.delete_table(u'public_encounter')

        # Removing M2M table for field items on 'Encounter'
        db.delete_table(db.shorten_name(u'public_encounter_items'))

        # Removing M2M table for field characters on 'Encounter'
        db.delete_table(db.shorten_name(u'public_encounter_characters'))

        # Deleting model 'Scenario'
        db.delete_table(u'public_scenario')

        # Removing M2M table for field encounters on 'Scenario'
        db.delete_table(db.shorten_name(u'public_scenario_encounters'))

        # Deleting model 'Chapter'
        db.delete_table(u'public_chapter')

        # Removing M2M table for field scenario on 'Chapter'
        db.delete_table(db.shorten_name(u'public_chapter_scenario'))

        # Deleting model 'Game'
        db.delete_table(u'public_game')

        # Removing M2M table for field players on 'Game'
        db.delete_table(db.shorten_name(u'public_game_players'))

        # Removing M2M table for field chapters on 'Game'
        db.delete_table(db.shorten_name(u'public_game_chapters'))


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
        u'public.chapter': {
            'Meta': {'object_name': 'Chapter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '10'}),
            'scenario': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': u"orm['public.Scenario']", 'symmetrical': 'False'})
        },
        u'public.character': {
            'Meta': {'object_name': 'Character'},
            'character_class': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['public.CharacterClass']"}),
            'hit_points': ('django.db.models.fields.IntegerField', [], {'default': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': u"orm['public.Item']", 'symmetrical': 'False'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '10'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['public.Nationality']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['auth.User']", 'to_field': "'username'"}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['public.Race']"}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Skill']", 'symmetrical': 'False'})
        },
        u'public.characterclass': {
            'Meta': {'object_name': 'CharacterClass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '50'})
        },
        u'public.encounter': {
            'Meta': {'object_name': 'Encounter'},
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': u"orm['public.Character']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': u"orm['public.Item']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '10'})
        },
        u'public.game': {
            'Meta': {'object_name': 'Game'},
            'chapters': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': u"orm['public.Chapter']", 'symmetrical': 'False'}),
            'game_master': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '10'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'related_name': "'Games'", 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        },
        u'public.gamemaster': {
            'Meta': {'object_name': 'GameMaster', '_ormbases': [u'auth.User']},
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'public.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '10'})
        },
        u'public.nationality': {
            'Meta': {'object_name': 'Nationality'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '10'})
        },
        u'public.player': {
            'Meta': {'object_name': 'Player', '_ormbases': [u'auth.User']},
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'public.race': {
            'Meta': {'object_name': 'Race'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '10'})
        },
        u'public.scenario': {
            'Meta': {'object_name': 'Scenario'},
            'encounters': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': u"orm['public.Encounter']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '10'})
        },
        u'public.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '10'})
        },
        u'public.weapon': {
            'Meta': {'object_name': 'Weapon', '_ormbases': [u'public.Item']},
            'damage': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            u'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['public.Item']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['public']