# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by Django 4.1.9 on 2023-06-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("microsite", "0023_alter_protocoltestpage_body_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MicrositeSettings",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "site_theme",
                    models.CharField(
                        choices=[("protocol-mozilla-theme", "Mozilla.org theme"), ("protocol-firefox-theme", "Firefox theme")],
                        default="protocol-mozilla-theme",
                        help_text="Choose the design theme for this site. Changes will be immediately applied - there is no preview",
                        max_length=64,
                    ),
                ),
            ],
            options={
                "verbose_name": "General site settings",
            },
        ),
        migrations.AlterModelOptions(
            name="footer",
            options={"verbose_name": "Configure Footer"},
        ),
    ]