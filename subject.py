import datajoint as dj

import reference

schema = dj.schema(dj.config['names.%s' % __name__], locals())



@schema
class Species(dj.Manual):
    # <class 'subjects.models.Species'>
    definition = """
    species_id:			int             # species id
    ---
    binomial:			varchar(255)	# binomial
    display_name:		varchar(255)	# display name
    """


@schema
class Strain(dj.Manual):
    # <class 'subjects.models.Strain'>
    definition = """
    strain_id:			int             # strain id
    ---
    descriptive_name:		varchar(255)	# descriptive name
    description:    		varchar(255)	# description
    """


@schema
class Sequence(dj.Manual):
    # <class 'subjects.models.Sequence'>
    definition = """
    sequence_id:		int             # sequence id
    ---
    base_pairs:			varchar(255)	# base pairs
    description:		varchar(255)	# description
    informal_name:		varchar(255)	# informal name
    """


@schema
class Allele(dj.Manual):
    # <class 'subjects.models.Allele'>
    definition = """
    allele_id:			int             # allele id
    ---
    standard_name:		varchar(255)	# standard name
    informal_name:		varchar(255)	# informal name
    """


@schema
class Line(dj.Manual):
    # <class 'subjects.models.Line'>
    # TODO: autoname index: basically autogenerates a unique sequence
    definition = """
    -> Species
    -> Strain
    -> Sequence
    line_id:				int             # line id
    ---
    name:				varchar(255)	# name
    description:			varchar(255)	# description
    target_phenotype:			varchar(255)	# target phenotype
    auto_name:				varchar(255)	# auto name
    is_active:				boolean		# is active
    subject_autoname_index:		integer		# subject autoname index
    breeding_pair_autoname_index:	integer		# breeding pair autoname index
    litter_autoname_index:		integer		# litter autoname index
    """


@schema
class Source(dj.Manual):
    # <class 'subjects.models.Source'>
    definition = """
    source_id:				int             # source id
    ---
    name:				varchar(255)	# name
    description:			varchar(255)	# description
    """


@schema
class SubjectRequest(dj.Manual):
    # <class 'subjects.models.SubjectRequest'>
    definition = """
    -> reference.User
    -> Line
    subject_request_id:			int     	# subject request id
    ---
    count:				integer		# count
    date_time:				date		# date time
    due_date:				date		# due date
    description:			varchar(255)	# description
    """


@schema
class Subject(dj.Manual):
    # <class 'subjects.models.Subject'>
    # todo:
    # - where did responsible_user go? RETEST ADDED
    # - -> SubjectRequest or track subjects as part table of subject request?
    #      RETEST ADDED

    definition = """
    subject_id:			int                     # subject id
    ---
    nickname:			varchar(255)		# nickname
    -> Line
    sex:			enum("M", "F", "U")	# sex
    birth_date:			date			# birth date
    death_date:			date			# death date
    wean_date:			date			# wean date
    genotype_date:		date			# genotype date
    (responsible_user)          -> reference.User
    (request)                   -> SubjectRequest(subject_request_id)
    -> Source
    lamis_cage:			integer			# lamis cage
    implant_weight:		float			# implant weight
    ear_mark:			varchar(255)		# ear mark
    protocol_number:		varchar(255)		# protocol number
    description:		varchar(255)		# description
    cull_method:		varchar(255)		# cull method
    adverse_effects:		varchar(255)		# adverse effects
    (actual_severity)		-> reference.Severity   # actual severity
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
        zygosity:		integer 		# zygosity
        """


@schema
class GenotypeTest(dj.Manual):
    # <class 'subjects.models.GenotypeTest'>
    definition = """
    -> Subject
    -> Sequence
    genotype_test_id:		int     	# genotype test id
    ---
    test_result:		integer		# test result
    """


@schema
class Birth(dj.Manual):
    # can be made redundant via queries:
    # <class 'subjects.models.BreedingPair'>
    # <class 'subjects.models.Litter'>
    #
    # This table *only* required since making subject atttributes w/i subjects
    # creates graph cycles.
    #
    # XXX: cage placement times to emulate previous BreedingPair
    # (if reproductive success, etc. req'd)
    definition = """
    -> Subject
    ---
    (father)			-> Subject		# father
    (mother1) 			-> Subject		# mother1
    # XXX: explain? (mother2)	-> [nullable] Subject	# mother2
    """


