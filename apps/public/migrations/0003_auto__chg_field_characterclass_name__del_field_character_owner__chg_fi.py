# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CharacterClass.name'
        db.alter_column(u'public_characterclass', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20))
        # Deleting field 'Character.owner'
        db.delete_column(u'public_character', 'owner_id')


        # Changing field 'Character.name'
        db.alter_column(u'public_character', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20))

        # Changing field 'Nationality.name'
        db.alter_column(u'public_nationality', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20))
        # Removing M2M table for field players on 'Encounter'
        db.delete_table(db.shorten_name(u'public_encounter_players'))


        # Changing field 'Encounter.name'
        db.alter_column(u'public_encounter', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20))

        # Changing field 'Game.name'
        db.alter_column(u'public_game', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20))

        # Changing field 'Chapter.name'
        db.alter_column(u'public_chapter', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20))

        # Changing field 'Item.name'
        db.alter_column(u'public_item', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20))

        # Changing field 'Scenario.name'
        db.alter_column(u'public_scenario', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20))

        # Changing field 'Skill.name'
        db.alter_column(u'public_skill', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20))

        # Changing field 'Weapon.damage'
        db.alter_column(u'public_weapon', 'damage', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Race.name'
        db.alter_column(u'public_race', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20))

    def backwards(self, orm):

        # Changing field 'CharacterClass.name'
        db.alter_column(u'public_characterclass', 'name', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True))

        # User chose to not deal with backwards NULL issues for 'Character.owner'
        raise RuntimeError("Cannot reverse this migration. 'Character.owner' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Character.owner'
        db.add_column(u'public_character', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], to_field='username'),
                      keep_default=False)


        # Changing field 'Character.name'
        db.alter_column(u'public_character', 'name', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True))

        # Changing field 'Nationality.name'
        db.alter_column(u'public_nationality', 'name', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True))
        # Adding M2M table for field players on 'Encounter'
        m2m_table_name = db.shorten_name(u'public_encounter_players')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('encounter', models.ForeignKey(orm[u'public.encounter'], null=False)),
            ('character', models.ForeignKey(orm[u'public.character'], null=False))
        ))
        db.create_unique(m2m_table_name, ['encounter_id', 'character_id'])


        # Changing field 'Encounter.name'
        db.alter_column(u'public_encounter', 'name', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True))

        # Changing field 'Game.name'
        db.alter_column(u'public_game', 'name', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True))

        # Changing field 'Chapter.name'
        db.alter_column(u'public_chapter', 'name', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True))

        # Changing field 'Item.name'
        db.alter_column(u'public_item', 'name', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True))

        # Changing field 'Scenario.name'
        db.alter_column(u'public_scenario', 'name', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True))

        # Changing field 'Skill.name'
        db.alter_column(u'public_skill', 'name', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True))

        # Changing field 'Weapon.damage'
        db.alter_column(u'public_weapon', 'damage', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Race.name'
        db.alter_column(u'public_race', 'name', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True))

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
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '20'}),
            'scenario': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': u"orm['public.Scenario']", 'symmetrical': 'False'})
        },
        u'public.character': {
            'Meta': {'object_name': 'Character'},
            'character_class': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['public.CharacterClass']", 'to_field': "'name'"}),
            'health': ('django.db.models.fields.IntegerField', [], {'default': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'related_name': "'characters'", 'symmetrical': 'False', 'to': u"orm['public.Item']"}),
            'maxHealth': ('django.db.models.fields.IntegerField', [], {'default': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '20'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['public.Nationality']"}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['public.Race']"}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Skill']", 'symmetrical': 'False'}),
            'sprite': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'weapon': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['public.Item']", 'to_field': "'name'"})
        },
        u'public.characterclass': {
            'Meta': {'object_name': 'CharacterClass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '20'})
        },
        u'public.encounter': {
            'Meta': {'object_name': 'Encounter'},
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': u"orm['public.Character']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': u"orm['public.Item']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '20'})
        },
        u'public.game': {
            'Meta': {'object_name': 'Game'},
            'chapters': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': u"orm['public.Chapter']", 'symmetrical': 'False'}),
            'game_master': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['public.Player']", 'to_field': "'username'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '20'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'related_name': "'Games'", 'symmetrical': 'False', 'to': u"orm['public.Player']"})
        },
        u'public.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '20'})
        },
        u'public.nationality': {
            'Meta': {'object_name': 'Nationality'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '20'})
        },
        u'public.player': {
            'Meta': {'object_name': 'Player', '_ormbases': [u'auth.User']},
            'character': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['public.Character']", 'unique': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'public.race': {
            'Meta': {'object_name': 'Race'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '20'})
        },
        u'public.scenario': {
            'Meta': {'object_name': 'Scenario'},
            'encounters': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': u"orm['public.Encounter']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '20'})
        },
        u'public.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '20'})
        },
        u'public.weapon': {
            'Meta': {'object_name': 'Weapon', '_ormbases': [u'public.Item']},
            'damage': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            u'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['public.Item']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['public']