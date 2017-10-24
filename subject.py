

import datajoint as dj

# schema = dj.schema(dj.config['FIXME'], locals())


@schema
class Species(dj.Manual):
    # <class 'subjects.models.Species'>
    definition = """
    species_id:				char(32)	# species id
    ---
    json:				varchar(255)	# json
    binomial:				varchar(255)	# binomial
    display_name:			varchar(255)	# display name
    """


@schema
class Strain(dj.Manual):
    # <class 'subjects.models.Strain'>
    definition = """
    strain_id:				char(32)	# strain id
    ---
    json:				varchar(255)	# json
    descriptive_name:			varchar(255)	# descriptive name
    description:    			varchar(255)	# description
    """


@schema
class Sequence(dj.Manual):
    # <class 'subjects.models.Sequence'>
    definition = """
    sequence_id:			char(32)	# sequence id
    ---
    base_pairs:				varchar(255)	# base pairs
    description:			varchar(255)	# description
    informal_name:			varchar(255)	# informal name
    json:				varchar(255)	# json
    """


@schema
class Allele(dj.Manual):
    # <class 'subjects.models.Allele'>
    definition = """
    allele_id:				char(32)	# allele id
    ---
    standard_name:			varchar(255)	# standard name
    informal_name:			varchar(255)	# informal name
    json:				varchar(255)	# json
    """


@schema
class Line(dj.Manual):
    # <class 'subjects.models.Line'>
    # XXX: autoname index: basically autogenerates a unique sequence
    definition = """
    -> Species
    -> Strain
    -> Sequence
    line_id:				char(32) 	# line id
    ---
    name:				varchar(255)	# name
    description:			varchar(255)	# description
    target_phenotype:			varchar(255)	# target phenotype
    auto_name:				varchar(255)	# auto name
    is_active:				boolean		# is active
    subject_autoname_index:		integer		# subject autoname index
    breeding_pair_autoname_index:	integer		# breeding pair autoname index
    litter_autoname_index:		integer		# litter autoname index
    json:				varchar(255)	# json
    """


@schema
class Source(dj.Manual):
    # <class 'subjects.models.Source'>
    definition = """
    source_id:				char(32)	# source id
    ---
    json:				varchar(255)	# json
    name:				varchar(255)	# name
    description:			varchar(255)	# description
    """


@schema
class SubjectRequest(dj.Manual):
    # <class 'subjects.models.SubjectRequest'>
    definition = """
    -> User
    -> Line
    subject_request_id:			char(32)	# subject request id
    ---
    json:				varchar(255)	# json
    count:				integer		# count
    date_time:				date		# date time
    due_date:				date		# due date
    description:			varchar(255)	# description
    """


@schema
class Subject(dj.Manual):
    # <class 'subjects.models.Subject'>
    # todo:
    # - where did responsible_user go?
    # - -> SubjectRequest or track subjects as part table of subject request?

    definition = """
    subject_id:			char(32)		# subject id
    ---
    -> Line
    nickname:			varchar(255)		# nickname
    json:			varchar(255)		# json
    sex:			enum("M", "F", "U")	# sex
    sex:			varchar(255)		# sex
    birth_date:			date			# birth date
    death_date:			date			# death date
    wean_date:			date			# wean date
    genotype_date:		date			# genotype date
    lamis_cage:			integer			# lamis cage
    implant_weight:		float			# implant weight
    ear_mark:			varchar(255)		# ear mark
    protocol_number:		varchar(255)		# protocol number
    description:		varchar(255)		# description
    cull_method:		varchar(255)		# cull method
    adverse_effects:		varchar(255)		# adverse effects
    (actual_severity)		-> Severity		# actual severity
    to_be_genotyped:		boolean			# to be genotyped
    to_be_culled:		boolean			# to be culled
    reduced:			boolean			# reduced
    reduced_date:		date			# reduced date
    """

    class Genotype(dj.Part):
        # <class 'subjects.models.Zygosity'>
        # genotype = models.ManyToManyField('Allele', through='Zygosity')
        definition = """
        -> Subject
        -> Allele
        ---
        zygosity:			integer		# zygosity
        """


@schema
class BreedingPair(dj.Manual):
    # <class 'subjects.models.BreedingPair'>
    definition = """
    breeding_pair_id:		char(32)		# breeding pair id
    ---
    name:			varchar(255)		# name
    description:		varchar(255)		# description
    start_date:			date			# start date
    end_date:			date			# end date
    (father)			-> Subject		# father
    (mother1) 			-> Subject		# mother1
    (mother2)			-> [nullable] Subject	# mother2
    json:			varchar(255)		# json
    """

    class Litter(dj.Part):
        # <class 'subjects.models.Litter'>
        definition = """
        -> BreedingPair
        litter_id:			char(32)	# litter id
        ---
        descriptive_name:		varchar(255)	# descriptive name
        description:			varchar(255)	# description
        birth_date:			date		# birth date
        json:				varchar(255)	# json
        """

    class Offspring(dj.Part):
        definition = """
        -> BreedingPair
        -> BreedingPair.Litter
        -> Subject
        """


@schema
class GenotypeTest(dj.Manual):
    # <class 'subjects.models.GenotypeTest'>
    definition = """
    -> Subject
    -> Sequence
    genotype_test_id:			char(32)	# genotype test id
    ---
    json:				varchar(255)	# json
    test_result:			integer		# test result
    """
