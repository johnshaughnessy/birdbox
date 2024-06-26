# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by Django 5.0.2 on 2024-03-31 11:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("microsite", "0106_alter_generalpurposepage_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="micrositesettings",
            name="site_theme",
            field=models.CharField(
                choices=[
                    ("mozilla", "Mozilla.org theme"),
                    ("firefox", "Firefox theme"),
                    ("innovation", "Innovations theme"),
                ],
                default="mozilla",
                help_text="Choose the design theme (typography, colours) for this site. Changes will be immediately applied - there is no preview",
                max_length=64,
            ),
        ),
    ]
