from django.contrib.auth.models import Group

# Create Group
content_editor_group = Group.objects.get_or_create(name="Content-Editor")
content_editor_group.permissions.set([
                                        'article.add_article',
                                        'article.change_article',
                                        'article.delete_article',
                                        'article.view_article',
                                      ])

