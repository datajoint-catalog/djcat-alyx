# <class 'misc.models.OrderedUser'>
# <class 'django.contrib.auth.models.User'>

@schema
class OrderedUser(dj.Manual):
    definition="""
    id:    type_unknown <class 'django.db.models.fields.AutoField'> # ID
    ---
    password:    varchar(255) # password
    last_login:    datetime # last login
    is_superuser:    boolean # superuser status
    username:    varchar(255) # username
    first_name:    varchar(255) # first name
    last_name:    varchar(255) # last name
    email:    varchar(255) # email address
    is_staff:    boolean # staff status
    is_active:    boolean # active
    date_joined:    datetime # date joined
    groups:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # groups
    user_permissions:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # user permissions
    """


# <class 'misc.models.BrainLocation'>
@schema
class BrainLocation(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    stereotaxic_coordinates:    longblob # stereotaxic coordinates
    description:    varchar(255) # description
    allen_location_ontology:    varchar(255) # allen location ontology
    """
