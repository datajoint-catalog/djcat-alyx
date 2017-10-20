# <class 'subjects.models.Species'>

@schema
class Species(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    binomial:    varchar(255) # binomial
    display_name:    varchar(255) # display name
    """

# <class 'subjects.models.Strain'>
@schema
class Strain(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    descriptive_name:    varchar(255) # descriptive name
    description:    varchar(255) # description
    """


# <class 'subjects.models.Line'>
@schema
class Line(dj.Manual):
    definition="""
    -> Strain
    -> Species
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    description:    varchar(255) # description
    target_phenotype:    varchar(255) # target phenotype
    auto_name:    varchar(255) # auto name
    subject_autoname_index:    integer # subject autoname index
    breeding_pair_autoname_index:    integer # breeding pair autoname index
    litter_autoname_index:    integer # litter autoname index
    is_active:    boolean # is active
    sequences:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # sequences
    """



# <class 'subjects.models.BreedingPair'>
# <class 'subjects.models.Litter'>
# <class 'subjects.models.Source'>

@schema
class BreedingPair(dj.Manual):
    definition="""
    -> Line
    -> Subject
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    start_date:    date # start date
    end_date:    date # end date
    description:    varchar(255) # description
    """

@schema
class Litter(dj.Manual):
    definition="""
    -> Line
    -> BreedingPair
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    descriptive_name:    varchar(255) # descriptive name
    description:    varchar(255) # description
    birth_date:    date # birth date
    """

@schema
class Source(dj.Manual):
    definition="""
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    name:    varchar(255) # name
    description:    varchar(255) # description
    """


# <class 'subjects.models.SubjectRequest'>

@schema
class SubjectRequest(dj.Manual):
    definition="""
    -> OrderedUser
    -> Line
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    count:    integer # count
    date_time:    date # date time
    due_date:    date # due date
    description:    varchar(255) # description
    """


# <class 'subjects.models.Subject'>

@schema
class Subject(dj.Manual):
    definition="""
    -> Species
    -> Litter
    -> Strain
    -> Source
    -> Line
    -> OrderedUser
    -> SubjectRequest
    id:    char(32) # id
    ---
    json:    varchar(255) # json
    nickname:    varchar(255) # nickname
    sex:    varchar(255) # sex
    birth_date:    date # birth date
    death_date:    date # death date
    wean_date:    date # wean date
    genotype_date:    date # genotype date
    lamis_cage:    integer # lamis cage
    implant_weight:    float # implant weight
    ear_mark:    varchar(255) # ear mark
    protocol_number:    varchar(255) # protocol number
    description:    varchar(255) # description
    cull_method:    varchar(255) # cull method
    adverse_effects:    varchar(255) # adverse effects
    actual_severity:    integer # actual severity
    to_be_genotyped:    boolean # to be genotyped
    to_be_culled:    boolean # to be culled
    reduced:    boolean # reduced
    reduced_date:    date # reduced date
    genotype:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # genotype
    genotype_test:    type_unknown <class 'django.db.models.fields.related.ManyToManyField'> # genotype test
    """

# BOOKMARK


# <class 'subjects.models.Allele'>
# <class 'subjects.models.Zygosity'>
# <class 'subjects.models.Sequence'>
# <class 'subjects.models.GenotypeTest'>
