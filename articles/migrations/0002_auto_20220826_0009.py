# Generated by Django 4.1 on 2022-08-26 00:09

from django.db import migrations

def populate_article_type(apps,schaeditor):
    a_types = {
        "Report": "A journalistic piece",
        "Column": "A journalist's opinion piece",
        "Editorial": "An opinion piece by an editor",
    }
    ArticleType = apps.get_model("articles.ArticleType")
    for name, desc in a_types.items():
        at_obj= ArticleType(name=name, description=desc)
        at_obj.save()

def populate_status(apps,schaeditor):
    statuses = {
        "Pending": "An article that has not been reviewed",
        "Approve": "An article that has been approved by the editor",
        "Rejected": "An article that has been rejected by the editor",
    }
    Status = apps.get_model("articles","Status")
    for name, desc in statuses.items():
        status_obj= Status(name=name, description=desc)
        status_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_article_type),
        migrations.RunPython(populate_status),
    ]
