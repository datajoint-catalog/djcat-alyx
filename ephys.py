import datajoint as dj

schema = dj.schema(dj.config['names.%s' % __name__], locals())
