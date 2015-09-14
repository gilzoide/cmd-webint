# Flask variables.
DEBUG = False
SQLALCHEMY_ECHO = False
WTF_CSRF_ENABLED = True

# Coh-Metrix-Dementia variables.
NLPNET_DATA_DIR = '/home/andre/Develop/nlpnet-py3/data/'

OPENNLP_MACMORPHO_BIN = '/home/andre/Develop/apache-opennlp-1.5.3/bin/opennlp'
OPENNLP_MACMORPHO_MODEL = '/home/andre/Dropbox/Mestrado/coh/models/opennlp/pt-pos-maxent.bin'

OPENNLP_UNIVERSAL_BIN = OPENNLP_MACMORPHO_BIN
OPENNLP_UNIVERSAL_MODEL = '/home/andre/Dropbox/Mestrado/coh/models/opennlp/pt_br_universal-pos-maxent.bin'

LX_STANFORD_PATH = '/home/andre/Develop/stanford_tools/stanford-parser-2010-11-30/'
LX_MODEL_PATH = '/home/andre/Dropbox/Mestrado/coh/models/lxparser/cintil.ser.gz'

MALT_WORKING_DIR = '/home/andre/Develop/universal_dependencies/maltparser-1.8.1'
MALT_MCO = 'ptmalt.linear-1.8.1.mco'
MALT_JAVA_ARGS = ['-Xmx512m']

LSA_DICT_PATH = '/home/andre/Develop/corpora/lsamodel_wordids_190k.txt.bz2'
LSA_MODEL_PATH = '/home/andre/Develop/corpora/lsamodel_lsi.model'

KENLM_LANGUAGE_MODEL = '/home/andre/Develop/corpora/corpus_3gram.binary'
