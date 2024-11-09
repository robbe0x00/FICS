ACTIONS = ''
LANGUAGES = 'C'
DATA_DIR = '/data/'  # Full path must be provided
PROJECTS_DIR = 'projects'
ASTS_DIR = 'asts'
SAVE_FORMAT = 'graph'  # json , graph , ast
BCS_DIR = 'bcs'
DATASETS_DIR = 'datasets'
PLOTS_DIR = 'plots'
CLUSTERING_ALGS = 'dbscancos_0.3,dbscancos_0.02'
CLUSTERING_FEAT = 'afs_NN,afs_G2v'
SECOND_CLUSTERING = 'offline'
COSE_SIMILARITY_CHUNK_SIZE = 200000  # BB 150000  # If there is 200G Ram
BIG_CLUSTERS_IGNORE = 50
CHUNK_WINDOW_SIZE = 1
SPLIT = False
SEARCH_SPACES = []  # Empty means everywhere in the projects
PROJECTS = ''  # 'ffmpeg-b2f0f37'  # Empty means all projects
IGNORE_COMPILE_COMMANDS = False
FEATURE_TYPES = 'afs_NN'  # afs_G2v, afs.bb2_NN
# CLANG_LIB_DIR = '../../tools/clang+llvm-5.0.1-x86_64-linux-gnu-ubuntu-16.04/lib'
CLANG_LIB_DIR = '/usr/lib/x86_64-linux-gnu'
LLVM_CONFIG = ''
INCLUDES = ''
CLANG = 'clang-3.8'  # 'clang-6.0'  #'clang-3.8'
PDG_DUMPER = './dg/tools/llvm-dg-dump'
STAT_TYPE = 'ST'  # SI, SS , ST
STAT_SIM_TYPES = 'NN,G2v'
INCONSISTENCY_TYPE = 'check'  # check, call, type, order
SIMILARITY_THRESHOLD = 0.7
GRANULARITY = 'afs,afs.bb1,afs.bb2'
DEPENDENCY = ''  # all , odd , cdd
CALL_INCONSISTENCY = 'free,close,memset,clear,bzero,remove,unlock,end,clean,cleanse,assert'
TYPE_INCONSISTENCY = 'trunc'  # 'fptrunc,sext,zext,call zeroext,call signext,sitofp,uitofp,bitcast'
STORE_INCONSISTENCY = 'null'
INCONSISTENCY_QUERY_OPTIONS = 'top_10'
COUNT_CPU = 8
BENCHMARK_GROUNDTRUTH_PATH = 'iBench/'
